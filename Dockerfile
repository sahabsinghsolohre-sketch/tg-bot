FROM python:3.12-slim

# Keep Python output unbuffered so host logs show everything live.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# The built-in health-check server listens here (Render/Koyeb health checks).
ENV PORT=8080
EXPOSE 8080

CMD ["python", "bot.py"]
