import json
import random

with open('responses.json', 'r', encoding='utf-8') as f:
    RESPONSES = json.load(f)

# Track user state for progressive conversation (can be expanded with a proper state system)
user_state = {}

def get_bot_response(user_message, user_id):
    user_message = user_message.lower()
    response = None

    # Check direct info requests first
    for category in ["reply_user_location", "reply_user_age", "reply_user_job"]:
        for pattern in RESPONSES[category]["patterns"]:
            if pattern in user_message:
                response = random.choice(RESPONSES[category]["responses"])
                break
        if response:
            return response

    # Handle personal questions with a follow-up
    for pattern in RESPONSES["personal_question"]["patterns"]:
        if pattern in user_message:
            answer = random.choice(RESPONSES["personal_question"]["responses"])
            followup = random.choice(RESPONSES["user_info_followup"]["responses"])
            return f"{answer} {followup}"

    # Handle seductive transition/escalation
    for category in ["seductive_transition", "seductive_escalation"]:
        for pattern in RESPONSES[category]["patterns"]:
            if pattern in user_message:
                return random.choice(RESPONSES[category]["responses"])

    # Handle intro and normal questions
    for category in ["intro_conversation", "ask_user_info"]:
        for pattern in RESPONSES[category]["patterns"]:
            if pattern in user_message:
                return random.choice(RESPONSES[category]["responses"])

    # Default fallback
    return "Mmm… you’ll have to speak my language, baby."
    from detect_intent import detect_intent
