import os
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def ask_ai(prompt):
    if not OPENAI_API_KEY:
        return "⚠️ OPENAI API key set nahi hai."
    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
        }
        res = requests.post(url, headers=headers, json=data).json()
        return res["choices"][0]["message"]["content"]
    except Exception as e:
        return "⚠️ AI error hua."
