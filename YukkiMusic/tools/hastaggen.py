from MukeshAPI import api
from pyrogram import filters
from strings.filters import command
from YukkiMusic import app


@app.on_message(command("هاشتاكات"))
async def hastag(bot, message):

    try:
        text = message.text.split(" ", 1)[1]
        res = api.hashtag(text)
        results = " ".join(res)
        hashtags = results.replace(",", "").replace("[", "").replace("]", "")

    except IndexError:
        return await message.reply_text("- اكتب هاشتاكات واسم هاشتاك برمجي كمثال بايثون")

    await message.reply_text(
        f"- اليك الهاشتاكات :\n<pre>{hashtags}</pre>", quote=True
    )


help = """
Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʜᴀsʜᴛᴀɢ ɢᴇɴᴇʀᴀᴛᴏʀ ᴡʜɪᴄʜ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ᴛᴏᴘ 𝟹𝟶 ᴀɴᴅ ᴍᴏʀᴇ ʜᴀsʜᴛᴀɢs ʙᴀsᴇᴅ ᴏғғ ᴏғ ᴏɴᴇ ᴋᴇʏᴡᴏʀᴅ sᴇʟᴇᴄᴛɪᴏɴ.
° /hastag enter word to generate hastag.
°Exᴀᴍᴘʟᴇ:  /hastag python """
