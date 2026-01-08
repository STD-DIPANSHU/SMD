import os
import requests
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def download_media(
    url: str,
    mode: str = "video",     # video | audio
    quality: str = "best"    # 360 | 720 | best
):
    os.makedirs("downloads", exist_ok=True)

    # ===============================
    # 🎵 AUDIO MODE
    # ===============================
    if mode == "audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/audio_%(extractor)s_%(id)s.%(ext)s",
            "quiet": True,
            "noplaylist": True,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info), "audio"

    # ===============================
    # 🎥 VIDEO MODE
    # ===============================
    try:
        if quality == "360":
            fmt = "best[height<=360]"
        elif quality == "720":
            fmt = "best[height<=720]"
        else:
            fmt = "best"

        ydl_opts = {
            "format": fmt,
            "outtmpl": "downloads/%(extractor)s_%(id)s.%(ext)s",
            "quiet": True,
            "noplaylist": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            if info.get("_type") != "playlist":
                return ydl.prepare_filename(info), "video"

    except Exception:
        pass

    # ===============================
    # 🖼️ PINTEREST / IMAGE FALLBACK
    # ===============================
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            img_url = og_image["content"]

            img_data = requests.get(img_url, headers=HEADERS).content
            ext = img_url.split(".")[-1].split("?")[0]
            path = f"downloads/image_{hash(img_url)}.{ext}"

            with open(path, "wb") as f:
                f.write(img_data)

            return path, "image"

    except Exception:
        pass

    raise Exception("No downloadable media found")
