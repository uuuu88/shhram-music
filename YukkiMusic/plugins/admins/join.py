from pyrogram import filters
from pyrogram.errors import ChatAdminRequired, InviteRequestSent, UserAlreadyParticipant
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import get_assistant
from pyrogram.types import Message 

@app.on_message(
    command(["انضم","ادخل","طب"]))
async def invite_assistant(client, message):
    try:
        # Get the music bot assistant
        userbot = await get_assistant(message.chat.id)

        # Check if the bot has admin rights in the group
        try:
            await client.get_chat_member(message.chat.id, "me")
        except ChatAdminRequired:
            return await message.reply_text(
                "• انطيني صلاحية اضافة مستخدمين ."
            )

        # Unban the assistant if it's banned in the group
        try:
            await client.unban_chat_member(message.chat.id, userbot.id)
        except:
            pass

        # Get the invite link for the group
        invitelink = await client.export_chat_invite_link(message.chat.id)

        # Invite the assistant to the group
        await userbot.join_chat(invitelink)

        await message.reply_text("-› تمت اضافة المساعد بنجاح .")

    except InviteRequestSent:
        await message.reply_text("-› بالفعل تم دعوة المساعد .")

    except UserAlreadyParticipant:
        await message.reply_text("-› ترى المساعد موجود .")

    except Exception as e:
        await message.reply_text(f"-› حدث خطأ .: {e}")
        

@app.on_message(command(["برا","اطلع","غادر"]) & SUDOERS)
async def leave_group(client, message):
    try:
        # Get the music bot assistant
        userbot = await get_assistant(message.chat.id)

        # Prepare a message to send before leaving the group
        leave_message = "شكرًا لكم جميعًا، وداعاً!"

        # Leave the group
        await app.send_message(message.chat.id, leave_message)
        await userbot.leave_chat(message.chat.id)
        await app.leave_chat(message.chat.id)

        await message.reply_text("-› غادرت المجموعة كما طلبت.")

    except Exception as e:
        await message.reply_text(f"-› حدث خطأ أثناء مغادرة المجموعة: {e}")
