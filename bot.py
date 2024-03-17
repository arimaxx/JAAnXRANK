import os
import asyncio
from pyrogram import Client, filters
from pymongo import MongoClient
import random 
from datetime import datetime, timedelta
from pyrogram.errors import UserNotParticipant, PeerIdInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

API_ID = "21971830"
API_HASH = "46389a1d51d331e5d30d4d6b8a101f3d"
BOT_TOKEN = "6904714157:AAG3A1V3A72Gf4j2-5AXudy1EFDsu1wORjU"
MONGO_URL = "mongodb+srv://seleno:seleno@cluster0.a4gsvlg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
BOT_USERNAME = "chat_rankbot"
SUPPORT_GROUP_USERNAME = "three_stars_ki_duniya"
SOURCE_CODE_CHANNEL_USERNAME = "ll_about_ari_ll"

app = Client(
    "Level" ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

IMAGE_URLS = [
    "https://telegra.ph/file/56f46a11100eb698563f1.jpg",
    "https://telegra.ph/file/66552cbeb49088f98f752.jpg",
    "https://telegra.ph/file/a9ada352fd34ec8a01013.jpg",
    "https://telegra.ph/file/47a852d5b1c4c11a497c2.jpg",
    "https://telegra.ph/file/f002db994f436aaee892c.jpg",
    "https://telegra.ph/file/35621d8878aefb0dcd899.jpg"
]

mongo_client = MongoClient(MONGO_URL)
db = mongo_client["your_database_name"]
top_members_collection = db["top_members"]

user_data = {}

async def top_members_with_image(message, text, photo_url):
    await message.reply_photo(
        photo= "https://telegra.ph/file/00c74d7d761fdb7ba201a.jpg",
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍃ᴛᴏᴅᴀʏ🍃", callback_data="today"),
                    InlineKeyboardButton("🍃ᴛᴏᴛᴀʟ🍃", callback_data="total")
                ],
                [
                    InlineKeyboardButton("🍃ᴄʜᴀɴɴᴇʟ🍃", callback_data="channel"),
                    InlineKeyboardButton("🍃ɢʀᴏᴜᴘ🍃", callback_data="group")
                ]
            ]
        )
    )

@app.on_message(filters.command("ranking"))
async def send_rankings_with_image(_, message):
    image_url = random.choice(IMAGE_URLS)
    text = "𝗧𝗵𝗶𝘀 𝗶𝘀 𝗧𝗦 𝗥𝗮𝗻𝗸𝗶𝗻𝗴 𝗕𝗼𝘁 \n 𝗰𝗼𝘂𝗻𝘁 𝘁𝗵𝗲 𝗰𝗵𝗮𝘁 𝗮𝗰𝘁𝗶𝘃𝗶𝘁𝘆 𝗼𝗳 𝘂𝘀𝗲𝗿𝘀 𝗶𝗻 𝘁𝗵𝗶𝘀 𝗴𝗿𝗼𝘂𝗽 \n 𝗬𝗼𝘂𝗿 𝗿𝗮𝗻𝗸𝗶𝗻𝗴 𝘁𝗲𝘅𝘁 𝗴𝗼𝗲𝘀 𝗵𝗲𝗿𝗲..."
    await top_members_with_image(message, text, image_url)

