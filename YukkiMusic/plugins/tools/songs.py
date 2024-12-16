import os
import glob
import random
import wget
import requests
import re
import yt_dlp
import logging
import asyncio
from pyrogram import Client, filters
from strings.filters import command
from youtube_search import YoutubeSearch
from YukkiMusic import app
import httpx
import time

def get_cookies_file():
    cookie_dir = "YukkiMusic/utils/cookies"
    cookies_files = [f for f in os.listdir(cookie_dir) if f.endswith(".txt")]

    cookie_file = os.path.join(cookie_dir, random.choice(cookies_files))
    return cookie_file

def sanitize_filename(title):
    return re.sub(r'[<>:"/\\|?*]', '', title).replace(' ', '_')

def download_audio_and_thumbnail(link, ydl_opts):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        audio_file = ydl.prepare_filename(info_dict)
        ydl.process_info(info_dict)
        
        # Get thumbnail URL
        thumbnail_url = info_dict.get("thumbnail")
        if thumbnail_url:
            thumb_file = wget.download(thumbnail_url)
        else:
            thumb_file = None

    return audio_file, thumb_file

@app.on_message(command(["song", "بحث", "تحميل", "تنزيل", "يوت", "yt"]) & (filters.private | filters.group | filters.channel))
async def song(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = message.from_user.mention

    query = " ".join(message.command[1:])
    
    m = await message.reply("⦗ جارٍ البحث ... ⦘")
    
    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "cookiefile": get_cookies_file()
    }

    if "youtube.com" in query or "youtu.be" in query:
        link = query
    else:
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            link = f"https://youtube.com{results[0]['url_suffix']}"
        except Exception as e:
            await m.edit("⦗ لم يتم العثور على الصوت ⦘")
            logging.error(f"Failed to fetch YouTube video: {str(e)}")
            return

    await m.edit("⦗ جارٍ التحميل ... ⦘")

    try:
        loop = asyncio.get_event_loop()
        audio_file, thumb_file = await loop.run_in_executor(None, download_audio_and_thumbnail, link, ydl_opts)
        
        rep = f"- بواسطة : {chutiya}" if chutiya else "voice"
        
        await message.reply_audio(
            audio_file,
            caption=rep,
            performer=" voice .",
            thumb=thumb_file,  # Use the fetched thumbnail
            title=None,
        )
        await m.delete()
    
    except Exception as e:
        await m.edit(f"[Victorious] **\n\\خطأ :** {e}")
        logging.error(f"Error while downloading audio: {str(e)}")

    finally:
        try:
            os.remove(audio_file)
            if thumb_file:
                os.remove(thumb_file)  # Delete the thumbnail file
        except Exception as e:
            logging.error(f"Failed to delete temporary files: {str(e)}")

@app.on_message(command(["نزلي فيديو","نزلي الفيديو"]) & (filters.private | filters.group | filters.channel))
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "cookiefile": get_cookies_file(),
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,
    }

    query = " ".join(message.command[1:])

    m = await message.reply("⦗ جارٍ البحث ... ⦘")

    if "youtube.com" in query or "youtu.be" in query:
        link = query
    else:
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            link = f"https://youtube.com{results[0]['url_suffix']}"
        except Exception as e:
            await m.edit("🚫 **خطأ:** لم يتم العثور على الفيديو")
            return

    await m.edit("⦗ جارٍ التحميل ... ⦘")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
        
        await message.reply_video(
            file_name,
            duration=int(ytdl_data["duration"]),
            thumb=None,
            caption=ytdl_data["title"],
        )

        await m.delete()  

    except Exception as e:
        await m.edit(f"🚫 **خطأ:** {e}")

    finally:
        try:
            os.remove(file_name)
        except Exception as e:
            logging.error(f"Failed to delete temporary files: {str(e)}")
