<div align="center">
<img src="https://raw.githubusercontent.com/raphaelmendes-dev/sofiavoice/main/assets/Rs4Machine.png" alt="Rs4Machine Logo" width="200" />

# 🧪 RS4 Lab

**AI Systems Engineering Laboratory · Rs4Machine**

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
- [Status](#-status)
- [Author](#-author)

---

## 🎯 What is RS4 Lab

**RS4 Lab** is the experimental laboratory of **Rs4Machine**. It is a controlled environment for testing intelligent systems, AI agents, and production-oriented engineering methods under real constraints.

This is not a startup sprint. It is not an unconstrained agent playground. It is a lab with a method.

The goal is to validate assumptions with evidence, measure real behavior, and keep the human accountable for critical decisions.

---

## 🧭 Principles

> Experiment first. Measure. Understand. Only then scale.

- A human remains the final decision-maker on every critical call.
- Every autonomous system needs a clear, fast way to be interrupted.
- Decisions driven by metrics, not intuition.

1. A human remains the final decision-maker and is accountable for the outcome.
2. Every autonomous system must have a clear, fast, and documented way to be interrupted.
3. Critical decisions are never fully delegated to agents.
4. Understanding and the ability to debug can never be outsourced.
5. Contingency plans are part of the method, not optional.
6. The greater a task's potential impact, the greater the level of supervision and restriction must be.

---

## 🏗️ Current Structure

```text
experiments/
├── 001-architeture-first
├── 002-pipeline-validation
├── 003-agent-assisted
├── 004-local-triage-automation
├── 005-ai-system-improvement
│   └── 001-sofiavoice
├── 006-cortex-flow
│
metrics/
docs/
```

Each experiment documents its own hypothesis, evidence, and evaluation criteria as needed.

---

## 🧪 Lab Experiments Index

High-level index of the active laboratory experiments. Each entry links only to the main README of the experiment; detailed metrics and run-level notes remain inside each experiment folder.

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

## 🚧 Status

**Under construction.**

Experiments started in August 2026. The lab is currently moving from initial documentation to comparative experiments with metrics and traceable evidence.

---

## 👤 Author

**Raphael Mendes**

**AI Systems Engineer & Founder · Rs4Machine**

> "Technology can expand our capability. It should not replace our responsibility."

