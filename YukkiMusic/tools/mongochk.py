import re

from pymongo import MongoClient
from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from YukkiMusic import app

mongo_url_pattern = re.compile(r"mongodb(?:\+srv)?:\/\/[^\s]+")


@app.on_message(command("مونجو"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply(
            "- اكتب الأمر مونجو وضع رابط المونجو ."
        )
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("- تم إضافة المونجو الجديد بنجاح ✅")
        except Exception as e:
            await message.reply(f"حدث خطا : {e}")
    else:
        await message.reply("- حدث خطا .")
