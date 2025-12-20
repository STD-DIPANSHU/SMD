import os
from telegram.ext import ApplicationBuilder
from handlers import register_handlers

BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN not found! Please set it in environment variables.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    register_handlers(app)

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
