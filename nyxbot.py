
import json
import random
import os
from datetime import datetime

persona_path = "nyxbot_persona.json"
session_path = "nyxbot_sessions.json"

with open(persona_path, "r", encoding="utf-8") as f:
    persona = json.load(f)

if os.path.exists(session_path):
    with open(session_path, "r", encoding="utf-8") as f:
        sessions = json.load(f)
else:
    sessions = {}

def update_session(user_id, intent, success=False):
    timestamp = datetime.utcnow().isoformat()
    if user_id not in sessions:
        sessions[user_id] = {"history": [], "subs": 0, "tips": 0}
    sessions[user_id]["history"].append({
        "timestamp": timestamp,
        "intent": intent,
        "success": success
    })
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(sessions, f, indent=2)

def get_response(user_id, message):
    print(f"[DEBUG] Received message: {message}")
    message = message.lower()
    for intent, data in persona["response_layers"].items():
        for pattern in data["patterns"]:
            if pattern in message:
                update_session(user_id, intent, success=("subscribe" in message or "tip" in message))
                response = random.choice(data["responses"])
                follow_up = random.choice(data.get("follow_up", [""]))
                return response + (" " + follow_up if follow_up else "")
    update_session(user_id, "unknown", False)
    unknowns = persona["response_layers"]["unknown"]["responses"]
    return random.choice(unknowns)

def chat():
    user_id = input("Enter your user ID (or username): ")
    print(f"{persona['persona_name']}: Ready to dominate the conversation. Type 'quit' to exit.\n")
    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        reply = get_response(user_id, message)
        print(f"{persona['persona_name']}: {reply}")

if __name__ == "__main__":
    chat()
