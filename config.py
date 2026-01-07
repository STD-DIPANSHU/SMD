import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")

OWNER_ID = int(os.getenv("OWNER_ID", 0))

DOWNLOAD_DIR = "downloads"
