# Telegram Bot

Ek simple Telegram bot jisme `/start` command par inline buttons dikhte hain.

## Features

- `/start` — welcome message + main menu buttons
- `/help` — commands ki list
- `/addproduct` — Admin command product add karne ke liye
- `/setstock` / `/stock` — Admin command stock view aur manage karne ke liye

## Setup

1. **Bot token lo** — Telegram par [@BotFather](https://t.me/BotFather) se `/newbot` karke token generate karo.

2. **Dependencies install karo:**

   ```powershell
   pip install -r requirements.txt
   ```

3. **Token aur Admin ID set karo** — `.env` file me apna token aur Telegram User ID (`ADMIN_ID`) set karo:
   - Telegram me `@userinfobot` se apna user ID jaan sakte hain.
   - `.env` file me: `ADMIN_ID=your_numeric_user_id`

4. **Bot run karo:**

   ```powershell
   python bot.py
   ```

5. Admin `/addproduct` ya `/stock` bheje ga toh guidance aur options dikhenge. Non-admin bheje ga toh bot koi response nahi dega.

## Admin Commands

### 1. Add Product (`/addproduct`)
Format:
```text
/addproduct id | name | price | description | stock | delivery
```
Example:
```text
/addproduct netflix_1m | 🎬 Netflix Premium | 5.00 | 4K Ultra HD 1 Month | 20 | Login details: user@mail.com / pass123
```

### 2. Manage Stock (`/setstock` / `/stock`)
- `/stock` — Sabhi products ka current stock aur guidance dekhein.
- `/setstock <product_id> <quantity>` — Stock number set karein (e.g. `/setstock netflix_1m 50`).
- `/setstock <product_id> unlimited` — Unlimited stock set karein.
- `/setstock <product_id> +10` — Current stock me 10 add karein.
- `/setstock <product_id> -5` — Current stock me se 5 kam karein.

## Notes

- Har product ka stock random rehta hai aur hamesha **100 se kam** (12–99). Stock har 5 minute
  me 1–3 kam hota hai (urgency ke liye) aur har 24 ghante me naya random value mil jata hai.
- `/setstock` se manual stock set karne par bot restart bhi karo to stock overwrite nahi hota —
  seeding sirf naye products ke liye stock set karta hai.
- Bot band karne ke liye terminal me `Ctrl+C` dabao.
- Har naye terminal session me `BOT_TOKEN` dobara set karna hoga (ya use `.env` + `python-dotenv`).
