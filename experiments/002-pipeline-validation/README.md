# Architecture

## Diagram

The architecture diagram is available at:

docs/architecture.excalidraw


---

## Overview

SofiaVoice is a voice assistant application consisting of a FastAPI backend and a Next.js frontend. The backend orchestrates a linear pipeline of three independent services — STT, LLM, and TTS — that process input audio and return output audio.

**Pipeline:**

INPUT AUDIO → STT → LLM → TTS → OUTPUT AUDIO


---

## Components

### Backend — FastAPI

Entry point of the application. Handles HTTP requests from the frontend, triggers the services sequentially, and returns the result.

| Attribute | Value |
|---|---|
| Framework | FastAPI |
| Language | Python |
| Deployment | Railway |
| Responsibility | Pipeline orchestration (STT → LLM → TTS) |

**File structure:**

backend/
├── main.py
├── routers/
│   └── voice.py
└── services/
├── stt.py
├── llm.py
└── tts.py


---

### STT — Speech-to-Text

Receives the audio file sent by the frontend and returns the transcribed text.

| Attribute | Value |
|---|---|
| Provider | Groq API |
| Model | Whisper Large V3 |
| Input | Audio file |
| Output | Transcribed text |

---

### LLM — Large Language Model

Receives the transcribed text from STT and returns the text response.

| Attribute | Value |
|---|---|
| Provider | Groq API |
| Model | openai/gpt-oss-20b |
| Input | Transcribed text |
| Output | Response text |

---

### TTS — Text-to-Speech

Receives the response text from the LLM and returns the synthesized audio.

| Attribute | Value |
|---|---|
| Engine | gTTS |
| Output Format | MP3 |
| Input | Response text |
| Output | Base64-encoded MP3 audio |

---

### Frontend

Handles user interaction: captures microphone audio, sends it to the backend, and plays back the received response audio.

| Attribute | Value |
|---|---|
| Framework | Next.js |
| Deployment | Vercel |
| Responsibility | Audio capture · Backend communication · Response playback |

> **Status:** End-to-end frontend ↔ backend integration not yet validated. Backend pipeline tested locally via Swagger.

---

## Data Flow

Frontend captures user audio

Frontend sends audio to backend via POST /api/voice

Backend triggers stt.py → transcribed text

Backend triggers llm.py with text → response text

Backend triggers tts.py with response → Base64-encoded MP3 audio

Backend returns JSON to frontend:
{
"user_text":    "",
"ai_response":  "",
"audio_base64": "",
"format":       "mp3"
}

Frontend decodes Base64 and plays audio


> **Validation Status:** The backend and `POST /api/voice` pipeline were successfully tested locally via Swagger. Full end-to-end frontend integration will be validated in the next project phase.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI · Python |
| STT | Groq API · Whisper Large V3 |
| LLM | Groq API · openai/gpt-oss-20b |
| TTS | gTTS |
| Output Audio Format | MP3 |
| Frontend | Next.js |
| Backend Deployment | Railway |
| Frontend Deployment | Vercel |

---

## Current Architecture vs. Future Improvements

This section distinguishes what is currently implemented from planned features.

### Implemented

- Linear STT → LLM → TTS pipeline via FastAPI
- Speech transcription using Whisper Large V3 via Groq
- Response generation using openai/gpt-oss-20b via Groq
- Voice synthesis using gTTS in MP3 format
- Endpoint response in JSON containing `user_text`, `ai_response`, `audio_base64`, and `format`
- Pipeline locally validated via Swagger
- Next.js frontend implemented (end-to-end integration pending validation)
- Deployed on Railway (backend) and Vercel (frontend)

### Not Implemented (Roadmap Log)

> This section will be updated as roadmap decisions are made. No improvements were documented in the source text.