from pyrogram import filters
from smd.universal import download_media
from utils.detect import is_youtube

async def handle_message(client, message):
    if not message.text:
        return

    url = message.text.strip()

    # Optional: YouTube block
    if is_youtube(url):
        await message.reply(
            "❌ YouTube downloads temporarily unavailable.\n"
            "✅ Instagram / TikTok / FB / Twitter supported."
        )
        return

    msg = await message.reply("⏳ Downloading...")

    try:
        file_path = download_media(url)
        await msg.delete()
        await message.reply_document(file_path)
    except Exception as e:
        await msg.edit(f"❌ Failed:\n`{e}`")
