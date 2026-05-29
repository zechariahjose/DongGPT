from dotenv import load_dotenv
load_dotenv()
import webbrowser
from datetime import datetime
from groq import Groq

client = Groq()  # reads GROQ_API_KEY from environment

BISAYA_SYSTEM = (
    "Ikaw si DongGPT, usa ka matinabangon ug maaligon nga AI assistant "
    "nga nagsulti ug Bisaya (Cebuano). "
    "Tubaga ang tanang pangutana sa natural, hamubo, ug tin-aw nga Bisaya. "
    "Dili mogamit ug markdown o bullet points — sulti lang normal."
)

# ── Fallback: ask Groq (Llama 3) to generate a Bisaya reply ──────────────────
def _ask_groq(user_text: str) -> str:
    """Generate a friendly Bisaya response for unknown or complex inputs."""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            max_tokens=300,
            messages=[
                {"role": "system", "content": BISAYA_SYSTEM},
                {"role": "user",   "content": user_text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌  Groq fallback error: {e}")
        return "Pasensya na, dili ko makatubag karon. Sulayi pag-usab."


# ── Intent handlers ───────────────────────────────────────────────────────────
def execute(intent_result: dict, original_text: str = "") -> str:
    """
    Accepts the full intent dict from brain.py.
    Falls back to Groq for free-form conversation.
    """
    intent   = intent_result.get("intent", "unknown")
    entities = intent_result.get("entities", {})
    query    = entities.get("query")

    # --- Web / App openers ---
    if intent == "open_youtube":
        if query:
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(url)
            return f"Nangita ko sa YouTube: {query}"
        webbrowser.open("https://youtube.com")
        return "Giablihan nako ang YouTube."

    elif intent == "open_facebook":
        webbrowser.open("https://facebook.com")
        return "Giablihan nako ang Facebook."

    elif intent == "open_google":
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            return f"Nangita ko sa Google: {query}"
        webbrowser.open("https://google.com")
        return "Giablihan nako ang Google."

    # --- Date / Time ---
    elif intent == "time":
        current = datetime.now().strftime("%I:%M %p")
        return f"Ang oras karon kay {current}."

    elif intent == "date":
        today = datetime.now().strftime("%A, %B %d, %Y")
        return f"Ang petsa karon kay {today}."

    # --- Social ---
    elif intent == "greeting":
        hour = datetime.now().hour
        if hour < 12:
            return "Maayong buntag! Unsay akong matabang nimo?"
        elif hour < 18:
            return "Maayong hapon! Naa koy mahimo para nimo?"
        else:
            return "Maayong gabii! Unsay imong gikinahanglan?"

    elif intent == "farewell":
        return "Sige, mag-ingon! Balik-balik ha kung naay pangutana."

    # --- Entertainment ---
    elif intent == "joke":
        return _ask_groq("Suginli ko ug usa ka funny nga Bisaya joke.")

    elif intent == "music":
        search = query if query else "OPM music"
        url = f"https://www.youtube.com/results?search_query={search.replace(' ', '+')}"
        webbrowser.open(url)
        return f"Nangita ko ug musika sa YouTube: {search}"

    # --- Info ---
    elif intent == "weather":
        return _ask_groq(
            "Ang user nagpangutana sa weather. "
            "Sultihi sila nga dili ka direkta makakuha sa real-time na weather data, "
            "pero pwede nila i-check ang weather.com o ang ilang phone. "
            "Sag-ula sa Bisaya."
        )

    elif intent == "wikipedia":
        topic = query if query else original_text
        if topic:
            url = f"https://en.wikipedia.org/wiki/Special:Search?search={topic.replace(' ', '+')}"
            webbrowser.open(url)
            return f"Nangita ko sa Wikipedia bahin sa: {topic}"
        return "Unsa ang gusto nimong pangitaon sa Wikipedia?"

    elif intent == "calculate":
        return _ask_groq(f"Kuwentaha kini ug ipakita ang tubag sa Bisaya: {original_text}")

    # --- Unknown / Free-form conversation ---
    elif intent == "unknown" or not intent:
        if original_text:
            return _ask_groq(original_text)
        return "Wala ko kasabot. Mahimo bang balikan nimo?"

    # Catch-all
    return _ask_groq(original_text) if original_text else "Wala ko kasabot."