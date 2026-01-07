from .instagram import download_instagram
from .facebook import download_facebook
from .youtube import download_youtube

DOWNLOADERS = {
    "instagram": download_instagram,
    "facebook": download_facebook,
    "youtube": download_youtube
}
