from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant, ChatWriteForbidden, ChatAdminRequired
from YukkiMusic import app
from config import Muntazer
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
from strings.filters import command
from config import BANNED_USERS

success_message = "-› تم انهاء الصوت ."

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(_, msg):
    if not Muntazer:
        return
    try:
        if msg.from_user is None:
            return
        try:
            await app.get_chat_member(Muntazer, msg.from_user.id)
        except UserNotParticipant:
            if Muntazer.isalpha():
                link = "https://t.me/" + Muntazer
            else:
                chat_info = await app.get_chat(Muntazer)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    "• | عليك الاشتراك بالقناة حتى تستطيع إستخدام الأمر .",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("⦗ قناة الإشتراك ⦘", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"البوت ليس مشرفًا في قناة الإشتراك {Muntazer}!")

# كود إيقاف الموسيقى
@app.on_message(command(["ايقاف", "اوقف", "التالي", "انهاء"]))
async def stop_music(cli, message: Message):
    if not len(message.command) == 1:
        return
    # التحقق من الاشتراك في القناة
    await must_join_channel(cli, message)
    # إيقاف الموسيقى
    await Yukki.stop_stream(message.chat.id)
    await set_loop(message.chat.id, 0)
    # إرسال رسالة تأكيد الإيقاف
    try:
        await message.reply_text(success_message)
    except ChatWriteForbidden:
        pass
    except Exception as e:
        print(f"حدث خطأ أثناء محاولة إرسال رسالة التأكيد: {str(e)}")
