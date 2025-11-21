from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, OPENAI_API_KEY, MONGO_DB_URI
from pymongo import MongoClient
import openai

# ------------ MongoDB Connection -------------
mongo = MongoClient(MONGO_DB_URI)
db = mongo["shruti_ai_chat"]
users = db["users"]

# ------------ OpenAI / Opera AI -------------
openai.api_key = OPENAI_API_KEY

# ------------ Pyrogram Bot ------------------
bot = Client(
    "AI-CHAT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ------------ Chat Handler -------------------
@bot.on_message(filters.text & ~filters.command(["start", "help"]))
async def ai_chat_handler(bot, message):

    user_id = message.from_user.id
    user_msg = message.text

    # Save user chat history
    users.update_one(
        {"user_id": user_id},
        {"$push": {"messages": {"role": "user", "content": user_msg}}},
        upsert=True
    )

    # Send to OpenAI / Opera AI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",     # opera/openai supported model
            messages=[{"role": "user", "content": user_msg}]
        )

        bot_reply = response["choices"][0]["message"]["content"]

    except Exception as e:
        bot_reply = f"⚠ AI Error: {e}"

    # Send reply to user
    await message.reply_text(bot_reply)

# ------------ Start Bot ----------------------
bot.run()
