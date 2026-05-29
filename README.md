# DongGPT — Bisaya AI Voice Assistant

A smart, voice-powered AI assistant that understands natural Bisaya (Cebuano) and English sentences. Powered by **Groq (Llama 3)** for free AI responses, **Whisper** for speech-to-text, and **pyttsx3** for text-to-speech.

---

##  Features

-  **Voice input** — speaks to you, listens back
-  **Natural language understanding** — understands full sentences, not just keywords
-  **Bisaya responses** — replies in Cebuano naturally
-  **Free-form conversation** — ask anything, even outside the command list
-  **Conversation loop** — keeps listening until you say "hunong"
-  **100% free AI** — powered by Groq (no credit card needed)

---

##  What DongGPT Can Do

| What you say | What it does |
|---|---|
| "Ablihan ang YouTube" | Opens YouTube |
| "Ablihan ang Facebook" | Opens Facebook |
| "Pangita sa Google ug..." | Searches Google |
| "Unsa man ang oras?" | Tells current time |
| "Unsa man ang petsa karon?" | Tells current date |
| "Maayong buntag Dong!" | Greets back |
| "Suginli ko ug joke" | Tells a Bisaya joke |
| "I-play ang OPM music" | Searches YouTube Music |
| "Unsa ang weather?" | Gives weather advice |
| "Mangita ug impormasyon bahin sa..." | Opens Wikipedia |
| "Kuwentaha ang 25 times 4" | Calculates and answers |
| Anything else | Free-form Bisaya conversation |

---

##  Project Structure

```
DongGPT/
├── main.py          # Entry point, conversation loop
├── brain.py         # Intent detection via Groq (Llama 3)
├── commands.py      # Command execution + Bisaya responses
├── recorder.py      # Microphone audio recording
├── stt.py           # Speech-to-text via Whisper
├── tts.py           # Text-to-speech via pyttsx3
├── .env             # Your API key (never commit this!)
└── .gitignore       # Ignores .env, wav files, cache
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/DongGPT.git
cd DongGPT
```

### 2. Install Python dependencies
```bash
pip install sounddevice scipy openai-whisper pyttsx3 groq python-dotenv
```

### 3. Install FFmpeg (required for Whisper)
Download from  https://ffmpeg.org/download.html and add it to your system PATH.

### 4. Get a FREE Groq API key
1. Go to  https://console.groq.com
2. Sign up (Google account works)
3. Click **API Keys → Create API Key**
4. Copy your key

### 5. Create your `.env` file
Create a file named `.env` in the project root:
```
GROQ_API_KEY=your-groq-api-key-here
```

### 6. Run DongGPT
```bash
python main.py
```

---

##  Security Notes

- **Never commit your `.env` file** — it contains your secret API key
- The `.gitignore` already excludes `.env`, `input.wav`, and `__pycache__`
- If you accidentally expose your key, revoke it immediately at https://console.groq.com

---

##  Dependencies

| Package | Purpose |
|---|---|
| `groq` | Free AI responses via Llama 3 |
| `openai-whisper` | Speech-to-text (runs locally) |
| `pyttsx3` | Text-to-speech (runs locally) |
| `sounddevice` | Microphone recording |
| `scipy` | Audio file writing |
| `python-dotenv` | Load API key from `.env` |

---

##  How to Stop

Say **"exit"**, **"quit"**, or **"hunong"** — or press `Ctrl+C`.

---

##  Built With

- [Groq](https://console.groq.com) — Free LLM API (Llama 3)
- [OpenAI Whisper](https://github.com/openai/whisper) — Speech recognition
- [pyttsx3](https://pypi.org/project/pyttsx3/) — Offline text-to-speech

---
