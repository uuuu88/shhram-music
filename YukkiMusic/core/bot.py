#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import sys

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"بدء البوت .")
        super().__init__(
            "YukkiMusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            workdir="datafiles",
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                text=f"<u><b>{self.mention}\n - تم بدء تشغيل البوت :</b><u>\n- ايدي البوت : <code>{self.id}</code>\n- الأسم : {self.name}\n- يوزر البوت : @{self.username}",
            )
        except:
            LOGGER(__name__).error(
                "- ارفع حساب المساعد مشرف وافتح اتصال ."
            )
            sys.exit()
        if config.SET_CMDS:
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("تشغيل", "تشغيل ملف في المجموعة"),
                        BotCommand("بنك", "عرض بنك البوت"),
                        BotCommand("سكب", "تخطي ملف صوتي"),
                        BotCommand("ايقاف", "ايقاف ملف صوتي"),
                        BotCommand("مؤقتا", "لايقاف التشغيل مؤقتا"),
                        BotCommand("استمرار", "استمرار تشغيل المتوقفة مؤقتا"),
                        BotCommand("انضم", "انضمام حساب المساعد الى المجموعة"),
                        BotCommand("غادر", "مغادرة حساب المساعد من المجموعة"),
                        BotCommand(
                            "مطور السورس",
                            "لعرض مطور سورس البوت .",
                        ),
                        BotCommand(
                            "الاوامر",
                            "لعرض اوامر البوت في المجموعة .",
                        ),
                    ]
                )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"تم تشغيل {self.name} بنجاح .")
