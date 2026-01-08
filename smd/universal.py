import os
import requests
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def download_media(url: str, mode="video"):
    os.makedirs("downloads", exist_ok=True)

    # 🎵 AUDIO (MP3)
    if mode == "audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/audio_%(extractor)s_%(id)s.%(ext)s",
            "quiet": True,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info), "audio"

    # 🎥 VIDEO (BEST QUALITY ONLY)
    try:
        ydl_opts = {
            "format": "best",
            "outtmpl": "downloads/%(extractor)s_%(id)s.%(ext)s",
            "quiet": True,
            "noplaylist": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info), "video"

    except Exception:
        pass

    # 🖼️ IMAGE FALLBACK (Pinterest / wallpaper)
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            img_url = og_image["content"]
            data = requests.get(img_url, headers=HEADERS).content
            ext = img_url.split(".")[-1].split("?")[0]
            path = f"downloads/image_{hash(img_url)}.{ext}"
            with open(path, "wb") as f:
                f.write(data)
            return path, "image"

    except Exception:
        pass

    raise Exception("No downloadable media found")
