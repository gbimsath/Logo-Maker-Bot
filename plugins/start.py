from config import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import User, Message
import os
import requests
import time
from database.db import Database

from io import BytesIO
from traceback import format_exc
import aiohttp

from pyrogram import Client, filters
from pyrogram.types import Message
from Python_ARQ import ARQ
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp
import yt_dlp
from urllib.parse import urlparse
from opencc import OpenCC
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
import database

db=database.db.db

@Client.on_message(filters.private & filters.command(["start"]))
async def help_me(bot, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await bot.send_message(
                LOG_CHANNEL,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n**ID:**{message.from_user.id}\n Started @{bot.username} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    file_id = S_STICKER
    await bot.send_sticker(message.chat.id, file_id)
    S_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('• 𝙊𝙪𝙩𝙧𝙪𝙞𝙓 • ™', url=f"https://t.me/TeamOutruix")
                 ],
                 [
                 InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{bot.username}?startgroup=true")
                 ]]
                  )
    await message.reply_text(
        text=START_STRING,
        reply_markup=S_BUTTON,
        disable_web_page_preview=True,
        quote=True
    )
@Client.on_message(filters.command("help"))
async def help(bot, message):
  await bot.send_sticker(message.chat.id, S_STICKER)
  await message.reply_text(text=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="start_menu")]]))

    
    
@Client.on_callback_query(filters.regex("start_menu"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(START_STRING,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", callback_data="help_menu"),InlineKeyboardButton(text="Repo", url="https://github.com/gbimsath/Logo-Maker-Bot")]]))

@Client.on_callback_query(filters.regex("help_menu"))
async def help_menu(_,query):
  await query.answer()
  await query.message.edit(HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="start_menu")]]))
