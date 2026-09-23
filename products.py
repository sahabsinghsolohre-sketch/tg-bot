"""
Product catalog for the Shop.

HOW TO ADD / EDIT PRODUCTS
--------------------------
Just edit the PRODUCTS list below. Each product is a dict with:

    "id"          : short unique string (letters/numbers/underscores). Don't reuse ids.
    "name"        : display name shown in the shop.
    "price"       : price in USD (float). Balance is deducted by this amount.
    "description" : short text shown on the product page (HTML allowed).
    "stock"       : how many are available. Use None for unlimited.
    "delivery"    : the content the buyer receives after purchase (HTML allowed).
                    e.g. an account, a code, a license key, or instructions.

Example of adding a new product — copy a block and change the values:

    {
        "id": "spotify_1m",
        "name": "🎵 Spotify Premium — 1 Month",
        "price": 2.50,
        "description": "Private Spotify Premium upgrade on your own account.",
        "stock": 20,
        "delivery": "Send your Spotify email to support and we'll upgrade it.",
    },

Notes:
  - Stock is decremented automatically on each successful purchase.
  - For real digital goods you'd usually store one-time codes; here `delivery`
    is a single message sent to every buyer. Keep it generic or wire it to your
    own fulfilment later.
"""

PRODUCTS = [
    {
        "id": "kiro_pro_1m",
        "name": "⚡ Kiro Pro — 1 Month",
        "price": 9.00,
        "description": (
            "⚡ <b>Kiro Pro</b> — perfect for everyday use.\n\n"
            "💵 Rate: <b>$9</b> / month\n"
            "⏳ Duration: <b>1 month</b>\n"
            "🎟 Credits: <b>1,000</b> credits\n"
            "🔄 Replacement: <b>Yes</b> — free replacement if it stops working"
        ),
        "stock": 100,
        "delivery": (
            "✅ Your <b>Kiro Pro (1 Month)</b> order is confirmed!\n"
            "Your access details will be delivered by support shortly.\n"
            "Keep your order ID handy for any replacement request."
        ),
    },
    {
        "id": "kiro_pro_plus_1m",
        "name": "✨ Kiro Pro+ — 1 Month",
        "price": 13.00,
        "description": (
            "✨ <b>Kiro Pro+</b> — more power for heavier workflows.\n\n"
            "💵 Rate: <b>$13</b> / month\n"
            "⏳ Duration: <b>1 month</b>\n"
            "🎟 Credits: <b>2,000</b> credits\n"
            "🔄 Replacement: <b>Yes</b> — free replacement if it stops working"
        ),
        "stock": 100,
        "delivery": (
            "✅ Your <b>Kiro Pro+ (1 Month)</b> order is confirmed!\n"
            "Your access details will be delivered by support shortly.\n"
            "Keep your order ID handy for any replacement request."
        ),
    },
    {
        "id": "kiro_pro_max_1m",
        "name": "🚀 Kiro Pro Max — 1 Month",
        "price": 35.00,
        "description": (
            "🚀 <b>Kiro Pro Max</b> — for power users and teams.\n\n"
            "💵 Rate: <b>$35</b> / month\n"
            "⏳ Duration: <b>1 month</b>\n"
            "🎟 Credits: <b>6,000</b> credits\n"
            "🔄 Replacement: <b>Yes</b> — free replacement if it stops working"
        ),
        "stock": 50,
        "delivery": (
            "✅ Your <b>Kiro Pro Max (1 Month)</b> order is confirmed!\n"
            "Your access details will be delivered by support shortly.\n"
            "Keep your order ID handy for any replacement request."
        ),
    },
    {
        "id": "kiro_power_1m",
        "name": "👑 Kiro Power — 1 Month",
        "price": 70.00,
        "description": (
            "👑 <b>Kiro Power</b> — the ultimate plan, maximum limits.\n\n"
            "💵 Rate: <b>$70</b> / month\n"
            "⏳ Duration: <b>1 month</b>\n"
            "🎟 Credits: <b>15,000</b> credits\n"
            "🔄 Replacement: <b>Yes</b> — free replacement if it stops working"
        ),
        "stock": 25,
        "delivery": (
            "✅ Your <b>Kiro Power (1 Month)</b> order is confirmed!\n"
            "Your access details will be delivered by support shortly.\n"
            "Keep your order ID handy for any replacement request."
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
