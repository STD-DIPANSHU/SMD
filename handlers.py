from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from smd.universal import download_media
import uuid

# 🔥 URL cache (callback_data limit fix)
URL_CACHE = {}


# =========================
# MAIN MESSAGE HANDLER
# =========================
async def handle_message(client, message):
    if not message.text:
        return

    url = message.text.strip()
    key = uuid.uuid4().hex[:8]
    URL_CACHE[key] = url

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🎥 Video", callback_data=f"media|video|{key}"),
                InlineKeyboardButton("🎵 Audio", callback_data=f"media|audio|{key}")
            ]
        ]
    )

    await message.reply(
        "Kya download karna hai?",
        reply_markup=keyboard
    )


# =========================
# MEDIA TYPE CALLBACK
# =========================
async def media_choice_cb(client, callback):
    _, mode, key = callback.data.split("|", 2)
    url = URL_CACHE.get(key)

    if not url:
        await callback.answer("❌ Session expired. Link dobara bhejo.", show_alert=True)
        return

    if mode == "audio":
        msg = await callback.message.edit_text("🎵 Audio download ho raha hai...")
        path, _ = download_media(url, mode="audio")
        await msg.delete()
        await callback.message.reply_audio(path)
        URL_CACHE.pop(key, None)
        return

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("360p", callback_data=f"quality|360|{key}"),
                InlineKeyboardButton("720p", callback_data=f"quality|720|{key}")
            ],
            [
                InlineKeyboardButton("⭐ Best", callback_data=f"quality|best|{key}")
            ]
        ]
    )

    await callback.message.edit_text(
        "Video quality select karo:",
        reply_markup=keyboard
    )


# =========================
# QUALITY CALLBACK
# =========================
async def quality_choice_cb(client, callback):
    _, quality, key = callback.data.split("|", 2)
    url = URL_CACHE.get(key)

    if not url:
        await callback.answer("❌ Session expired. Link dobara bhejo.", show_alert=True)
        return

    msg = await callback.message.edit_text(
        f"🎥 Video ({quality}) download ho raha hai..."
    )

    path, _ = download_media(url, mode="video", quality=quality)

    await msg.delete()
    await callback.message.reply_video(path)
    URL_CACHE.pop(key, None)
