
import os  
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
BOT_TOKEN = os.getenv("BOT_TOKEN")
START_STING = """
**🔮 Hello There, You Can Use Me To Create Awesome Logos...**
➤ Click /help Or The Button Below To Know How To Use Me
"""
S_STICKER = os.getenv("S_STICKER", "CAADBQADKgYAAqf_YFVnWOiahdbj0wI")

HELP = """
**🖼 How To Use Me ?**
**To Make Logo -** `/logo Your Name`
**To Make Square Logo - ** `/logosq Your Name`
**♻️ Example:** 
`/logo Pakeya`
"""
HELP_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖒𝖘𝖊", callback_data="cloce")
                 ]]
                 )
