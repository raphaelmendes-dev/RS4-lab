# SofiaVoice v2.0 — Engineering Notes & Security Audit

## ⚡ Performance Matrix (v1.0 vs v2.0)

| Layer | v1.0 (Legacy Baseline) | v2.0 (Async Pipeline) | Delta / Impact |
|---|---|---|---|
| **STT** | ~0.718s (Whisper) | **~0.613s** (Groq Whisper Large V3) | 🚀 14.6% reduction |
| **LLM** | ~0.673s (Llama 3) | **~0.385s - 0.479s** (`openai/gpt-oss-20b`) | 🚀 38.3% reduction |
| **TTS** | ~4.415s (gTTS) | **~1.728s - 2.100s** (Edge-TTS FranciscaNeural) | 🚀 58.1% reduction |
| **Total Latency** | **~5.806s** | **~2.800s** | 🚀 **51.7% overall speedup** |
| **Payload Size** | 64.5 KB | **30.8 KB** | 📉 **52.2% payload reduction** |

---

## 🛡️ Resilience & Security Audit Report

The following guardrails were implemented and validated during Phase 14 security testing:

| Security Test Case | Guardrail Mechanism | Target Route | Status |
|---|---|---|---|
| **Excessive Payload (>10MB)** | `Content-Length` Middleware Enforcement | `/api/transcribe` | ✅ **HTTP 413 Payload Too Large** |
| **XSS / Script Injection** | Text Input Sanitization (`sanitize_text`) | `/api/chat` | ✅ **Sanitized / Escaped** |
| **Unauthorized Cross-Origin** | Restricted Domain CORS Middleware | Global API | ✅ **Access Denied (Non-Whitelisted)** |
| **Null / Silent Audio Payload** | Empty File Validation & Graceful Silence Guard | `/api/transcribe` | ✅ **HTTP 400 Bad Request** |

---

## 🔧 Technical Changelog (v2.0.0 Release)

- **ASGI Migration:** Fully converted backend orchestration from synchronous handlers to FastAPI async/await coroutines.
- **Model Standardization:** Standardized primary production LLM endpoint to `openai/gpt-oss-20b` via `AsyncGroq`.
- **Neural Speech Synthesis:** Replaced `gTTS` with Microsoft `Edge-TTS` (`pt-BR-FranciscaNeural`) for humanized pitch and reduced latency.
- **VAD Adjustment:** Expanded silence capture window from `0.7s` to `1.5s - 2.0s` to prevent premature user truncation.