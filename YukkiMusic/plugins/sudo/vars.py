#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
import asyncio

from pyrogram import filters

import config
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database.memorydatabase import get_video_limit
from YukkiMusic.utils.formatters import convert_bytes

@app.on_message(command(["⦗ فاراتي ⦘", "فاراتي"]) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text("⦗ سيتم جلب الفارات الأن ⦘")
    v_limit = await get_video_limit()
    bot_name = app.mention
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    play_duration = config.DURATION_LIMIT_MIN
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "Yes"
    else:
        pvt = "No"
    if not config.GITHUB_REPO:
        git = "No"
    else:
        git = f"[السورس]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "No"
    else:
        start = f"[صورة]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "No"
    else:
        s_c = f"[القناة]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "No"
    else:
        s_g = f"[التحديثات]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "No"
    else:
        token = "Yes"
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        sotify = "No"
    else:
        sotify = "Yes"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    
    telegram_audio_url = config.TELEGRAM_AUDIO_URL
    telegram_video_url = config.TELEGRAM_VIDEO_URL
    muntazer = config.Muntazer
    assistant = config.assistant

    text = f"""**⦗ عزيزي المطور هذا هي فارات تنصيبك ⦘**\n⎯ ⎯ ⎯ ⎯
-› اسم بوتك : **{bot_name}**
-› الحد الأدنى للتشغيل : **{play_duration} دقيقة**
-› ايدي المالك : **{owner_id}**    
⎯ ⎯ ⎯ ⎯
-› رابط السورس : **{up_r}**
-› اسم الفرع : **{up_b}**
-› توكن السورس :** {token}**
⎯ ⎯ ⎯ ⎯
-› مغادرة المساعد : **{ass}**
-› وقت كل مغادرة : **{auto_leave} ثانية**
-› نوع البوت : **{pvt}**
⎯ ⎯ ⎯ ⎯
-› تحميل الأدنى للصوت :** {tg_aud}**
-› تحميل الأدنى للفيديوهات :** {tg_vid}**
-› قناة السورس : **{s_c}**
⎯ ⎯ ⎯ ⎯
-› قناة التحديثات : ** {s_g}**
-› صورة كليشة ستارت : ** {start}**
-› رابط صورة تشغيل الصوت : **[صورة]({telegram_audio_url})**
⎯ ⎯ ⎯ ⎯
-› رابط صورة تشغيل الفيديو : **[صورة]({telegram_video_url})**
-› قناة الأشتراك الاجباري : **@{muntazer}**
-› حساب المساعد : **@{assistant}**
    """
    await asyncio.sleep(1)

    await mystic.edit_text(text)
