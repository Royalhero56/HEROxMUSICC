from pyrogram import filters
from HeroXMusic import app
from g4f.client import Client

g4f_client = Client()

@app.on_message(filters.private & filters.text)
async def ai_chat_handler(_, message):
    try:
        prompt = message.text

        response = g4f_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        reply_text = response.choices[0].message.content
        await message.reply_text(reply_text)

    except Exception as e:
        await message.reply_text(f"AI Error: {e}")
