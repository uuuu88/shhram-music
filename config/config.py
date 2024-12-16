
import sys
from os import getenv
import os
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
import re

API_ID = int(getenv("API_ID",16290917"))
API_HASH = getenv("API_HASH","abee7dcf07eeddb0ee0ef2ed2132ad43")
OWNER = int(os.getenv("OWNER", "7456826812"))
BOT_TOKEN = getenv("BOT_TOKEN","7767399482:AAGUcxDLh2-iKtBQfQ6uOy4w_G8SJCtI8Qg")
Muntazer = getenv("Muntazer","E_C_CC")
assistant = getenv("assistant","T7_29")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://omsnkok:muntazer@cluster0.ywxsjao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "50000"))  
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1002352201010"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "freedom")
PROTECT_CONTENT = getenv("PROTECT_CONTENT", "True")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7456826812").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/fps90/Hot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN","")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/E_C_CC")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/SOLO1_CR7") 
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "50000"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "3000"))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))
GITHUB_REPO = getenv("GITHUB_REPO","")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5")) 
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "2147483648")) 
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "2147483648")) 
SET_CMDS = getenv("SET_CMDS", "False")
STRING1 = getenv("STRING_SESSION", "BAD4lGUAfuDXgsg9suvrDyqUvP2wUncg_wZ3jkMbWbG_-ii-b7A3ajTzGrbGWis0fOONfpFgN8cGntKG7gkgkfSV4Pd-pgbUwdhWS0eqTgJ05h_lcTOpjJqjXqKOZQpTPdU-htG0cqmcHAR0QpbIOG7XbeAXbqesSGLfTHvqdUuOZeVy-WrVEO_8QioFXU3ybzAk88lvoHL08fMQ4ENihBgMq8LN6f21FgdAvgDKIJFYODQQdDoFEdlhr0E1fuVA6Bd0cgtZ_MtQoL_xYsskK_hht4rSfsbqQCHv7Pg6k2XfjMGGI6K6wyOYd4dZ6JelfXv2qzQgkYDWBZ79dlR39yNFnBiHqQAAAAHmrT55AA")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")
START_IMG_URL = getenv("START_IMG_URL","https://graph.org/file/3cf49673f408204004418.jpg",)
PING_IMG_URL = getenv("PING_IMG_URL","https://telegra.ph/file/91533956c91d0fd7c9f20.jpg",)
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL","https://telegra.ph/file/f4edfbd83ec3150284aae.jpg",)
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL","https://telegra.ph/file/de1db74efac1770b1e8e9.jpg",)
STATS_IMG_URL = getenv("STATS_IMG_URL","https://telegra.ph/file/4dd9e2c231eaf7c290404.jpg",)
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL","https://graph.org/file/086743f8c57d5134a008b.jpg",)
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL","https://graph.org/file/086743f8c57d5134a008b.jpg",)
STREAM_IMG_URL = getenv("STREAM_IMG_URL","https://telegra.ph/file/e24f4a5f695ec5576a8f3.jpg",)
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL","https://telegra.ph/file/7645d1e04021323c21db9.jpg",)
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL","https://graph.org/file/a0eaebe4d586f5c0b91d1.jpg",)
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL","https://telegra.ph/file/b7758d4e1bc32aa9fb6ec.jpg",)
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL","https://telegra.ph/file/60ed85638e00df10985db.jpg",)
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL","https://telegra.ph/file/f4edfbd83ec3150284aae.jpg",)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if MUSIC_BOT_NAME is None:
    MUSIC_BOT_NAME = "Music player"

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()



if STATS_IMG_URL:
    if STATS_IMG_URL != "https://telegra.ph/file/4dd9e2c231eaf7c290404.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://telegra.ph/file/8234d704952738ebcda7f.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://telegra.ph/file/e24f4a5f695ec5576a8f3.jpg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://telegra.ph/file/7645d1e04021323c21db9.jpg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://telegra.ph/file/76d29aa31c40a7f026d7e.jpg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://telegra.ph/file/8d02ff3bde400e465219a.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
PHOTO = list(
    filter(
        None,
        getenv("PHOTO_LINKS", "").split(),
    )
)
