from pyrogram import filters
from utils.detect import detect_platform
from smd import DOWNLOADERS

async def handle_message(client, message):
    if not message.text:
        return

    url = message.text.strip()
    platform = detect_platform(url)

    if not platform:
        await message.reply("❌ Unsupported link")
        return

    await message.reply("⏳ Downloading...")

    try:
        file_path = DOWNLOADERS[platform](url)
        await message.reply_document(file_path)
    except Exception as e:
        await message.reply(f"❌ Error: {e}")
