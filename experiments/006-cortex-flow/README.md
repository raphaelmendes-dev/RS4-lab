# 🧪 RS4 Cortex Flow — Experiment Index

RS4 Cortex Flow (EXP006) covers controlled multi-agent orchestration experiments executed against a local **Ollama** instance (`qwen2.5:7b`). Every run is recorded under `testNN-vX.Y.Z/` together with holistic **CEO RS4** metrics covering **Code / System**, **Ollama / Model**, and **Agent / Cline**.

## 🗂 Test Index

| Test | Focus | Result | Report (MD) | Metrics (JSON) | Input |
|---|---|---|:---:|---|---|---|
| **test01-v1.0.0** | Backend pipeline — 4-agent flow · `qwen2.5:7b` · local Ollama (`http://localhost:11434`) · 1,024-token cap | ✅ SUCCESS — 4/4 agents OK · 0.0% error · 605.88s pipeline | [`metrics_teste_backend_20260918_180917.md`](test01-v1.0.0/metrics_teste_backend_20260918_180917.md)<br>[`metrics_orquestrador_teste_backend_20260918_180917.md`](test01-v1.0.0/metrics_orquestrador_teste_backend_20260918_180917.md) | [`metrics_teste_backend_20260918_180917.json`](test01-v1.0.0/metrics_teste_backend_20260918_180917.json)<br>[`metrics_orquestrador_teste_backend_20260918_180917.json`](test01-v1.0.0/metrics_orquestrador_teste_backend_20260918_180917.json) | [`test_backend.txt`](test01-v1.0.0/test_backend.txt) |