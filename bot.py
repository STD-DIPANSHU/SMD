from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH
from handlers import handle_message

app = Client(
    "smd-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.private & filters.text)
async def downloader(client, message):
    await handle_message(client, message)

print("🔥 SMD Bot Started")
app.run()
