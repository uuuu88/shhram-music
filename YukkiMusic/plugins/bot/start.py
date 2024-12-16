from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import SUPPORT_GROUP, SUPPORT_CHANNEL, OWNER, START_IMG_URL, assistant, Muntazer

# المتغيرات
served_users = set()
served_chats = set()
blacklisted_chats_list = set()

async def add_served_user(user_id: int):
    served_users.add(user_id)

async def is_served_chat(chat_id):
    return chat_id in served_chats

async def add_served_chat(chat_id):
    served_chats.add(chat_id)

async def blacklisted_chats():
    return blacklisted_chats_list

@app.on_message(filters.command(["start", "help"]) & filters.private)
async def start_(client: Client, message: Message):
    user_id = message.from_user.id
    await add_served_user(user_id)
    await message.reply_photo(
        photo=START_IMG_URL,
        caption=f"""أَهلًا بك عزيزي في بوت تشغيل الميديا الصوتية في المجموعات والقنوات مع دعم مُميزات كثيرة يُمكنُك التحقُق منها عن طريق إِستخدام الازرار أدناه . \n⎯ ⎯ ⎯ ⎯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⦗ اوامر البوت ⦘", callback_data="command_list")
                ],
                [
                    InlineKeyboardButton(text="⦗ قناة السورس ⦘", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton(text="⦗ قناة التحديثات ⦘", url=SUPPORT_GROUP),
                ],
                [
                    InlineKeyboardButton(text="⦗ مطور البوت ⦘", user_id=int(OWNER)),
                ],
            ]
        )
    )

@app.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
    await query.answer("قائمة التحكم")
    await query.edit_message_text(
        f"""أَهلًا بك عزيزي في بوت تشغيل الميديا الصوتية في المجموعات والقنوات مع دعم مُميزات كثيرة يُمكنُك التحقُق منها عن طريق إِستخدام الازرار أدناه . \n⎯ ⎯ ⎯ ⎯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⦗ اوامر البوت ⦘", callback_data="command_list")
                ],
                [
                    InlineKeyboardButton(text="⦗ قناة السورس ⦘", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton(text="⦗ قناة التحديثات ⦘", url=SUPPORT_GROUP),
                ],
                [
                    InlineKeyboardButton(text="⦗ مطور البوت ⦘", user_id=int(OWNER)),
                ],
            ]
        )
    )

# المزيد من الدوال والتصريحات الأخرى للأحداث والاستجابات

@app.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
    await query.answer("قائمة التحكم")
    await query.edit_message_text(
        f"""أَهلًا بك عزيزي في بوت تشغيل الميديا الصوتية في المجموعات والقنوات مع دعم مُميزات كثيرة يُمكنُك التحقُق منها عن طريق إِستخدام الازرار أدناه . \n⎯ ⎯ ⎯ ⎯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⦗ اوامر البوت ⦘", callback_data="command_list")
                ],
                [
                    InlineKeyboardButton(text="⦗ قناة السورس ⦘", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton(text="⦗ قناة التحديثات ⦘", url=SUPPORT_GROUP),
                ],
                [
                    InlineKeyboardButton(text="⦗ مطور البوت ⦘", user_id=int(OWNER)),
                ],
            ]
        )
    )

@app.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery):
    await query.answer("تم فتح لوحة التشغيل")
    await query.edit_message_text(
        f"""- تم فتح لوحة التحكم ↓
 – – – – – – 
⦗ تستطيع التحكم عن طريق الأزرار أدناه ⦘""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ أوامر التشغيل ⦘", callback_data="user_command"),
                ],
                [
                    InlineKeyboardButton("⦗ الرجوع ⦘", callback_data="home_start"),
                    InlineKeyboardButton("⦗ التالي ⦘", callback_data="next"),
                ],
            ]
        )
    )

@app.on_callback_query(filters.regex("next"))
async def commands_set(_, query: CallbackQuery):
    await query.answer("تم فتح لوحة الأدمن")
    await query.edit_message_text(
        f"""- تم فتح لوحة التحكم ↓
 – – – – – – 
⦗ تستطيع التحكم عن طريق الأزرار أدناه ⦘""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ أوامر المشرفين ⦘", callback_data="developer_commands"),
                ],
                [
                    InlineKeyboardButton("⦗ الرجوع ⦘", callback_data="command_list"),
                    InlineKeyboardButton("⦗ التالي ⦘", callback_data="ghaith"),
                ],
            ]
        )
    )

@app.on_callback_query(filters.regex("ghaith"))
async def commands_set(_, query: CallbackQuery):
    await query.answer("تم فتح لوحة المطور")
    await query.edit_message_text(
        f"""- تم فتح لوحة التحكم ↓
 – – – – – – 
⦗ تستطيع التحكم عن طريق الأزرار أدناه ⦘""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ اوامر المطور ⦘", callback_data="owner_commands"),
                ],
                [
                    InlineKeyboardButton("⦗ الرجوع ⦘", callback_data="home_start"),
                    InlineKeyboardButton("⦗ التالي ⦘", callback_data="command_list"),
                ],
            ]
        )
    )

