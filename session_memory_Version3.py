import json
from datetime import datetime

class SessionMemory:
    def __init__(self, filename="session_memory.json"):
        self.filename = filename
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.memory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.memory = {}

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=2, ensure_ascii=False)

    def get_user(self, username):
        if username not in self.memory:
            self.memory[username] = {
                "thread": [],
                "history": [],
                "subs": 0,
                "tips": 0,
                "promo_clicks": 0,
                "last_intent": None,
                "last_success": None,
                "favorite_intents": [],
                "last_mood": None,
                "user_profile": {
                    "name": username,
                    "interests": [],
                    "personality_notes": "",
                    "engagement_level": "low",
                    "last_seen": None
                }
            }
        return self.memory[username]

    def append_exchange(self, username, sender, message, intent):
        user = self.get_user(username)
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "sender": sender,
            "message": message,
            "intent": intent
        }
        user["thread"].append(entry)
        # Keep only last 10 exchanges (5 turns)
        user["thread"] = user["thread"][-10:]
        self.save()

    def get_last_thread(self, username, n=5):
        user = self.get_user(username)
        return user["thread"][-n*2:]  # n turns (user+bot)

    # ... (other existing methods remain unchanged)