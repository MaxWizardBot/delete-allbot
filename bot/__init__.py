#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from bot.get_config import get_config


# apparently, no error appears even if the path does not exists
load_dotenv("config.env")


# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = int(get_config("APP_ID", should_prompt=True))
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
# string session for running as user
TG_USER_SESSION = get_config("TG_USER_SESSION", should_prompt=True)
TG_BOT_SESSION = get_config("TG_BOT_SESSION", "bot")
# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "MessageDeletErBot.log")
# number of messages that can be deleted in One Request, in Telegram
TG_MAX_SEL_MESG = int(get_config("TG_MAX_SEL_MESG", 99))
TG_MIN_SEL_MESG = int(get_config("TG_MIN_SEL_MESG", 0))
# a dictionary to store the currently running processes
AKTIFPERINTAH = {}


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)


REQD_PERMISSIONS = "https://t.me/@MaxxBotChat"
GIT_REPO_LINK = "@MaxxBots"
""" strings to be used in the bot """
START_MESSAGE = get_config("START_MESSAGE", (
    "𝗛𝗲𝘆 𝗗𝗲𝗮𝗿!🙋.\n\n🔖<code> I am Telegram All Message Deleter Bot😊!</code>\n<code>I can Delete Your Channel, group, supergroup all Messages in few Seconds 🤩</code>.\n\n⭕𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲?? follow These Steps 👇\n➪ <b>Add me to the channel/supergroup as admin (with at least delete messages, invite users and add admins permissions)</b>\n➪ </b>Send /delall if you want all the messages to be deleted</b>\n➪ <b>Send /delfrom & /delto before using /delsel in reply to a message if you want to delete that and all subsequent messages.</b> "
    "\n\n"
    f"<b>JOIN SUPPORT CHAT</b>" 👉 {REQD_PERMISSIONS} 👈"
    "\n\n"
    f"<b>📮BOT CHANNEL 📮</b> {GIT_REPO_LINK}"
))
START_COMMAND = get_config("START_COMMAND", "start")
DEL_ALL_COMMAND = get_config("DEL_ALL_COMMAND", "delall")
BEGINNING_DEL_ALL_MESSAGE = get_config("BEGINNING_DEL_ALL_MESSAGE", (
    "trying to delete all messages"
))
IN_CORRECT_PERMISSIONS_MESSAGE = get_config("IN_CORRECT_PERMISSIONS_MESSAGE", (
    "something went wrong. \n\n"
    "<code>{}</code>"
    "\n\n"
    f"please verify <a href='{REQD_PERMISSIONS}'>all permissions</a>, "
    "and try again after sometime."
))
SEL_DEL_COMMAND = get_config("SEL_DEL_COMMAND", "delsel")
BEGINNING_SEL_DEL_MESSAGE = get_config("BEGINNING_SEL_DEL_MESSAGE", (
    "trying to delete your selected messages"
))
DEL_FROM_COMMAND = get_config("DEL_FROM_COMMAND", "delfrom")
DEL_TO_COMMAND = get_config("DEL_TO_COMMAND", "delto")
NOT_USED_DEL_FROM_DEL_TO_MESSAGE = get_config(
    "NOT_USED_DEL_FROM_DEL_TO_MESSAGE", (
        f"please use /{DEL_FROM_COMMAND} or /{DEL_TO_COMMAND} "
        f"before using /{SEL_DEL_COMMAND}"
    )
)
TL_FILE_TYPES = (
    "photo",
    "animation",
    "audio",
    "document",
    "video",
    "video_note",
    "voice",
    # "contact",
    # "dice",
    # "poll",
    # "location",
    # "venue",
    "sticker",
    "text"
)
