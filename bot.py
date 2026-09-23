"""
Telegram bot: Shop, Deposit, My Profile, Support, Refer & Earn, Language.

Features:
  - Multi-language (EN/HI/ES/RU). Each user's choice is saved in SQLite and
    every response renders in their language.
  - BEP20 (BSC) USDT deposits with automatic detection via public RPC nodes
    (no API key). Users get a unique amount + QR; a background job credits
    their balance when the payment arrives.
  - Refer & Earn: personal invite link (/start=ref<id>), referral tracking,
    and an automatic reward to the referrer on their invitee's first deposit.

Setup:
    1. pip install -r requirements.txt
    2. Fill in .env (see .env.example): BOT_TOKEN, BEP20_ADDRESS
    3. python bot.py
"""

import asyncio
import html
import io
import logging
import os
import random
import threading
import urllib.parse

import qrcode
from dotenv import load_dotenv
from telegram import (
    BotCommand,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputFile,
    Update,
)
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import db
import products as catalog
from bscscan import get_incoming_usdt_transfers, get_latest_block
from lang import LANG_NAMES, SUPPORTED, t

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

SUPPORT_CONTACT = os.environ.get("SUPPORT_CONTACT", "@your_support_username")

def is_admin(user_id: int) -> bool:
    """Check if user_id is configured as an admin in env (ADMIN_ID or ADMIN_IDS)."""
    if not user_id:
        return False
    env_val = os.environ.get("ADMIN_ID") or os.environ.get("ADMIN_IDS") or ""
    admin_ids = set()
    for item in env_val.replace(";", ",").split(","):
        item = item.strip()
        if item.isdigit() and int(item) > 0:
            admin_ids.add(int(item))
    return user_id in admin_ids

# --- Crypto deposit config (from .env) ---
# Payments are read directly from public BSC RPC nodes, so NO API key is needed.
BEP20_ADDRESS = os.environ.get("BEP20_ADDRESS", "0xYourBep20WalletAddressHere")
DEPOSIT_WINDOW_MINUTES = int(os.environ.get("DEPOSIT_WINDOW_MINUTES", "30"))

MIN_DEPOSIT = 1.0
MAX_DEPOSIT = 100000.0
POLL_INTERVAL = 30

# Require this many block confirmations before crediting a deposit. On BSC a
# block is ~3s, so 6 confirmations is roughly 18s — enough to avoid crediting
# a transaction that could still be dropped by a short chain reorganisation.
MIN_CONFIRMATIONS = 6


# ---------------------------------------------------------------------------
# Language helpers
# ---------------------------------------------------------------------------
def user_lang(user_id: int) -> str:
    return db.get_language(user_id)


# ---------------------------------------------------------------------------
# Safe message editing
# ---------------------------------------------------------------------------
async def safe_edit(query, text: str, reply_markup=None, **kwargs) -> None:
    """
    Edit a callback message, tolerating Telegram's common, harmless errors:
      - "Message is not modified" (user re-tapped the same button)
      - "Query is too old" / "message can't be edited" (edit -> send fallback)
    """
    try:
        await query.edit_message_text(
            text, parse_mode=ParseMode.HTML, reply_markup=reply_markup, **kwargs
        )
    except BadRequest as exc:
        msg = str(exc).lower()
        if "not modified" in msg:
            return  # nothing to do — content is already shown
        # The original message may be gone or uneditable; send a fresh one.
        try:
            await query.message.reply_text(
                text, parse_mode=ParseMode.HTML, reply_markup=reply_markup, **kwargs
            )
        except Exception as exc2:  # noqa: BLE001
            logger.warning("safe_edit fallback failed: %s", exc2)


# ---------------------------------------------------------------------------
# Keyboards (translated per user)
# ---------------------------------------------------------------------------
def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(t("btn_shop", lang), callback_data="products")],
        [
            InlineKeyboardButton(t("btn_deposit", lang), callback_data="deposit"),
            InlineKeyboardButton(t("btn_profile", lang), callback_data="profile"),
        ],
        [
            InlineKeyboardButton(t("btn_support", lang), callback_data="support"),
            InlineKeyboardButton(t("btn_refer", lang), callback_data="refer"),
        ],
        [InlineKeyboardButton(t("btn_language", lang), callback_data="language")],
    ]
    return InlineKeyboardMarkup(keyboard)


def language_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(LANG_NAMES["en"], callback_data="lang_en"),
            InlineKeyboardButton(LANG_NAMES["hi"], callback_data="lang_hi"),
        ],
        [
            InlineKeyboardButton(LANG_NAMES["es"], callback_data="lang_es"),
            InlineKeyboardButton(LANG_NAMES["ru"], callback_data="lang_ru"),
        ],
        [
            InlineKeyboardButton(LANG_NAMES["zh"], callback_data="lang_zh"),
            InlineKeyboardButton(LANG_NAMES["ar"], callback_data="lang_ar"),
        ],
        [
            InlineKeyboardButton(LANG_NAMES["fr"], callback_data="lang_fr"),
            InlineKeyboardButton(LANG_NAMES["pt"], callback_data="lang_pt"),
        ],
        [
            InlineKeyboardButton(LANG_NAMES["de"], callback_data="lang_de"),
            InlineKeyboardButton(LANG_NAMES["id"], callback_data="lang_id"),
        ],
        [InlineKeyboardButton(t("btn_back", lang), callback_data="menu")],
    ]
    return InlineKeyboardMarkup(keyboard)


def shop_keyboard(lang: str) -> InlineKeyboardMarkup:
    """List every product as a button, plus My Orders and Back."""
    rows = []
    for p in catalog.all_products():
        stock = db.get_stock(p["id"])
        sold_out = stock is not None and stock <= 0
        label = f"{p['name']} — ${p['price']:.2f}"
        if sold_out:
            label = f"❌ {label}"
        rows.append([InlineKeyboardButton(label, callback_data=f"prod_{p['id']}")])
    rows.append([InlineKeyboardButton(t("btn_orders", lang), callback_data="orders")])
    rows.append([InlineKeyboardButton(t("btn_back", lang), callback_data="menu")])
    return InlineKeyboardMarkup(rows)


def product_keyboard(lang: str, product_id: str, can_buy: bool) -> InlineKeyboardMarkup:
    rows = []
    if can_buy:
        rows.append(
            [InlineKeyboardButton(t("btn_buy", lang), callback_data=f"buy_{product_id}")]
        )
    else:
        rows.append(
            [InlineKeyboardButton(t("btn_deposit_now", lang), callback_data="deposit")]
        )
    rows.append([InlineKeyboardButton(t("btn_back_shop", lang), callback_data="products")])
    return InlineKeyboardMarkup(rows)


def confirm_keyboard(lang: str, product_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(t("btn_confirm", lang), callback_data=f"confirm_{product_id}")],
            [InlineKeyboardButton(t("btn_back_shop", lang), callback_data="products")],
        ]
    )


def orders_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(t("btn_back_shop", lang), callback_data="products")]]
    )


def back_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(t("btn_back", lang), callback_data="menu")]]
    )


def cancel_deposit_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(t("btn_cancel", lang), callback_data="menu")]]
    )


def refer_keyboard(lang: str, share_url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(t("btn_share", lang), url=share_url)],
            [InlineKeyboardButton(t("btn_back", lang), callback_data="menu")],
        ]
    )


# ---------------------------------------------------------------------------
# Misc helpers
# ---------------------------------------------------------------------------
def make_qr_png(payload: str) -> io.BytesIO:
    img = qrcode.make(payload)
    buf = io.BytesIO()
    buf.name = "deposit_qr.png"
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


def _make_unique_amount(base_amount: float) -> float:
    """
    Add a tiny unique tail so we can tell users' payments apart, while keeping
    the extra cost negligible. The tail is just 1..99 cents (e.g. 10.01–10.99),
    so a $10 deposit becomes something like 10.07 — at most ~$0.99 extra, and
    usually a couple of cents.
    """
    for _ in range(99):
        tail = random.randint(1, 99) / 100.0  # 0.01 .. 0.99
        candidate = round(base_amount + tail, 2)
        if not db.unique_amount_taken(candidate):
            return candidate
    # Fallback (almost never hit): just add a random cent tail anyway.
    return round(base_amount + random.randint(1, 99) / 100.0, 2)


