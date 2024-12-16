from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database.memorydatabase import get_active_chats, get_active_video_chats
from config import SUPPORT_CHANNEL
from strings.filters import command

@app.on_message(command(["⦗ الاتصالات النشطة ⦘", "الاتصالات النشطة"]))
async def active_chats(_, message: Message):
    if message.from_user.id not in SUDOERS:
        return await message.reply_text(
            "عذرًا، هذا الأمر مخصص للمطور فقط -"
        )

    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("⦗ قناة التحديثات ⦘", url=SUPPORT_CHANNEL)],
        ]
    )

    # تعديل التنسيق ليكون على سطر واحد بالكامل بدون فواصل غير ضرورية
    await message.reply_text(
        f"-› عزيزي المطور هذه هي المجموعات الصوتية والفيديو التي يتم تشغيل المساعد فيها:\n\n-› الصوت: {ac_audio}\n-› الفيديو: {ac_video}",
        reply_markup=keyboard,
    )
