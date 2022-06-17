import datetime
import motor.motor_asyncio
from pyrogram.errors import *
import asyncio
import traceback
from config import *

class Database:
    def __init__(self, url, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(url)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, user_id):
        return dict(id=user_id)

    async def add_user(self, user_id):
        user = self.new_user(user_id)
        await self.col.insert_one(user)

    async def is_user_exist(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})
 
    async def remove_ban(self, id):
            ban_status = dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason="",
            )
            await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})
     
    async def ban_user(self, user_id, ban_duration, ban_reason):
            ban_status = dict(
                is_banned=True,
                ban_duration=ban_duration,
                banned_on=datetime.date.today().isoformat(),
                ban_reason=ban_reason,
            )
            await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})

    async def get_ban_status(self, id):
            default = dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason="",
            )
            user = await self.col.find_one({"id": int(id)})
            return user.get("ban_status", default)

    async def get_all_banned_users(self):
            banned_users = self.col.find({"ban_status.is_banned": True})
            return banned_users
    
    async def set_notif(self, id, notif):
        await self.col.update_one({"id": id}, {"$set": {"notif": notif}})

    async def get_notif(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("notif", False)

    async def get_all_notif_user(self):
        notif_users = self.col.find({"notif": True})
        return notif_users

    async def total_notif_users_count(self):
        count = await self.col.count_documents({"notif": True})
        return 

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        
DATABASE_URL=MONGO_URI
db = Database(DATABASE_URL, "LOGOMAKER")

#riRH120OmGNXw5cV