def _crypto_configured() -> bool:
    return (
        BEP20_ADDRESS.startswith("0x")
        and len(BEP20_ADDRESS) == 42
        and BEP20_ADDRESS != "0xYourBep20WalletAddressHere"
    )


def _referral_link(bot_username: str, user_id: int) -> str:
    return f"https://t.me/{bot_username}?start=ref{user_id}"


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    db.ensure_user(user.id)

    # Capture a referral payload like: /start ref123456789
    if context.args:
        payload = context.args[0]
        if payload.startswith("ref"):
            try:
                referrer_id = int(payload[3:])
                if db.set_referrer(user.id, referrer_id):
                    logger.info("User %s was referred by %s", user.id, referrer_id)
            except ValueError:
                pass

    lang = user_lang(user.id)
    await update.message.reply_text(
        t("welcome", lang, name=html.escape(user.first_name)),
        parse_mode="HTML",
        reply_markup=main_menu_keyboard(lang),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = user_lang(update.effective_user.id)
    await update.message.reply_text(t("help", lang), parse_mode="HTML")


# ---------------------------------------------------------------------------
# Admin product addition flow
# ---------------------------------------------------------------------------
async def send_add_product_guidance(update: Update) -> None:
    guidance = (
        "🛠 <b>Admin Product Addition Guidance</b>\n\n"
        "Naya product add karne ke liye niche diye gaye format me command bhejein:\n\n"
        "<b>Syntax / Format:</b>\n"
        "<code>/addproduct id | name | price | description | stock | delivery</code>\n\n"
        "<b>Parameters Detail:</b>\n"
        "1️⃣ <b>id</b>: Unique ID (letters, numbers, underscore. e.g. <code>netflix_1m</code>)\n"
        "2️⃣ <b>name</b>: Shop me dikhne wala naam (e.g. <code>🎬 Netflix Premium — 1 Month</code>)\n"
        "3️⃣ <b>price</b>: USD price (e.g. <code>5.00</code> ya <code>10</code>)\n"
        "4️⃣ <b>description</b>: Product description (HTML supported)\n"
        "5️⃣ <b>stock</b>: Available stock quantity (e.g. <code>20</code> ya <code>unlimited</code>)\n"
        "6️⃣ <b>delivery</b>: Buy hone par customer ko bheja jane wala detail/code/message\n\n"
        "<b>Example Command:</b>\n"
        "<code>/addproduct netflix_1m | 🎬 Netflix Premium (1 Month) | 5.00 | 4K Ultra HD Private Account | 20 | Login Email: user@example.com / Password: pass123</code>\n\n"
        "<i>Note: Har parameter ke bich me <b>|</b> (pipe) symbol hona zaroori hai.</i>"
    )
    await update.message.reply_text(guidance, parse_mode="HTML")


async def add_product_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not is_admin(user.id):
        # Non-admin user gets NO response at all (silent ignore)
        return

    full_text = update.message.text or ""
    parts_cmd = full_text.split(None, 1)
    if len(parts_cmd) < 2:
        await send_add_product_guidance(update)
        return

    args_text = parts_cmd[1].strip()
    if not args_text or args_text.lower() in ["help", "guidance"]:
        await send_add_product_guidance(update)
        return

    # Parse parameters separated by '|' (maximum 6 parts)
    parts = [p.strip() for p in args_text.split("|", 5)]
    if len(parts) < 6:
        await update.message.reply_text(
            "⚠️ <b>Invalid Format!</b>\n\n"
            "Product add karne ke liye sabhi 6 parameters (pipe <code>|</code> se separated) zaroori hain.\n\n"
            "<b>Format:</b>\n"
            "<code>/addproduct id | name | price | description | stock | delivery</code>\n\n"
            "Guidance dekhne ke liye type karein: <code>/addproduct</code>",
            parse_mode="HTML",
        )
        return

    prod_id, name, price_str, description, stock_str, delivery = parts

    # Validate Product ID
    if not prod_id or not all(c.isalnum() or c == "_" for c in prod_id):
        await update.message.reply_text(
            "❌ <b>Invalid Product ID!</b>\nID me sirf letters, numbers aur underscores (<code>_</code>) allowed hain (e.g. <code>netflix_1m</code>).",
            parse_mode="HTML",
        )
        return

    # Validate Price
    try:
        price = float(price_str.replace("$", "").strip())
        if price < 0:
            raise ValueError
    except ValueError:
        await update.message.reply_text(
            "❌ <b>Invalid Price!</b> Price numeric number hona chahiye (e.g. <code>5.00</code> ya <code>10</code>).",
            parse_mode="HTML",
        )
        return

    # Validate Stock
    stock = None
    if stock_str.lower() not in ["unlimited", "none", "null", "-1", ""]:
        try:
            stock = int(stock_str)
            if stock < 0:
                stock = None
        except ValueError:
            await update.message.reply_text(
                "❌ <b>Invalid Stock!</b> Stock quantity number (e.g. <code>50</code>) ya <code>unlimited</code> hona chahiye.",
                parse_mode="HTML",
            )
            return

    if not name or not description or not delivery:
        await update.message.reply_text(
            "❌ <b>Missing Fields!</b> Name, Description aur Delivery empty nahi ho sakte.",
            parse_mode="HTML",
        )
        return

    # Save product to Database
    db.add_product(
        product_id=prod_id,
        name=name,
        price=price,
        description=description,
        stock=stock,
        delivery=delivery,
    )

    stock_display = "Unlimited" if stock is None else str(stock)
    success_msg = (
        f"✅ <b>Product Successfully Added!</b>\n\n"
        f"🆔 <b>ID:</b> <code>{html.escape(prod_id)}</code>\n"
        f"📦 <b>Name:</b> {html.escape(name)}\n"
        f"💵 <b>Price:</b> ${price:.2f}\n"
        f"📊 <b>Stock:</b> {stock_display}\n"
        f"📝 <b>Description:</b> {html.escape(description)}\n"
        f"🚚 <b>Delivery:</b> {html.escape(delivery)}"
    )
    await update.message.reply_text(success_msg, parse_mode="HTML")


# ---------------------------------------------------------------------------
# Admin product stock management flow
# ---------------------------------------------------------------------------
async def send_stock_guidance(update: Update) -> None:
    prods = catalog.all_products()
    stock_lines = []
    if not prods:
        stock_lines.append("<i>Catalog me koi product nahi hai.</i>")
    else:
        for idx, p in enumerate(prods, 1):
            s = db.get_stock(p["id"])
            s_text = "<b>Unlimited</b>" if s is None else f"<b>{s}</b>"
            stock_lines.append(
                f"{idx}. {html.escape(p['name'])} (<code>{html.escape(p['id'])}</code>): {s_text}"
            )

    stocks_msg = "\n".join(stock_lines)

    guidance = (
        f"📊 <b>Current Stock Status:</b>\n\n"
        f"{stocks_msg}\n\n"
        f"🛠 <b>Stock Management Commands & Guidance:</b>\n\n"
        f"<b>1️⃣ Specific Quantity Set Karna:</b>\n"
        f"<code>/setstock &lt;product_id&gt; &lt;quantity&gt;</code>\n"
        f"Example: <code>/setstock netflix_1m 50</code>\n\n"
        f"<b>2️⃣ Unlimited Stock Set Karna:</b>\n"
        f"<code>/setstock &lt;product_id&gt; unlimited</code>\n"
        f"Example: <code>/setstock netflix_1m unlimited</code>\n\n"
        f"<b>3️⃣ Stock Add ya Deduct Karna:</b>\n"
        f"<code>/setstock &lt;product_id&gt; +10</code> (10 add karega)\n"
        f"<code>/setstock &lt;product_id&gt; -5</code> (5 reduce karega)"
    )
    await update.message.reply_text(guidance, parse_mode="HTML")


async def stock_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not is_admin(user.id):
        # Non-admin user gets NO response at all (silent ignore)
        return

    full_text = update.message.text or ""
    parts_cmd = full_text.split(None, 1)
    if len(parts_cmd) < 2:
        await send_stock_guidance(update)
        return

    args_str = parts_cmd[1].strip()
    args = args_str.split()
    if not args or args[0].lower() in ["help", "guidance"]:
        await send_stock_guidance(update)
        return

    prod_id = args[0].strip()
    product = catalog.get_product(prod_id)
    if not product:
        await update.message.reply_text(
            f"❌ <b>Product Not Found!</b> ID <code>{html.escape(prod_id)}</code> naam ka koi product exist nahi karta.",
            parse_mode="HTML",
        )
        return

    # If only 1 argument provided, show current stock for that product
    if len(args) == 1:
        s = db.get_stock(prod_id)
        s_text = "Unlimited" if s is None else str(s)
        await update.message.reply_text(
            f"📦 <b>Product:</b> {html.escape(product['name'])}\n"
            f"🆔 <b>ID:</b> <code>{html.escape(prod_id)}</code>\n"
            f"📊 <b>Current Stock:</b> <b>{s_text}</b>\n\n"
            f"Stock change karne ke liye syntax:\n"
            f"<code>/setstock {html.escape(prod_id)} 50</code>\n"
            f"<code>/setstock {html.escape(prod_id)} unlimited</code>\n"
            f"<code>/setstock {html.escape(prod_id)} +10</code>",
            parse_mode="HTML",
        )
        return

    val = args[1].strip()

    # Relative adjustment e.g. +10 or -5
    if val.startswith("+") or (val.startswith("-") and val[1:].isdigit()):
        try:
            delta = int(val)
        except ValueError:
            await update.message.reply_text("❌ Invalid number format.", parse_mode="HTML")
            return

        success, new_stock = db.adjust_stock(prod_id, delta)
        if not success:
            await update.message.reply_text("❌ Stock update fail ho gaya.", parse_mode="HTML")
            return

        s_text = "Unlimited" if new_stock is None else str(new_stock)
        await update.message.reply_text(
            f"✅ <b>Stock Updated Successfully!</b>\n\n"
            f"📦 <b>Product:</b> {html.escape(product['name'])}\n"
            f"🆔 <b>ID:</b> <code>{html.escape(prod_id)}</code>\n"
            f"📊 <b>New Stock:</b> <b>{s_text}</b>",
            parse_mode="HTML",
        )
        return

    # Unlimited / None
    if val.lower() in ["unlimited", "none", "null", "infinite", "-1"]:
        db.set_stock(prod_id, None)
        await update.message.reply_text(
            f"✅ <b>Stock Updated Successfully!</b>\n\n"
            f"📦 <b>Product:</b> {html.escape(product['name'])}\n"
            f"🆔 <b>ID:</b> <code>{html.escape(prod_id)}</code>\n"
            f"📊 <b>New Stock:</b> <b>Unlimited</b>",
            parse_mode="HTML",
        )
        return

    # Specific integer number
    try:
        new_stock = int(val)
        if new_stock < 0:
            raise ValueError
    except ValueError:
        await update.message.reply_text(
            "❌ <b>Invalid Stock Value!</b> Number (e.g. <code>50</code>), relative value (e.g. <code>+10</code>), ya <code>unlimited</code> specify karein.",
            parse_mode="HTML",
        )
        return

    db.set_stock(prod_id, new_stock)
    await update.message.reply_text(
        f"✅ <b>Stock Updated Successfully!</b>\n\n"
        f"📦 <b>Product:</b> {html.escape(product['name'])}\n"
        f"🆔 <b>ID:</b> <code>{html.escape(prod_id)}</code>\n"
        f"📊 <b>New Stock:</b> <b>{new_stock}</b>",
        parse_mode="HTML",
    )


# ---------------------------------------------------------------------------
# Deposit flow
# ---------------------------------------------------------------------------
async def send_deposit_instructions(chat_id: int, deposit: dict, lang: str, context) -> None:
    qr_buf = make_qr_png(BEP20_ADDRESS)
    caption = t(
        "deposit_instructions",
        lang,
        amount=deposit["unique_amount"],
        address=html.escape(BEP20_ADDRESS),
        minutes=DEPOSIT_WINDOW_MINUTES,
    )
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=InputFile(qr_buf),
        caption=caption,
        parse_mode="HTML",
        reply_markup=back_menu_keyboard(lang),
    )


