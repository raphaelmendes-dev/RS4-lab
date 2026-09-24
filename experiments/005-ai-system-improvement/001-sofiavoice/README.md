<div align="center">
<img src="https://raw.githubusercontent.com/raphaelmendes-dev/sofiavoice/main/assets/Rs4Machine.png" alt="Rs4Machine Logo" width="200" />

# RS4 Machine · AI Research Lab

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://portfolio-modular-rs4-machine.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raphaelmendes-dev/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:python.dev.raphael@gmail.com)

[🇧🇷 Mudar para Português](README.pt-BR.md) · **🇺🇸 English (this file)**

### Controlled AI Experiments · Low Latency & Production Systems

</div>

The **RS4 Lab** is Rs4Machine's experimental research lab — a space for controlled experimentation in intelligent systems, AI agents, and software engineering. It isn't a startup, and it isn't an agent playground: it's a lab with a method, where hypotheses become experiments, experiments become evidence, and evidence becomes decisions — always with a human as the final decision-maker.

---

## 🧪 Research Experiments

| ID | Experiment | Focus | Status | Production / Artifacts |
|---|---|---|:---:|---|
| **EXP001** | **[Architecture First](experiments/001-architecture-first/)** | Synchronous Baseline & Bottleneck Mapping | 🧊 Frozen | [📄 View Case](experiments/001-architecture-first/) |
| **EXP005** | **[SofiaVoice v2.0](experiments/005-ai-system-improvement/001-sofiavoice/)** | Async Rebuild, Edge-TTS Neural & API Guardrails | ✅ Released | [🚀 Case Study](experiments/005-ai-system-improvement/001-sofiavoice/) · [App Repo](https://github.com/raphaelmendes-dev/sofiavoice) |

---

## 📊 EXP005 Highlight — SofiaVoice v2.0 Benchmark

| Layer | v1.0 Baseline | v2.0 Release | Improvement |
|---|---|---|---|
| **STT** | ~0.72s (Whisper) | **~0.61s** (Whisper Large V3) | 🚀 15% faster |
| **LLM** | ~0.67s (LLaMA 3.3) | **~0.41s** (openai/gpt-oss-20b) | 🚀 38% faster |
| **TTS** | ~4.41s (gTTS) | **~1.85s** (Edge-TTS Neural) | 🚀 58% faster |
| **Latency** | **~5.80s** | **~2.80s** | 🚀 **51.7% faster** |

---

## 🧪 EXP005 Experiment Index — SofiaVoice v2.0 Test Runs

Controlled stress runs executed against the `voice` endpoint (`http://localhost:8000`) with `test_stress_sofia.py`.

| Test | Description | SLO Verdict | Report / Artifacts |
|---|---|---|:---:|---|
| **test00-sofia-v2.0.0** | v1.0 legacy baseline & v2.0 engineering notes / security audit | — | [`BASELINE.md`](test00-sofia-v2.0.0/BASELINE.md) · [`notes.md`](test00-sofia-v2.0.0/notes.md) |
| **test01-sofia-v2.0.0** | Stress run — endpoint unreachable (`ConnectionRefusedError`), 100% error rate | ❌ FAIL | [`Result_20260920_141520_EN.md`](test01-sofia-v2.0.0/Result_20260920_141520_EN.md) |
| **test02-sofia-v2.0.0** | Real audio asset (`assets/test02-sofia.wav`) — 3/3 OK, latency above SLO | ❌ FAIL | [`Result_20260922_190343.md`](test02-sofia-v2.0.0/Result_20260922_190343.md) |
| **test03-sofia-v2.0.0** | Synthetic audio — 3/3 OK, latency within SLO | ✅ PASS | [`Result_20260922_191537.md`](test03-sofia-v2.0.0/Result_20260922_191537.md) |
| **test04-sofia-v2.0.0** | Synthetic audio — 3/3 OK, latency within SLO | ✅ PASS | [`Result_20260922_192311.md`](test04-sofia-v2.0.0/Result_20260922_192311.md) |
| **test05-sofia-v2.0.0** | EXP005 consolidated metrics (production environment audit) | — | [`metrics.json`](test05-sofia-v2.0.0/metrics.json) |

---

## 🛠️ Stack & Infrastructure

![Python](https://img.shields.io/badge/Python-3.14.2-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-009688?style=flat&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15.5.12-000000?style=flat&logo=next.js&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Whisper_V3_%7C_gpt--oss--20b-F6B000?style=flat&logoColor=white)
![Edge-TTS](https://img.shields.io/badge/Edge--TTS-FranciscaNeural-0078D4?style=flat&logo=microsoft&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white)

---

## 📬 Contact

📩 [python.dev.raphael@gmail.com](mailto:python.dev.raphael@gmail.com) ·
🔗 [LinkedIn](https://www.linkedin.com/in/raphaelmendes-dev/) ·
🌐 [Portfolio](https://portfolio-modular-rs4-machine.vercel.app/)

<div align="center">

*Raphael Mendes · Rs4Machine · September 2026*

</div>