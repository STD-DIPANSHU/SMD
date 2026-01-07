from yt_dlp import YoutubeDL
import os

def download_instagram(url):
    ydl_opts = {
        "format": "best",
        "outtmpl": "downloads/ig_%(id)s.%(ext)s",
        "quiet": True
    }

    os.makedirs("downloads", exist_ok=True)

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
