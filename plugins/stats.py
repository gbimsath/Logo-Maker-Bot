from pyrogram import Client, filters
import config
import database.db
import random

db=database.db.db


@Client.on_message(filters.command("status"), group=5)
async def status(bot, update):
    if upsdate.from_user.id not in AUTH_USERS:
        await update.delete()
        return 
    if not await db.is_user_exist(update.from_user.id):
         await db.add_user(update.from_user.id)
         
    
    total_users = await db.total_users_count()
    text = "**Bot Advanced Statistics 📊**\n"
    text += f"\n**Total Users:** `{total_users}`"

    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )
