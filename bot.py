from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH
from handlers import handle_message, media_choice_cb, quality_choice_cb

app = Client(
    "smd-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@app.on_message(filters.private & filters.text)
async def on_message(client, message):
    await handle_message(client, message)


@app.on_callback_query(filters.regex("^media\\|"))
async def on_media_choice(client, callback):
    await media_choice_cb(client, callback)


@app.on_callback_query(filters.regex("^quality\\|"))
async def on_quality_choice(client, callback):
    await quality_choice_cb(client, callback)


print("🔥 SMD Bot Started")
app.run()
