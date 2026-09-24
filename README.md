<div align="center">
<img src="https://raw.githubusercontent.com/raphaelmendes-dev/sofiavoice/main/assets/Rs4Machine.png" alt="Rs4Machine Logo" width="200" />


# 🧪 RS4 Lab

**Rs4Machine's Experimental Lab**

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-Under%20construction-yellow)

[🇧🇷 Português](README.pt-BR.md) · **🇺🇸 English (this file)**

> Experiment first. Measure. Understand. Only then scale.

</div>

---

## 📑 Table of Contents

- [What is RS4 Lab](#-what-is-rs4-lab)
- [Principles](#-principles)
- [Current Structure](#️-current-structure)
- [Lab Experiments Index](#-lab-experiments-index)
- [Working Model](#-working-model)
- [Verification Layers](#-verification-layers)
- [About Agents](#-about-agents)
- [Capital Side (Future)](#-capital-side-future)
- [Status](#-status)
- [Author](#-author)

---

## 🎯 What is RS4 Lab

RS4 Lab is a space for controlled experimentation in intelligent systems, AI agents, and software engineering.

It's not a startup.
It's not an agent playground.
It's a lab with a method.

Here we log hypotheses, run small experiments, collect evidence, and decide based on data — always keeping a human as the final decision-maker.

---

## 🧭 Principles

1. A human remains the final decision-maker and is accountable for the outcome.
2. Every autonomous system must have a clear, fast, and documented way to be interrupted.
3. Critical decisions are never fully delegated to agents.
4. Understanding and the ability to debug can never be outsourced.
5. Contingency plans are part of the method, not optional.
6. The greater a task's potential impact, the greater the level of supervision and restriction must be.

---

## 🏗️ Current Structure

```
experiments/
├── 001-architeture-first
├── 002-pipeline-validation
├── 003-Agent-Assisted
├── 004-local-triage-automation
├── 005-ai-system-improvement
│   └── 001-sofiavoice
└── 006-cortex-flow

metrics/
docs/
```

Each experiment has its own documentation, evidence, and metrics as needed.

---

## 🧪 Lab Experiments Index

High-level index of the active laboratory experiments. Each entry links only to the **main README** of the experiment; individual test runs and metrics are documented inside each experiment folder.

| # | Experiment | Status | Main README |
|---|---|---|---|
| 004 | Local Triage Automation | Under experimentation | [Read experiment](./experiments/004-local-triage-automation/experiment-001/README.md) |
| 005 | AI System Improvement — SofiaVoice v2.0 | Released | [Read experiment](./experiments/005-ai-system-improvement/001-sofiavoice/README.md) |
| 006 | Cortex Flow | Under experimentation | [Read experiment](./experiments/006-cortex-flow/README.md) |

---

## 🔁 Working Model

```mermaid
flowchart TD
    A["RS4 (method)"] --> B["Raphael — decision"]
    B --> C["Scoped task"]
    C --> D["Agent — execution (within scope)"]
    D --> E["Verification (Tester 1 to 4)"]
    E --> F["Evidence → Results → Data"]
    F --> G["Analysis → Learning"]
    G --> H["Next decision"]
    H --> B
```

---

## ✅ Verification Layers

| Tester | Role |
|---|---|
| **Tester 1** | Machine (automated tests) |
| **Tester 2** | Verifier agent |
| **Tester 3** | Measurement (metrics) |
| **Tester 4** | Human (0–3 understanding scale) |

---

## 🤖 About Agents

Agents execute within their delegated scope.

**They can:**

- Write, review, and test code
- Generate documentation
- Collect and organize data
- Produce proposals

**They cannot:**

- Set the project's direction
- Approve critical changes
- Replace human understanding
- Push relevant changes to production on their own

---

## 💰 Capital Side (Future)

The technical lab and the operational (capital) side move together, but at different paces.

While the Lab validates methods and quality, the capital side will explore ways to generate revenue at near-zero cost (affiliates, templates, automations, etc.).

Capital exists to provide stability and the conditions to keep the work going. It is not the primary goal.

---

## 🚧 Status

**Under construction.**

Experiments started in August 2026. The lab is currently moving from initial documentation to comparative experiments with metrics.

---

## 👤 Author

**Raphael Mendes**
Rs4Machine | AI Research Lab

> *"Technology can expand our capability. It should not replace our responsibility."*
