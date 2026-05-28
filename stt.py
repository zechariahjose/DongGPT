import whisper

print("⏳ Loading Whisper model...")

model = whisper.load_model("base")

print("✅ Whisper loaded")

def transcribe(audio_path):

    result = model.transcribe(audio_path)

    text = result["text"]

    return text.strip()