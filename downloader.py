import yt_dlp
import os

async def download_and_send(url, update):
    # Inform user
    await update.message.reply_text("⏳ Downloading... Please wait!")

    try:
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'mp4/bestaudio/best',
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # Send video
        with open(file_path, "rb") as video:
            await update.message.reply_video(video)

        # Cleanup
        os.remove(file_path)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")
