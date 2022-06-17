
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('• 𝙊𝙪𝙩𝙧𝙪𝙞𝙓 • ™', url=f"https://t.me/TeamOutruix")
                 ],
                 [
                 InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{}t?startgroup=true")
                 ]]
                  )

START_STING = """
**🔮 Hello There, You Can Use Me To Create Awesome Logos...**
➤ Click /help Or The Button Below To Know How To Use Me
"""
S_STICKER = os.getenv("S_STICKER")