async def handle_deposit_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.user_data.get("awaiting_deposit_amount"):
        return

    lang = user_lang(update.effective_user.id)
    text = (update.message.text or "").strip().replace(",", "").lstrip("$")
    try:
        base_amount = float(text)
    except ValueError:
        await update.message.reply_text(
            t("deposit_not_number", lang),
            parse_mode="HTML",
            reply_markup=cancel_deposit_keyboard(lang),
        )
        return

    if base_amount < MIN_DEPOSIT or base_amount > MAX_DEPOSIT:
        await update.message.reply_text(
            t("deposit_range", lang, min=MIN_DEPOSIT, max=MAX_DEPOSIT),
            parse_mode="HTML",
            reply_markup=cancel_deposit_keyboard(lang),
        )
        return

    if not _crypto_configured():
        await update.message.reply_text(
            t("deposit_not_configured", lang),
            parse_mode="HTML",
            reply_markup=back_menu_keyboard(lang),
        )
        context.user_data["awaiting_deposit_amount"] = False
        return

    user_id = update.effective_user.id
    unique_amount = _make_unique_amount(base_amount)
    deposit = db.create_pending_deposit(
        user_id, base_amount, unique_amount, DEPOSIT_WINDOW_MINUTES
    )
    context.user_data["awaiting_deposit_amount"] = False
    await send_deposit_instructions(update.effective_chat.id, deposit, lang, context)


