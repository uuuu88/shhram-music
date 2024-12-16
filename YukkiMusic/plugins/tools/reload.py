
import asyncio
import logging

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message
from strings.filters import command
from config import BANNED_USERS, adminlist, lyrical
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.misc import db
from YukkiMusic.utils.database import get_authuser_names, get_cmode
from YukkiMusic.utils.decorators import ActualAdminCB, AdminActual, language
from YukkiMusic.utils.formatters import alpha_to_int


@app.on_message(command(["تحديث", "اوقف", "أدمن", "حدث"]) & ~BANNED_USERS)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = app.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        async for user in admins:
            if user.privileges.can_manage_video_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            " ~ لم يتم التحديث ."
        )


@app.on_message(command(["ريست", "⦗ ريست ⦘"]) & ~BANNED_USERS)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"~ جاري عمل ريست سريع البوت ..."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Yukki.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Yukki.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text("~ تم الريست، تستطيع إستخدام البوت الأن ...")


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except Exception as e:
        logging.exception(e)
        try:
            await app.delete_messages(
                chat_id=CallbackQuery.message.chat.id,
                message_ids=CallbackQuery.message.id,
            )
        except Exception as e:
            logging.exception(e)
            return


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("stop_downloading") & ~BANNED_USERS)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "• تم التنزيل ..", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "• بالفعل تم التنزيل .",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer("• تم إلغاء التنزيل .", show_alert=True)
            return await CallbackQuery.edit_message_text(
                f"• تم التنزيل بواسطة {CallbackQuery.from_user.mention}"
            )
        except:
            return await CallbackQuery.answer(
                "• فشلت إيقاف التنزيل .", show_alert=True
            )

    await CallbackQuery.answer("• فشل .", show_alert=True)
