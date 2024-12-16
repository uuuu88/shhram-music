import logging
import uuid

from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.raw import base
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.phone import (
    CreateGroupCall,
    DiscardGroupCall,
    ExportGroupCallInvite,
    GetGroupParticipants,
)
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired, BadRequest
import logging
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.utils.database import get_assistant


@app.on_message(command(["افتح اتصال","فتح تصال","تصال"]))
async def startvc(client, message: Message):

    call_name = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else " VC"
    hell = await message.reply_text("-› ابشر جاري فتح الأتصال .")
    userbot = await get_assistant(message.chat.id)

    try:
        await userbot.invoke(
            CreateGroupCall(
                peer=(await userbot.resolve_peer(message.chat.id)),
                random_id=int(str(uuid.uuid4().int)[:8]),
                title=call_name,
            )
        )

        await hell.edit_text("⦗ تم بدء إتصال ⦘ ")
    except ChatAdminRequired:
        await hell.edit_text(
            "-› ارفع حساب المساعد مشرف ."
        )
    except Exception as e:
        logging.exception(e)
        await hell.edit_text(str(e))


@app.on_message(command(["سد الاتصال","سد تصال","سد الأتصال"]))
async def endvc(client, message: Message):
    hell = await message.reply_text("-› ابشر جاري غلق الأتصال .")
    userbot = await get_assistant(message.chat.id)

    try:
        full_chat: base.messages.ChatFull = await userbot.invoke(
            GetFullChannel(channel=(await userbot.resolve_peer(message.chat.id)))
        )
        await userbot.invoke(DiscardGroupCall(call=full_chat.full_chat.call))
        await hell.edit_text("⦗ تم انهاء إتصال ⦘ .")
    except ChatAdminRequired:
        await hell.edit_text(
            "-› ارفع المساعد مشرف ."
        )
    except Exception as e:
        if "'NoneType' object has no attribute 'write'" in str(e):
            await hell.edit_text("-› الأتصال مسدود ترى .")
        elif "phone.DiscardGroupCall" in str(e):
            await hell.edit_text(
                "- ارفع المساعد مشرف ."
            )
        else:
            logging.exception(e)
            await hell.edit_text(e)


@app.on_message(command(["عدد الصاعدين","الصاعدين"]))
async def vcmembers(client, message: Message):
    userbot = await get_assistant(message.chat.id)
    hell = await message.reply_text("-› ابشر جاري عد الصاعدين .")

    try:
        full_chat: base.messages.ChatFull = await userbot.invoke(
            GetFullChannel(channel=(await userbot.resolve_peer(message.chat.id)))
        )
        participants: base.phone.GroupParticipants = await userbot.invoke(
            GetGroupParticipants(
                call=full_chat.full_chat.call,
                ids=[],
                sources=[],
                offset="",
                limit=1000,
            )
        )
        count = participants.count
        text = f"-› مجموع الصاعدين بالأتصال هم : {count}\n"
        users = []
        for participant in participants.participants:
            users.append(participant.peer.user_id)
        for i in users:
            b = await app.get_users(i)
            text += f"[{b.first_name + (' ' + b.last_name if b.last_name else '')}](tg://user?id={b.id})\n"

        await hell.edit_text(text)
    except ChatAdminRequired:
        await hell.edit_text(
            "- ارفع المساعد مشرف ."
        )
    except Exception as e:
        if "'NoneType' object has no attribute 'write'" in str(e):
            await hell.edit_text("-› الأتصال مسدود ترى .")
        else:
            logging.exception(e)
            await hell.edit_text(e)


__MODULE__ = "Vᴏɪᴄᴇᴄʜᴀᴛ"
__HELP__ = """
/startvc - sᴛᴀʀᴛ ᴛʜᴇ ᴠᴄ [ᴍᴀᴋᴇ sᴜʀᴇ Assɪsɪᴛᴀɴᴛ ɪs ᴀɴ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ]
/vcend - Eɴᴅ ᴛʜᴇ ᴠᴄ [ᴍᴀᴋᴇ sᴜʀᴇ Assɪsɪᴛᴀɴᴛ ɪs ᴀɴ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ]
/vclink - ɢᴇᴛ ᴠᴏɪᴄᴇᴄʜᴀᴛ ʟɪɴᴋ
/vcmembers - Gᴇᴛ ᴍᴇᴍᴇʙᴇʀ ʟɪsᴛ ᴛʜᴀᴛ ɪs ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ
"""
