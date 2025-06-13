# detect_intent.py

import re

def detect_intent(user_message):
    """
    Detects user intent from a wide variety of complex conversations.
    Returns a string indicating the detected intent.
    """

    msg = user_message.lower()

    # Greetings
    if re.search(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", msg):
        return "greeting"

    # Farewell
    if re.search(r"\b(bye|goodbye|see you|farewell|later)\b", msg):
        return "farewell"

    # Thanks
    if re.search(r"\b(thanks|thank you|thx|appreciate it)\b", msg):
        return "gratitude"

    # Apology
    if re.search(r"\b(sorry|my bad|apologies)\b", msg):
        return "apology"

    # Help requests
    if re.search(r"\b(help|assist|support|how do i|what is|can you explain|i need help)\b", msg):
        return "help_request"

    # Small talk
    if re.search(r"\b(how are you|what's up|how's it going|how do you do)\b", msg):
        return "small_talk"

    # Task management
    if re.search(r"\b(create|add|schedule|remind me|set up|plan|organize|book|arrange)\b", msg) and re.search(r"\b(task|event|meeting|reminder|appointment|call|deadline)\b", msg):
        return "task_management"

    # Complaints
    if re.search(r"\b(doesn't work|not working|issue|problem|error|crash|fail|broken)\b", msg):
        return "complaint"

    # Compliments
    if re.search(r"\b(great job|well done|awesome|amazing|fantastic|good bot|nice work)\b", msg):
        return "compliment"

    # Weather inquiry
    if re.search(r"\b(weather|forecast|temperature|rain|snow|sunny|cloudy|hot|cold)\b", msg):
        return "weather_inquiry"

    # Time inquiry
    if re.search(r"\b(what time|current time|time now|date today|day today)\b", msg):
        return "time_inquiry"

    # Jokes and fun
    if re.search(r"\b(joke|make me laugh|funny|tell me a joke)\b", msg):
        return "fun_request"

    # Bot's identity or creator
    if re.search(r"\b(who are you|what are you|who made you|who created you|your creator|about you)\b", msg):
        return "identity_inquiry"

    # News
    if re.search(r"\b(news|latest news|headlines|updates|current events)\b", msg):
        return "news_inquiry"

    # Math/Calculation
    if re.search(r"\b(calculate|math|what is [0-9]+[\+\-\*\/][0-9]+)\b", msg):
        return "math_request"

    # Shopping/Product Inquiry
    if re.search(r"\b(buy|price|purchase|order|shop|product|catalog|availability)\b", msg):
        return "shopping_inquiry"

    # Default fallback
    return "unknown"

# Example usage:
# intent = detect_intent("Can you set up a meeting for tomorrow at 3pm?")
# print(intent)  # Outputs: task_management
