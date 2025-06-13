from session_memory import SessionMemory

session = SessionMemory()

def generate_response(username, user_message):
    intent = detect_intent(user_message)

    # Append user message to thread
    session.append_exchange(username, "user", user_message, intent)

    # Fetch last context
    recent_thread = session.get_last_thread(username, n=3)  # Last 3 turns

    # Build response with reference to context
    response = ""
    # Example: Reference user last topic if relevant
    for exchange in reversed(recent_thread):
        if exchange["sender"] == "user" and exchange["intent"] == "emotional_disclosure":
            response = "You mentioned feeling down earlier. Has your mood changed at all? "
            break

    # Now, create your base response as before
    core_response = ... # (existing logic)

    response += core_response

    # Append bot message to thread
    session.append_exchange(username, "bot", response, intent)

    return response