from pyrogram import Client ,idle
from config import *

plugins = dict(root="plugins")

bot=Client( 
    "Image upload bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins)

bot.start()
uname = (bot.get_me()).username
print(f"""
{uname} has been deployed!
""")
idle()