@app.on_callback_query(filters.regex("user_command"))
async def user_commands_set(_, query: CallbackQuery):
    await query.answer("- تم فتح اوامر التشغيل .")
    await query.edit_message_text(
        f"""-› تم فتح اوامر التشغيل ♡゙  .
– – – – – –

-› شغل - لتشغيل ملفات صوتية في القناة 
-› مباشر - لتشغيل رابط بث مبارة مباشر .
-› يوت -  تحميل ملف صوت من اليوتيوب 
-› تحميل - يمكنك تحميل فيديو من اليوتيوب
-› ايقاف - إيقاف تشغيل الملف الصوتي نهائيا
-› تخطي - تخطي اغنية من قوائم التشغيل 
-› كتم الصوت - كتم صوت حساب المساعد 
-› الغاء الكتم - رفع كتم صوت حساب المساعد
-› مؤقتا -  ايقاف الملف الصوتي المشغل مؤقتا 
-› استمرار - استمرار تشغيل الملف الصوتي 
-› تكرار - وعدد الرقم حتى يتم تكرارة
-› تقديم - وعدد الثواني لتقديم الصوت المشغل""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ التالي ⦘", callback_data="next")
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("developer_commands"))
async def developer_commands_set(_, query: CallbackQuery):
    await query.answer("- تم فتح اوامر المشرفين .")
    await query.edit_message_text(
        f"""-› تم فتح اوامر المشرفين ♡゙  .

– – – – – –
-› احفظ - واسم الاغنية حتى يتم حفظها
-› المحفوظات - رؤية عدد الأغاني المحفوظة
-› حذف الأغاني - مسح الأغاني المحفوظة
-› فتح اتصال - فتح اتصال في المجموعة
-› سد اتصال - إغلاق اتصال المجموعة نهائي
-› الصاعدين - ينطيك عدد الصاعدين بالأتصال
-› تحديث - تحديث قائمة مشرفين المجموعة 
-› فريدوم - اسألة اي شي وراح يجاوبك علية 
-› احذف منا - برد الرسالة ليتم بدء حذف رسائل
-› انضم - دعوة المساعد الى مجموعة التشغيل
-› غادر - لمغادرة المساعد من مجموعة التشغيل""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ التالي ⦘", callback_data="ghaith")
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("owner_commands"))
async def owner_commands_set(_, query: CallbackQuery):
    await query.answer("- تم فتح اوامر المطور الأساسي .")
    await query.edit_message_text(
        f"""-› تم فتح اوامر المطور الأساسي ♡゙  .

– – – – – –
-› اسم - واكتب اسم حساب المساعد الجديد
-› بنك - عرض بنك البوت الحقيقي بالثانية
-› اضف - بالأيدي او بالرد لرفع مطور بالبوت
-› ازالة - بالأيدي او بالرد لأزالة مطور بالبوت
-› ساعات التشغيل - عرض ساعات تشغيل البوت
-› المطورين - عرض مطورين البوت بقائمة
-› حذف فار - واسم الفار حتى يتم حذفة 
-› اضف فار - واسم الفار والقيمة لأضافة فار
-› ضع - ضع حساب مساعد آخر يعمل بديلاً
-› اذاعة - بالرد ليتم اذاعتها في المجموعات
-› مونجو - لتغيير المونجو وتخفيف الضغط
-› ريست - عمل ريست سريع في المجموعات
-› ادمن - لتحديث قائمة ادمنية المجموعات""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ التالي ⦘", callback_data="home_start")
                ],
            ]
        ),
    )

@app.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if not await is_served_chat(chat_id):
        await add_served_chat(chat_id)
    
    for member in m.new_chat_members:
        try:
            # فحص إذا كان العضو الجديد هو البوت نفسه
            if member.id == c.me.id:
                # التحقق إذا كانت المجموعة محظورة
                if chat_id in await blacklisted_chats():
                    await m.reply_text(
                        "❗️ This chat has been blacklisted by a sudo user and you're not allowed to use me in this chat."
                    )
                    return await c.leave_chat(chat_id)
                
                # إرسال رسالة ترحيب عند إضافة البوت
                await m.reply(
                    "🎗️ وأخيرا ضفتوني ، طبعاً شكراً للي ضافني !\n\n"
                    "👍🏻 اضغط على زر الاوامر حتى تشوف شلون تشغلني ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("-› قناة السورس", url=f"{SUPPORT_CHANNEL}"),
                                InlineKeyboardButton("-› الاوامر", callback_data="command_list")
                            ],
                            [
                                InlineKeyboardButton("-› حساب المساعد", url=f"https://t.me/{assistant}") if assistant else None
                            ]
                        ]
                    )
                )
        except Exception as e:
            print(f"Error: {e}")

@app.on_message(filters.regex("^الاوامر$"))
async def mmmezat(client, message):
    await message.reply_text(
        f"-› إليك عزيزنا {message.from_user.mention}\nقائمة أوامر البوت لكي تتعرف على المميزات وطريقة التشغيل الجديدة .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⦗ قائمة الأوامر ⦘", callback_data="command_list"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⦗ مسح الزر ⦘", callback_data="close"
                    ),
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("close"))
async def close_button(client: Client, callback_query: CallbackQuery):
    await callback_query.message.delete()