# ---------------------------------------------------------------------------
# Callback (button) handler
# ---------------------------------------------------------------------------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    try:
        await query.answer()
    except BadRequest:
        pass  # callback query too old / already answered — safe to ignore
    data = query.data
    user_id = query.from_user.id
    db.ensure_user(user_id)

    # Any button press cancels an in-progress amount entry.
    context.user_data["awaiting_deposit_amount"] = False

    # Language change first (so the reply is already in the new language).
    if data.startswith("lang_"):
        code = data.split("_", 1)[1]
        if code in SUPPORTED:
            db.set_language(user_id, code)
        lang = user_lang(user_id)
        await safe_edit(
            query,
            t("language_updated", lang, lang=LANG_NAMES.get(code, "English 🇬🇧")),
            reply_markup=back_menu_keyboard(lang),
        )
        return

    lang = user_lang(user_id)

    if data == "menu":
        await safe_edit(
            query,
            t("welcome", lang, name=html.escape(query.from_user.first_name)),
            reply_markup=main_menu_keyboard(lang),
        )

    elif data == "deposit":
        context.user_data["awaiting_deposit_amount"] = True
        await safe_edit(
            query,
            t("deposit_intro", lang, min=MIN_DEPOSIT, max=MAX_DEPOSIT),
            reply_markup=cancel_deposit_keyboard(lang),
        )

    elif data == "profile":
        u = db.get_user(user_id)
        await safe_edit(
            query,
            t(
                "profile",
                lang,
                name=html.escape(query.from_user.first_name),
                user_id=user_id,
                balance=u["balance"],
                orders=u["orders"],
                referrals=u["referrals"],
                earnings=u["referral_earnings"],
            ),
            reply_markup=back_menu_keyboard(lang),
        )

    elif data == "products":
        await show_shop(query, lang)

    elif data == "orders":
        await show_orders(query, user_id, lang)

    elif data.startswith("prod_"):
        await show_product(query, data[len("prod_"):], user_id, lang)

    elif data.startswith("buy_"):
        await show_confirm(query, data[len("buy_"):], user_id, lang)

    elif data.startswith("confirm_"):
        await do_purchase(query, context, data[len("confirm_"):], user_id, lang)

    elif data == "support":
        await safe_edit(
            query,
            t("support", lang, contact=html.escape(SUPPORT_CONTACT)),
            reply_markup=back_menu_keyboard(lang),
        )

    elif data == "refer":
        u = db.get_user(user_id)
        link = _referral_link(context.bot.username, user_id)
        share_url = (
            "https://t.me/share/url?"
            + urllib.parse.urlencode({"url": link, "text": t("share_text", lang)})
        )
        await safe_edit(
            query,
            t(
                "refer",
                lang,
                referrals=u["referrals"],
                earnings=u["referral_earnings"],
                link=link,
            ),
            disable_web_page_preview=True,
            reply_markup=refer_keyboard(lang, share_url),
        )

    elif data == "language":
        await safe_edit(
            query,
            t("language_choose", lang),
            reply_markup=language_keyboard(lang),
        )


