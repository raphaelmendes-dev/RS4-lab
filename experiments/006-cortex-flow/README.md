# RS4 Cortex Flow — Experiment 006

This experiment covers controlled orchestration runs for a multi-agent backend pipeline executed against a local Ollama instance. The objective is to validate how agent handoff, synthesis, triage, and final integration behave under a bounded token budget and repeated execution scenarios.

## Objective

- Validate end-to-end orchestration across multiple specialized agents
- Exercise the local `qwen2.5:7b` runtime via Ollama
- Capture reproducible metrics for orchestration quality and latency
- Store the test evidence as JSON metrics and markdown summaries

## Environment

| Field | Value |
| --- | --- |
| Runtime | Local Ollama |
| Model | `qwen2.5:7b` |
| Endpoint | `http://localhost:11434` |
| Focus | Multi-agent orchestration and integration validation |
| Primary output | JSON metrics + markdown reports |

## Version overview

| Version | Focus | Key artifacts |
| --- | --- | --- |
| [v1.0.0](./v1.0.0) | Initial backend orchestration validation | `metrics_teste_backend_20260918_180917.*`, `metrics_orquestrador_teste_backend_20260918_180917.*`, `test_backend.txt` |
| [v2.0.0](./v2.0.0) | Expanded multi-agent pipeline validation | `00` to `13` orchestration metrics, plus trial and integration drafts |

## v1.0.0

This first version validates the backend pipeline with a single focused end-to-end execution and a refinement report.

| Artifact | Type | Description |
| --- | --- | --- |
| [metrics_teste_backend_20260918_180917.json](./v1.0.0/metrics_teste_backend_20260918_180917.json) | Metrics | Backend execution summary and test scoring |
| [metrics_teste_backend_20260918_180917.md](./v1.0.0/metrics_teste_backend_20260918_180917.md) | Report | Human-readable analysis of backend validation |
| [metrics_orquestrador_teste_backend_20260918_180917.json](./v1.0.0/metrics_orquestrador_teste_backend_20260918_180917.json) | Metrics | Orchestrator-level execution metrics |
| [metrics_orquestrador_teste_backend_20260918_180917.md](./v1.0.0/metrics_orquestrador_teste_backend_20260918_180917.md) | Report | Orchestration breakdown and signal review |
| [test_backend.txt](./v1.0.0/test_backend.txt) | Raw output | Terminal/test log of the execution |
| [refining-report](./v1.0.0/refining-report) | Folder | Refinement output artifacts and follow-up analysis |

## v2.0.0

This second version expands the pipeline into a more granular multi-agent flow, covering setup, ingestion, synthesis, review, and final integration steps.

### Core orchestration sequence

| Stage | Artifact | Type | Purpose |
| --- | --- | --- | --- |
| 00 | [00-metrics_setup_v2.json](./v2.0.0/00-metrics_setup_v2.json) | Metrics | Pipeline bootstrap and environment initialization |
| 01 | [01-metrics_chroma_v2.json](./v2.0.0/01-metrics_chroma_v2.json) | Metrics | Chroma/vector setup validation |
| 02 | [02-metrics_agente0_v2.json](./v2.0.0/02-metrics_agente0_v2.json) | Metrics | Agent 0 processing stage |
| 03 | [03-metrics_agente1_v2.json](./v2.0.0/03-metrics_agente1_v2.json) | Metrics | Agent 1 analysis stage |
| 04 | [04-metrics_seed_dna_v2.json](./v2.0.0/04-metrics_seed_dna_v2.json) | Metrics | Seed + DNA generation and branching |
| 05 | [05-metrics_agente2_redator_v2.json](./v2.0.0/05-metrics_agente2_redator_v2.json) | Metrics | Redaction / writing agent stage |
| 06 | [06-metrics_agente3_techscout_v2.json](./v2.0.0/06-metrics_agente3_techscout_v2.json) | Metrics | Tech scout agent output |
| 07 | [07-metrics_triagem_v2.json](./v2.0.0/07-metrics_triagem_v2.json) | Metrics | Triage and routing stage |
| 08 | [08-metrics_agente4_critico_v2.json](./v2.0.0/08-metrics_agente4_critico_v2.json) | Metrics | Critical review stage |
| 09 | [09-metrics_agente5_sintetizador_v2.json](./v2.0.0/09-metrics_agente5_sintetizador_v2.json) | Metrics | Synthesis stage |
| 10 | [10-metrics_agente6_builder_v2.json](./v2.0.0/10-metrics_agente6_builder_v2.json) | Metrics | Builder / implementation stage |
| 11 | [11-metrics_integracao_v2.json](./v2.0.0/11-metrics_integracao_v2.json) | Metrics | Integration layer validation |
| 12 | [12-metrics_agente7_evaluator_v2.json](./v2.0.0/12-metrics_agente7_evaluator_v2.json) | Metrics | Evaluator / quality gate |
| 13 | [13-metrics_triagem_v2.json](./v2.0.0/13-metrics_triagem_v2.json) | Metrics | Final triage/checkpoint |

### Supporting folders

| Folder | Description |
| --- | --- |
| [drafts](./v2.0.0/drafts) | Draft artifacts used during candidate synthesis and iteration |
| [implementation-tests-agents](./v2.0.0/implementation-tests-agents) | Agent implementation test assets and validation outputs |

## Experiment status

This experiment is primarily a research and validation suite for agent orchestration behavior, not a production deployment. It is designed to capture reproducibility, failure modes, and optimization signals across the orchestration lifecycle.

---

Last reviewed for README documentation updates in the RS4 lab repository.