@app.on_message(filters.private & filters.command("start"))
async def start_private_chat(client, message):
    # Choose a random image URL
    image_url = random.choice(IMAGE_URLS)

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️‍🔥ᴀᴅᴅ ᴍᴇ❤️‍🔥", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
                InlineKeyboardButton("💫ꜱᴜᴘᴘᴏʀᴛ💫", url=f"t.me/{SUPPORT_GROUP_USERNAME}"),
            ],
            [
                InlineKeyboardButton("💖ꜱᴏᴜʀᴄᴇ💖", url=f"t.me/{SOURCE_CODE_CHANNEL_USERNAME}"),
            ]
        ])

    await client.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption="<b>нυι</b> тнιѕ ιѕ 「🛡ᴛꜱ ʀᴀɴᴋɪɴɢ ʙᴏᴛ🛡」❖ 💖\n"
                "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n"
                "💫 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛꜱ ʀᴀɴᴋɪɴɢ ʙᴏᴛ!.\n "
                "🌟 ᴅɪꜱᴄᴏᴠᴇʀ ᴡʜᴏ ꜱʜɪɴᴇꜱ ᴛʜᴇ ʙʀɪɢʜᴛᴇꜱᴛ ɪɴ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ! ꜰʀᴏᴍ ᴀᴄᴛɪᴠᴇ ᴍᴇᴍʙᴇʀꜱ ᴛᴏ ᴛᴏᴘ ᴄᴏɴᴛʀɪʙᴜᴛᴏʀꜱ, ᴡᴇ'ʀᴇ ʜᴇʀᴇ ᴛᴏ ʀᴇᴄᴏɢɴɪᴢᴇ ᴇxᴄᴇʟʟᴇɴᴄᴇ.\n"
                "📊 Stay updated with real-time rankings, track your progress, and compete with friends to climb the leaderboard!\n"
                "❖Join us in celebrating achievements and fostering a vibrant community together!❖\n"
                "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n\n"
                "ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ <a href=\"https://t.me/lll_notookk_lll\">||ᴀʀɪ||❣️</a>",
        reply_markup=keyboard
      )
    accha = await message.reply_text(
        text="__ᴅιиg ᴅιиg ꨄ︎ ѕтαятιиg..__"
    )
    await asyncio.sleep(0.2)
    await accha.edit("__ᴅιиg ᴅιиg ꨄ sтαятιиg.....__")
    await asyncio.sleep(0.2)
    await accha.edit("__ᴅιиg ᴅιиg ꨄ︎ sтαятιиg..__")
    await asyncio.sleep(0.2)
    await accha.delete()

async def get_chat_member_safe(chat_id, user_id):
    try:
        chat_member = await app.get_chat_member(chat_id, user_id)
        return chat_member
    except UserNotParticipant:
        return None
    except PeerIdInvalid:
        return None

async def send_response(message, response, reply_markup=None):
    await message.reply_text(response, reply_markup=reply_markup)

@app.on_callback_query()
async def callback_handler(_, query):
    if query.data == "today":
        await handle_today_query(query)
    elif query.data == "total":
        await handle_total_query(query)
    elif query.data == "channel":
        await handle_channel_query(query)
    elif query.data == "group":
        await handle_group_query(query)

async def handle_today_query(query):
    top_members = await get_top_members("today")
    response = " 𝗧𝗢𝗗𝗔𝗬 𝗟𝗘𝗔𝗗𝗘𝗥𝗕𝗢𝗔��������:\n\n"
    counter = 1
    for member in top_members:
        user_id = member["_id"]
        chat_member = await get_chat_member_safe(query.message.chat.id, user_id)

        if chat_member:
            total_messages = member["total_messages"]
            full_name = f"{chat_member.user.first_name} {chat_member.user.last_name}" if chat_member.user.last_name else chat_member.user.first_name
            username = chat_member.user.username
            user_info = f"{counter}. {full_name} , ⏤͟͞{total_messages}\n"

            response += user_info
            counter += 1

    await query.message.edit_text(response, reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍃ᴛᴏᴅᴀʏ🍃", callback_data="today"),
                    InlineKeyboardButton("🍃ᴛᴏᴛᴀʟ🍃", callback_data="total")
                ],
                [
                    InlineKeyboardButton("🔙 Back", callback_data="back"),
                    InlineKeyboardButton("🔒 Close", callback_data="close")
                ]
            ]
        ))

async def handle_total_query(query):
    top_members = await get_top_members("overall")
    response = " 𝗚𝗟𝗢𝗕𝗔𝗟 𝗟𝗘𝗔𝗗𝗘𝗥𝗕𝗢𝗔𝗥𝗗 | 🌍\n\n"
    counter = 1
    for member in top_members:
        user_id = member["_id"]
        chat_member = await get_chat_member_safe(query.message.chat.id, user_id)

        if chat_member:
            total_messages = member["total_messages"]
            full_name = f"{chat_member.user.first_name} {chat_member.user.last_name}" if chat_member.user.last_name else chat_member.user.first_name
            username = chat_member.user.username
            user_info = f"{counter}. {full_name}, ⏤͟͞{total_messages}\n"

            response += user_info
            counter += 1

    await query.message.edit_text(response, reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍃ᴛᴏᴅᴀʏ🍃", callback_data="today"),
                    InlineKeyboardButton("🍃ᴛᴏᴛᴀʟ🍃", callback_data="total")
                ],
                [
                    InlineKeyboardButton("🔙 Back", callback_data="back"),
                    InlineKeyboardButton("🔒 Close", callback_data="close")
                ]
            ]
        ))

