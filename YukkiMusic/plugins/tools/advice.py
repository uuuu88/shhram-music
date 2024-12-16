from pyrogram import filters
from strings.filters import command
from config import LOG_GROUP_ID
from YukkiMusic import api, app


@app.on_message(command("advice"))
async def advice(_, message):
    A = await message.reply_text("...")
    res = await api.advice()
    await A.edit(b["advice"])


@app.on_message(command("احداث فلكية"))
async def advice(_, message):
    a = await api.astronomy()
    if a["success"]:
        c = a["date"]
        url = a["imageUrl"]
        b = a["explanation"]
        caption = f"-› بتاريخ [{c}] مثل هذا اليوم حدث هذا :\n\n{b}"
        await message.reply_photo(url, caption=caption)
    else:
        await message.reply_photo("ᴛʀʏ ᴀғᴛᴇʀ sᴏᴍᴇ ᴛɪᴍᴇ")
        await app.send_message(LOG_GROUP_ID, "الامر لايعمل")