# ---------------------------------------------------------------------------
# Shop / purchase / orders
# ---------------------------------------------------------------------------
def _stock_label(product_id: str, lang: str) -> str:
    stock = db.get_stock(product_id)
    return t("stock_unlimited", lang) if stock is None else str(stock)


async def show_shop(query, lang: str) -> None:
    prods = catalog.all_products()
    if not prods:
        await query.edit_message_text(
            t("shop_empty", lang),
            parse_mode="HTML",
            reply_markup=back_menu_keyboard(lang),
        )
        return
    balance = db.get_balance(query.from_user.id)
    await query.edit_message_text(
        t("shop_list", lang, balance=balance),
        parse_mode="HTML",
        reply_markup=shop_keyboard(lang),
    )


async def show_product(query, product_id: str, user_id: int, lang: str) -> None:
    product = catalog.get_product(product_id)
    if not product:
        await show_shop(query, lang)
        return
    balance = db.get_balance(user_id)
    stock = db.get_stock(product_id)
    sold_out = stock is not None and stock <= 0
    can_buy = (not sold_out) and balance >= product["price"]

    if sold_out:
        await query.edit_message_text(
            t("out_of_stock", lang),
            parse_mode="HTML",
            reply_markup=product_keyboard(lang, product_id, can_buy=False),
        )
        return

    await query.edit_message_text(
        t(
            "product_detail",
            lang,
            name=html.escape(product["name"]),
            description=product["description"],
            price=product["price"],
            stock=_stock_label(product_id, lang),
            balance=balance,
        ),
        parse_mode="HTML",
        reply_markup=product_keyboard(lang, product_id, can_buy),
    )


