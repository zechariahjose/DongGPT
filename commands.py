import webbrowser
from datetime import datetime

def execute(intent):

    if intent == "open_youtube":

        webbrowser.open("https://youtube.com")

        return "Giablihan nako ang YouTube"

    elif intent == "time":

        current = datetime.now().strftime("%I:%M %p")

        return f"Ang oras karon kay {current}"

    elif intent == "greeting":

        return "Maayong adlaw! Unsay akong matabang?"

    return "Wala ko kasabot."