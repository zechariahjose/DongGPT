from recorder import record_audio
from stt import transcribe
from tts import speak
from brain import detect_intent
from commands import execute

WAKE_WORDS = ["dong", "donggpt", "hey dong", "huy dong"]

def contains_wake_word(text: str) -> bool:
    t = text.lower()
    return any(w in t for w in WAKE_WORDS)

def main():
    print("=" * 45)
    print("🤖  DongGPT — Bisaya AI Assistant")
    print("=" * 45)
    print("💡  Tip: Ingon 'Dong' para makuha ang akong atensyon.")
    print("💡  Ingon 'exit' o 'quit' para mahunong.\n")

    speak("Helo! Ako si DongGPT, andam na ko motabang nimo.")

    while True:
        try:
            print("\n🎤  Namati ko... (5 segundos)")
            audio = record_audio(duration=5)

            text = transcribe(audio)
            if not text:
                continue

            print(f"📝  Giingon nimo: {text}")

            # ── Exit commands ──────────────────────────────────────────────
            if any(w in text.lower() for w in ["exit", "quit", "stop", "hunong"]):
                speak("Sige, mag-ingon! Balik-balik ha.")
                print("👋  DongGPT stopped.")
                break

            # ── Optional: require wake word ────────────────────────────────
            # Uncomment the block below if you want wake-word gating:
            # if not contains_wake_word(text):
            #     print("💤  (Waiting for wake word...)")
            #     continue

            # ── Detect intent via Claude ───────────────────────────────────
            intent_result = detect_intent(text)
            print(f"🧠  Intent: {intent_result.get('intent')}  "
                  f"(confidence: {intent_result.get('confidence', '?')})")

            # ── Execute & respond ─────────────────────────────────────────
            response = execute(intent_result, original_text=text)
            print(f"🤖  DongGPT: {response}")
            speak(response)

        except KeyboardInterrupt:
            speak("Sige, mag-ingon!")
            print("\n👋  Interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌  Error: {e}")
            speak("Adunay sayop. Sulayi pag-usab.")

if __name__ == "__main__":
    main()