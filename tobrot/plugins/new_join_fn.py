#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
 
# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
 
import pyrogram
 
 
from tobrot import (
    AUTH_CHANNEL
)
 
 
async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    await message.delete(revoke=True)
 
 
async def help_message_f(client, message):
    
    await message.reply_text("""Hi Bro""")
 