async def show_confirm(query, product_id: str, user_id: int, lang: str) -> None:
    product = catalog.get_product(product_id)
    if not product:
        await show_shop(query, lang)
        return
    balance = db.get_balance(user_id)
    if balance < product["price"]:
        await query.edit_message_text(
            t("insufficient", lang, price=product["price"], balance=balance),
            parse_mode="HTML",
            reply_markup=product_keyboard(lang, product_id, can_buy=False),
        )
        return
    await query.edit_message_text(
        t(
            "confirm_purchase",
            lang,
            name=html.escape(product["name"]),
            price=product["price"],
            after=balance - product["price"],
        ),
        parse_mode="HTML",
        reply_markup=confirm_keyboard(lang, product_id),
    )


async def do_purchase(query, context, product_id: str, user_id: int, lang: str) -> None:
    product = catalog.get_product(product_id)
    if not product:
        await show_shop(query, lang)
        return

    result = db.purchase(user_id, product)

    if not result["ok"]:
        if result["reason"] == "insufficient":
            await query.edit_message_text(
                t("insufficient", lang, price=result["price"], balance=result["balance"]),
                parse_mode="HTML",
                reply_markup=product_keyboard(lang, product_id, can_buy=False),
            )
        else:  # out_of_stock / unknown
            await query.edit_message_text(
                t("out_of_stock", lang),
                parse_mode="HTML",
                reply_markup=orders_keyboard(lang),
            )
        return

    await query.edit_message_text(
        t(
            "order_success",
            lang,
            order_id=result["order_id"],
            name=html.escape(product["name"]),
            price=product["price"],
            balance=result["new_balance"],
            delivery=product["delivery"],
        ),
        parse_mode="HTML",
        reply_markup=orders_keyboard(lang),
    )
    logger.info(
        "User %s bought %s (order #%s) for %.2f",
        user_id, product_id, result["order_id"], product["price"],
    )


