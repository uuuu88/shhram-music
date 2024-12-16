from YukkiMusic import app
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message
from config import OWNER

# تحديد لوحة المفاتيح
keyboard_main = ReplyKeyboardMarkup(
    [
        [('⦗ حذف كافة صور المساعد ⦘'), ('⦗ حذف صورة المساعد ⦘')],
        [('⦗ تعيين صورة المساعد ⦘'), ('⦗ فاراتي ⦘')],
        [('⦗ مطورين البوت ⦘'), ('⦗ احصائيات البوت ⦘')],
        [('⦗ الداينو ⦘'), ('⦗ تحديث السورس ⦘')],
        [('⦗ سجلات التشغيل ⦘'), ('⦗ اعادة تشغيل ⦘')],
        [('⦗ الاتصالات النشطة ⦘'), ('⦗ معلومات النظام ⦘')],
        [('⦗ تنظيف السجلات ⦘')],
        [('⦗ حذف الكيبورد ⦘')]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

keyboard_remove = ReplyKeyboardMarkup(
    [
        [('⦗ فتح الكيبورد ⦘')],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

@app.on_message(command(["⦗ فتح الكيبورد ⦘", "تنصيب الكيبورد"]) & filters.private & filters.user(OWNER))
async def start_or_help_command(client, message: Message):
    await message.reply_text('اهلأ بك عزيزي ⦗ المطور الاساسي ⦘ \n – – – – – – \n⦗ يمكنك التحكم عن طريق الأزرار أدناه ⦘', reply_markup=keyboard_main)

@app.on_message(command(["⦗ حذف الكيبورد ⦘"]) & filters.private & filters.user(OWNER))
async def remove_keyboard(client, message: Message):
    await message.reply_text('اهلأ بك عزيزي ⦗ المطور الاساسي ⦘ \n– – – – – – \n⦗ تم تنفيذ أمر لوحة التحكم ⦘', reply_markup=keyboard_remove)
