import os
from yt_dlp import YoutubeDL

def download_media(url: str):
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "format": "best",  # 🔥 no merge issue
        "outtmpl": "downloads/%(extractor)s_%(id)s.%(ext)s",
        "noplaylist": True,
        "quiet": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        # Pinterest / image-only case
        if info.get("formats") is None and info.get("url"):
            return info["url"], "image"

        return ydl.prepare_filename(info), "video"
