from pyrogram import Client, filters
from ai import ask_ai
from database import save_user, save_chat

@Client.on_message(filters.private & ~filters.command(["start", "help", "chat"]))
async def handle_inline_chat(client, message):
    user_msg = message.text
    save_user(message.from_user.id, message.from_user.first_name)
    reply = ask_ai(user_msg)
    save_chat(message.from_user.id, user_msg, reply)
    await message.reply(reply)

@Client.on_message(filters.command("chat"))
async def handle_chat_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Use: `/chat your message`")
    query = " ".join(message.command[1:])
    save_user(message.from_user.id, message.from_user.first_name)
    reply = ask_ai(query)
    save_chat(message.from_user.id, query, reply)
    await message.reply(reply)
