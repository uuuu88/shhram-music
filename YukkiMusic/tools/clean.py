import os
import shutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from config import SUPPORT_CHANNEL

@app.on_message(command(["تنظيف السجلات","⦗ تنظيف السجلات ⦘"]) & SUDOERS)
async def clean(_, message):
    A = await message.reply_text("- جاري التنظيف الأن .")
    dir = "downloads"
    dir1 = "cache"
    shutil.rmtree(dir)
    shutil.rmtree(dir1)
    os.mkdir(dir)
    os.mkdir(dir1)
    
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("⦗ قناة التحديثات ⦘", url=SUPPORT_CHANNEL)]]
    )
    
    await A.edit("- تم التنظيف بنجاح .", reply_markup=keyboard)