async def show_orders(query, user_id: int, lang: str) -> None:
    orders = db.get_orders(user_id)
    if not orders:
        await query.edit_message_text(
            t("orders_empty", lang),
            parse_mode="HTML",
            reply_markup=orders_keyboard(lang),
        )
        return
    lines = [t("orders_header", lang)]
    for o in orders:
        lines.append(
            t(
                "orders_line",
                lang,
                order_id=o["id"],
                name=html.escape(o["product_name"]),
                price=o["price"],
            )
        )
    await query.edit_message_text(
        "\n".join(lines),
        parse_mode="HTML",
        reply_markup=orders_keyboard(lang),
    )


# ---------------------------------------------------------------------------
# Background payment watcher
# ---------------------------------------------------------------------------
async def poll_deposits(context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _crypto_configured():
        return

    db.expire_old_deposits()
    open_deposits = db.get_open_deposits()
    if not open_deposits:
        return

    transfers = await asyncio.to_thread(get_incoming_usdt_transfers, BEP20_ADDRESS)
    if not transfers:
        return

    by_amount = {round(tx["amount"], 4): tx for tx in transfers}

    for dep in open_deposits:
        target = round(dep["unique_amount"], 4)
        tx = by_amount.get(target)
        if not tx:
            continue

        db.mark_paid(dep["id"], tx["tx_hash"])
        new_balance = db.credit_balance(dep["user_id"], dep["base_amount"])
        logger.info(
            "Credited user %s with %.2f (tx %s)",
            dep["user_id"], dep["base_amount"], tx["tx_hash"],
        )

        # Notify the depositor in their language.
        dep_lang = user_lang(dep["user_id"])
        try:
            await context.bot.send_message(
                chat_id=dep["user_id"],
                text=t(
                    "deposit_received",
                    dep_lang,
                    amount=dep["unique_amount"],
                    credited=dep["base_amount"],
                    balance=new_balance,
                ),
                parse_mode="HTML",
                reply_markup=back_menu_keyboard(dep_lang),
            )
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not notify user %s: %s", dep["user_id"], exc)

        # Reward the referrer with a percentage of qualifying deposits.
        reward = db.reward_referrer_for_deposit(dep["user_id"], dep["base_amount"])
        if reward:
            ref_lang = user_lang(reward["referrer_id"])
            try:
                await context.bot.send_message(
                    chat_id=reward["referrer_id"],
                    text=t(
                        "referral_bonus_notify",
                        ref_lang,
                        reward=reward["reward"],
                        balance=reward["new_referrer_balance"],
                    ),
                    parse_mode="HTML",
                    reply_markup=back_menu_keyboard(ref_lang),
                )
            except Exception as exc:  # noqa: BLE001
                logger.warning(
                    "Could not notify referrer %s: %s", reward["referrer_id"], exc
                )


# ---------------------------------------------------------------------------
# App bootstrap
# ---------------------------------------------------------------------------
def start_health_check_server() -> None:
    """Start a lightweight HTTP server to pass Render web service health checks."""
    from http.server import BaseHTTPRequestHandler, HTTPServer
    class HealthHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        def log_message(self, format, *args):
            pass

    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    logger.info("Health check HTTP server listening on port %s", port)
    server.serve_forever()


def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "BOT_TOKEN environment variable is not set. "
            "Get a token from @BotFather and set it before running."
        )

    # Start HTTP server thread for cloud platforms like Render
    threading.Thread(target=start_health_check_server, daemon=True).start()

    db.init_db()
    db.seed_products(catalog.PRODUCTS)

    if not _crypto_configured():
        logger.warning(
            "BEP20_ADDRESS not set (or invalid) in .env — crypto deposits are "
            "disabled until you set a valid 0x... address."
        )
    else:
        logger.info(
            "Crypto deposits enabled (no API key needed) — watching %s via public BSC RPC.",
            BEP20_ADDRESS,
        )

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("addproduct", add_product_command))
    application.add_handler(CommandHandler("add_product", add_product_command))
    application.add_handler(CommandHandler("stock", stock_command))
    application.add_handler(CommandHandler("setstock", stock_command))
    application.add_handler(CommandHandler("addstock", stock_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_deposit_amount)
    )

    application.job_queue.run_repeating(poll_deposits, interval=POLL_INTERVAL, first=10)

    logger.info("Bot is starting... Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
