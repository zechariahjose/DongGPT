def detect_intent(text):

    text = text.lower()

    if "youtube" in text:
        return "open_youtube"

    elif "oras" in text or "time" in text:
        return "time"

    elif "hello" in text or "hi" in text:
        return "greeting"

    return "unknown"