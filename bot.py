from pyrogram import Client, filters
from config import BOT_TOKEN
from handlers import handle_message

app = Client(
    "smd-bot",
    bot_token=BOT_TOKEN
)

@app.on_message(filters.private & filters.text)
async def downloader(client, message):
    await handle_message(client, message)

print("🔥 SMD Bot Running...")
app.run()
