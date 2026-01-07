def detect_platform(url: str):
    url = url.lower()

    if "instagram.com" in url:
        return "instagram"
    if "facebook.com" in url or "fb.watch" in url:
        return "facebook"
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"

    return None
