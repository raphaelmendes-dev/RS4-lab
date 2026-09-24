# Baseline — Manual Triage

## Objective

Record how a file-triage task is executed without AI assistance, creating a reference for comparison with the Agent-Assisted experiment.

The baseline represents the current human working condition.

---

## Rule

The task was executed without an agent, LLM, or decision automation.

The human opened, read, and evaluated each file individually and decided whether it should be:

* approved;
* discarded.

No file was permanently deleted during the baseline.

Approved files were moved to:

`_APROVADOS`

Discarded files were moved to:

`_LIXEIRA_DESKTOP`

---

## Sample

Planned quantity:

**5 files**

Quantity actually executed:

**6 files**

The sample consisted of real files from the collection being triaged.

Types found in the sample:

* Word;
* Markdown;
* TXT.

The difference between the planned and executed quantity was recorded as part of the experiment, without repeating the measurement.

---

## Procedure

For each file:

1. Record the start of the analysis.
2. Open and read the content necessary to understand the file.
3. Decide whether the file would be approved or discarded.
4. Record the time spent on the analysis.
5. Record the decision.
6. Move the file to the corresponding destination.
7. Record relevant observations.

---

## Observed result

### File 1

**File:** `etapa1..doc/.docx`
**Time:** 30 s
**Decision:** S — Approved
**Destination:** `_APROVADOS`
**Content/observation:** WhatsApp bot with n8n.

### File 2

**File:** `INT_ia.doc/.docx`
**Time:** 54 s
**Decision:** S — Approved
**Destination:** `_APROVADOS`
**Content/observation:** MetaPrompt + strategy for a technical profile.

### File 3

**File:** `makedown.md`
**Time:** 19 s
**Decision:** S — Approved
**Destination:** `_APROVADOS`
**Content/observation:** UNIVESP university simulation project on AI, referring to the first semester.

### File 4

**File:** `proposta_maltbot .doc/.docx`
**Time:** 13 s
**Decision:** N — Not approved
**Destination:** `_LIXEIRA_DESKTOP`
**Content/observation:** AI + n8n chatbot project related to freelance work.

### File 5

**File:** `resultado.txt`
**Time:** 24 s
**Decision:** N — Not approved
**Destination:** `_LIXEIRA_DESKTOP`
**Content/observation:** Possible free tools.

### File 6

**File:** `Como estruturar... ..doc/.docx`
**Time:** 43 s
**Decision:** S — Approved
**Destination:** `_APROVADOS`
**Content/observation:** Document related to the question "why multiple templates?".

---

## Consolidated data

| Metric                  | Result |
| ----------------------- | ------: |
| Planned files           |       5 |
| Processed files         |       6 |
| Approved                |       4 |
| Not approved            |       2 |
| Total time              |   183 s |
| Total time              | 3 min 03 s |
| Average time per file   | 30.5 s  |

### Distribution

**Approved:** 4 of 6 — 66.7%

**Not approved:** 2 of 6 — 33.3%

---

## Observation on time

The analysis time varied between:

**13 s and 54 s per file.**

The variation indicates that the triage effort was not uniform across documents.

The file `INT_ia..doc/.docx` presented the longest analysis time, at **54 seconds**.

The file `proposta_maltbot..doc/.docx` presented the shortest analysis time, at **13 seconds**.

This variation will be considered later in the comparison with AI-assisted triage.

---

## Baseline metrics

### 1. Time per file

Elapsed time during the human analysis of each file.

Observed result:

**30.5 s/file on average**

### 2. Total time

Time required to complete the sample analysis:

**183 seconds / 3 min 03 s**

### 3. Processed volume

**6 files**

### 4. Decision distribution

* Approved: **4**
* Not approved: **2**

### 5. Errors or difficulties

No technical error or movement failure was recorded during the baseline execution.

---

## File control

The six files were effectively moved after the human decision.

Destination of approved files:

`_APROVADOS`

Destination of not-approved files:

`_LIXEIRA_DESKTOP`

No file was permanently deleted.

---

## Interpretation

The baseline establishes an initial reference for manual triage.

In the observed condition, Raphael took on average **30.5 seconds per file** to analyze and decide on the six-file sample.

This result does not represent a target nor a conclusion about efficiency.

It will be used later for comparison with AI-assisted triage.

The human decision remains the experiment's control reference.

---

## Question for the next stage

> Can the use of a local model reduce the time required to understand and triage files, while keeping the decision and the authorization for file movement exclusively under human control?

---

## Status

**COMPLETED — BASELINE EXECUTED**

Next step:

**Define the operational specification of Experiment-001 of Local Triage Automation before implementation.**