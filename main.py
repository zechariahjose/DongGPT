from recorder import record_audio
from stt import transcribe
from tts import speak
from brain import detect_intent
from commands import execute

print("🚀 DongGPT Started")

audio = record_audio(duration=5)

text = transcribe(audio)

print("📝 You said:", text)

intent = detect_intent(text)

response = execute(intent)

speak(response)