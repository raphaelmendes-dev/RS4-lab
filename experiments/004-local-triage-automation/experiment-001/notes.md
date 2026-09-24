# Experiment-004 — Local Triage Automation

## Notes

### Reference

The human baseline used in this experiment is recorded separately in:

`baseline.md`

The sample used in the model runs is the same one used in the baseline, allowing later comparison under the same document set.

---

# 27/08/2026 — First batch

## Model

`llama3.2:3b`

First experimental batch with the six files used in the human baseline.

| File                     | Read time | Total time | Score |
| ------------------------ | ---------: | ----------: | ----: |
| etapa1.docx              |    89.05 s |    105.57 s |     2 |
| INT_ia.docx              |    54.03 s |     63.50 s |     2 |
| makedown.md              |    61.53 s |    173.48 s |     0 |
| proposta_maltbot.docx    |     7.20 s |     15.70 s |     2 |
| resultado.txt            |     9.58 s |     22.18 s |     2 |
| Como estruturar... .docx |    17.72 s |     32.60 s |     2 |

### Result

**Total batch time:** 413.03 s

**Average time per file:** 68.84 s

**Human baseline:** 30.5 s/file

Summary quality:

* 5 files scored 2.
* 1 file scored 0.
* None scored 3.

### Observations

* The model produced summaries considered adequate for 5 of the 6 files.
* The file `makedown.md` showed a significant failure to adhere to the instruction.
* The document was approximately 300 lines, and the model produced a "summary" of approximately 202 lines.
* In that case, the model did not adequately present the requested central points.
* There was large variation in the total time across files.
* The model responded in Portuguese.
* The model has no direct access to the system's files; the content had to be provided to the model.
* In a prior exploratory test, when asked to access `baseline.md` without receiving its content, it correctly reported that it had no access to the file.
* In an exploratory self-assessment test, it produced a narrative about its own performance. That response was not considered a performance metric.

### Assessment

The first batch indicates that the model produced useful summaries in part of the cases, but showed a significant failure to adhere to the requested format in one of the files.

The results do not allow concluding that the model is suitable or unsuitable for triage automation.

---

# 27/08/2026 — Second batch

## Model

`qwen2.5:3b`

Second experimental batch using the same six files, the same task, and the same protocol used in the previous batch.

| File                     | Read time | Total time | Score |
| ------------------------ | ---------: | ----------: | ----: |
| etapa1.docx              |    16.75 s |     20.71 s |     3 |
| INT_ia.docx              |    45.99 s |     57.81 s |     3 |
| makedown.md              |    39.46 s |    170.09 s |     1 |
| proposta_maltbot.docx    |     7.80 s |     12.90 s |     3 |
| resultado.txt            |     8.54 s |     19.56 s |     3 |
| Como estruturar... .docx |    17.86 s |     28.95 s |     3 |

### Result

**Total batch time:** 310.02 s

**Average time per file:** 51.67 s

**Human baseline:** 30.5 s/file

Summary quality:

* 5 files scored 3.
* 1 file scored 1.
* None scored 0 or 2.

**Average quality:** 2.67/3

### Observations

* The model produced responses considered adequate for 5 of the 6 files.
* `etapa1.docx` scored 3.
* `INT_ia.docx` scored 3.
* `proposta_maltbot.docx` scored 3. The summary was considered clear, captured the essence of the document, and used 3 lines.
* `resultado.txt` scored 3.
* `Como estruturar... .docx` scored 3.
* The file `makedown.md` again showed difficulty producing a simple explanation of a large document.
* In `makedown.md`, the model did not respect the line limit defined in the protocol.
* The `makedown.md` file scored 1.
* The `makedown.md` read time was lower than the one observed with Llama 3.2 3B, but the total time remained high.
* The model responded in Portuguese.

### Assessment

The second batch showed, in this sample, a lower average time than the one observed in the first batch with the Llama 3.2 3B, and higher quality scores in the human evaluation.

However, the `makedown.md` file again showed difficulty adhering to the requested format, although with a better score than the one observed with the Llama 3.2 3B.

The results of this batch do not allow concluding that the Qwen 2.5 3B is generally superior to the Llama 3.2 3B, or that it is suitable for triage automation.

The data must be compared formally using the same protocol and the same metrics.

---

# Methodological note

The two batches were performed using:

* the same six files;
* the same task;
* the same protocol;
* human evaluation of quality;
* separation between read time and total time.

The objective of this stage is to produce a first comparable observation between the models.

The time measurements of this phase were performed manually.

Automated measurement will be implemented later, after closing and validating the experiment metrics.

---

# Next steps

1. Finalize the `metrics.json` format.
2. Record the baseline, Llama 3.2 3B, and Qwen 2.5 3B data in `metrics.json`.
3. Check the calculations and the consistency of the data.
4. Review the files before versioning.
5. Run `git status`.
6. Version and push the changes to GitHub.
7. Later, implement automated measurement in Python.