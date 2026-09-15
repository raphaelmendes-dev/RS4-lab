# SofiaVoice v1.0 — Legacy Baseline Report

## 📌 Historical Overview
SofiaVoice v1.0 was designed as a synchronous/blocking proof-of-concept system[cite: 1, 3]. It lacked layer-by-layer latency tracking, async coroutines, and granular observability[cite: 1, 3].

## 🐢 Humanized Behavior & Bottlenecks
* **Audio Synthesis (gTTS):** The Google Text-to-Speech library generated a robotic and slow audio response, consuming ~76.1% of the total request execution time (~4.415s out of ~5.806s total)[cite: 1, 3].
* **Microphone Cutoff:** Early mic termination window (~0.7s) frequently led to fragmented audio inputs and premature request dispatches[cite: 1, 3].
* **Error Handling:** Unhandled exceptions during STT execution caused high failure rates on silent inputs, ambient noise, or ultra-short audio payloads[cite: 1, 3].
* **Pipeline Latency:** Total request latency hovered around ~5.806s with zero visibility into component-level overhead[cite: 1, 3].

## 📊 Legacy Performance Summary

| Metric | Measured Value |
|---|---|
| **STT Latency (Whisper)** | ~0.718s |
| **LLM Latency (Llama 3)** | ~0.673s |
| **TTS Latency (gTTS)** | ~4.415s |
| **Total Roundtrip Latency** | ~5.806s |
| **Average Payload Size** | ~64.5 KB |