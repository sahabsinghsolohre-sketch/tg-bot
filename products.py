"""
Product catalog for the Shop.

HOW TO ADD / EDIT PRODUCTS
----------------------------
  /addproduct id | name | price | description | stock | delivery
  /editproduct <id> stock 50
  /editproduct <id> account email:password
  /removeproduct <id>
"""

PRODUCTS = [
    # ------------------------------------------------------------------ Canva
    {
        "id": "canva_pro_1m",
        "name": "✏️ Canva Pro — 1 Month",
        "price": 2.00,
        "description": (
            "<b>Unlock Canva's full creative suite</b> — 610,000+ premium templates, "
            "AI-powered Magic Studio, brand kits and 1 TB cloud storage.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$2.00</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🖼  Templates    —  <b>610,000+ premium</b>\n"
            "🤖  AI Tools      —  <b>Magic Studio, Text to Image</b>\n"
            "☁️  Storage       —  <b>1 TB cloud storage</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Canva Pro (1 Month) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    {
        "id": "canva_edu_3y",
        "name": "✏️ Canva Pro EDU Invite — 3 Years",
        "price": 1.00,
        "description": (
            "<b>Get Canva Pro free via an official Education invite</b> — "
            "all Pro features unlocked on your own account for 3 full years.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$1.00</b>\n"
            "📅  Duration     —  <b>3 Years</b>\n"
            "🎓  Type          —  <b>Education invite (your own account)</b>\n"
            "✅  Features     —  <b>Full Canva Pro access</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Canva Pro EDU (3 Years) — Order Confirmed!</b>\n\n"
            "Your invite link will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ YouTube
    {
        "id": "youtube_3m",
        "name": "▶️ YouTube Premium — 3 Months",
        "price": 3.50,
        "description": (
            "<b>Watch YouTube completely ad-free, offline and in the background</b> — "
            "YouTube Music Premium included at no extra cost.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$3.50</b>\n"
            "📅  Duration     —  <b>3 Months</b>\n"
            "🚫  Ads            —  <b>100% ad-free</b>\n"
            "📲  Background —  <b>Play with screen off</b>\n"
            "🎵  Bonus         —  <b>YouTube Music included</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>YouTube Premium (3 Months) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Adobe
    {
        "id": "adobe_cc_4m",
        "name": "🎨 Adobe CC — 4 Months Official",
        "price": 3.00,
        "description": (
            "<b>Full Adobe Creative Cloud suite</b> — 20+ industry-leading apps "
            "including Photoshop, Illustrator, Premiere Pro, Acrobat Pro and "
            "Adobe Firefly AI.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$3.00</b>\n"
            "📅  Duration     —  <b>4 Months</b>\n"
            "🖥  Apps           —  <b>Photoshop, Illustrator, Premiere &amp; 20+ more</b>\n"
            "🤖  AI              —  <b>Adobe Firefly AI included</b>\n"
            "☁️  Storage       —  <b>100 GB cloud storage</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Adobe CC (4 Months) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Amazon
    {
        "id": "amazon_prime_6m",
        "name": "📦 Amazon Prime — 6 Months",
        "price": 2.50,
        "description": (
            "<b>Six months of Amazon Prime</b> — free fast delivery, "
            "Prime Video, Prime Music and exclusive member deals.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$2.50</b>\n"
            "📅  Duration     —  <b>6 Months</b>\n"
            "🚚  Delivery     —  <b>Free fast delivery</b>\n"
            "🎬  Video         —  <b>Prime Video included</b>\n"
            "🎵  Music         —  <b>Prime Music included</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Amazon Prime (6 Months) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Netflix
    {
        "id": "netflix_649",
        "name": "🎬 Netflix Premium — Private Account",
        "price": 2.50,
        "description": (
            "<b>Your own private Netflix Premium account</b> — "
            "4K Ultra HD streaming with Dolby Atmos and HDR on all devices.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$2.50</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "👤  Account      —  <b>Private (yours only)</b>\n"
            "📺  Quality       —  <b>4K Ultra HD + HDR</b>\n"
            "🔊  Audio         —  <b>Dolby Atmos</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Netflix Premium (Private Account) — Order Confirmed!</b>\n\n"
            "Your private account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Microsoft Office
    {
        "id": "office365_100gb",
        "name": "💼 Microsoft 365 Personal — 5 Months",
        "price": 2.77,
        "description": (
            "<b>Full Microsoft 365 Personal subscription</b> — Word, Excel, "
            "PowerPoint, Outlook and 100 GB OneDrive across all your devices.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$2.77</b>\n"
            "📅  Duration     —  <b>5 Months</b>\n"
            "💻  Apps           —  <b>Word, Excel, PowerPoint, Outlook</b>\n"
            "☁️  Storage       —  <b>100 GB OneDrive</b>\n"
            "📱  Devices       —  <b>PC, Mac, Mobile, Tablet</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Microsoft 365 Personal — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    {
        "id": "office365_family",
        "name": "🏠 Microsoft 365 Family — 5 Members",
        "price": 4.00,
        "description": (
            "<b>Microsoft 365 Family plan — share with up to 5 members</b> — "
            "everyone gets the full Office suite plus 1 TB OneDrive each.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$4.00</b>\n"
            "📅  Duration     —  <b>5 Months</b>\n"
            "👥  Members     —  <b>Up to 5 users</b>\n"
            "☁️  Storage       —  <b>1 TB OneDrive per user</b>\n"
            "💻  Apps           —  <b>Full Office suite on all devices</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Microsoft 365 Family — Order Confirmed!</b>\n\n"
            "Admin account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Surfshark
    {
        "id": "surfshark_vpn",
        "name": "🦈 Surfshark VPN — 1 Month",
        "price": 3.50,
        "description": (
            "<b>One of the fastest VPNs — unlimited devices, one account</b> — "
            "3,200+ servers in 100+ countries with strict no-logs policy.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$3.50</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🌍  Servers       —  <b>3,200+ in 100+ countries</b>\n"
            "📱  Devices       —  <b>Unlimited simultaneous</b>\n"
            "🔒  Privacy       —  <b>No-logs, AES-256 encryption</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Surfshark VPN — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Windows
    {
        "id": "windows10_pro",
        "name": "🪟 Windows 10 Pro — Retail Key",
        "price": 2.77,
        "description": (
            "<b>Genuine Windows 10 Pro retail activation key</b> — "
            "lifetime licence with BitLocker, Remote Desktop and Hyper-V. "
            "Upgradeable to Windows 11.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$2.77</b>\n"
            "📅  Duration     —  <b>Lifetime</b>\n"
            "🔑  Type          —  <b>Retail Key (1 PC)</b>\n"
            "🛡  Features     —  <b>BitLocker, Remote Desktop, Hyper-V</b>\n"
            "⬆️  Upgrade       —  <b>Upgradeable to Windows 11</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Windows 10 Pro Key — Order Confirmed!</b>\n\n"
            "Your activation key will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    {
        "id": "windows11_pro",
        "name": "🪟 Windows 11 Pro — Lifetime Key",
        "price": 2.77,
        "description": (
            "<b>Genuine Windows 11 Pro lifetime activation key</b> — "
            "the latest Windows with Snap layouts, DirectStorage, "
            "Auto HDR and enhanced security.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$2.77</b>\n"
            "📅  Duration     —  <b>Lifetime</b>\n"
            "🔑  Type          —  <b>Retail Key (1 PC)</b>\n"
            "🛡  Features     —  <b>BitLocker, TPM 2.0, Secure Boot</b>\n"
            "🎮  Gaming        —  <b>DirectStorage &amp; Auto HDR</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Windows 11 Pro Key — Order Confirmed!</b>\n\n"
            "Your activation key will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ ChatGPT
    {
        "id": "chatgptplus_1m",
        "name": "🤖 ChatGPT Plus — 1 Month",
        "price": 6.00,
        "description": (
            "<b>OpenAI's most advanced AI — GPT-4o, image generation and "
            "real-time web browsing</b> in one subscription.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$6.00</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🧠  Models        —  <b>GPT-4o, GPT-4o mini</b>\n"
            "🎨  Image Gen    —  <b>DALL·E 3 included</b>\n"
            "🌐  Web Access  —  <b>Real-time browsing</b>\n"
            "📱  Platform     —  <b>Mobile &amp; PC</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>ChatGPT Plus (1 Month) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ QuillBot
    {
        "id": "quillbot_1m",
        "name": "✍️ QuillBot Premium — 1 Month",
        "price": 2.20,
        "description": (
            "<b>AI writing assistant trusted by 35 million users</b> — "
            "unlimited paraphrasing in all modes, advanced grammar check "
            "and unlimited summarising.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$2.20</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "✏️  Paraphrase  —  <b>Unlimited (all 9 modes)</b>\n"
            "📝  Grammar     —  <b>Advanced grammar checker</b>\n"
            "📄  Summariser —  <b>Unlimited summarising</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>QuillBot Premium (1 Month) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Coursera
    {
        "id": "coursera_plus_12m",
        "name": "🎓 Coursera Plus — 12 Months",
        "price": 6.50,
        "description": (
            "<b>Unlimited access to 7,000+ courses from world's top universities</b> — "
            "Google, Meta, IBM and 325+ institutions with certificates included.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$6.50</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "📚  Courses     —  <b>7,000+ courses &amp; projects</b>\n"
            "🏆  Certificates —  <b>Professional certs included</b>\n"
            "🏛  Partners     —  <b>Google, Meta, IBM &amp; 325+ unis</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Coursera Plus (12 Months) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Kiro
    {
        "id": "kiro_pro_1m",
        "name": "⚡ Kiro Pro — 1 Month",
        "price": 6.00,
        "description": (
            "<b>AWS's AI-powered IDE — spec-driven development at its best.</b>\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$6.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>1,000 credits</b>\n"
            "🤖  Models        —  <b>Claude Sonnet 4.5 + open-weight</b>\n"
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
    {
        "id": "kiro_pro_plus_1m",
        "name": "⚡ Kiro Pro+ — 1 Month",
        "price": 12.00,
        "description": (
            "<b>Double the power for demanding development workflows.</b>\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$12.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>2,000 credits</b>\n"
            "🤖  Models        —  <b>Claude Sonnet 5 + premium models</b>\n"
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
    {
        "id": "kiro_pro_max_1m",
        "name": "🚀 Kiro Pro Max — 1 Month",
        "price": 31.00,
        "description": (
            "<b>For power users and professional teams — Claude Opus 5.</b>\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$31.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>5,000 credits</b>\n"
            "🤖  Models        —  <b>Claude Opus 5 + all premium</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Kiro Pro Max (1 Month) — Order Confirmed!</b>\n\n"
            "Your access credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    {
        "id": "kiro_power_1m",
        "name": "👑 Kiro Power — 1 Month",
        "price": 59.00,
        "description": (
            "<b>The ultimate Kiro plan — maximum credits, all models unlocked.</b>\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$59.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>10,000 credits</b>\n"
            "🤖  Models        —  <b>All models including Claude Opus 5</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": (
            "✅ <b>Kiro Power (1 Month) — Order Confirmed!</b>\n\n"
            "Your access credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
]


import db


def all_products() -> list:
    db_prods = db.get_all_products()
    if db_prods:
        return db_prods
    return PRODUCTS


def get_product(product_id: str) -> dict | None:
    p = db.get_product(product_id)
    if p:
        return p
    for item in PRODUCTS:
        if item["id"] == product_id:
            return item
    return None
