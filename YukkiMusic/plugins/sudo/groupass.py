from pyrogram import filters
from pyrogram.types import Message
from YukkiMusic import app
from strings.filters import command
from YukkiMusic.core.userbot import assistants
from YukkiMusic.utils.assistant import assistant, get_assistant_details
from YukkiMusic.utils.database import get_assistant, save_assistant, set_assistant
from YukkiMusic.utils.filter import admin_filter


@app.on_message(command("مساعد عشوائي") & admin_filter)
async def assis_change(_, message: Message):
    avt = await assistant()
    if avt == True:
        return await message.reply_text(
            "⦗ لايمكنك تغيير حساب المساعد بسبب لم يتم إضافة اكثر من حساب ⦘"
        )
    usage = f"- إستخدامك للأمر خطا ."
    if len(message.command) > 2:
        return await message.reply_text(usage)
    a = await get_assistant(message.chat.id)
    DETAILS = f"-› تم تغيير المساعد من [{a.name}](https://t.me/{a.username}) "
    try:
        await a.leave_chat(message.chat.id)
    except:
        pass
    b = await set_assistant(message.chat.id)
    DETAILS += f"-› الى [{b.name}](https://t.me/{b.username})"
    try:
        await b.join_chat(message.chat.id)
    except:
        pass
    await message.reply_text(DETAILS, disable_web_page_preview=True, protect_content=PK)


@app.on_message(command("ضع") & admin_filter)
async def assis_set(_, message: Message):
    avt = await assistant()
    if avt == True:
        return await message.reply_text(
            "⦗ لايمكنك تغيير حساب المساعد بسبب لم يتم إضافة اكثر من حساب ⦘"
        )
    usage = await get_assistant_details()
    if len(message.command) != 2:
        return await message.reply_text(
            usage, disable_web_page_preview=True, protect_content=PK
        )
    query = message.text.split(None, 1)[1].strip()
    if query not in assistants:
        return await message.reply_text(
            usage, disable_web_page_preview=True, protect_content=PK
        )
    a = await get_assistant(message.chat.id)
    try:
        await a.leave_chat(message.chat.id)
    except:
        pass
    await save_assistant(message.chat.id, query)
    b = await get_assistant(message.chat.id)
    try:
        await b.join_chat(message.chat.id)
    except:
        pass
    DETAILS = f"""  -›  تفاصيل المساعد الجديد :
                    -› اسم المساعد :- {a.name}
                    -› يوزر المساعد  :- {a.username}
                    -› ايدي المساعد :- @{a.id}"""
    await message.reply_text(DETAILS, disable_web_page_preview=True, protect_content=PK)


@app.on_message(command("الحالي") & admin_filter)
async def check_ass(_, message: Message):
    assistant = await get_assistant(message.chat.id)
    DETAILS = f"""-› المساعد الحالي :
-› اسم المساعد :- {assistant.name}
-› يوزر المساعد :- {assistant.username}
-› ايدي المساعد:- @{assistant.id}"""
    await message.reply_text(DETAILS, disable_web_page_preview=True, protect_content=PK)
