<div align="center">
<img src="https://raw.githubusercontent.com/raphaelmendes-dev/sofiavoice/main/assets/Rs4Machine.png" alt="Rs4Machine Logo" width="180" />

# 🧪 RS4 Lab

**Experimental Systems Lab · Rs4Machine**

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-Active%20experimentation-blue)

> Experiment first. Measure. Understand. Only then scale.

</div>

---

## What RS4 Lab does today

RS4 Lab is the execution and evidence layer of the Rs4Machine research program. The repository is currently focused on controlled experimentation of AI systems, agent orchestration, latency measurement, and production-oriented validation workflows.

The active work is not a product delivery sprint; it is a measurement-first lab for validating assumptions under controlled conditions. The current emphasis is on:

- benchmarking AI and agent pipelines under repeatable conditions;
- validating end-to-end orchestration under local execution;
- tracking latency, status, and artifact generation per node or stage;
- turning experiments into traceable evidence, not intuition-driven decisions.

The most recent work is concentrated in the `experiments/005-ai-system-improvement` and `experiments/006-cortex-flow` tracks, with a clear move from architecture baseline mapping to multi-agent evaluation and telemetry capture.

---

## Current project status

The repository is in an active research and validation phase.

Current signals from the codebase:

- `experiments/005-ai-system-improvement/001-sofiavoice/` documents the SofiaVoice v2.0 release path, including latency benchmark comparisons and execution reports.
- `experiments/006-cortex-flow/` is the active orchestration experiment. Its v2.0.0 branch includes per-agent metrics, integration tests, and consolidated validation artifacts.
- The repo structure is organized around experiment folders, not a monolithic application layout.
- Telemetry is captured as JSON metrics and Markdown reports rather than as a single global processing layer.

A repo-level `Metrics/` directory is not currently the primary organizational structure; the recent telemetry is stored within the experiment folders themselves, especially under `experiments/006-cortex-flow/v2.0.0/`.

---

## Repository structure

```text
.
├── LICENSE
├── README.md
├── README.pt-BR.md
├── .gitignore
├── experiments/
│   ├── 001-architeture-first/
│   ├── 002-pipeline-validation/
│   ├── 003-Agent-Assisted/
│   ├── 004-local-triage-automation/
│   ├── 005-ai-system-improvement/
│   │   └── 001-sofiavoice/
│   ├── 006-cortex-flow/
│   │   ├── README.md
│   │   ├── v1.0.0/
│   │   └── v2.0.0/
│   │       ├── 00-metrics_setup_v2.json
│   │       ├── 01-metrics_chroma_v2.json
│   │       ├── ...
│   │       ├── 11-metrics_integracao_v2.json
│   │       ├── 12-metrics_agente7_evaluator_v2.json
│   │       ├── 13-metrics_triagem_v2.json
│   │       ├── implementation-tests-agents/
│   │       └── drafts/
│   └── 007-commerce-pipeline/
└── docs/ (as needed by the experiments)
```

### Main experiment tracks

- `experiments/001-architeture-first/` — baseline architecture and bottleneck mapping.
- `experiments/002-pipeline-validation/` — pipeline overview and validation notes.
- `experiments/003-Agent-Assisted/` — assisted-agent experiments and statistical validation.
- `experiments/004-local-triage-automation/` — triage automation studies.
- `experiments/005-ai-system-improvement/001-sofiavoice/` — SofiaVoice benchmarking, release evidence, and latency comparisons.
- `experiments/006-cortex-flow/` — current multi-agent orchestration experiment with telemetry-rich validation.
- `experiments/007-commerce-pipeline/` — commerce-oriented pipeline experiments and result artifacts.

---

## Metrics and validation suite implemented

The repo currently uses a layered measurement model based on artifacts and evidence, not only execution scripts.

### Measurement model

- per-node metrics JSON snapshots;
- end-to-end integration reports in Markdown;
- compiled validation of modified Python files;
- agent execution tracking with timestamps and status fields;
- route-level verification for orchestration flows.

### Current telemetry pattern

The newest experiment (`experiments/006-cortex-flow/v2.0.0/`) follows this pattern:

- `00-metrics_setup_v2.json` to `13-metrics_triagem_v2.json` — per-stage metrics for the orchestration flow;
- `11-metrics_integracao_v2.json` — consolidated end-to-end integration result;
- `implementation-tests-agents/` — Python scripts that exercise agent nodes and the full pipeline;
- `drafts/` — evaluation, offer, refined synthesis, and template drafts produced during the run;
- `Result_*.md` and related artifacts in other experiments for execution reports.

This setup provides traceability for:

- node execution status;
- latency per stage;
- total pipeline timing;
- artifact existence and content validation;
- regression and comparison between experiment versions.

---

## Recent test and execution structure

The latest Cortex Flow work includes a suite of validation scripts under:

```text
experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/
├── 01-test_nodo0.py
├── 02-test_nodo1.py
├── 03-test_nodo_redator.py
├── 04-test_nodo_techscout.py
├── 05-test_nodo_critico.py
├── 06-test_nodo_sintetizador.py
├── 07-test_nodo_builder.py
├── 08-test_nodo_builder.py
├── 09-test_esteira_completa.py
```

These scripts validate:

- node-level execution;
- routing sequence and state transitions;
- syntax and compile-time validation;
- integration of the full pipeline;
- generation and persistence of metrics artifacts for later comparison.

---

## How to run the test scripts

Use the repository root as the working directory.

### 1) Run a single validation script

```bash
python experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/09-test_esteira_completa.py
```

This executes the full integrated route validation, collects JSON metrics, and writes the consolidated integration report.

### 2) Run a route-specific variant

```bash
python experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/09-test_esteira_completa.py A
python experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/09-test_esteira_completa.py B
```

The script accepts the route selection in the validation workflow and merges the results into the same metrics file without changing the core execution logic.

### 3) Validate syntax and basic project health

```bash
python -m py_compile \
  experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/01-test_nodo0.py \
  experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/02-test_nodo1.py
```

### 4) Use pytest when the target folder contains unit-style checks

```bash
pytest experiments/003-Agent-Assisted/
```

This repository is primarily organized around experiment scripts and evidence output, so the dominant execution pattern is direct Python invocation of the validation files rather than a single global runner.

---

## Execution standards

RS4 Lab follows a strict experimental discipline:

- verify an assumption before scaling it;
- keep evidence close to the run;
- prefer reproducible metrics over qualitative claims;
- keep test artifacts auditable;
- maintain human accountability for critical decisions.

---

## Status

The project is in an active experimental phase focused on measurement, orchestration validation, and agent-evidence generation.

The current repository state reflects a transition from architecture documentation to metric-driven experimentation, with the most mature recent material under:

- `experiments/005-ai-system-improvement/001-sofiavoice/`
- `experiments/006-cortex-flow/v2.0.0/`

---

## Author

**Raphael Mendes**

**AI Systems Engineer · Rs4Machine**

> Technology can expand our capability. It should not replace our responsibility.
