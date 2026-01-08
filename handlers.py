from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from smd.universal import download_media


# =========================
# 🔹 MAIN MESSAGE HANDLER
# =========================
async def handle_message(client, message):
    if not message.text:
        return

    url = message.text.strip()

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🎥 Video", callback_data=f"media|video|{url}"),
                InlineKeyboardButton("🎵 Audio", callback_data=f"media|audio|{url}")
            ]
        ]
    )

    await message.reply(
        "Kya download karna hai?",
        reply_markup=keyboard
    )


# =========================
# 🔹 MEDIA TYPE CALLBACK
# =========================
async def media_choice_cb(client, callback):
    _, mode, url = callback.data.split("|", 2)

    if mode == "audio":
        msg = await callback.message.edit_text("🎵 Audio download ho raha hai...")
        path, _ = download_media(url, mode="audio")
        await msg.delete()
        await callback.message.reply_audio(path)
        return

    # VIDEO → ask quality
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("360p", callback_data=f"quality|360|{url}"),
                InlineKeyboardButton("720p", callback_data=f"quality|720|{url}")
            ],
            [
                InlineKeyboardButton("⭐ Best", callback_data=f"quality|best|{url}")
            ]
        ]
    )

    await callback.message.edit_text(
        "Video quality select karo:",
        reply_markup=keyboard
    )


# =========================
# 🔹 QUALITY CALLBACK
# =========================
async def quality_choice_cb(client, callback):
    _, quality, url = callback.data.split("|", 2)

    msg = await callback.message.edit_text(
        f"🎥 Video ({quality}) download ho raha hai..."
    )

    path, _ = download_media(url, mode="video", quality=quality)

    await msg.delete()
    await callback.message.reply_video(path)
