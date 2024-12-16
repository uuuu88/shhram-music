from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from config import BANNED_USERS
from YukkiMusic import app
from YukkiMusic.utils.decorators.play import PlayWrapper
from YukkiMusic.utils.logger import play_logs
from YukkiMusic.utils.stream.stream import stream

# Command
@app.on_message(command(["بث","مباشر","رابط"]) & ~BANNED_USERS)
@PlayWrapper
async def stream_command(
    client,
    message: Message,
    _,
    chat_id,
    video,
    channel,
    playmode,
    url,
    fplay,
):
    if url:
        mystic = await message.reply_text(
            _["play_2"].format(channel) if channel else _["play_1"]
        )
        try:
            await stream(
                _,
                mystic,
                message.from_user.id,
                url,
                chat_id,
                message.from_user.first_name,
                message.chat.id,
                video=True,
                streamtype="index",
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
            return await mystic.edit_text(err)
        return await play_logs(message, streamtype="• ارسل الرابط صحيح .")
    else:
        await message.reply_text(_["str_1"])
