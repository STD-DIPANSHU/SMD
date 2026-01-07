from smd.universal import download_media

async def handle_message(client, message):
    if not message.text:
        return

    url = message.text.strip()
    msg = await message.reply("⏳ Downloading...")

    try:
        path, mtype = download_media(url)

        await msg.delete()

        if mtype == "video":
            await message.reply_video(path)
        else:
            await message.reply_photo(path)

    except Exception as e:
        await msg.edit(f"❌ Failed:\n{e}")
