import os
import requests
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def download_media(url: str):
    os.makedirs("downloads", exist_ok=True)

    # 🔹 TRY yt-dlp FIRST (video, gif, reels)
    try:
        ydl_opts = {
            "format": "best",
            "outtmpl": "downloads/%(extractor)s_%(id)s.%(ext)s",
            "noplaylist": True,
            "quiet": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            if info.get("_type") != "playlist":
                return ydl.prepare_filename(info), "video"

    except Exception:
        pass

    # 🔹 PINTEREST IMAGE FALLBACK
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            img_url = og_image["content"]

            img_data = requests.get(img_url, headers=HEADERS).content
            ext = img_url.split(".")[-1].split("?")[0]
            path = f"downloads/pinterest_{hash(img_url)}.{ext}"

            with open(path, "wb") as f:
                f.write(img_data)

            return path, "image"

    except Exception:
        pass

    raise Exception("No downloadable media found")
