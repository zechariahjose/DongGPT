# DongGPT – Bisaya Voice Assistant

> Lightweight Python voice assistant that understands spoken Bisaya and English commands and responds using speech synthesis.

---

## Overview

DongGPT is an MVP (Minimum Viable Product) of a future Jarvis-style AI assistant.

The assistant listens through a microphone, converts speech into text using Whisper, detects user intent, executes commands, and responds with text-to-speech.

---

# Features

| Feature | Description |
|---|---|
| Voice Input | Captures audio from microphone |
| Speech-to-Text | Uses Whisper for transcription |
| Intent Detection | Rule-based NLP command matching |
| Command Execution | Handles YouTube, greetings, time, etc. |
| Text-to-Speech | Responds using synthesized speech |

---

# System Architecture

```text
┌───────────────┐
│ Voice Input   │
└──────┬────────┘
       ↓
┌───────────────┐
│ Whisper STT   │
└──────┬────────┘
       ↓
┌───────────────┐
│ Intent Logic  │
└──────┬────────┘
       ↓
┌───────────────┐
│ Command Exec  │
└──────┬────────┘
       ↓
┌───────────────┐
│ Text-to-Speech│
└───────────────┘


1. Clone the Repository
git clone https://github.com/yourusername/donggpt.git
cd donggpt


2. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install openai-whisper sounddevice scipy pyttsx3


4. Install FFmpeg
Download FFmpeg from:

https://www.gyan.dev/ffmpeg/builds/

Add FFmpeg to your system PATH:

C:\ffmpeg\bin

Verify installation:

ffmpeg -version
Run the Assistant
python main.py
