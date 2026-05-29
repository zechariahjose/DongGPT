from dotenv import load_dotenv
load_dotenv()
from groq import Groq
import json

client = Groq()  # reads GROQ_API_KEY from environment

SYSTEM_PROMPT = """Ikaw usa ka intent classifier para sa usa ka Bisaya AI assistant nga ginganlag DongGPT.

Ang imong trabaho: basaha ang input sa user ug ibalik ang pinaka-angay nga intent isip JSON.

Mga available nga intents:
- open_youtube       : gusto ablihan ang YouTube
- open_facebook      : gusto ablihan ang Facebook
- open_google        : gusto ablihan ang Google
- time               : nagpangutana sa oras karon
- date               : nagpangutana sa petsa karon
- greeting           : nagkomusta o nagbati
- farewell           : nagpaalam o nag-goodbye
- joke               : nagpangayo ug joke
- weather            : nagpangutana sa panahon (weather)
- music              : gusto mamati ug musika sa YouTube
- wikipedia          : gusto mangita ug impormasyon
- calculate          : gusto mag-compute o mag-calculate
- unknown            : wala sa lista o dili klaro

Ibalik LAMANG ang usa ka valid JSON nga adunay kini nga format (walay markdown, walay explanation):
{
  "intent": "<intent_name>",
  "entities": {
    "query": "<relevant keyword or topic kung naay, otherwise null>"
  },
  "confidence": <0.0 to 1.0>
}

Pananglitan:
Input: "Palihug ablihan ang YouTube"
Output: {"intent": "open_youtube", "entities": {"query": null}, "confidence": 0.99}

Input: "Mangita ko ug recipe sa adobo"
Output: {"intent": "wikipedia", "entities": {"query": "adobo recipe"}, "confidence": 0.85}

Input: "Unsa man ang weather ugma?"
Output: {"intent": "weather", "entities": {"query": null}, "confidence": 0.97}
"""

def detect_intent(text: str) -> dict:
    """
    Uses Groq (free) to detect the intent of the user's text.
    Returns a dict with 'intent', 'entities', and 'confidence'.
    """
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            max_tokens=256,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": text}
            ]
        )

        raw = response.choices[0].message.content.strip()

        # Strip markdown code fences if present
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
            raw = raw.strip()

        result = json.loads(raw)
        return result

    except (json.JSONDecodeError, IndexError, KeyError) as e:
        print(f"⚠️  Brain parse error: {e}")
        return {"intent": "unknown", "entities": {"query": None}, "confidence": 0.0}

    except Exception as e:
        print(f"❌  Brain API error: {e}")
        return {"intent": "unknown", "entities": {"query": None}, "confidence": 0.0}