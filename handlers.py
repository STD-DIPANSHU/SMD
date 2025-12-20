from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, ContextTypes, filters
from downloader import download_and_send

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Send me any social media video link, I'll download it for you!"
    )

async def video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    await download_and_send(url, update)

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, video_handler))