async def handle_channel_query(query):
    await query.message.reply_text("𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗳𝗼𝗿 𝗺𝗼𝗿𝗲 𝘂𝗽𝗱𝗮𝘁𝗲𝘀: @ll_about_ari_ll")

async def handle_group_query(query):
    await query.message.reply_text("𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝗳𝗼𝗿 𝗱𝗶������������������������������������: @three_stars_ki_duniya")

async def handle_back_query(query):
    await query.message.edit_reply_markup(
        InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍃ᴛᴏᴅᴀʏ🍃", callback_data="today"),
                    InlineKeyboardButton("🍃ᴛᴏᴛᴀʟ🍃", callback_data="total")
                ],
                [
                    InlineKeyboardButton("🍃ᴄʜᴀɴɴᴇʟ🍃", callback_data="channel"),
                    InlineKeyboardButton("🍃ɢʀᴏᴜᴘ🍃", callback_data="group")
                ]
            ]
        )
    )

async def handle_close_query(query):
    await query.message.delete()

async def get_top_members(timeframe):
    if timeframe == "overall":
        cursor = top_members_collection.find().sort("total_messages", -1).limit(10)
    elif timeframe == "today":
        today_start = datetime.combine(datetime.today(), datetime.min.time())
        today_end = today_start + timedelta(days=1)
        cursor = top_members_collection.find({
            "last_updated": {"$gte": today_start, "$lt": today_end}
        }).sort("total_messages", -1).limit(10)

    return await cursor.to_list(length=10)

@app.on_message()
async def handle_messages(_, message):
    user_id = message.from_user.id
    user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
    user_data[user_id]["total_messages"] += 1

    today_start = datetime.combine(datetime.today(), datetime.min.time())
    top_members_collection.update_one(
        {"_id": user_id},
        {"$inc": {"total_messages": 1}, "$set": {"last_updated": datetime.now()}},
        upsert=True
    )

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪
║┏━━━━━━➣
║┣⪼ ᴏᴡɴᴇʀ :- @lll_notookk_lll
║┣⪼ ᴘᴀʀᴛ ᴏғ :- @ll_about_ari_ll
║┗━━━━━━➣
║╔═════ஜ۩۞۩ஜ════╗
║   ᴍᴇʀᴇ ʟɪʏᴇ ᴍᴇʀɪ ᴅᴜɴɪʏᴀ ʜᴏ ᴛᴍ..♥️ ᴍᴀɪɴᴇ
║
║ ᴊᴏ ᴍᴀɴɢɪ ᴡᴏ ᴅᴜᴀ ʜᴏ ᴛᴍ💞 ᴍᴇʀɪ ɴᴀᴢᴀʀ
║
║ ᴋɪ ᴛᴀʟᴀꜱʜ ʜᴏ ᴛᴍ✅ ᴍᴀɪɴᴇ ᴊᴏ ᴄʜᴀʜᴀ ᴡᴏ
║
║ ᴘʏᴀʀ ʜᴏ ᴛᴍ😍 ᴍᴇʀᴇ ɪɴᴛᴇᴢᴀᴀʀ ᴋɪ ʀᴀʜᴀᴛ
║
║ ʜᴏ ᴛᴍ✨ ᴍᴇʀᴇ ᴅɪʟ ᴋɪ ᴄʜᴀʜᴀᴛ ʜᴏ ᴛᴍ💖
║
║ ᴛᴜᴍ ʜᴏ ᴛᴏ ᴍᴜᴊʜᴇ ᴏʀ ᴋᴜᴄʜ ɴʜɪ ᴄʜᴀʜɪʏᴇ❣️ 
║ ᴋᴀɪꜱᴇ ᴋᴀʜᴜɴ ꜱɪʀꜰ  ᴘʏᴀʀ ɴᴀʜɪ 🥀 ᴍᴇʀɪ ᴊᴀᴀɴ ʜᴏ ᴛᴍ💥
║╚═════ஜ۩۞۩ஜ════╝
╚═════════════════❍⊱❁ """)

app.run()
