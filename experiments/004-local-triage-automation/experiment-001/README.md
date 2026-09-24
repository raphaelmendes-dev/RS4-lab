# Experiment-001 — Local Triage Automation

**Project:** RS4-Lab
**Experimental line:** 004 — Local Triage Automation
**Status:** Specification under development
**Date:** 26/08/2026

**Artifacts:**

| Artifact | Description |
|---|---|
| [baseline.md](baseline.md) | Manual (human) triage baseline — reference values for comparison |
| [notes.md](notes.md) | Run notes — model batches (Llama 3.2 3B and Qwen 2.5 3B) |
| [metrics.json](metrics.json) | Measured data for baseline and model batches |

---

## 1. Objective

Investigate whether a local language model, executed through Ollama and orchestrated by Python, can assist in the triage of local documents, reducing the time required to understand each file while keeping the decision and the authorization for file movement exclusively under human control.

The experiment does not intend to replace human decision-making.

The system shall:

1. locate the files;
2. read and extract their content;
3. use the local model to interpret the content;
4. present a brief summary to the operator;
5. wait for the human decision;
6. execute only the authorized action.

---

## 2. Hypothesis

A system composed of Python + Ollama + a local language model can assist in the triage of unstructured files, providing summaries that are sufficiently useful for the human operator to make a decision more quickly, without removing human control over the final destination of the files.

---

## 3. Authority principle

The AI may:

* read;
* interpret;
* summarize;
* present information.

The AI **may not decide the destination of the file**.

The decision belongs exclusively to the human operator.

Flow:

```text
File
   ↓
Python
   ↓
Extraction
   ↓
Ollama + local model
   ↓
Summary
   ↓
Raphael
   ↓
S / N / Q
   ↓
Python executes the authorized action
```

---

## 4. Containment principle

No file will be permanently deleted by the system.

The possible actions are:

### S — Approve

Move the file to:

`_APROVADOS`

### N — Do not approve

Move the file to:

`_LIXEIRA_DESKTOP`

The `_LIXEIRA_DESKTOP` folder works as a contingency area for later manual review or cleanup.

### Q — Interrupt

Interrupt the experiment.

The currently displayed file must not be moved.

The system must have a clear way to interrupt during execution.

---

## 5. Workspace

The files used in the experiment will remain outside the Git repository.

Operational structure:

```text
Área de Trabalho/
│
├── _TRIAGEM_RAIZ/
├── _APROVADOS/
└── _LIXEIRA_DESKTOP/
```

Python must look for the files inside:

`_TRIAGEM_RAIZ`

Approved files will be sent to:

`_APROVADOS`

Not-approved files will be sent to:

`_LIXEIRA_DESKTOP`

---

## 6. File types

The following will be considered for the first pilot:

* `.doc`
* `.docx`
* `.md`
* `.txt`

PDF will not be part of the first pilot.

The inclusion of other formats may be investigated later in another experiment or controlled extension.

---

## 7. Operational flow

### Stage 1 — Scan

Python locates the existing files in `_TRIAGEM_RAIZ`.

No file must be moved in this stage.

### Stage 2 — Read and extraction

The system obtains the content necessary for analysis.

The extraction strategy must respect the file type.

### Stage 3 — Interpretation

The extracted content is sent to Ollama for analysis by the local model.

The objective is to obtain a short synthesis containing the document's central concepts.

### Stage 4 — Presentation

The terminal presents to the operator:

* file name;
* produced summary;
* file location;
* decision options.

Example:

```text
File: exemplo.docx

Summary:
Document related to an automation project
using AI and n8n.

[S] Approve
[N] Do not approve
[Q] Interrupt
```

### Stage 5 — Human decision

Raphael chooses:

```text
S
N
Q
```

The model does not make this choice.

### Stage 6 — Execution

After the decision:

```text
S → _APROVADOS
N → _LIXEIRA_DESKTOP
Q → interrupt
```

---

## 8. Metrics

The experiment will initially use four main metrics.

### M1 — Time

Record the time of each execution.

Two different times will be recorded.

#### Machine processing time

Definition:

> From the start of file reading until the summary is ready to be presented to the human.

This time will be measured automatically by Python.

#### Human decision time

Definition:

> From the moment the summary is presented to the operator until the `S`, `N`, or `Q` response.

It must also be recorded automatically.

---

### M2 — Summary quality

Human scale from 0 to 3:

| Score | Meaning              |
| ----- | -------------------- |
| 0     | Incorrect            |
| 1     | Not very useful      |
| 2     | Adequate             |
| 3     | Accurate and sufficient |

The evaluation will be performed by the human operator.

Summary quality does not represent the S/N decision.

They are different assessments.

---

### M3 — Processed volume

Record:

* total quantity of processed files;
* quantity of approved;
* quantity of not approved;
* quantity of interruptions.

---

### M4 — Errors

Record occurrences such as:

* read error;
* extraction error;
* model error;
* incompatible file;
* movement failure;
* interruption;
* any other relevant error.

---

## 9. Evidence recording

The metrics produced during execution must be stored in:

[`metrics.json`](metrics.json)

The file must record the actual execution data to allow later analysis.

The detailed JSON format will be defined before implementation.

---

## 10. Baseline

Before using the AI, a manual triage was performed.

Baseline result:

* processed files: 6;
* approved: 4;
* not approved: 2;
* total time: 183 seconds;
* average time: 30.5 seconds per file.

The real sample consisted of:

* 3 Word files initially;
* 1 Markdown file;
* 1 TXT file;
* 1 Word file.

The baseline represents the reference condition for comparison with AI-assisted triage.

The result must not be treated as a target nor as a conclusion about efficiency.

---

## 11. Comparison

The comparison must consider:

```text
MANUAL BASELINE

read
   ↓
comprehension
   ↓
decision

vs.

ASSISTED TRIAGE

read / extraction
   ↓
Ollama
   ↓
summary
   ↓
human decision
```

The analysis must consider separately:

* machine processing time;
* human decision time;
* total time;
* summary quality;
* processed volume;
* errors.

---

## 12. Control criterion

The experiment will not be considered successful merely because the system works technically.

The assessment must consider simultaneously:

1. summary usefulness;
2. time;
3. absence of inadvertent data loss;
4. maintenance of human decision;
5. possibility of interruption;
6. correct operation of authorized movement.

The experiment must produce enough evidence to decide whether the approach deserves a next stage.

---

## 13. Scope of the first pilot

The first pilot will be small.

Objectives:

* verify that the files can be processed;
* verify content extraction;
* verify communication with Ollama;
* verify summary quality;
* verify the S/N/Q interface;
* verify controlled movement;
* verify metrics collection;
* verify safe interruption.

There will be no attempt to scale the system before analyzing the pilot results.

---

## 14. Out of scope

Not part of this experiment:

* automatic file deletion;
* automatic approval or discard decision;
* PDF processing;
* Obsidian integration;
* NotebookLM integration;
* large-scale automation;
* building a complete platform;
* remote execution;
* sending documents to external APIs.

---

## 15. State

**Baseline:** completed.

**Specification:** under development.

**Implementation:** not started.

**Pilot test:** not started.

**System metrics:** not yet collected.

---

## 16. Next step

Before implementation, review and approve this specification.

After approval:

1. define the local model;
2. define the extraction strategy for the accepted formats;
3. define the final `metrics.json` format;
4. implement the first version;
5. run the pilot;
6. verify the results;
7. record the evidence;
8. compare with the baseline.

**Experiment rule:**

> First define what the system must do.
> Then implement.
> Then measure.
> Then interpret.