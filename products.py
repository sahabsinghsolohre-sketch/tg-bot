"""
Product catalog for the Shop.

HOW TO ADD / EDIT PRODUCTS
--------------------------
Each product is a dict with:
    "id"          : short unique string (letters/numbers/underscores).
    "name"        : display name shown in the shop.
    "price"       : price in USD (float).
    "description" : structured text shown on the product page (HTML allowed).
    "stock"       : how many are available. Use None for unlimited.
    "delivery"    : default delivery text.
"""

PRODUCTS = [
    {
        "id": "chatgptplus_1m",
        "name": "🤖 ChatGPT Plus — 1 Month",
        "price": 8.00,
        "description": (
            "🤖 <b>ChatGPT Plus</b> — GPT-4o, DALL-E 3 & Web Browsing.\n\n"
            "💵 Rate: <b>$8 / month</b>\n"
            "⏳ Duration: <b>1 month</b>\n"
            "📱 Platform: <b>Mobile & PC</b>\n"
            "🔄 Replacement: <b>No</b> — no replacement provided"
        ),
        "stock": 0,
        "delivery": "Digital Account Credentials",
    },
    {
        "id": "kiro_pro_1m",
        "name": "⚡ Kiro Pro — 1 Month",
        "price": 9.00,
        "description": (
            "⚡ <b>Kiro Pro</b> — perfect for everyday use.\n\n"
            "💵 Rate: <b>$9 / month</b>\n"
            "⏳ Duration: <b>1 month</b>\n"
            "🎟 Credits: <b>1,000 credits</b>\n"
            "🔄 Replacement: <b>No</b> — no replacement provided"
        ),
        "stock": 100,
        "delivery": (
            "✅ Your <b>Kiro Pro (1 Month)</b> order is confirmed!\n"
            "Your access details will be delivered shortly."
        ),
    },
    {
        "id": "kiro_pro_plus_1m",
        "name": "✨ Kiro Pro+ — 1 Month",
        "price": 13.00,
        "description": (
            "✨ <b>Kiro Pro+</b> — more power for heavier workflows.\n\n"
            "💵 Rate: <b>$13 / month</b>\n"
            "⏳ Duration: <b>1 month</b>\n"
            "🎟 Credits: <b>2,000 credits</b>\n"
            "🔄 Replacement: <b>No</b> — no replacement provided"
        ),
        "stock": 100,
        "delivery": (
            "✅ Your <b>Kiro Pro+ (1 Month)</b> order is confirmed!\n"
            "Your access details will be delivered shortly."
        ),
    },
    {
        "id": "kiro_pro_max_1m",
        "name": "🚀 Kiro Pro Max — 1 Month",
        "price": 35.00,
        "description": (
            "🚀 <b>Kiro Pro Max</b> — for power users and teams.\n\n"
            "💵 Rate: <b>$35 / month</b>\n"
            "⏳ Duration: <b>1 month</b>\n"
            "🎟 Credits: <b>6,000 credits</b>\n"
            "🔄 Replacement: <b>No</b> — no replacement provided"
        ),
        "stock": 50,
        "delivery": (
            "✅ Your <b>Kiro Pro Max (1 Month)</b> order is confirmed!\n"
            "Your access details will be delivered shortly."
        ),
    },
    {
        "id": "kiro_power_1m",
        "name": "👑 Kiro Power — 1 Month",
        "price": 70.00,
        "description": (
            "👑 <b>Kiro Power</b> — the ultimate plan, maximum limits.\n\n"
            "💵 Rate: <b>$70 / month</b>\n"
            "⏳ Duration: <b>1 month</b>\n"
            "🎟 Credits: <b>15,000 credits</b>\n"
            "🔄 Replacement: <b>No</b> — no replacement provided"
        ),
        "stock": 25,
        "delivery": (
            "✅ Your <b>Kiro Power (1 Month)</b> order is confirmed!\n"
            "Your access details will be delivered shortly."
        ),
    },
]


import db


def all_products() -> list:
    """Return all products from the database, falling back to static PRODUCTS if empty."""
    db_prods = db.get_all_products()
    if db_prods:
        return db_prods
    return PRODUCTS


def get_product(product_id: str) -> dict | None:
    """Look up a single product by its id from the database."""
    p = db.get_product(product_id)
    if p:
        return p
    for item in PRODUCTS:
        if item["id"] == product_id:
            return item
    return None
