import os
import requests
from yt_dlp import YoutubeDL

def download_media(url: str):
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "format": "best",                  # 🔥 no merge error
        "outtmpl": "downloads/%(extractor)s_%(id)s.%(ext)s",
        "noplaylist": True,
        "quiet": True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            # ✅ VIDEO / GIF / SHORT
            if info.get("_type") != "playlist":
                return ydl.prepare_filename(info), "video"

    except Exception:
        pass  # fallback to image

    # 🔥 IMAGE FALLBACK (Pinterest / wallpapers / posts)
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200 and "image" in r.headers.get("Content-Type", ""):
            ext = r.headers["Content-Type"].split("/")[-1]
            path = f"downloads/image_{hash(url)}.{ext}"
            with open(path, "wb") as f:
                f.write(r.content)
            return path, "image"
    except Exception:
        pass

    raise Exception("No downloadable media found")
