# 🚀 24/7 Hosting Guide (bot PC pe chalane ki zarurat nahi)

Bot ek **long-running polling** process hai (webhook nahi), isliye aisa host chahiye
jo process ko 24 ghante chalu rakhe. Neeche 3 tested raaste hain.

---

## 1) Render (sabse aasan, web dashboard)

1. Render Dashboard → **New → Blueprint** → repo select karo (is repo me `render.yaml` hai).
2. Neeche wale **Environment Variables** daalo (values `.env` me se hi):

   | Key | Value |
   |---|---|
   | `BOT_TOKEN` | BotFather ka token |
   | `SUPPORT_CONTACT` | `@NarayaniAdmin` |
   | `DATABASE_URL` | Neon Postgres URL (`postgresql://...sslmode=require`) |
   | `ADMIN_ID` | apna Telegram numeric ID |
   | `BEP20_ADDRESS` | USDT BEP20 wallet address |
   | `BSCSCAN_API_KEY` | bscscan.com se free API key |
   | `DEPOSIT_WINDOW_MINUTES` | `30` |

3. **Create** → deploy start. Logs me ye dikhna chahiye:
   `Bot is starting... Press Ctrl+C to stop.`

⚠️ **Free plan 15 min inactivity ke baad sleep karta hai.** Isse bachne ke liye
[cron-job.org](https://cron-job.org) pe free job banao jo har **10 minute** me
`https://<your-service>.onrender.com/` ko ping kare — bot 24/7 jagta rehta hai.
(Permanent 24/7 ke liye Render ka paid instance type sabse clean hai.)

## 2) Koyeb / Railway / Fly.io (Docker se, sleep nahi)

Repo me `Dockerfile` ready hai:

- **Koyeb**: New Service → GitHub → Dockerfile → **nano** instance (free, no sleep) → env vars → Deploy.
- **Railway**: New Project → Deploy from GitHub → Variables me wahi env vars.
- **Fly.io**: `fly launch` (Dockerfile auto detect) → `fly secrets set BOT_TOKEN=... DATABASE_URL=...`

## 3) Apna VPS / Oracle Cloud Free VM

```bash
git clone <your-repo-url> && cd tg-bot
pip install -r requirements.txt
# .env banao (BOT_TOKEN, DATABASE_URL, ADMIN_ID, ...)
python bot.py            # ya systemd service / docker compose se 24/7
```

---

## ⚡ Speed — 2 rules

1. **Host ko DB ke paas rakho.** Abhi DB `us-east-2` (Ohio) me hai; host bhi US-East
   rakho to har query ~10ms, warna ~1s. (Bot me cache + connection reuse hai, isliye
   yeh worst-case bhi playable rehta hai.)
2. Neon project ko India/Asia me shift karna chaaho to naya project banao (same region
   jo aapke users ke paas hai) aur `DATABASE_URL` badal do.

## ⛔ Sabse important

**Ek token pe ek hi instance chalao.** Do jagah chalaoge to Telegram `409 Conflict`
dega aur bot dono jagah aadha-adhoora kaam karega. Naya host lagane se pehle purana
service **Suspend/Delete** karo.
