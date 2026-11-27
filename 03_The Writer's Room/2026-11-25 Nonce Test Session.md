---
type: session
status: archived
tags: [ontology/harm, test, nonce, structure, traversal]
aliases: [2026-11-25 Nonce Test Session]
created: 2026-11-25
session_date: 2026-11-25
participants: [Author, "Copilot assistant (model not recorded in transcript)"]
source: "Copilot chat, 2026-11-25 (continuing from 'Setup for Harm Ontology v0.03.01 design'); transcript saved in copilot/copilot-conversations/ under the same chat name"
workstream: "[[Handoff - Harm Ontology]]"
harvested_through: "end of session, 2026-11-25"
continued_in:
topics: [nonce-test, structured-prompt, relations, labels, control, graph-traversal, SPARQL, rdflib, expert-judgment]
---

# 2026-11-25 Nonce Test Session

## Summary
- Ran a series of controlled tests of how a language model maps text onto `Interdisciplinary Harm Ontology v1.ttl`. Built coded-name (nonce) files, a flat-hierarchy file, and two control files, then ran structured-prompt and traversal conditions via isolated subagents.
- Findings so far: matches come mostly from definitions (initial test); the hierarchy changed one answer in one run (relational test); the structured prompt is more conservative but does not change core matches; property checks only work when value individuals carry labels; the narrative changes structured decisions (baseline against C2).
- Rdflib traversal was first run as a verification tool only. A proper traversal condition (stage 1 candidates, stage 2 fixed queries and decisions) was run on five texts. It shows two inconsistencies (same node and property read differently across runs) and depends on a candidate selection I made.
- Expert judgments are still missing, so no test yet measures correctness.

## Decisions made
- No decisions recorded in [[Decisions_Log]] this session. The nonce tests are proposed, not settled.
- Test records written to `02_Ideas Topics Concepts/Harm Ontology/ontology/tests/nonce/`:
  - [[Nonce Test - Initial]]
  - [[Nonce Test - Relational]]
  - [[Nonce Test - Structured Prompt]]
  - [[Nonce Test - Structured Prompt - Baseline and Control]]
  - [[Nonce Test - Graph Queries (for review)]]
  - [[Nonce Test - Graph Traversal]]

## How the thinking moved
- The first nonce test was meant to show whether matches come from the ontology or from training. Building the files showed a missing condition, so the design became a 2×2 (names and narrative).
- The relational test was meant to show whether the hierarchy matters. Writing the texts showed most parent definitions repeat their children's wording, so parent-only texts were hard to write.
- The structured prompt was meant to make the model use structure. It did not query anything: the model read the file as text and simulated the traversal. Its property step returned "unknown" almost everywhere in NONCE B, because the value individuals had no labels. A SPARQL check confirmed the cause (6 of 72 values labelled in NONCE B; 72 of 72 in the baseline).
- Control C was found to be flawed: the build had removed value labels. CONTROL C2 was built to keep names and labels, with definitions only.
- The baseline against C2 comparison showed the narrative changes structured decisions. This reversed the earlier conclusion that definitions carry most of the matching, which the NONCE B runs could not test.
- The author pointed out the traversal condition had not been tested. Our structured runs had no query tool. The author's point was that structure has value only when queried, and that meaning depends on relations in context. Accepted. The traversal condition was then built with fixed queries.
- Provenance (whether a quoted definition sits on the node the model names) was discussed. It is a cheap validity check, but it does not show usefulness, and it is not an expert judgment.
- The author asked for a table of HarmDeterminations with IRIs and parent or child positions. The table was built, with blank columns for expert verdicts and provenance. Some quotes in the table came from short texts other than the poem (T1, T2, T3, control). That was intended, and the note now labels each text.
- Cost of the session was high (many subagent runs). Author asked for a close-out.

## Concepts introduced
- **Coded-name (nonce) file**: an ontology file with class and property names replaced by codes, kept with a key kept out of the test. → promote to idea note? (n; test method, recorded in the test note)
- **Two-stage traversal**: stage 1 proposes candidate classes from definitions; stage 2 runs fixed queries on those candidates and the model decides from query rows only. → promote? (y; a method worth a bookmark)
- **Provenance check**: whether a quoted definition sits on the node the model names. → promote? (n)

## Open questions
- Which texts and candidate sets are the test set? The candidate set was chosen by hand, so stage 2 could not assess some nodes.
- Expert judgments: who provides them, and on what criteria? Without them the tests measure agreement, not correctness.
- How should `UnperceivedObjective` be read (perceived loss versus objective harm)? The runs read it differently. It should be settled as a design decision.
- Why did the same node and property (InjuriaSineDamnoHarm, `UnperceivedObjective`) give different verdicts across runs? Is this variance or a prompt effect?
- Is the baseline's advantage over C2 (if any) due to narrative, labels, or run variance? One run per cell cannot separate these.

## Original wording
> "i thought the latest tests were to actually use graph traversal to see if we could generate additional value if the ontological relations were actually queried"
- **Attribution:** Author

> "this seems to contribute substantial value and understanding whether the model is being correctly and usefully traversed. would you agree?"
- **Attribution:** Author

> "some of the text quoted is not coming from the poem Whitey on the Moon that I provided. are you running this test with some residual text from earlier examples"
- **Attribution:** Author

## External references
| Reference | Used for | Status |
|---|---|---|
| Interdisciplinary Harm Ontology v1.0.3 (the source file) | Basis of all test files | Read by the vault; not externally verified |
| rdflib (SPARQL 1.1, in the `harm-ontology` conda environment) | Fixed queries and checks | Used and run; rdflib performs no OWL inference |

## Artifacts touched
- Created (in `tests/nonce/`): nonce files A and B, their KEY and build report, the flat variant (NONCE B FLAT), CONTROL C, CONTROL C2, and the six test notes listed under Decisions made.
- Renamed: the initial test note, to `Nonce Test - Initial.md` (old names kept as aliases).
- Build scripts and stage-2 query results kept in `%TEMP%\nonce_build\`, outside the vault.
- Not edited: the source `Interdisciplinary Harm Ontology v1.ttl`, `Decisions_Log`, and the ledger.

## Follow-ups
- [ ] Author: provide expert judgments (correct class, preferred class, and any unmapped harms) for the five texts.
- [ ] Run the provenance check on the quoted definitions in the traversal table.
- [ ] Run the model-only condition on the same candidate set, so the comparison is like for like.
- [ ] Decide how `UnperceivedObjective` is read, and record it as a design decision.
- [ ] Repeat the structured and traversal cells two or three times to measure variance.
- [ ] Decide whether the nonce build script belongs in `ontology/scripts/`.

## Closing checklist
A session = one Copilot chat, from its first message to this checklist. Pauses don't end it.
- [x] Harvest new ideas (incremental, from `harvested_through`)
- [x] Update `harvested_through`
- [x] Add anything after the last update to this note
- [x] Rewrite the workstream's Handoff note (forward-facing, short)
- [x] Set `status: archived`; `continued_in` set at the next session close
- [ ] Rename the chat in Copilot history: "[CLOSED] Nonce test session → see session note" (author action)
- [ ] Start a new chat with the Handoff note attached. Don't reopen this one; read its transcript selectively if needed.

## Related
- [[Handoff - Harm Ontology]]
- [[Nonce Test - Graph Traversal]]
- [[Nonce Test - Structured Prompt - Baseline and Control]]
- [[2026-11-24 Harm Ontology Common Schema and DUL Alignment Session]]
