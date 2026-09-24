# Experiment 001 - SofiaVoice Architecture

> 🧊 **FROZEN HISTORICAL RECORD — Baseline v1.0 (Legacy Synchronous)**
> This document describes the reference state **v1.0** and MUST NOT be retroactively modified.
> The transition to the asynchronous v2.0 pipeline is documented in
> [`experiments/005-ai-system-improvement/001-sofiavoice/`](../005-ai-system-improvement/001-sofiavoice/).

**Date:** 19/08/2026  
**Objective:** Map SofiaVoice's current architecture and identify bottlenecks.

## Current Architecture (baseline v1.0)
- **Frontend:** Next.js (audio capture via Web Audio API)
- **Backend:** FastAPI (runs on Render)
- **STT:** Whisper (via Groq)
- **LLM:** LLaMA 3.3 70B (via Groq)
- **TTS:** gTTS (saves file, converts to base64)

## Identified Bottlenecks
1. TTS saves file to disk → extra latency
2. Sequential pipeline (one step waits for the other)
3. Multiple HTTP round trips