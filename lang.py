"""
Translations for the bot in English, Hindi, Spanish and Russian.

Usage:
    from lang import t
    text = t("welcome", lang, name="Alex")

`t(key, lang, **kwargs)` looks up the string for `lang`, falls back to English
if the key or language is missing, and applies .format(**kwargs).

Strings use Telegram HTML formatting (<b>, <i>, <blockquote>, <code>).
"""

SUPPORTED = {"en", "hi", "es", "ru", "zh", "ar", "fr", "pt", "de", "id"}

LANG_NAMES = {
    "en": "English 🇬🇧",
    "hi": "हिन्दी 🇮🇳",
    "es": "Español 🇪🇸",
    "ru": "Русский 🇷🇺",
    "zh": "中文 🇨🇳",
    "ar": "العربية 🇸🇦",
    "fr": "Français 🇫🇷",
    "pt": "Português 🇵🇹",
    "de": "Deutsch 🇩🇪",
    "id": "Indonesia 🇮🇩",
}

TRANSLATIONS = {
    # ------------------------------------------------------------------ EN
    "en": {
        "welcome": (
            "👋 <b>Hey {name}, welcome!</b>\n\n"
            "Your one-stop shop for <b>premium digital subscriptions</b> "
            "at unbeatable prices — <i>fast, secure, and fully automated.</i> ⚡\n\n"
            "<blockquote>"
            "🔥 <b>200,000+</b> orders delivered\n"
            "⭐ <b>4.9/5</b> rating from happy customers\n"
            "⏱ <b>Instant</b> automated delivery, 24/7"
            "</blockquote>\n\n"
            "<b>What would you like to do?</b>\n"
            "<blockquote>"
            "🛍 <b>Shop</b> — Browse &amp; buy products\n"
            "💵 <b>Deposit</b> — Add funds to your wallet\n"
            "🪪 <b>My Profile</b> — Balance, orders &amp; settings\n"
            "🆘 <b>Support</b> — Get help anytime\n"
            "⭐ <b>Refer &amp; Earn</b> — Invite friends &amp; earn rewards\n"
            "🌐 <b>Language</b> — Change your language"
            "</blockquote>\n\n"
            "👇 <b>Tap an option below to get started!</b>"
        ),
        "btn_shop": "🛍 Shop",
        "btn_deposit": "💵 Deposit",
        "btn_profile": "🪪 My Profile",
        "btn_support": "🆘 Support",
        "btn_refer": "⭐ Refer & Earn",
        "btn_language": "🌐 Language",
        "btn_back": "⬅️ Back to menu",
        "btn_cancel": "⬅️ Cancel",
        "btn_share": "📤 Share invite link",
        "deposit_intro": (
            "💵 <b>Deposit — USDT (BEP20)</b>\n\n"
            "Top up your wallet with USDT on Binance Smart Chain.\n\n"
            "<blockquote>"
            "💰 Enter the amount to deposit (in USDT)\n"
            "📉 Min <b>${min:.0f}</b>  •  📈 Max <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 Just type a number, e.g. <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ That doesn't look like a number. Please type an amount like "
            "<code>25</code>."
        ),
        "deposit_range": "❌ Amount must be between ${min:.0f} and ${max:,.0f}.",
        "deposit_not_configured": (
            "⚠️ Crypto deposits aren't configured yet. Please contact support."
        ),
        "deposit_instructions": (
            "💵 <b>Send exactly this amount</b> 👇\n\n"
            "💰 Amount: <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 Network: <b>BEP20 (BSC)</b>\n"
            "📥 Address:\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ Send the <b>exact</b> amount shown above — the extra decimals "
            "identify your payment.\n"
            "⚠️ Use the <b>BEP20 (BSC)</b> network only. Other networks will be lost.\n"
            "⏱ This request expires in <b>{minutes} minutes</b>."
            "</blockquote>\n\n"
            "✅ Your balance is credited automatically after the transfer confirms."
        ),
        "deposit_received": (
            "✅ <b>Deposit received!</b>\n\n"
            "We received <b>{amount:.2f} USDT</b> and credited "
            "<b>${credited:.2f}</b> to your wallet.\n\n"
            "👛 New balance: <b>${balance:.2f}</b>\n\n"
            "Thanks for your payment! 🎉"
        ),
        "profile": (
            "🪪 <b>My Profile</b>\n\n"
            "👤 Name: <b>{name}</b>\n"
            "🆔 User ID: <code>{user_id}</code>\n"
            "👛 Balance: <b>${balance:.2f}</b>\n"
            "📦 Orders: <b>{orders}</b>\n\n"
            "⭐ <b>Referrals</b>\n"
            "<blockquote>"
            "👥 Friends invited: <b>{referrals}</b>\n"
            "💰 Rewards earned: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 Tap <b>Refer &amp; Earn</b> to get your invite link, or "
            "<b>Deposit</b> to add funds."
        ),
        "shop": (
            "🛍 <b>Shop</b>\n\n"
            "Our shelves are being restocked right now. 📦\n\n"
            "🔔 New drops are coming very soon, so check back shortly!\n"
            "<i>Tip: keep some funds ready so you don't miss out.</i> 💎"
        ),
        "support": (
            "🆘 <b>Support</b>\n\n"
            "Stuck on something or have a question? We've got you. 🤝\n\n"
            "📩 Reach us at {contact}\n"
            "⏱ We typically reply within a few hours."
        ),
        "refer": (
            "⭐ <b>Refer &amp; Earn</b>\n\n"
            "Invite friends and earn rewards when they deposit! 🎁\n\n"
            "<blockquote>"
            "👥 Friends invited: <b>{referrals}</b>\n"
            "💰 Rewards earned: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>Your invite link:</b>\n"
            "{link}\n\n"
            "Share it anywhere — you get rewarded automatically. 🚀"
        ),
        "language_choose": (
            "🌐 <b>Choose your language</b>\n\n"
            "Select your preferred language below. 👇"
        ),
        "language_updated": (
            "✅ <b>Language updated</b>\n\n"
            "Your language is now set to <b>{lang}</b>."
        ),
        "help": (
            "ℹ️ <b>Help &amp; commands</b>\n\n"
            "/start — Open the main menu\n"
            "/help — Show this help message\n\n"
            "Use the buttons on the menu to shop, deposit, view your profile, "
            "get support, or refer friends. 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>Referral reward!</b>\n\n"
            "One of your invited friends just made their first deposit.\n"
            "💰 You earned <b>${reward:.2f}</b>!\n"
            "👛 New balance: <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "Join me on this bot for premium digital subscriptions at great prices! 🚀"
        ),
        "btn_buy": "🛒 Buy now",
        "btn_confirm": "✅ Confirm purchase",
        "btn_orders": "📜 ✦ My Order History ✦",
        "btn_back_shop": "⬅️ Back to shop",
        "btn_deposit_now": "💵 Deposit now",
        "shop_list": (
            "🛍 <b>Shop</b>\n\n"
            "👛 Your balance: <b>${balance:.2f}</b>\n\n"
            "Choose a product below to see details and buy. 👇"
        ),
        "shop_empty": (
            "🛍 <b>Shop</b>\n\n"
            "No products are available right now. Check back soon! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 Price: <b>${price:.2f}</b>\n"
            "📦 Stock: <b>{stock}</b>\n"
            "👛 Your balance: <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>Confirm your purchase</b>\n\n"
            "🛍 Product: <b>{name}</b>\n"
            "💵 Price: <b>${price:.2f}</b>\n"
            "👛 Balance after: <b>${after:.2f}</b>\n\n"
            "Tap <b>Confirm purchase</b> to proceed."
        ),
        "insufficient": (
            "❌ <b>Not enough balance</b>\n\n"
            "This item costs <b>${price:.2f}</b> but your balance is "
            "<b>${balance:.2f}</b>.\n\n"
            "💡 Tap <b>Deposit now</b> to top up."
        ),
        "out_of_stock": (
            "😔 <b>Out of stock</b>\n\n"
            "This product just sold out. Please check back later!"
        ),
        "order_success": (
            "✅ <b>Purchase complete!</b>\n\n"
            "🧾 Order <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 Paid: <b>${price:.2f}</b>\n"
            "👛 New balance: <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "Thank you for your order! 🎉"
        ),
        "orders_empty": (
            "📦 <b>My Orders</b>\n\n"
            "You haven't placed any orders yet.\n"
            "Head to the <b>Shop</b> to grab something! 🛍"
        ),
        "orders_header": "📜 <b>My Order History</b>\n\nYour recent orders:\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "Unlimited",
    },
    # ------------------------------------------------------------------ HI
    "hi": {
        "welcome": (
            "👋 <b>नमस्ते {name}, स्वागत है!</b>\n\n"
            "<b>प्रीमियम डिजिटल सब्सक्रिप्शन</b> के लिए आपकी एक ही जगह — "
            "<i>तेज़, सुरक्षित और पूरी तरह ऑटोमैटिक।</i> ⚡\n\n"
            "<blockquote>"
            "🔥 <b>2,00,000+</b> ऑर्डर पूरे हुए\n"
            "⭐ ग्राहकों से <b>4.9/5</b> रेटिंग\n"
            "⏱ <b>तुरंत</b> ऑटोमैटिक डिलीवरी, 24/7"
            "</blockquote>\n\n"
            "<b>आप क्या करना चाहेंगे?</b>\n"
            "<blockquote>"
            "🛍 <b>शॉप</b> — प्रोडक्ट देखें और खरीदें\n"
            "💵 <b>डिपॉज़िट</b> — वॉलेट में पैसे जोड़ें\n"
            "🪪 <b>मेरी प्रोफ़ाइल</b> — बैलेंस, ऑर्डर और सेटिंग\n"
            "🆘 <b>सपोर्ट</b> — कभी भी मदद पाएं\n"
            "⭐ <b>रेफ़र करें और कमाएं</b> — दोस्तों को बुलाएं और इनाम पाएं\n"
            "🌐 <b>भाषा</b> — अपनी भाषा बदलें"
            "</blockquote>\n\n"
            "👇 <b>शुरू करने के लिए नीचे कोई विकल्प चुनें!</b>"
        ),
        "btn_shop": "🛍 शॉप",
        "btn_deposit": "💵 डिपॉज़िट",
        "btn_profile": "🪪 मेरी प्रोफ़ाइल",
        "btn_support": "🆘 सपोर्ट",
        "btn_refer": "⭐ रेफ़र करें",
        "btn_language": "🌐 भाषा",
        "btn_back": "⬅️ मेन्यू पर वापस",
        "btn_cancel": "⬅️ रद्द करें",
        "btn_share": "📤 इनवाइट लिंक शेयर करें",
        "deposit_intro": (
            "💵 <b>डिपॉज़िट — USDT (BEP20)</b>\n\n"
            "Binance Smart Chain पर USDT से अपना वॉलेट भरें।\n\n"
            "<blockquote>"
            "💰 डिपॉज़िट की रकम लिखें (USDT में)\n"
            "📉 न्यूनतम <b>${min:.0f}</b>  •  📈 अधिकतम <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 बस एक नंबर लिखें, जैसे <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ यह कोई नंबर नहीं लग रहा। कृपया रकम ऐसे लिखें, जैसे <code>25</code>।"
        ),
        "deposit_range": "❌ रकम ${min:.0f} और ${max:,.0f} के बीच होनी चाहिए।",
        "deposit_not_configured": (
            "⚠️ क्रिप्टो डिपॉज़िट अभी सेट नहीं है। कृपया सपोर्ट से संपर्क करें।"
        ),
        "deposit_instructions": (
            "💵 <b>बिलकुल यही रकम भेजें</b> 👇\n\n"
            "💰 रकम: <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 नेटवर्क: <b>BEP20 (BSC)</b>\n"
            "📥 पता:\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ ऊपर दिखाई गई <b>बिलकुल सटीक</b> रकम भेजें — बाकी दशमलव आपके "
            "पेमेंट की पहचान हैं।\n"
            "⚠️ सिर्फ <b>BEP20 (BSC)</b> नेटवर्क इस्तेमाल करें। दूसरे नेटवर्क पर पैसा खो जाएगा।\n"
            "⏱ यह रिक्वेस्ट <b>{minutes} मिनट</b> में खत्म हो जाएगी।"
            "</blockquote>\n\n"
            "✅ ट्रांसफर कन्फर्म होते ही आपका बैलेंस अपने आप जुड़ जाएगा।"
        ),
        "deposit_received": (
            "✅ <b>डिपॉज़िट मिल गया!</b>\n\n"
            "हमें <b>{amount:.2f} USDT</b> मिले और आपके वॉलेट में "
            "<b>${credited:.2f}</b> जोड़ दिए गए।\n\n"
            "👛 नया बैलेंस: <b>${balance:.2f}</b>\n\n"
            "आपके पेमेंट के लिए धन्यवाद! 🎉"
        ),
        "profile": (
            "🪪 <b>मेरी प्रोफ़ाइल</b>\n\n"
            "👤 नाम: <b>{name}</b>\n"
            "🆔 यूज़र ID: <code>{user_id}</code>\n"
            "👛 बैलेंस: <b>${balance:.2f}</b>\n"
            "📦 ऑर्डर: <b>{orders}</b>\n\n"
            "⭐ <b>रेफ़रल</b>\n"
            "<blockquote>"
            "👥 बुलाए गए दोस्त: <b>{referrals}</b>\n"
            "💰 कमाया इनाम: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 इनवाइट लिंक के लिए <b>रेफ़र करें</b> दबाएं, या पैसे जोड़ने के लिए "
            "<b>डिपॉज़िट</b> दबाएं।"
        ),
        "shop": (
            "🛍 <b>शॉप</b>\n\n"
            "अभी हमारा स्टॉक दोबारा भरा जा रहा है। 📦\n\n"
            "🔔 नए प्रोडक्ट बहुत जल्द आ रहे हैं, थोड़ी देर बाद फिर देखें!\n"
            "<i>टिप: कुछ पैसे तैयार रखें ताकि मौका न छूटे।</i> 💎"
        ),
        "support": (
            "🆘 <b>सपोर्ट</b>\n\n"
            "कहीं अटक गए हैं या कोई सवाल है? हम मदद के लिए हैं। 🤝\n\n"
            "📩 हमसे संपर्क करें: {contact}\n"
            "⏱ हम आमतौर पर कुछ घंटों में जवाब देते हैं।"
        ),
        "refer": (
            "⭐ <b>रेफ़र करें और कमाएं</b>\n\n"
            "दोस्तों को बुलाएं और उनके डिपॉज़िट पर इनाम कमाएं! 🎁\n\n"
            "<blockquote>"
            "👥 बुलाए गए दोस्त: <b>{referrals}</b>\n"
            "💰 कमाया इनाम: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>आपका इनवाइट लिंक:</b>\n"
            "{link}\n\n"
            "इसे कहीं भी शेयर करें — इनाम अपने आप मिलेगा। 🚀"
        ),
        "language_choose": (
            "🌐 <b>अपनी भाषा चुनें</b>\n\n"
            "नीचे अपनी पसंदीदा भाषा चुनें। 👇"
        ),
        "language_updated": (
            "✅ <b>भाषा बदल गई</b>\n\n"
            "अब आपकी भाषा <b>{lang}</b> सेट कर दी गई है।"
        ),
        "help": (
            "ℹ️ <b>मदद और कमांड</b>\n\n"
            "/start — मेन्यू खोलें\n"
            "/help — यह मदद संदेश दिखाएं\n\n"
            "मेन्यू के बटनों से शॉप, डिपॉज़िट, प्रोफ़ाइल, सपोर्ट या रेफ़रल इस्तेमाल करें। 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>रेफ़रल इनाम!</b>\n\n"
            "आपके बुलाए एक दोस्त ने अभी अपना पहला डिपॉज़िट किया।\n"
            "💰 आपने <b>${reward:.2f}</b> कमाए!\n"
            "👛 नया बैलेंस: <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "बढ़िया दामों में प्रीमियम डिजिटल सब्सक्रिप्शन के लिए इस बोट पर मेरे साथ जुड़ें! 🚀"
        ),
        "btn_buy": "🛒 अभी खरीदें",
        "btn_confirm": "✅ खरीद पक्की करें",
        "btn_orders": "📜 ✦ मेरा ऑर्डर इतिहास ✦",
        "btn_back_shop": "⬅️ शॉप पर वापस",
        "btn_deposit_now": "💵 अभी डिपॉज़िट करें",
        "shop_list": (
            "🛍 <b>शॉप</b>\n\n"
            "👛 आपका बैलेंस: <b>${balance:.2f}</b>\n\n"
            "नीचे कोई प्रोडक्ट चुनें, डिटेल देखें और खरीदें। 👇"
        ),
        "shop_empty": (
            "🛍 <b>शॉप</b>\n\n"
            "अभी कोई प्रोडक्ट उपलब्ध नहीं है। थोड़ी देर बाद देखें! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 कीमत: <b>${price:.2f}</b>\n"
            "📦 स्टॉक: <b>{stock}</b>\n"
            "👛 आपका बैलेंस: <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>अपनी खरीद पक्की करें</b>\n\n"
            "🛍 प्रोडक्ट: <b>{name}</b>\n"
            "💵 कीमत: <b>${price:.2f}</b>\n"
            "👛 बाद में बैलेंस: <b>${after:.2f}</b>\n\n"
            "आगे बढ़ने के लिए <b>खरीद पक्की करें</b> दबाएं।"
        ),
        "insufficient": (
            "❌ <b>बैलेंस कम है</b>\n\n"
            "इस आइटम की कीमत <b>${price:.2f}</b> है पर आपका बैलेंस "
            "<b>${balance:.2f}</b> है।\n\n"
            "💡 टॉप-अप के लिए <b>अभी डिपॉज़िट करें</b> दबाएं।"
        ),
        "out_of_stock": (
            "😔 <b>स्टॉक खत्म</b>\n\n"
            "यह प्रोडक्ट अभी बिक गया। कृपया बाद में देखें!"
        ),
        "order_success": (
            "✅ <b>खरीद पूरी हुई!</b>\n\n"
            "🧾 ऑर्डर <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 भुगतान: <b>${price:.2f}</b>\n"
            "👛 नया बैलेंस: <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "आपके ऑर्डर के लिए धन्यवाद! 🎉"
        ),
        "orders_empty": (
            "📦 <b>मेरे ऑर्डर</b>\n\n"
            "आपने अभी तक कोई ऑर्डर नहीं किया।\n"
            "कुछ लेने के लिए <b>शॉप</b> पर जाएं! 🛍"
        ),
        "orders_header": "📜 <b>मेरा ऑर्डर इतिहास</b>\n\nआपके हाल के ऑर्डर:\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "असीमित",
    },
    # ------------------------------------------------------------------ ES
    "es": {
        "welcome": (
            "👋 <b>¡Hola {name}, bienvenido!</b>\n\n"
            "Tu tienda para <b>suscripciones digitales premium</b> a precios "
            "inmejorables — <i>rápido, seguro y totalmente automático.</i> ⚡\n\n"
            "<blockquote>"
            "🔥 <b>200.000+</b> pedidos entregados\n"
            "⭐ <b>4.9/5</b> de valoración de clientes\n"
            "⏱ Entrega <b>instantánea</b> y automática, 24/7"
            "</blockquote>\n\n"
            "<b>¿Qué te gustaría hacer?</b>\n"
            "<blockquote>"
            "🛍 <b>Tienda</b> — Explora y compra productos\n"
            "💵 <b>Depositar</b> — Añade fondos a tu monedero\n"
            "🪪 <b>Mi perfil</b> — Saldo, pedidos y ajustes\n"
            "🆘 <b>Soporte</b> — Recibe ayuda cuando sea\n"
            "⭐ <b>Invita y gana</b> — Invita amigos y gana recompensas\n"
            "🌐 <b>Idioma</b> — Cambia tu idioma"
            "</blockquote>\n\n"
            "👇 <b>¡Toca una opción para empezar!</b>"
        ),
        "btn_shop": "🛍 Tienda",
        "btn_deposit": "💵 Depositar",
        "btn_profile": "🪪 Mi perfil",
        "btn_support": "🆘 Soporte",
        "btn_refer": "⭐ Invita y gana",
        "btn_language": "🌐 Idioma",
        "btn_back": "⬅️ Volver al menú",
        "btn_cancel": "⬅️ Cancelar",
        "btn_share": "📤 Compartir enlace",
        "deposit_intro": (
            "💵 <b>Depósito — USDT (BEP20)</b>\n\n"
            "Recarga tu monedero con USDT en Binance Smart Chain.\n\n"
            "<blockquote>"
            "💰 Escribe la cantidad a depositar (en USDT)\n"
            "📉 Mín <b>${min:.0f}</b>  •  📈 Máx <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 Solo escribe un número, p. ej. <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ Eso no parece un número. Escribe una cantidad como <code>25</code>."
        ),
        "deposit_range": "❌ La cantidad debe estar entre ${min:.0f} y ${max:,.0f}.",
        "deposit_not_configured": (
            "⚠️ Los depósitos cripto aún no están configurados. Contacta con soporte."
        ),
        "deposit_instructions": (
            "💵 <b>Envía exactamente esta cantidad</b> 👇\n\n"
            "💰 Cantidad: <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 Red: <b>BEP20 (BSC)</b>\n"
            "📥 Dirección:\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ Envía la cantidad <b>exacta</b> mostrada arriba — los decimales "
            "extra identifican tu pago.\n"
            "⚠️ Usa solo la red <b>BEP20 (BSC)</b>. Otras redes se perderán.\n"
            "⏱ Esta solicitud caduca en <b>{minutes} minutos</b>."
            "</blockquote>\n\n"
            "✅ Tu saldo se acredita automáticamente al confirmarse la transferencia."
        ),
        "deposit_received": (
            "✅ <b>¡Depósito recibido!</b>\n\n"
            "Recibimos <b>{amount:.2f} USDT</b> y acreditamos "
            "<b>${credited:.2f}</b> en tu monedero.\n\n"
            "👛 Nuevo saldo: <b>${balance:.2f}</b>\n\n"
            "¡Gracias por tu pago! 🎉"
        ),
        "profile": (
            "🪪 <b>Mi perfil</b>\n\n"
            "👤 Nombre: <b>{name}</b>\n"
            "🆔 ID de usuario: <code>{user_id}</code>\n"
            "👛 Saldo: <b>${balance:.2f}</b>\n"
            "📦 Pedidos: <b>{orders}</b>\n\n"
            "⭐ <b>Referidos</b>\n"
            "<blockquote>"
            "👥 Amigos invitados: <b>{referrals}</b>\n"
            "💰 Recompensas ganadas: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 Toca <b>Invita y gana</b> para tu enlace, o <b>Depositar</b> "
            "para añadir fondos."
        ),
        "shop": (
            "🛍 <b>Tienda</b>\n\n"
            "Estamos reponiendo el stock ahora mismo. 📦\n\n"
            "🔔 ¡Pronto llegan novedades, vuelve en un rato!\n"
            "<i>Consejo: ten fondos listos para no perderte nada.</i> 💎"
        ),
        "support": (
            "🆘 <b>Soporte</b>\n\n"
            "¿Atascado o con dudas? Estamos aquí. 🤝\n\n"
            "📩 Escríbenos a {contact}\n"
            "⏱ Solemos responder en unas horas."
        ),
        "refer": (
            "⭐ <b>Invita y gana</b>\n\n"
            "¡Invita amigos y gana recompensas cuando depositen! 🎁\n\n"
            "<blockquote>"
            "👥 Amigos invitados: <b>{referrals}</b>\n"
            "💰 Recompensas ganadas: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>Tu enlace de invitación:</b>\n"
            "{link}\n\n"
            "Compártelo donde quieras — la recompensa es automática. 🚀"
        ),
        "language_choose": (
            "🌐 <b>Elige tu idioma</b>\n\n"
            "Selecciona tu idioma preferido abajo. 👇"
        ),
        "language_updated": (
            "✅ <b>Idioma actualizado</b>\n\n"
            "Tu idioma ahora es <b>{lang}</b>."
        ),
        "help": (
            "ℹ️ <b>Ayuda y comandos</b>\n\n"
            "/start — Abrir el menú principal\n"
            "/help — Mostrar esta ayuda\n\n"
            "Usa los botones del menú para comprar, depositar, ver tu perfil, "
            "obtener soporte o invitar amigos. 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>¡Recompensa por referido!</b>\n\n"
            "Uno de tus amigos invitados acaba de hacer su primer depósito.\n"
            "💰 ¡Ganaste <b>${reward:.2f}</b>!\n"
            "👛 Nuevo saldo: <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "¡Únete conmigo a este bot de suscripciones digitales premium a buen precio! 🚀"
        ),
        "btn_buy": "🛒 Comprar ya",
        "btn_confirm": "✅ Confirmar compra",
        "btn_orders": "📜 ✦ Historial de pedidos ✦",
        "btn_back_shop": "⬅️ Volver a la tienda",
        "btn_deposit_now": "💵 Depositar ahora",
        "shop_list": (
            "🛍 <b>Tienda</b>\n\n"
            "👛 Tu saldo: <b>${balance:.2f}</b>\n\n"
            "Elige un producto abajo para ver detalles y comprar. 👇"
        ),
        "shop_empty": (
            "🛍 <b>Tienda</b>\n\n"
            "No hay productos disponibles ahora. ¡Vuelve pronto! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 Precio: <b>${price:.2f}</b>\n"
            "📦 Stock: <b>{stock}</b>\n"
            "👛 Tu saldo: <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>Confirma tu compra</b>\n\n"
            "🛍 Producto: <b>{name}</b>\n"
            "💵 Precio: <b>${price:.2f}</b>\n"
            "👛 Saldo después: <b>${after:.2f}</b>\n\n"
            "Toca <b>Confirmar compra</b> para continuar."
        ),
        "insufficient": (
            "❌ <b>Saldo insuficiente</b>\n\n"
            "Este artículo cuesta <b>${price:.2f}</b> pero tu saldo es "
            "<b>${balance:.2f}</b>.\n\n"
            "💡 Toca <b>Depositar ahora</b> para recargar."
        ),
        "out_of_stock": (
            "😔 <b>Agotado</b>\n\n"
            "Este producto acaba de agotarse. ¡Vuelve más tarde!"
        ),
        "order_success": (
            "✅ <b>¡Compra completada!</b>\n\n"
            "🧾 Pedido <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 Pagado: <b>${price:.2f}</b>\n"
            "👛 Nuevo saldo: <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "¡Gracias por tu pedido! 🎉"
        ),
        "orders_empty": (
            "📦 <b>Mis pedidos</b>\n\n"
            "Aún no has hecho ningún pedido.\n"
            "¡Ve a la <b>Tienda</b> para conseguir algo! 🛍"
        ),
        "orders_header": "📜 <b>Historial de pedidos</b>\n\nTus pedidos recientes:\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "Ilimitado",
    },
    # ------------------------------------------------------------------ RU
    "ru": {
        "welcome": (
            "👋 <b>Привет, {name}! Добро пожаловать!</b>\n\n"
            "Ваш магазин <b>премиум цифровых подписок</b> по лучшим ценам — "
            "<i>быстро, безопасно и полностью автоматически.</i> ⚡\n\n"
            "<blockquote>"
            "🔥 <b>200 000+</b> выполненных заказов\n"
            "⭐ Оценка <b>4.9/5</b> от клиентов\n"
            "⏱ <b>Мгновенная</b> автоматическая доставка, 24/7"
            "</blockquote>\n\n"
            "<b>Что бы вы хотели сделать?</b>\n"
            "<blockquote>"
            "🛍 <b>Магазин</b> — Смотреть и покупать товары\n"
            "💵 <b>Пополнить</b> — Добавить средства в кошелёк\n"
            "🪪 <b>Мой профиль</b> — Баланс, заказы и настройки\n"
            "🆘 <b>Поддержка</b> — Получить помощь\n"
            "⭐ <b>Приглашай и зарабатывай</b> — Зовите друзей и получайте награды\n"
            "🌐 <b>Язык</b> — Сменить язык"
            "</blockquote>\n\n"
            "👇 <b>Нажмите кнопку ниже, чтобы начать!</b>"
        ),
        "btn_shop": "🛍 Магазин",
        "btn_deposit": "💵 Пополнить",
        "btn_profile": "🪪 Мой профиль",
        "btn_support": "🆘 Поддержка",
        "btn_refer": "⭐ Приглашай",
        "btn_language": "🌐 Язык",
        "btn_back": "⬅️ В меню",
        "btn_cancel": "⬅️ Отмена",
        "btn_share": "📤 Поделиться ссылкой",
        "deposit_intro": (
            "💵 <b>Пополнение — USDT (BEP20)</b>\n\n"
            "Пополните кошелёк через USDT в сети Binance Smart Chain.\n\n"
            "<blockquote>"
            "💰 Введите сумму пополнения (в USDT)\n"
            "📉 Мин <b>${min:.0f}</b>  •  📈 Макс <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 Просто напишите число, напр. <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ Это не похоже на число. Введите сумму, например <code>25</code>."
        ),
        "deposit_range": "❌ Сумма должна быть от ${min:.0f} до ${max:,.0f}.",
        "deposit_not_configured": (
            "⚠️ Крипто-пополнения ещё не настроены. Свяжитесь с поддержкой."
        ),
        "deposit_instructions": (
            "💵 <b>Отправьте ровно эту сумму</b> 👇\n\n"
            "💰 Сумма: <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 Сеть: <b>BEP20 (BSC)</b>\n"
            "📥 Адрес:\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ Отправьте <b>точную</b> сумму выше — лишние знаки после запятой "
            "определяют ваш платёж.\n"
            "⚠️ Используйте только сеть <b>BEP20 (BSC)</b>. Другие сети будут потеряны.\n"
            "⏱ Запрос истекает через <b>{minutes} мин</b>."
            "</blockquote>\n\n"
            "✅ Баланс пополнится автоматически после подтверждения перевода."
        ),
        "deposit_received": (
            "✅ <b>Пополнение получено!</b>\n\n"
            "Мы получили <b>{amount:.2f} USDT</b> и зачислили "
            "<b>${credited:.2f}</b> на ваш кошелёк.\n\n"
            "👛 Новый баланс: <b>${balance:.2f}</b>\n\n"
            "Спасибо за оплату! 🎉"
        ),
        "profile": (
            "🪪 <b>Мой профиль</b>\n\n"
            "👤 Имя: <b>{name}</b>\n"
            "🆔 ID пользователя: <code>{user_id}</code>\n"
            "👛 Баланс: <b>${balance:.2f}</b>\n"
            "📦 Заказы: <b>{orders}</b>\n\n"
            "⭐ <b>Рефералы</b>\n"
            "<blockquote>"
            "👥 Приглашено друзей: <b>{referrals}</b>\n"
            "💰 Заработано: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 Нажмите <b>Приглашай</b> для ссылки или <b>Пополнить</b>, чтобы "
            "добавить средства."
        ),
        "shop": (
            "🛍 <b>Магазин</b>\n\n"
            "Сейчас мы пополняем ассортимент. 📦\n\n"
            "🔔 Новинки уже совсем скоро, загляните попозже!\n"
            "<i>Совет: держите средства наготове, чтобы не упустить.</i> 💎"
        ),
        "support": (
            "🆘 <b>Поддержка</b>\n\n"
            "Возник вопрос или проблема? Мы поможем. 🤝\n\n"
            "📩 Пишите нам: {contact}\n"
            "⏱ Обычно отвечаем в течение нескольких часов."
        ),
        "refer": (
            "⭐ <b>Приглашай и зарабатывай</b>\n\n"
            "Приглашайте друзей и получайте награды за их пополнения! 🎁\n\n"
            "<blockquote>"
            "👥 Приглашено друзей: <b>{referrals}</b>\n"
            "💰 Заработано: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>Ваша реферальная ссылка:</b>\n"
            "{link}\n\n"
            "Делитесь где угодно — награда начисляется автоматически. 🚀"
        ),
        "language_choose": (
            "🌐 <b>Выберите язык</b>\n\n"
            "Выберите предпочитаемый язык ниже. 👇"
        ),
        "language_updated": (
            "✅ <b>Язык обновлён</b>\n\n"
            "Теперь ваш язык — <b>{lang}</b>."
        ),
        "help": (
            "ℹ️ <b>Помощь и команды</b>\n\n"
            "/start — Открыть главное меню\n"
            "/help — Показать это сообщение\n\n"
            "Используйте кнопки меню, чтобы покупать, пополнять, смотреть профиль, "
            "получать поддержку или приглашать друзей. 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>Реферальная награда!</b>\n\n"
            "Один из приглашённых друзей только что сделал первое пополнение.\n"
            "💰 Вы заработали <b>${reward:.2f}</b>!\n"
            "👛 Новый баланс: <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "Присоединяйся ко мне в этом боте — премиум цифровые подписки по отличным ценам! 🚀"
        ),
        "btn_buy": "🛒 Купить",
        "btn_confirm": "✅ Подтвердить покупку",
        "btn_orders": "📜 ✦ История заказов ✦",
        "btn_back_shop": "⬅️ В магазин",
        "btn_deposit_now": "💵 Пополнить",
        "shop_list": (
            "🛍 <b>Магазин</b>\n\n"
            "👛 Ваш баланс: <b>${balance:.2f}</b>\n\n"
            "Выберите товар ниже, чтобы увидеть детали и купить. 👇"
        ),
        "shop_empty": (
            "🛍 <b>Магазин</b>\n\n"
            "Сейчас нет доступных товаров. Загляните позже! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 Цена: <b>${price:.2f}</b>\n"
            "📦 В наличии: <b>{stock}</b>\n"
            "👛 Ваш баланс: <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>Подтвердите покупку</b>\n\n"
            "🛍 Товар: <b>{name}</b>\n"
            "💵 Цена: <b>${price:.2f}</b>\n"
            "👛 Баланс после: <b>${after:.2f}</b>\n\n"
            "Нажмите <b>Подтвердить покупку</b>, чтобы продолжить."
        ),
        "insufficient": (
            "❌ <b>Недостаточно средств</b>\n\n"
            "Этот товар стоит <b>${price:.2f}</b>, а ваш баланс "
            "<b>${balance:.2f}</b>.\n\n"
            "💡 Нажмите <b>Пополнить</b>, чтобы добавить средства."
        ),
        "out_of_stock": (
            "😔 <b>Нет в наличии</b>\n\n"
            "Этот товар только что закончился. Загляните позже!"
        ),
        "order_success": (
            "✅ <b>Покупка завершена!</b>\n\n"
            "🧾 Заказ <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 Оплачено: <b>${price:.2f}</b>\n"
            "👛 Новый баланс: <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "Спасибо за заказ! 🎉"
        ),
        "orders_empty": (
            "📦 <b>Мои заказы</b>\n\n"
            "У вас пока нет заказов.\n"
            "Загляните в <b>Магазин</b>, чтобы что-нибудь выбрать! 🛍"
        ),
        "orders_header": "📜 <b>История заказов</b>\n\nВаши недавние заказы:\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "Без лимита",
    },
    # ------------------------------------------------------------------ ZH
    "zh": {
        "welcome": (
            "👋 <b>你好 {name}，欢迎！</b>\n\n"
            "这里是购买<b>高级数字订阅</b>的一站式平台，价格超值——"
            "<i>快速、安全、全自动。</i> ⚡\n\n"
            "<blockquote>"
            "🔥 已完成 <b>200,000+</b> 笔订单\n"
            "⭐ 客户评分 <b>4.9/5</b>\n"
            "⏱ <b>即时</b>自动交付，全天候 24/7"
            "</blockquote>\n\n"
            "<b>您想做什么？</b>\n"
            "<blockquote>"
            "🛍 <b>商店</b> — 浏览并购买产品\n"
            "💵 <b>充值</b> — 向钱包添加资金\n"
            "🪪 <b>我的资料</b> — 余额、订单和设置\n"
            "🆘 <b>客服</b> — 随时获取帮助\n"
            "⭐ <b>推荐赚钱</b> — 邀请好友并赚取奖励\n"
            "🌐 <b>语言</b> — 更改语言"
            "</blockquote>\n\n"
            "👇 <b>点击下方选项开始吧！</b>"
        ),
        "btn_shop": "🛍 商店",
        "btn_deposit": "💵 充值",
        "btn_profile": "🪪 我的资料",
        "btn_support": "🆘 客服",
        "btn_refer": "⭐ 推荐赚钱",
        "btn_language": "🌐 语言",
        "btn_back": "⬅️ 返回菜单",
        "btn_cancel": "⬅️ 取消",
        "btn_share": "📤 分享邀请链接",
        "deposit_intro": (
            "💵 <b>充值 — USDT (BEP20)</b>\n\n"
            "使用币安智能链上的 USDT 为钱包充值。\n\n"
            "<blockquote>"
            "💰 请输入充值金额（USDT）\n"
            "📉 最少 <b>${min:.0f}</b>  •  📈 最多 <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 直接输入数字，例如 <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ 这看起来不是数字。请输入金额，例如 <code>25</code>。"
        ),
        "deposit_range": "❌ 金额必须在 ${min:.0f} 到 ${max:,.0f} 之间。",
        "deposit_not_configured": (
            "⚠️ 加密货币充值尚未配置。请联系客服。"
        ),
        "deposit_instructions": (
            "💵 <b>请精确发送以下金额</b> 👇\n\n"
            "💰 金额：<code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 网络：<b>BEP20 (BSC)</b>\n"
            "📥 地址：\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ 请发送上面显示的<b>精确</b>金额——多余的小数用于识别您的付款。\n"
            "⚠️ 仅使用 <b>BEP20 (BSC)</b> 网络。其他网络将导致资金丢失。\n"
            "⏱ 此请求将在 <b>{minutes} 分钟</b>后过期。"
            "</blockquote>\n\n"
            "✅ 转账确认后，您的余额将自动到账。"
        ),
        "deposit_received": (
            "✅ <b>已收到充值！</b>\n\n"
            "我们收到了 <b>{amount:.2f} USDT</b>，并已向您的钱包充值 "
            "<b>${credited:.2f}</b>。\n\n"
            "👛 新余额：<b>${balance:.2f}</b>\n\n"
            "感谢您的付款！🎉"
        ),
        "profile": (
            "🪪 <b>我的资料</b>\n\n"
            "👤 姓名：<b>{name}</b>\n"
            "🆔 用户 ID：<code>{user_id}</code>\n"
            "👛 余额：<b>${balance:.2f}</b>\n"
            "📦 订单：<b>{orders}</b>\n\n"
            "⭐ <b>推荐</b>\n"
            "<blockquote>"
            "👥 已邀请好友：<b>{referrals}</b>\n"
            "💰 已赚取奖励：<b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 点击 <b>推荐赚钱</b> 获取邀请链接，或点击 <b>充值</b> 添加资金。"
        ),
        "shop": (
            "🛍 <b>商店</b>\n\n"
            "我们正在补货中。📦\n\n"
            "🔔 新品即将上架，请稍后再来！\n"
            "<i>提示：准备好资金，以免错过。</i> 💎"
        ),
        "support": (
            "🆘 <b>客服</b>\n\n"
            "遇到问题或有疑问？我们随时为您服务。🤝\n\n"
            "📩 联系我们：{contact}\n"
            "⏱ 我们通常在几小时内回复。"
        ),
        "refer": (
            "⭐ <b>推荐赚钱</b>\n\n"
            "邀请好友，好友充值即可赚取奖励！🎁\n\n"
            "<blockquote>"
            "👥 已邀请好友：<b>{referrals}</b>\n"
            "💰 已赚取奖励：<b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>您的邀请链接：</b>\n"
            "{link}\n\n"
            "随时分享——奖励将自动到账。🚀"
        ),
        "language_choose": (
            "🌐 <b>选择您的语言</b>\n\n"
            "请在下方选择您偏好的语言。👇"
        ),
        "language_updated": (
            "✅ <b>语言已更新</b>\n\n"
            "您的语言现已设置为 <b>{lang}</b>。"
        ),
        "help": (
            "ℹ️ <b>帮助与命令</b>\n\n"
            "/start — 打开主菜单\n"
            "/help — 显示此帮助信息\n\n"
            "使用菜单按钮购物、充值、查看资料、联系客服或推荐好友。👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>推荐奖励！</b>\n\n"
            "您邀请的一位好友刚刚完成了首次充值。\n"
            "💰 您赚取了 <b>${reward:.2f}</b>！\n"
            "👛 新余额：<b>${balance:.2f}</b>"
        ),
        "share_text": (
            "快来和我一起使用这个机器人，超值购买高级数字订阅！🚀"
        ),
        "btn_buy": "🛒 立即购买",
        "btn_confirm": "✅ 确认购买",
        "btn_orders": "📜 ✦ 我的订单记录 ✦",
        "btn_back_shop": "⬅️ 返回商店",
        "btn_deposit_now": "💵 立即充值",
        "shop_list": (
            "🛍 <b>商店</b>\n\n"
            "👛 您的余额：<b>${balance:.2f}</b>\n\n"
            "在下方选择产品查看详情并购买。👇"
        ),
        "shop_empty": (
            "🛍 <b>商店</b>\n\n"
            "目前没有可购买的产品。请稍后再来！🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 价格：<b>${price:.2f}</b>\n"
            "📦 库存：<b>{stock}</b>\n"
            "👛 您的余额：<b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>确认您的购买</b>\n\n"
            "🛍 产品：<b>{name}</b>\n"
            "💵 价格：<b>${price:.2f}</b>\n"
            "👛 购买后余额：<b>${after:.2f}</b>\n\n"
            "点击 <b>确认购买</b> 继续。"
        ),
        "insufficient": (
            "❌ <b>余额不足</b>\n\n"
            "此商品价格为 <b>${price:.2f}</b>，但您的余额为 <b>${balance:.2f}</b>。\n\n"
            "💡 点击 <b>立即充值</b> 进行充值。"
        ),
        "out_of_stock": (
            "😔 <b>已售罄</b>\n\n"
            "此产品刚刚售罄。请稍后再来！"
        ),
        "order_success": (
            "✅ <b>购买成功！</b>\n\n"
            "🧾 订单 <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 已支付：<b>${price:.2f}</b>\n"
            "👛 新余额：<b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "感谢您的订购！🎉"
        ),
        "orders_empty": (
            "📦 <b>我的订单</b>\n\n"
            "您还没有任何订单。\n"
            "前往 <b>商店</b> 挑选一些吧！🛍"
        ),
        "orders_header": "📜 <b>我的订单记录</b>\n\n您最近的订单：\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "无限",
    },
    # ------------------------------------------------------------------ AR
    "ar": {
        "welcome": (
            "👋 <b>مرحباً {name}!</b>\n\n"
            "وجهتك الأولى لـ<b>الاشتراكات الرقمية المميزة</b> بأفضل الأسعار — "
            "<i>سريع وآمن وتلقائي بالكامل.</i> ⚡\n\n"
            "<blockquote>"
            "🔥 تم تسليم <b>+200,000</b> طلب\n"
            "⭐ تقييم <b>4.9/5</b> من العملاء\n"
            "⏱ تسليم <b>فوري</b> وتلقائي، على مدار الساعة"
            "</blockquote>\n\n"
            "<b>ماذا تريد أن تفعل؟</b>\n"
            "<blockquote>"
            "🛍 <b>المتجر</b> — تصفح واشترِ المنتجات\n"
            "💵 <b>إيداع</b> — أضف رصيداً إلى محفظتك\n"
            "🪪 <b>ملفي</b> — الرصيد والطلبات والإعدادات\n"
            "🆘 <b>الدعم</b> — احصل على المساعدة\n"
            "⭐ <b>ادعُ واربح</b> — ادعُ أصدقاءك واربح مكافآت\n"
            "🌐 <b>اللغة</b> — غيّر لغتك"
            "</blockquote>\n\n"
            "👇 <b>اختر خياراً أدناه للبدء!</b>"
        ),
        "btn_shop": "🛍 المتجر",
        "btn_deposit": "💵 إيداع",
        "btn_profile": "🪪 ملفي",
        "btn_support": "🆘 الدعم",
        "btn_refer": "⭐ ادعُ واربح",
        "btn_language": "🌐 اللغة",
        "btn_back": "⬅️ العودة للقائمة",
        "btn_cancel": "⬅️ إلغاء",
        "btn_share": "📤 مشاركة رابط الدعوة",
        "deposit_intro": (
            "💵 <b>إيداع — USDT (BEP20)</b>\n\n"
            "اشحن محفظتك بـ USDT على شبكة Binance Smart Chain.\n\n"
            "<blockquote>"
            "💰 أدخل مبلغ الإيداع (بالـ USDT)\n"
            "📉 الحد الأدنى <b>${min:.0f}</b>  •  📈 الأقصى <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 اكتب رقماً فقط، مثل <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ هذا لا يبدو رقماً. اكتب مبلغاً مثل <code>25</code>."
        ),
        "deposit_range": "❌ يجب أن يكون المبلغ بين ${min:.0f} و ${max:,.0f}.",
        "deposit_not_configured": (
            "⚠️ الإيداع بالعملات الرقمية غير مُهيأ بعد. يرجى التواصل مع الدعم."
        ),
        "deposit_instructions": (
            "💵 <b>أرسل هذا المبلغ بالضبط</b> 👇\n\n"
            "💰 المبلغ: <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 الشبكة: <b>BEP20 (BSC)</b>\n"
            "📥 العنوان:\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ أرسل المبلغ <b>الدقيق</b> الموضح أعلاه — الأرقام العشرية الإضافية "
            "تُحدد دفعتك.\n"
            "⚠️ استخدم شبكة <b>BEP20 (BSC)</b> فقط. الشبكات الأخرى ستُفقد.\n"
            "⏱ ينتهي هذا الطلب خلال <b>{minutes} دقيقة</b>."
            "</blockquote>\n\n"
            "✅ يُضاف رصيدك تلقائياً بعد تأكيد التحويل."
        ),
        "deposit_received": (
            "✅ <b>تم استلام الإيداع!</b>\n\n"
            "استلمنا <b>{amount:.2f} USDT</b> وأضفنا <b>${credited:.2f}</b> "
            "إلى محفظتك.\n\n"
            "👛 الرصيد الجديد: <b>${balance:.2f}</b>\n\n"
            "شكراً لدفعتك! 🎉"
        ),
        "profile": (
            "🪪 <b>ملفي</b>\n\n"
            "👤 الاسم: <b>{name}</b>\n"
            "🆔 المعرّف: <code>{user_id}</code>\n"
            "👛 الرصيد: <b>${balance:.2f}</b>\n"
            "📦 الطلبات: <b>{orders}</b>\n\n"
            "⭐ <b>الدعوات</b>\n"
            "<blockquote>"
            "👥 الأصدقاء المدعوون: <b>{referrals}</b>\n"
            "💰 المكافآت المكتسبة: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 اضغط <b>ادعُ واربح</b> للحصول على رابطك، أو <b>إيداع</b> لإضافة رصيد."
        ),
        "shop": (
            "🛍 <b>المتجر</b>\n\n"
            "نقوم بإعادة تعبئة المخزون الآن. 📦\n\n"
            "🔔 منتجات جديدة قريباً جداً، عُد لاحقاً!\n"
            "<i>نصيحة: جهّز بعض الرصيد حتى لا تفوّت الفرصة.</i> 💎"
        ),
        "support": (
            "🆘 <b>الدعم</b>\n\n"
            "هل واجهت مشكلة أو لديك سؤال؟ نحن هنا لمساعدتك. 🤝\n\n"
            "📩 تواصل معنا عبر {contact}\n"
            "⏱ نرد عادةً خلال ساعات قليلة."
        ),
        "refer": (
            "⭐ <b>ادعُ واربح</b>\n\n"
            "ادعُ أصدقاءك واربح مكافآت عند إيداعهم! 🎁\n\n"
            "<blockquote>"
            "👥 الأصدقاء المدعوون: <b>{referrals}</b>\n"
            "💰 المكافآت المكتسبة: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>رابط دعوتك:</b>\n"
            "{link}\n\n"
            "شاركه أينما شئت — تُضاف المكافأة تلقائياً. 🚀"
        ),
        "language_choose": (
            "🌐 <b>اختر لغتك</b>\n\n"
            "اختر لغتك المفضلة أدناه. 👇"
        ),
        "language_updated": (
            "✅ <b>تم تحديث اللغة</b>\n\n"
            "لغتك الآن هي <b>{lang}</b>."
        ),
        "help": (
            "ℹ️ <b>المساعدة والأوامر</b>\n\n"
            "/start — فتح القائمة الرئيسية\n"
            "/help — عرض رسالة المساعدة\n\n"
            "استخدم أزرار القائمة للتسوق والإيداع وعرض ملفك والدعم ودعوة الأصدقاء. 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>مكافأة دعوة!</b>\n\n"
            "أحد أصدقائك المدعوين أجرى للتو أول إيداع له.\n"
            "💰 لقد ربحت <b>${reward:.2f}</b>!\n"
            "👛 الرصيد الجديد: <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "انضم إليّ في هذا البوت للاشتراكات الرقمية المميزة بأسعار رائعة! 🚀"
        ),
        "btn_buy": "🛒 اشترِ الآن",
        "btn_confirm": "✅ تأكيد الشراء",
        "btn_orders": "📜 ✦ سجل طلباتي ✦",
        "btn_back_shop": "⬅️ العودة للمتجر",
        "btn_deposit_now": "💵 إيداع الآن",
        "shop_list": (
            "🛍 <b>المتجر</b>\n\n"
            "👛 رصيدك: <b>${balance:.2f}</b>\n\n"
            "اختر منتجاً أدناه لعرض التفاصيل والشراء. 👇"
        ),
        "shop_empty": (
            "🛍 <b>المتجر</b>\n\n"
            "لا توجد منتجات متاحة حالياً. عُد قريباً! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 السعر: <b>${price:.2f}</b>\n"
            "📦 المخزون: <b>{stock}</b>\n"
            "👛 رصيدك: <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>أكّد عملية الشراء</b>\n\n"
            "🛍 المنتج: <b>{name}</b>\n"
            "💵 السعر: <b>${price:.2f}</b>\n"
            "👛 الرصيد بعد الشراء: <b>${after:.2f}</b>\n\n"
            "اضغط <b>تأكيد الشراء</b> للمتابعة."
        ),
        "insufficient": (
            "❌ <b>رصيد غير كافٍ</b>\n\n"
            "سعر هذا العنصر <b>${price:.2f}</b> لكن رصيدك <b>${balance:.2f}</b>.\n\n"
            "💡 اضغط <b>إيداع الآن</b> لإضافة رصيد."
        ),
        "out_of_stock": (
            "😔 <b>نفد المخزون</b>\n\n"
            "نفد هذا المنتج للتو. يرجى العودة لاحقاً!"
        ),
        "order_success": (
            "✅ <b>اكتمل الشراء!</b>\n\n"
            "🧾 الطلب <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 المدفوع: <b>${price:.2f}</b>\n"
            "👛 الرصيد الجديد: <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "شكراً لطلبك! 🎉"
        ),
        "orders_empty": (
            "📦 <b>طلباتي</b>\n\n"
            "لم تقم بأي طلب بعد.\n"
            "توجّه إلى <b>المتجر</b> لتحصل على شيء! 🛍"
        ),
        "orders_header": "📜 <b>سجل طلباتي</b>\n\nطلباتك الأخيرة:\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "غير محدود",
    },
    # ------------------------------------------------------------------ FR
    "fr": {
        "welcome": (
            "👋 <b>Salut {name}, bienvenue !</b>\n\n"
            "Votre boutique pour des <b>abonnements numériques premium</b> à prix "
            "imbattables — <i>rapide, sécurisé et entièrement automatisé.</i> ⚡\n\n"
            "<blockquote>"
            "🔥 <b>200 000+</b> commandes livrées\n"
            "⭐ Note de <b>4.9/5</b> des clients\n"
            "⏱ Livraison <b>instantanée</b> et automatique, 24h/24"
            "</blockquote>\n\n"
            "<b>Que souhaitez-vous faire ?</b>\n"
            "<blockquote>"
            "🛍 <b>Boutique</b> — Parcourir et acheter\n"
            "💵 <b>Dépôt</b> — Ajouter des fonds\n"
            "🪪 <b>Mon profil</b> — Solde, commandes et réglages\n"
            "🆘 <b>Support</b> — Obtenir de l'aide\n"
            "⭐ <b>Parrainez et gagnez</b> — Invitez des amis\n"
            "🌐 <b>Langue</b> — Changer de langue"
            "</blockquote>\n\n"
            "👇 <b>Touchez une option pour commencer !</b>"
        ),
        "btn_shop": "🛍 Boutique",
        "btn_deposit": "💵 Dépôt",
        "btn_profile": "🪪 Mon profil",
        "btn_support": "🆘 Support",
        "btn_refer": "⭐ Parrainer",
        "btn_language": "🌐 Langue",
        "btn_back": "⬅️ Retour au menu",
        "btn_cancel": "⬅️ Annuler",
        "btn_share": "📤 Partager le lien",
        "deposit_intro": (
            "💵 <b>Dépôt — USDT (BEP20)</b>\n\n"
            "Rechargez votre portefeuille en USDT sur Binance Smart Chain.\n\n"
            "<blockquote>"
            "💰 Entrez le montant à déposer (en USDT)\n"
            "📉 Min <b>${min:.0f}</b>  •  📈 Max <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 Tapez juste un nombre, ex. <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ Cela ne ressemble pas à un nombre. Tapez un montant comme <code>25</code>."
        ),
        "deposit_range": "❌ Le montant doit être entre ${min:.0f} et ${max:,.0f}.",
        "deposit_not_configured": (
            "⚠️ Les dépôts crypto ne sont pas encore configurés. Contactez le support."
        ),
        "deposit_instructions": (
            "💵 <b>Envoyez exactement ce montant</b> 👇\n\n"
            "💰 Montant : <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 Réseau : <b>BEP20 (BSC)</b>\n"
            "📥 Adresse :\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ Envoyez le montant <b>exact</b> ci-dessus — les décimales "
            "supplémentaires identifient votre paiement.\n"
            "⚠️ Utilisez uniquement le réseau <b>BEP20 (BSC)</b>. Les autres seront perdus.\n"
            "⏱ Cette demande expire dans <b>{minutes} minutes</b>."
            "</blockquote>\n\n"
            "✅ Votre solde est crédité automatiquement après confirmation."
        ),
        "deposit_received": (
            "✅ <b>Dépôt reçu !</b>\n\n"
            "Nous avons reçu <b>{amount:.2f} USDT</b> et crédité "
            "<b>${credited:.2f}</b> sur votre portefeuille.\n\n"
            "👛 Nouveau solde : <b>${balance:.2f}</b>\n\n"
            "Merci pour votre paiement ! 🎉"
        ),
        "profile": (
            "🪪 <b>Mon profil</b>\n\n"
            "👤 Nom : <b>{name}</b>\n"
            "🆔 ID : <code>{user_id}</code>\n"
            "👛 Solde : <b>${balance:.2f}</b>\n"
            "📦 Commandes : <b>{orders}</b>\n\n"
            "⭐ <b>Parrainages</b>\n"
            "<blockquote>"
            "👥 Amis invités : <b>{referrals}</b>\n"
            "💰 Récompenses gagnées : <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 Touchez <b>Parrainer</b> pour votre lien, ou <b>Dépôt</b> pour recharger."
        ),
        "shop": (
            "🛍 <b>Boutique</b>\n\n"
            "Nous réapprovisionnons en ce moment. 📦\n\n"
            "🔔 De nouveautés arrivent très bientôt, revenez plus tard !\n"
            "<i>Astuce : gardez des fonds prêts pour ne rien manquer.</i> 💎"
        ),
        "support": (
            "🆘 <b>Support</b>\n\n"
            "Bloqué ou une question ? Nous sommes là. 🤝\n\n"
            "📩 Écrivez-nous : {contact}\n"
            "⏱ Nous répondons généralement en quelques heures."
        ),
        "refer": (
            "⭐ <b>Parrainez et gagnez</b>\n\n"
            "Invitez des amis et gagnez des récompenses sur leurs dépôts ! 🎁\n\n"
            "<blockquote>"
            "👥 Amis invités : <b>{referrals}</b>\n"
            "💰 Récompenses gagnées : <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>Votre lien d'invitation :</b>\n"
            "{link}\n\n"
            "Partagez-le partout — la récompense est automatique. 🚀"
        ),
        "language_choose": (
            "🌐 <b>Choisissez votre langue</b>\n\n"
            "Sélectionnez votre langue préférée ci-dessous. 👇"
        ),
        "language_updated": (
            "✅ <b>Langue mise à jour</b>\n\n"
            "Votre langue est maintenant <b>{lang}</b>."
        ),
        "help": (
            "ℹ️ <b>Aide et commandes</b>\n\n"
            "/start — Ouvrir le menu principal\n"
            "/help — Afficher cette aide\n\n"
            "Utilisez les boutons pour acheter, déposer, voir votre profil, "
            "le support ou parrainer. 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>Récompense de parrainage !</b>\n\n"
            "Un ami invité vient de faire son premier dépôt.\n"
            "💰 Vous avez gagné <b>${reward:.2f}</b> !\n"
            "👛 Nouveau solde : <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "Rejoins-moi sur ce bot d'abonnements numériques premium à petit prix ! 🚀"
        ),
        "btn_buy": "🛒 Acheter",
        "btn_confirm": "✅ Confirmer l'achat",
        "btn_orders": "📜 ✦ Historique des commandes ✦",
        "btn_back_shop": "⬅️ Retour à la boutique",
        "btn_deposit_now": "💵 Déposer",
        "shop_list": (
            "🛍 <b>Boutique</b>\n\n"
            "👛 Votre solde : <b>${balance:.2f}</b>\n\n"
            "Choisissez un produit ci-dessous pour voir les détails et acheter. 👇"
        ),
        "shop_empty": (
            "🛍 <b>Boutique</b>\n\n"
            "Aucun produit disponible pour le moment. Revenez bientôt ! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 Prix : <b>${price:.2f}</b>\n"
            "📦 Stock : <b>{stock}</b>\n"
            "👛 Votre solde : <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>Confirmez votre achat</b>\n\n"
            "🛍 Produit : <b>{name}</b>\n"
            "💵 Prix : <b>${price:.2f}</b>\n"
            "👛 Solde après : <b>${after:.2f}</b>\n\n"
            "Touchez <b>Confirmer l'achat</b> pour continuer."
        ),
        "insufficient": (
            "❌ <b>Solde insuffisant</b>\n\n"
            "Cet article coûte <b>${price:.2f}</b> mais votre solde est "
            "<b>${balance:.2f}</b>.\n\n"
            "💡 Touchez <b>Déposer</b> pour recharger."
        ),
        "out_of_stock": (
            "😔 <b>Rupture de stock</b>\n\n"
            "Ce produit vient d'être épuisé. Revenez plus tard !"
        ),
        "order_success": (
            "✅ <b>Achat terminé !</b>\n\n"
            "🧾 Commande <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 Payé : <b>${price:.2f}</b>\n"
            "👛 Nouveau solde : <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "Merci pour votre commande ! 🎉"
        ),
        "orders_empty": (
            "📦 <b>Mes commandes</b>\n\n"
            "Vous n'avez pas encore de commande.\n"
            "Allez à la <b>Boutique</b> pour en trouver ! 🛍"
        ),
        "orders_header": "📜 <b>Historique des commandes</b>\n\nVos commandes récentes :\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "Illimité",
    },
    # ------------------------------------------------------------------ PT
    "pt": {
        "welcome": (
            "👋 <b>Olá {name}, bem-vindo!</b>\n\n"
            "Sua loja para <b>assinaturas digitais premium</b> a preços "
            "imbatíveis — <i>rápido, seguro e totalmente automático.</i> ⚡\n\n"
            "<blockquote>"
            "🔥 <b>200.000+</b> pedidos entregues\n"
            "⭐ Avaliação <b>4.9/5</b> dos clientes\n"
            "⏱ Entrega <b>instantânea</b> e automática, 24/7"
            "</blockquote>\n\n"
            "<b>O que você gostaria de fazer?</b>\n"
            "<blockquote>"
            "🛍 <b>Loja</b> — Explorar e comprar\n"
            "💵 <b>Depósito</b> — Adicionar saldo\n"
            "🪪 <b>Meu perfil</b> — Saldo, pedidos e ajustes\n"
            "🆘 <b>Suporte</b> — Obter ajuda\n"
            "⭐ <b>Indique e ganhe</b> — Convide amigos\n"
            "🌐 <b>Idioma</b> — Mudar idioma"
            "</blockquote>\n\n"
            "👇 <b>Toque numa opção para começar!</b>"
        ),
        "btn_shop": "🛍 Loja",
        "btn_deposit": "💵 Depósito",
        "btn_profile": "🪪 Meu perfil",
        "btn_support": "🆘 Suporte",
        "btn_refer": "⭐ Indicar",
        "btn_language": "🌐 Idioma",
        "btn_back": "⬅️ Voltar ao menu",
        "btn_cancel": "⬅️ Cancelar",
        "btn_share": "📤 Compartilhar link",
        "deposit_intro": (
            "💵 <b>Depósito — USDT (BEP20)</b>\n\n"
            "Adicione saldo com USDT na Binance Smart Chain.\n\n"
            "<blockquote>"
            "💰 Digite o valor a depositar (em USDT)\n"
            "📉 Mín <b>${min:.0f}</b>  •  📈 Máx <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 Basta digitar um número, ex. <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ Isso não parece um número. Digite um valor como <code>25</code>."
        ),
        "deposit_range": "❌ O valor deve estar entre ${min:.0f} e ${max:,.0f}.",
        "deposit_not_configured": (
            "⚠️ Os depósitos em cripto ainda não estão configurados. Fale com o suporte."
        ),
        "deposit_instructions": (
            "💵 <b>Envie exatamente este valor</b> 👇\n\n"
            "💰 Valor: <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 Rede: <b>BEP20 (BSC)</b>\n"
            "📥 Endereço:\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ Envie o valor <b>exato</b> acima — as casas decimais extras "
            "identificam seu pagamento.\n"
            "⚠️ Use apenas a rede <b>BEP20 (BSC)</b>. Outras redes serão perdidas.\n"
            "⏱ Este pedido expira em <b>{minutes} minutos</b>."
            "</blockquote>\n\n"
            "✅ Seu saldo é creditado automaticamente após a confirmação."
        ),
        "deposit_received": (
            "✅ <b>Depósito recebido!</b>\n\n"
            "Recebemos <b>{amount:.2f} USDT</b> e creditamos "
            "<b>${credited:.2f}</b> na sua carteira.\n\n"
            "👛 Novo saldo: <b>${balance:.2f}</b>\n\n"
            "Obrigado pelo pagamento! 🎉"
        ),
        "profile": (
            "🪪 <b>Meu perfil</b>\n\n"
            "👤 Nome: <b>{name}</b>\n"
            "🆔 ID: <code>{user_id}</code>\n"
            "👛 Saldo: <b>${balance:.2f}</b>\n"
            "📦 Pedidos: <b>{orders}</b>\n\n"
            "⭐ <b>Indicações</b>\n"
            "<blockquote>"
            "👥 Amigos convidados: <b>{referrals}</b>\n"
            "💰 Recompensas ganhas: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 Toque em <b>Indicar</b> para seu link, ou <b>Depósito</b> para recarregar."
        ),
        "shop": (
            "🛍 <b>Loja</b>\n\n"
            "Estamos repondo o estoque agora. 📦\n\n"
            "🔔 Novidades chegam em breve, volte mais tarde!\n"
            "<i>Dica: tenha saldo pronto para não perder.</i> 💎"
        ),
        "support": (
            "🆘 <b>Suporte</b>\n\n"
            "Travou ou tem uma dúvida? Estamos aqui. 🤝\n\n"
            "📩 Fale conosco: {contact}\n"
            "⏱ Normalmente respondemos em algumas horas."
        ),
        "refer": (
            "⭐ <b>Indique e ganhe</b>\n\n"
            "Convide amigos e ganhe recompensas nos depósitos deles! 🎁\n\n"
            "<blockquote>"
            "👥 Amigos convidados: <b>{referrals}</b>\n"
            "💰 Recompensas ganhas: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>Seu link de convite:</b>\n"
            "{link}\n\n"
            "Compartilhe onde quiser — a recompensa é automática. 🚀"
        ),
        "language_choose": (
            "🌐 <b>Escolha seu idioma</b>\n\n"
            "Selecione seu idioma preferido abaixo. 👇"
        ),
        "language_updated": (
            "✅ <b>Idioma atualizado</b>\n\n"
            "Seu idioma agora é <b>{lang}</b>."
        ),
        "help": (
            "ℹ️ <b>Ajuda e comandos</b>\n\n"
            "/start — Abrir o menu principal\n"
            "/help — Mostrar esta ajuda\n\n"
            "Use os botões para comprar, depositar, ver seu perfil, "
            "obter suporte ou indicar amigos. 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>Recompensa de indicação!</b>\n\n"
            "Um amigo convidado acabou de fazer o primeiro depósito.\n"
            "💰 Você ganhou <b>${reward:.2f}</b>!\n"
            "👛 Novo saldo: <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "Junte-se a mim neste bot de assinaturas digitais premium a ótimos preços! 🚀"
        ),
        "btn_buy": "🛒 Comprar agora",
        "btn_confirm": "✅ Confirmar compra",
        "btn_orders": "📜 ✦ Histórico de pedidos ✦",
        "btn_back_shop": "⬅️ Voltar à loja",
        "btn_deposit_now": "💵 Depositar agora",
        "shop_list": (
            "🛍 <b>Loja</b>\n\n"
            "👛 Seu saldo: <b>${balance:.2f}</b>\n\n"
            "Escolha um produto abaixo para ver detalhes e comprar. 👇"
        ),
        "shop_empty": (
            "🛍 <b>Loja</b>\n\n"
            "Nenhum produto disponível agora. Volte em breve! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 Preço: <b>${price:.2f}</b>\n"
            "📦 Estoque: <b>{stock}</b>\n"
            "👛 Seu saldo: <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>Confirme sua compra</b>\n\n"
            "🛍 Produto: <b>{name}</b>\n"
            "💵 Preço: <b>${price:.2f}</b>\n"
            "👛 Saldo após: <b>${after:.2f}</b>\n\n"
            "Toque em <b>Confirmar compra</b> para continuar."
        ),
        "insufficient": (
            "❌ <b>Saldo insuficiente</b>\n\n"
            "Este item custa <b>${price:.2f}</b> mas seu saldo é "
            "<b>${balance:.2f}</b>.\n\n"
            "💡 Toque em <b>Depositar agora</b> para recarregar."
        ),
        "out_of_stock": (
            "😔 <b>Esgotado</b>\n\n"
            "Este produto acabou de esgotar. Volte mais tarde!"
        ),
        "order_success": (
            "✅ <b>Compra concluída!</b>\n\n"
            "🧾 Pedido <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 Pago: <b>${price:.2f}</b>\n"
            "👛 Novo saldo: <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "Obrigado pelo seu pedido! 🎉"
        ),
        "orders_empty": (
            "📦 <b>Meus pedidos</b>\n\n"
            "Você ainda não fez nenhum pedido.\n"
            "Vá para a <b>Loja</b> para pegar algo! 🛍"
        ),
        "orders_header": "📜 <b>Histórico de pedidos</b>\n\nSeus pedidos recentes:\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "Ilimitado",
    },
    # ------------------------------------------------------------------ DE
    "de": {
        "welcome": (
            "👋 <b>Hallo {name}, willkommen!</b>\n\n"
            "Deine Anlaufstelle für <b>Premium-Digital-Abos</b> zu unschlagbaren "
            "Preisen — <i>schnell, sicher und vollautomatisch.</i> ⚡\n\n"
            "<blockquote>"
            "🔥 <b>200.000+</b> Bestellungen geliefert\n"
            "⭐ <b>4.9/5</b> Bewertung von Kunden\n"
            "⏱ <b>Sofortige</b> automatische Lieferung, rund um die Uhr"
            "</blockquote>\n\n"
            "<b>Was möchtest du tun?</b>\n"
            "<blockquote>"
            "🛍 <b>Shop</b> — Produkte ansehen &amp; kaufen\n"
            "💵 <b>Einzahlen</b> — Guthaben aufladen\n"
            "🪪 <b>Mein Profil</b> — Guthaben, Bestellungen &amp; Einstellungen\n"
            "🆘 <b>Support</b> — Hilfe erhalten\n"
            "⭐ <b>Empfehlen &amp; Verdienen</b> — Freunde einladen\n"
            "🌐 <b>Sprache</b> — Sprache ändern"
            "</blockquote>\n\n"
            "👇 <b>Tippe unten auf eine Option, um zu starten!</b>"
        ),
        "btn_shop": "🛍 Shop",
        "btn_deposit": "💵 Einzahlen",
        "btn_profile": "🪪 Mein Profil",
        "btn_support": "🆘 Support",
        "btn_refer": "⭐ Empfehlen",
        "btn_language": "🌐 Sprache",
        "btn_back": "⬅️ Zurück zum Menü",
        "btn_cancel": "⬅️ Abbrechen",
        "btn_share": "📤 Einladungslink teilen",
        "deposit_intro": (
            "💵 <b>Einzahlung — USDT (BEP20)</b>\n\n"
            "Lade dein Wallet mit USDT auf Binance Smart Chain auf.\n\n"
            "<blockquote>"
            "💰 Gib den Einzahlungsbetrag ein (in USDT)\n"
            "📉 Min <b>${min:.0f}</b>  •  📈 Max <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 Tippe einfach eine Zahl, z. B. <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ Das sieht nicht wie eine Zahl aus. Gib einen Betrag wie <code>25</code> ein."
        ),
        "deposit_range": "❌ Der Betrag muss zwischen ${min:.0f} und ${max:,.0f} liegen.",
        "deposit_not_configured": (
            "⚠️ Krypto-Einzahlungen sind noch nicht eingerichtet. Bitte kontaktiere den Support."
        ),
        "deposit_instructions": (
            "💵 <b>Sende genau diesen Betrag</b> 👇\n\n"
            "💰 Betrag: <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 Netzwerk: <b>BEP20 (BSC)</b>\n"
            "📥 Adresse:\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ Sende den <b>exakten</b> Betrag oben — die zusätzlichen "
            "Nachkommastellen identifizieren deine Zahlung.\n"
            "⚠️ Nutze nur das <b>BEP20 (BSC)</b>-Netzwerk. Andere gehen verloren.\n"
            "⏱ Diese Anfrage läuft in <b>{minutes} Minuten</b> ab."
            "</blockquote>\n\n"
            "✅ Dein Guthaben wird nach Bestätigung automatisch gutgeschrieben."
        ),
        "deposit_received": (
            "✅ <b>Einzahlung erhalten!</b>\n\n"
            "Wir haben <b>{amount:.2f} USDT</b> erhalten und "
            "<b>${credited:.2f}</b> deinem Wallet gutgeschrieben.\n\n"
            "👛 Neues Guthaben: <b>${balance:.2f}</b>\n\n"
            "Danke für deine Zahlung! 🎉"
        ),
        "profile": (
            "🪪 <b>Mein Profil</b>\n\n"
            "👤 Name: <b>{name}</b>\n"
            "🆔 Benutzer-ID: <code>{user_id}</code>\n"
            "👛 Guthaben: <b>${balance:.2f}</b>\n"
            "📦 Bestellungen: <b>{orders}</b>\n\n"
            "⭐ <b>Empfehlungen</b>\n"
            "<blockquote>"
            "👥 Eingeladene Freunde: <b>{referrals}</b>\n"
            "💰 Verdiente Prämien: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 Tippe auf <b>Empfehlen</b> für deinen Link oder <b>Einzahlen</b> zum Aufladen."
        ),
        "shop": (
            "🛍 <b>Shop</b>\n\n"
            "Wir füllen gerade die Regale auf. 📦\n\n"
            "🔔 Neue Angebote kommen bald, schau später wieder vorbei!\n"
            "<i>Tipp: Halte etwas Guthaben bereit, um nichts zu verpassen.</i> 💎"
        ),
        "support": (
            "🆘 <b>Support</b>\n\n"
            "Steckst du fest oder hast eine Frage? Wir helfen. 🤝\n\n"
            "📩 Kontaktiere uns: {contact}\n"
            "⏱ Wir antworten meist innerhalb weniger Stunden."
        ),
        "refer": (
            "⭐ <b>Empfehlen &amp; Verdienen</b>\n\n"
            "Lade Freunde ein und verdiene Prämien bei ihren Einzahlungen! 🎁\n\n"
            "<blockquote>"
            "👥 Eingeladene Freunde: <b>{referrals}</b>\n"
            "💰 Verdiente Prämien: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>Dein Einladungslink:</b>\n"
            "{link}\n\n"
            "Teile ihn überall — die Prämie kommt automatisch. 🚀"
        ),
        "language_choose": (
            "🌐 <b>Wähle deine Sprache</b>\n\n"
            "Wähle unten deine bevorzugte Sprache. 👇"
        ),
        "language_updated": (
            "✅ <b>Sprache aktualisiert</b>\n\n"
            "Deine Sprache ist jetzt <b>{lang}</b>."
        ),
        "help": (
            "ℹ️ <b>Hilfe &amp; Befehle</b>\n\n"
            "/start — Hauptmenü öffnen\n"
            "/help — Diese Hilfe anzeigen\n\n"
            "Nutze die Menü-Buttons zum Kaufen, Einzahlen, Profil ansehen, "
            "Support oder Freunde empfehlen. 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>Empfehlungsprämie!</b>\n\n"
            "Einer deiner eingeladenen Freunde hat gerade zum ersten Mal eingezahlt.\n"
            "💰 Du hast <b>${reward:.2f}</b> verdient!\n"
            "👛 Neues Guthaben: <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "Komm mit mir zu diesem Bot für Premium-Digital-Abos zu Top-Preisen! 🚀"
        ),
        "btn_buy": "🛒 Jetzt kaufen",
        "btn_confirm": "✅ Kauf bestätigen",
        "btn_orders": "📜 ✦ Meine Bestellhistorie ✦",
        "btn_back_shop": "⬅️ Zurück zum Shop",
        "btn_deposit_now": "💵 Jetzt einzahlen",
        "shop_list": (
            "🛍 <b>Shop</b>\n\n"
            "👛 Dein Guthaben: <b>${balance:.2f}</b>\n\n"
            "Wähle unten ein Produkt für Details und Kauf. 👇"
        ),
        "shop_empty": (
            "🛍 <b>Shop</b>\n\n"
            "Momentan sind keine Produkte verfügbar. Schau bald wieder vorbei! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 Preis: <b>${price:.2f}</b>\n"
            "📦 Bestand: <b>{stock}</b>\n"
            "👛 Dein Guthaben: <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>Bestätige deinen Kauf</b>\n\n"
            "🛍 Produkt: <b>{name}</b>\n"
            "💵 Preis: <b>${price:.2f}</b>\n"
            "👛 Guthaben danach: <b>${after:.2f}</b>\n\n"
            "Tippe auf <b>Kauf bestätigen</b>, um fortzufahren."
        ),
        "insufficient": (
            "❌ <b>Nicht genug Guthaben</b>\n\n"
            "Dieser Artikel kostet <b>${price:.2f}</b>, dein Guthaben beträgt "
            "<b>${balance:.2f}</b>.\n\n"
            "💡 Tippe auf <b>Jetzt einzahlen</b> zum Aufladen."
        ),
        "out_of_stock": (
            "😔 <b>Ausverkauft</b>\n\n"
            "Dieses Produkt ist gerade ausverkauft. Bitte später erneut versuchen!"
        ),
        "order_success": (
            "✅ <b>Kauf abgeschlossen!</b>\n\n"
            "🧾 Bestellung <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 Bezahlt: <b>${price:.2f}</b>\n"
            "👛 Neues Guthaben: <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "Danke für deine Bestellung! 🎉"
        ),
        "orders_empty": (
            "📦 <b>Meine Bestellungen</b>\n\n"
            "Du hast noch keine Bestellung aufgegeben.\n"
            "Geh zum <b>Shop</b>, um etwas zu holen! 🛍"
        ),
        "orders_header": "📜 <b>Meine Bestellhistorie</b>\n\nDeine letzten Bestellungen:\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "Unbegrenzt",
    },
    # ------------------------------------------------------------------ ID
    "id": {
        "welcome": (
            "👋 <b>Hai {name}, selamat datang!</b>\n\n"
            "Tempat terbaik untuk <b>langganan digital premium</b> dengan harga "
            "tak tertandingi — <i>cepat, aman, dan sepenuhnya otomatis.</i> ⚡\n\n"
            "<blockquote>"
            "🔥 <b>200.000+</b> pesanan terkirim\n"
            "⭐ Rating <b>4.9/5</b> dari pelanggan\n"
            "⏱ Pengiriman <b>instan</b> otomatis, 24/7"
            "</blockquote>\n\n"
            "<b>Apa yang ingin kamu lakukan?</b>\n"
            "<blockquote>"
            "🛍 <b>Toko</b> — Jelajahi &amp; beli produk\n"
            "💵 <b>Deposit</b> — Tambah saldo dompet\n"
            "🪪 <b>Profil Saya</b> — Saldo, pesanan &amp; pengaturan\n"
            "🆘 <b>Dukungan</b> — Dapatkan bantuan\n"
            "⭐ <b>Ajak &amp; Dapatkan</b> — Undang teman &amp; raih hadiah\n"
            "🌐 <b>Bahasa</b> — Ubah bahasa"
            "</blockquote>\n\n"
            "👇 <b>Ketuk salah satu opsi di bawah untuk memulai!</b>"
        ),
        "btn_shop": "🛍 Toko",
        "btn_deposit": "💵 Deposit",
        "btn_profile": "🪪 Profil Saya",
        "btn_support": "🆘 Dukungan",
        "btn_refer": "⭐ Ajak Teman",
        "btn_language": "🌐 Bahasa",
        "btn_back": "⬅️ Kembali ke menu",
        "btn_cancel": "⬅️ Batal",
        "btn_share": "📤 Bagikan tautan undangan",
        "deposit_intro": (
            "💵 <b>Deposit — USDT (BEP20)</b>\n\n"
            "Isi dompetmu dengan USDT di Binance Smart Chain.\n\n"
            "<blockquote>"
            "💰 Masukkan jumlah deposit (dalam USDT)\n"
            "📉 Min <b>${min:.0f}</b>  •  📈 Maks <b>${max:,.0f}</b>"
            "</blockquote>\n\n"
            "👉 Cukup ketik angka, mis. <code>25</code>"
        ),
        "deposit_not_number": (
            "❌ Itu sepertinya bukan angka. Ketik jumlah seperti <code>25</code>."
        ),
        "deposit_range": "❌ Jumlah harus antara ${min:.0f} dan ${max:,.0f}.",
        "deposit_not_configured": (
            "⚠️ Deposit kripto belum dikonfigurasi. Silakan hubungi dukungan."
        ),
        "deposit_instructions": (
            "💵 <b>Kirim tepat jumlah ini</b> 👇\n\n"
            "💰 Jumlah: <code>{amount:.2f}</code> <b>USDT</b>\n"
            "🌐 Jaringan: <b>BEP20 (BSC)</b>\n"
            "📥 Alamat:\n"
            "<code>{address}</code>\n\n"
            "<blockquote>"
            "⚠️ Kirim jumlah yang <b>tepat</b> di atas — desimal tambahan "
            "mengidentifikasi pembayaranmu.\n"
            "⚠️ Gunakan hanya jaringan <b>BEP20 (BSC)</b>. Jaringan lain akan hilang.\n"
            "⏱ Permintaan ini kedaluwarsa dalam <b>{minutes} menit</b>."
            "</blockquote>\n\n"
            "✅ Saldomu otomatis bertambah setelah transfer terkonfirmasi."
        ),
        "deposit_received": (
            "✅ <b>Deposit diterima!</b>\n\n"
            "Kami menerima <b>{amount:.2f} USDT</b> dan menambahkan "
            "<b>${credited:.2f}</b> ke dompetmu.\n\n"
            "👛 Saldo baru: <b>${balance:.2f}</b>\n\n"
            "Terima kasih atas pembayaranmu! 🎉"
        ),
        "profile": (
            "🪪 <b>Profil Saya</b>\n\n"
            "👤 Nama: <b>{name}</b>\n"
            "🆔 ID Pengguna: <code>{user_id}</code>\n"
            "👛 Saldo: <b>${balance:.2f}</b>\n"
            "📦 Pesanan: <b>{orders}</b>\n\n"
            "⭐ <b>Referral</b>\n"
            "<blockquote>"
            "👥 Teman diundang: <b>{referrals}</b>\n"
            "💰 Hadiah diperoleh: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "💡 Ketuk <b>Ajak Teman</b> untuk tautanmu, atau <b>Deposit</b> untuk mengisi saldo."
        ),
        "shop": (
            "🛍 <b>Toko</b>\n\n"
            "Kami sedang mengisi ulang stok. 📦\n\n"
            "🔔 Produk baru segera hadir, cek lagi nanti!\n"
            "<i>Tips: siapkan saldo agar tidak ketinggalan.</i> 💎"
        ),
        "support": (
            "🆘 <b>Dukungan</b>\n\n"
            "Terkendala atau ada pertanyaan? Kami siap membantu. 🤝\n\n"
            "📩 Hubungi kami di {contact}\n"
            "⏱ Kami biasanya membalas dalam beberapa jam."
        ),
        "refer": (
            "⭐ <b>Ajak &amp; Dapatkan</b>\n\n"
            "Undang teman dan dapatkan hadiah dari deposit mereka! 🎁\n\n"
            "<blockquote>"
            "👥 Teman diundang: <b>{referrals}</b>\n"
            "💰 Hadiah diperoleh: <b>${earnings:.2f}</b>"
            "</blockquote>\n\n"
            "🔗 <b>Tautan undanganmu:</b>\n"
            "{link}\n\n"
            "Bagikan di mana saja — hadiah otomatis diberikan. 🚀"
        ),
        "language_choose": (
            "🌐 <b>Pilih bahasamu</b>\n\n"
            "Pilih bahasa yang kamu inginkan di bawah. 👇"
        ),
        "language_updated": (
            "✅ <b>Bahasa diperbarui</b>\n\n"
            "Bahasamu sekarang <b>{lang}</b>."
        ),
        "help": (
            "ℹ️ <b>Bantuan &amp; perintah</b>\n\n"
            "/start — Buka menu utama\n"
            "/help — Tampilkan pesan bantuan ini\n\n"
            "Gunakan tombol menu untuk belanja, deposit, lihat profil, "
            "dukungan, atau ajak teman. 👇"
        ),
        "referral_bonus_notify": (
            "🎉 <b>Hadiah referral!</b>\n\n"
            "Salah satu teman yang kamu undang baru saja melakukan deposit pertama.\n"
            "💰 Kamu memperoleh <b>${reward:.2f}</b>!\n"
            "👛 Saldo baru: <b>${balance:.2f}</b>"
        ),
        "share_text": (
            "Gabung denganku di bot ini untuk langganan digital premium dengan harga hebat! 🚀"
        ),
        "btn_buy": "🛒 Beli sekarang",
        "btn_confirm": "✅ Konfirmasi pembelian",
        "btn_orders": "📜 ✦ Riwayat Pesanan ✦",
        "btn_back_shop": "⬅️ Kembali ke toko",
        "btn_deposit_now": "💵 Deposit sekarang",
        "shop_list": (
            "🛍 <b>Toko</b>\n\n"
            "👛 Saldomu: <b>${balance:.2f}</b>\n\n"
            "Pilih produk di bawah untuk melihat detail dan membeli. 👇"
        ),
        "shop_empty": (
            "🛍 <b>Toko</b>\n\n"
            "Belum ada produk tersedia saat ini. Cek lagi nanti! 🔔"
        ),
        "product_detail": (
            "🛍 <b>{name}</b>\n\n"
            "{description}\n\n"
            "💵 Harga: <b>${price:.2f}</b>\n"
            "📦 Stok: <b>{stock}</b>\n"
            "👛 Saldomu: <b>${balance:.2f}</b>"
        ),
        "confirm_purchase": (
            "🧾 <b>Konfirmasi pembelianmu</b>\n\n"
            "🛍 Produk: <b>{name}</b>\n"
            "💵 Harga: <b>${price:.2f}</b>\n"
            "👛 Saldo setelahnya: <b>${after:.2f}</b>\n\n"
            "Ketuk <b>Konfirmasi pembelian</b> untuk melanjutkan."
        ),
        "insufficient": (
            "❌ <b>Saldo tidak cukup</b>\n\n"
            "Item ini seharga <b>${price:.2f}</b> tetapi saldomu <b>${balance:.2f}</b>.\n\n"
            "💡 Ketuk <b>Deposit sekarang</b> untuk mengisi saldo."
        ),
        "out_of_stock": (
            "😔 <b>Stok habis</b>\n\n"
            "Produk ini baru saja habis. Silakan cek lagi nanti!"
        ),
        "order_success": (
            "✅ <b>Pembelian selesai!</b>\n\n"
            "🧾 Pesanan <b>#{order_id}</b>\n"
            "🛍 <b>{name}</b>\n"
            "💵 Dibayar: <b>${price:.2f}</b>\n"
            "👛 Saldo baru: <b>${balance:.2f}</b>\n\n"
            "<blockquote>{delivery}</blockquote>\n\n"
            "Terima kasih atas pesananmu! 🎉"
        ),
        "orders_empty": (
            "📦 <b>Pesanan Saya</b>\n\n"
            "Kamu belum melakukan pesanan apa pun.\n"
            "Kunjungi <b>Toko</b> untuk mengambil sesuatu! 🛍"
        ),
        "orders_header": "📜 <b>Riwayat Pesanan</b>\n\nPesanan terbarumu:\n",
        "orders_line": "🧾 #{order_id} — {name} — <b>${price:.2f}</b>",
        "stock_unlimited": "Tanpa batas",
    },
}


def t(key: str, lang: str = "en", **kwargs) -> str:
    """Return the translated string for `key` in `lang`, formatted with kwargs.

    Falls back to English if the language or key is missing.
    """
    lang = lang if lang in TRANSLATIONS else "en"
    table = TRANSLATIONS[lang]
    template = table.get(key) or TRANSLATIONS["en"].get(key, key)
    try:
        return template.format(**kwargs) if kwargs else template
    except (KeyError, IndexError, ValueError):
        return template
