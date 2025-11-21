from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL")

mongo = MongoClient(MONGO_URL)
db = mongo["MusicChatBot"]        # Database Name

users = db["users"]               # User collection
chatlogs = db["chatlogs"]         # Chat collection

def save_user(user_id, name):
    if not users.find_one({"user_id": user_id}):
        users.insert_one({
            "user_id": user_id,
            "name": name
        })

def save_chat(user_id, message, reply):
    chatlogs.insert_one({
        "user_id": user_id,
        "message": message,
        "reply": reply
    })
