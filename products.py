"""
Product catalog for the Shop.

HOW TO ADD PRODUCTS
-------------------
Use /addproduct command in Telegram (admin only):
   /addproduct id | name | price | description | stock | delivery

HOW TO ADD STOCK / ACCOUNTS
----------------------------
   /addstock <product_id> email:password
"""

PRODUCTS = [
    # ------------------------------------------------------------------ ChatGPT Plus
    {
        "id": "chatgptplus_1m",
        "name": "🤖 ChatGPT Plus — 1 Month",
        "price": 7.00,
        "description": (
            "Access OpenAI's most advanced AI — smarter answers, image generation, "
            "and real-time web browsing, all in one subscription.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$7.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🧠  Models        —  <b>GPT-4o, GPT-4o mini</b>\n"
            "🎨  Image Gen    —  <b>DALL·E 3 included</b>\n"
            "🌐  Web Access  —  <b>Real-time browsing</b>\n"
            "📱  Platform     —  <b>Mobile &amp; PC</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 0,
        "delivery": (
            "✅ <b>ChatGPT Plus (1 Month) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Netflix
    {
        "id": "netflix_649",
        "name": "🎬 Netflix Premium — Private Account",
        "price": 2.00,
        "description": (
            "Your own private Netflix Premium account — enjoy the highest-quality "
            "streaming experience with 4K Ultra HD and Dolby Atmos sound.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$2.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "👤  Account      —  <b>Private (yours only)</b>\n"
            "👨‍👩‍👧‍👦  Profiles      —  <b>Up to 5 Profiles</b>\n"
            "📺  Quality       —  <b>4K Ultra HD + HDR</b>\n"
            "🔊  Audio         —  <b>Dolby Atmos</b>\n"
            "📲  Devices       —  <b>TV, Mobile, PC, Tablet</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 0,
        "delivery": (
            "✅ <b>Netflix Premium (Private Account) — Order Confirmed!</b>\n\n"
            "Your private account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Kiro Pro
    {
        "id": "kiro_pro_1m",
        "name": "⚡ Kiro Pro — 1 Month",
        "price": 7.00,
        "description": (
            "Kiro is AWS's AI-powered IDE that writes specs before code — "
            "turning your ideas into production-ready software faster than ever.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$7.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>1,000 credits</b>\n"
            "🤖  Models        —  <b>Claude Sonnet 4.5 + open-weight</b>\n"
            "⚙️  Agents         —  <b>Spec-driven autonomous agents</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Kiro Pro (1 Month) — Order Confirmed!</b>\n\n"
            "Your access credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Kiro Pro+
    {
        "id": "kiro_pro_plus_1m",
        "name": "✨ Kiro Pro+ — 1 Month",
        "price": 13.00,
        "description": (
            "Double the power of Kiro Pro — built for developers who push the limits "
            "of what AI can build.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$13.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>2,000 credits</b>\n"
            "🤖  Models        —  <b>Claude Sonnet 5 + premium models</b>\n"
            "⚙️  Agents         —  <b>Parallel autonomous agents</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Kiro Pro+ (1 Month) — Order Confirmed!</b>\n\n"
            "Your access credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Kiro Pro Max
    {
        "id": "kiro_pro_max_1m",
        "name": "🚀 Kiro Pro Max — 1 Month",
        "price": 32.00,
        "description": (
            "For power users and professional teams — Claude Opus 5 access with "
            "5,000 credits for large-scale, complex codebases.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$32.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>5,000 credits</b>\n"
            "🤖  Models        —  <b>Claude Opus 5 + all premium models</b>\n"
            "⚙️  Agents         —  <b>High-capacity parallel agents</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 50,
        "delivery": (
            "✅ <b>Kiro Pro Max (1 Month) — Order Confirmed!</b>\n\n"
            "Your access credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Kiro Power
    {
        "id": "kiro_power_1m",
        "name": "👑 Kiro Power — 1 Month",
        "price": 60.00,
        "description": (
            "The ultimate Kiro plan — maximum credits, all models unlocked, "
            "designed for teams building at enterprise scale.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$60.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>10,000 credits</b>\n"
            "🤖  Models        —  <b>All models including Claude Opus 5</b>\n"
            "⚙️  Agents         —  <b>Unlimited parallel agents</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 25,
        "delivery": (
            "✅ <b>Kiro Power (1 Month) — Order Confirmed!</b>\n\n"
            "Your access credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
]


import db


def all_products() -> list:
    """Return all products from the database; fall back to static list if DB is empty."""
    db_prods = db.get_all_products()
    if db_prods:
        return db_prods
    return PRODUCTS


def get_product(product_id: str) -> dict | None:
    """Look up a single product by its id — DB first, then static fallback."""
    p = db.get_product(product_id)
    if p:
        return p
    for item in PRODUCTS:
        if item["id"] == product_id:
            return item
    return None
