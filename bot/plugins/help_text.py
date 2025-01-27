#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

from pyrogram import filters
from pyrogram.types import Message
from bot import (
    START_COMMAND,
    START_MESSAGE
)
from bot.bot import Bot


@Bot.on_message(
    filters.command(START_COMMAND) &
    filters.private
)
async def start_command_fn(_, message: Message):
    await message.reply_text(
        text=START_MESSAGE,
        quote=True,
        disable_web_page_preview=True,
        disable_notification=True
    )
