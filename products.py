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
        "stock": 39,
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
        "stock": 14,
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
        "stock": 46,
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
        "stock": 81,
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
        "stock": 17,
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
        "stock": 93,
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
        "stock": 5,
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
        "stock": 65,
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
        "stock": 55,
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
        "stock": 13,
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
        "stock": 10,
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
        "stock": 74,
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
        "stock": 76,
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
        "stock": 8,
        "delivery": (
            "✅ <b>Coursera Plus (12 Months) — Order Confirmed!</b>\n\n"
            "Your account credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ------------------------------------------------------------------ Kiro
    {
        "id": "kiro_pro_max_1m",
        "name": "🚀 Kiro Pro Max — 1 Month",
        "price": 27.00,
        "description": (
            "<b>For power users and professional teams — Claude Opus 5.</b>\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$27.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>5,000 credits</b>\n"
            "🤖  Models        —  <b>Claude Opus 5 + all premium</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 59,
        "delivery": (
            "✅ <b>Kiro Pro Max (1 Month) — Order Confirmed!</b>\n\n"
            "Your access credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    {
        "id": "kiro_power_1m",
        "name": "👑 Kiro Power — 1 Month",
        "price": 35.00,
        "description": (
            "<b>The ultimate Kiro plan — maximum credits, all models unlocked.</b>\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$35.00 / month</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🎟  Credits       —  <b>10,000 credits</b>\n"
            "🤖  Models        —  <b>All models including Claude Opus 5</b>\n"
            "🔄  Replacement —  <b>No</b>"
            "</blockquote>"
        ),
        "stock": 87,
        "delivery": (
            "✅ <b>Kiro Power (1 Month) — Order Confirmed!</b>\n\n"
            "Your access credentials will be delivered by support shortly.\n"
            "📌 Keep your <b>Order ID</b> handy for reference."
        ),
    },
    # ================================================================== NEW PRODUCTS
    # ------------------------------------------------------------------ Lenny's Bundle
    {
        "id": "lennys_bundle",
        "name": "🎁 Lenny's Pass — Products Bundle",
        "price": 45.00,
        "description": (
            "<b>The ultimate Lenny's Pass — a curated bundle of premium tools "
            "and subscriptions in one massive package.</b>\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$45.00</b>\n"
            "📦  Type          —  <b>Full products bundle</b>\n"
            "🎯  Value          —  <b>Best value pack</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Lenny's Pass Bundle — Order Confirmed!</b>\n\nYour bundle access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ ChatGPT Plus 4M
    {
        "id": "chatgpt_plus_4m",
        "name": "🤖 ChatGPT Plus — 4 Months (Scheduled FW)",
        "price": 18.00,
        "description": (
            "<b>ChatGPT Plus for 4 months on a scheduled activation</b> — "
            "GPT-4o, DALL·E 3, web browsing. Full warranty.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$18.00</b>\n"
            "📅  Duration     —  <b>4 Months (scheduled)</b>\n"
            "🧠  Models        —  <b>GPT-4o, DALL·E 3, Web browsing</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>ChatGPT Plus (4 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Manus Pro
    {
        "id": "manus_pro_12m",
        "name": "🧩 Manus Pro — 12 Months (Full Warranty)",
        "price": 18.00,
        "description": (
            "<b>Manus Pro — the autonomous AI agent platform</b> for a full year "
            "with complete warranty coverage.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$18.00</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "🤖  Type          —  <b>Autonomous AI agent</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Manus Pro (12 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Claude Pro 1M
    {
        "id": "claude_pro_1m",
        "name": "🟠 Claude Pro — 1 Month (Full Warranty)",
        "price": 10.00,
        "description": (
            "<b>Claude Pro by Anthropic — 1 month</b> with 5x more usage, "
            "priority access and the latest Claude Opus &amp; Sonnet models.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$10.00</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🧠  Models        —  <b>Claude Opus &amp; Sonnet</b>\n"
            "⚡  Usage         —  <b>5x more than free</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Claude Pro (1 Month) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Factory Pro
    {
        "id": "factory_pro_12m",
        "name": "🏭 Factory Pro — 12 Months (Warranty)",
        "price": 11.00,
        "description": (
            "<b>Factory Pro — AI-powered software development platform</b> "
            "for a full year with warranty coverage.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$11.00</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "⚙️  Type          —  <b>AI development automation</b>\n"
            "🔄  Warranty     —  <b>Yes</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Factory Pro (12 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ GitHub Student
    {
        "id": "github_student_2y",
        "name": "🐙 GitHub Student Pack — 2 Years (FW)",
        "price": 4.00,
        "description": (
            "<b>GitHub Student Developer Pack for 2 years</b> — free Copilot, "
            "cloud credits and 100+ premium developer tools.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$4.00</b>\n"
            "📅  Duration     —  <b>2 Years</b>\n"
            "🎁  Includes     —  <b>Copilot + 100+ dev tools</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>GitHub Student Pack (2 Years) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ ChatGPT Business 48M
    {
        "id": "chatgpt_business_48m",
        "name": "🤖 ChatGPT Business — 48 Months (1 Seat)",
        "price": 12.00,
        "description": (
            "<b>ChatGPT Business seat for 48 months</b> — advanced data "
            "privacy, admin controls and the full model lineup.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$12.00</b>\n"
            "📅  Duration     —  <b>48 Months (1 free seat)</b>\n"
            "🏢  Plan          —  <b>Business tier</b>\n"
            "🔒  Privacy       —  <b>Data not used for training</b>\n"
            "🔄  Warranty     —  <b>Yes</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>ChatGPT Business (48 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Supabase
    {
        "id": "supabase_pro_12m",
        "name": "⚡ Supabase Pro — 12 Months",
        "price": 18.00,
        "description": (
            "<b>Supabase Pro — the open-source Firebase alternative</b> for "
            "a full year with managed Postgres, Auth, Storage and Edge Functions.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$18.00</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "🗄  Backend      —  <b>Postgres, Auth, Storage, Edge Fns</b>\n"
            "🔄  Warranty     —  <b>Yes</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Supabase Pro (12 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Cursor Pro 1M
    {
        "id": "cursor_pro_1m",
        "name": "🖱 Cursor Pro — 1 Month (FW)",
        "price": 11.00,
        "description": (
            "<b>Cursor Pro — the AI-first code editor</b> for 1 month with "
            "unlimited completions and premium model access.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$11.00</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🤖  AI              —  <b>GPT-4 &amp; Claude powered</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Cursor Pro (1 Month) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Claude Pro 9M
    {
        "id": "claude_pro_9m",
        "name": "🟠 Claude Pro — 9 Months Account (FW)",
        "price": 60.00,
        "description": (
            "<b>Claude Pro account with 9 months of premium access</b> — "
            "long-term subscription with full warranty.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$60.00</b>\n"
            "📅  Duration     —  <b>9 Months</b>\n"
            "🧠  Models        —  <b>Claude Opus &amp; Sonnet</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Claude Pro (9 Months) — Order Confirmed!</b>\n\nYour account will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Grok Super
    {
        "id": "grok_super_3m",
        "name": "🛰 Grok Super — 3 Months Account (NW)",
        "price": 12.00,
        "description": (
            "<b>Grok Super by xAI — 3 months</b> of the most capable Grok "
            "models with real-time X (Twitter) integration.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$12.00</b>\n"
            "📅  Duration     —  <b>3 Months</b>\n"
            "🧠  Type          —  <b>Grok Super (xAI)</b>\n"
            "🔄  Warranty     —  <b>No warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Grok Super (3 Months) — Order Confirmed!</b>\n\nYour account will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Claude Pro K12
    {
        "id": "claude_pro_12m_k12",
        "name": "🟠 Claude Pro — 12M K12 Teachers (FW)",
        "price": 32.00,
        "description": (
            "<b>Claude Pro for K-12 teachers — 12 months</b> of full "
            "premium access under Anthropic's education programme.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$32.00</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "🎓  Type          —  <b>K-12 Teachers programme</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Claude Pro (12M K12 Teachers) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Resend
    {
        "id": "resend_12m",
        "name": "📧 Resend — 12 Months (Method)",
        "price": 15.00,
        "description": (
            "<b>Resend — the developer email API</b> for a full year with "
            "high deliverability and simple integration.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$15.00</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "📨  Type          —  <b>Transactional email API</b>\n"
            "🔄  Warranty     —  <b>Method based</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Resend (12 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ LinkedIn Method
    {
        "id": "linkedin_method",
        "name": "💼 LinkedIn Method — YT, NordVPN, Lovable",
        "price": 28.00,
        "description": (
            "<b>LinkedIn method bundle</b> — unlocks YouTube Premium, "
            "NordVPN and Lovable perks in one package.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$28.00</b>\n"
            "🎁  Includes     —  <b>YouTube, NordVPN, Lovable</b>\n"
            "📦  Type          —  <b>Method bundle</b>\n"
            "🔄  Warranty     —  <b>Method based</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>LinkedIn Method Bundle — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ ChatGPT Business 1M
    {
        "id": "chatgpt_business_1m",
        "name": "🤖 ChatGPT Business — 1 Month Seat (FW)",
        "price": 9.00,
        "description": (
            "<b>ChatGPT Business standard seat for 1 month</b> — advanced "
            "privacy, admin controls and full model access.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$9.00</b>\n"
            "📅  Duration     —  <b>1 Month (1 seat)</b>\n"
            "🏢  Plan          —  <b>Business standard</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>ChatGPT Business (1 Month) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ ChatGPT Plus 1M FW
    {
        "id": "chatgpt_plus_1m_fw",
        "name": "🤖 ChatGPT Plus — 1 Month (Full Warranty)",
        "price": 7.00,
        "description": (
            "<b>ChatGPT Plus for 1 month with full warranty</b> — "
            "GPT-4o, DALL·E 3 and real-time web browsing.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$7.00</b>\n"
            "📅  Duration     —  <b>1 Month</b>\n"
            "🧠  Models        —  <b>GPT-4o, DALL·E 3, Web browsing</b>\n"
            "🔄  Warranty     —  <b>Yes, full warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>ChatGPT Plus (1 Month FW) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Runway Pro
    {
        "id": "runway_pro_12m",
        "name": "🎥 Runway Pro — 12 Months (Lenny's)",
        "price": 11.00,
        "description": (
            "<b>Runway Pro — AI video generation</b> for a full year with "
            "Gen-3 models, high-res exports and creative tools.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$11.00</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "🎬  Type          —  <b>AI video generation (Gen-3)</b>\n"
            "🔄  Warranty     —  <b>Yes</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Runway Pro (12 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Higgsfield
    {
        "id": "higgsfield_12m",
        "name": "🎞 Higgsfield — 12 Months (Lenny's)",
        "price": 40.00,
        "description": (
            "<b>Higgsfield — advanced AI video &amp; motion tools</b> for a "
            "full year of creative production.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$40.00</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "🎬  Type          —  <b>AI video &amp; motion</b>\n"
            "🔄  Warranty     —  <b>Yes</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Higgsfield (12 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ ChatGPT MomoPay
    {
        "id": "chatgpt_plus_momopay",
        "name": "🤖 ChatGPT Plus — MomoPay (NW)",
        "price": 4.00,
        "description": (
            "<b>ChatGPT Plus via MomoPay method</b> — budget-friendly "
            "access to GPT-4o and premium features.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$4.00</b>\n"
            "🧠  Models        —  <b>GPT-4o, DALL·E 3</b>\n"
            "💳  Method        —  <b>MomoPay</b>\n"
            "🔄  Warranty     —  <b>No warranty</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>ChatGPT Plus (MomoPay) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
    },
    # ------------------------------------------------------------------ Cursor Pro 12M
    {
        "id": "cursor_pro_12m",
        "name": "🖱 Cursor Pro — 12 Months (Lenny's)",
        "price": 38.00,
        "description": (
            "<b>Cursor Pro — the AI-first code editor</b> for a full year with "
            "unlimited completions and premium models.\n\n"
            "<blockquote>"
            "💵  Price         —  <b>$38.00</b>\n"
            "📅  Duration     —  <b>12 Months</b>\n"
            "🤖  AI              —  <b>GPT-4 &amp; Claude powered</b>\n"
            "🔄  Warranty     —  <b>Yes</b>"
            "</blockquote>"
        ),
        "stock": 100,
        "delivery": "✅ <b>Cursor Pro (12 Months) — Order Confirmed!</b>\n\nYour access will be delivered by support shortly.\n📌 Keep your <b>Order ID</b> handy.",
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
