import os
from yt_dlp import YoutubeDL

def download_media(url: str):
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "downloads/%(extractor)s_%(id)s.%(ext)s",
        "quiet": True,
        "noplaylist": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
