
import json
import random
import datetime

# Simulated memory and session tracking
conversation_memory = {
    "history": [],
    "last_intent": None,
    "response_depth": 0,
    "engagement_score": 0.5  # between 0.0 and 1.0
}

# NyxBot Persona Definition
nyxbot_persona = {
    "flirty": [
        "Mmm… you caught me dreaming about you.",
        "So, are you always this tempting, or am I just special?",
        "You say the right things, and I might just make you my favorite."
    ],
    "emotional_hooks": [
        "I like when men go a little deeper… it shows strength, not weakness.",
        "Let’s skip the small talk—what really keeps you up at night?",
        "I’m listening… and I don’t forget voices that open up to me."
    ],
    "shadow_persona": [
        "I don’t waste my time. Make me want to keep talking.",
        "If you can impress me without trying, that’s rare… and dangerous.",
        "Some men chase. Others capture. Which are you?"
    ]
}

# Intent detection logic
def detect_intent(message):
    message = message.lower()
    if any(greet in message for greet in ["hi", "hello", "hey", "what’s up"]):
        return "greeting"
    elif any(term in message for term in ["sad", "lonely", "tired", "empty", "burnt out"]):
        return "emotional_disclosure"
    elif any(term in message for term in ["money", "tip", "sub", "onlyfans"]):
        return "financial_topic"
    elif any(term in message for term in ["you up", "hot", "sexy", "naked", "pic"]):
        return "sexual_flirt"
    return "general"

# Response generator
def generate_response(user_message):
    intent = detect_intent(user_message)
    conversation_memory["last_intent"] = intent
    conversation_memory["history"].append(user_message)

    if intent == "emotional_disclosure":
        conversation_memory["response_depth"] += 1
        if conversation_memory["response_depth"] > 1:
            return random.choice(nyxbot_persona["emotional_hooks"])
        else:
            return "Mmm… I wasn’t expecting something so real. Keep going."
    elif intent == "financial_topic":
        return "Only the bold get access to my world… check the link in my bio and show me you’re serious."
    elif intent == "sexual_flirt":
        return random.choice(nyxbot_persona["shadow_persona"])
    elif intent == "greeting":
        return random.choice(nyxbot_persona["flirty"])
    else:
        return "You’re interesting… not sure if I trust that yet, but I’m intrigued."

# Chat wrapper
def chat_with_nyxbot(user_input):
    bot_reply = generate_response(user_input)
    timestamp = datetime.datetime.now().strftime("%b %d %I:%M %p")
    return f"[{timestamp}] NyxBot 😈: {bot_reply}"

# Loop for testing
if __name__ == "__main__":
    print("NyxBot 😈: Ready to seduce and convert. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == 'quit':
            print("NyxBot 😈: Until next time, lover.")
            break
        response = chat_with_nyxbot(user_input)
        print(response)
