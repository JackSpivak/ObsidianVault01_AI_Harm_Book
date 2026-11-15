---
fileClass: Idea
type: idea
status: seed
bookmark: HO-002
canonical_id: ho-002-ontology-stress-test-suite
territory: new
tags: [ontology/harm, ontology/testing]
aliases: [HO-002, Ontology Stress-Test Suite, Harm Ontology Test Cases]
created: 2026-11-14
filed: 2026-11-14
---

# HO-002 — Ontology Stress-Test Suite

Index: [[_Harm Ontology Bookmark Index]] · Top-level

## Why this is distinct
- It's the one place where the ontology is tested against hard cases. In the redesign session, Claude repeatedly *claimed* that the new structure blocks certain traps (the horizon trap, offsetting, relativism). **None of those claims has been demonstrated yet.** This note turns them into tests that can pass or fail.

## Anticipated direction
- Each test case is modelled with the current layers (Factor → CausalRole → Effect → Assessment → Perspective → Divergence). The result is recorded as **Pass / Partial / Fail / Untested**, and every failure links to the design change it caused.
- Over time: express each case as RDF instances, with SHACL shapes acting as automated checks (a regression suite, run again after each design change).
- Feed in the adversarial councils and stress tests (philosopher, Classical Council, and others from [[Claude_philosophers]]).

## Conceptual territory
- New. It applies the idea of a software test suite to a conceptual model: each case is a fixed test, and a design change must not break earlier passes.

## Summary
- A design claim counts only once a case shows it. The suite records which layers each case exercises, which trap it probes, how the model is expected to represent it, and what actually happened.

## Test format
For each case:
- **Case:** a short description, with its source.
- **Exercises:** the layers and properties involved.
- **Trap probed:** the failure the case is designed to catch.
- **Expected representation:** how the model should handle it.
- **Result:** Pass / Partial / Fail / Untested, plus the date and any design change it led to.

## Test cases (initial list, all Untested)

| # | Case | Exercises | Trap probed |
|---|---|---|---|
| T01 | **Sai Weng's horse** (塞翁失马) | horizon, framing, chainStatus, Divergence | Horizon trap: whoever sets the horizon sets the verdict |
| T02 | **The shooting chain** | Factor, CausalRole, phenomenality | Fixed cause/effect classes; "causes can't be phenomena" |
| T03 | **Covert AI profiling, unnoticed** | standards, verdicts, Divergence (Normative) | v1 contradiction: one event both harm and not-harm |
| T04 | **Shadowban** | observability (observableBy / hiddenFrom), Undisclosed | Fixed phenomenality; visibility that depends on the observer |
| T05 | **Posthumous AI defamation** | experienceability, patient, worldview standards | Unfelt harm treated as no harm |
| T06 | **Missed diagnosis** (an omission) | Omission factor, felt effect | "Nothing happened, so no cause" |
| T07 | **Rubber-stamping** (002.II.a) | AlgorithmicAssessment → Judgment, captured assent | Authority on paper mistaken for authority actually exercised |
| T08 | ***TransUnion v. Ramirez*** (risk, standing) | Judgment, modality, horizon | Risk excluded as a harm (case details unverified) |
| T09 | **"Net benefit to society"** | scope, forPatient, Integration | Offsetting trap: a net verdict hides a harm at one link |
| T10 | **Harmless trespass** | rights-based standard judging the act; no Effect | Wrong without harm forced into "harm" |
| T11 | **Whistleblower fired → reform** | Effect leadsTo Effect, valence flip | Fixed valence on an effect |
| T12 | **Convenience → dependence → deskilling** | dispositional effect, habituation (HO-001) | Welcomed harm treated as no harm |
| T13 | **Future generations** (non-identity) | patient type, counterfactual standard | Counterfactual test failing for people not yet born |
| T14 | **The household vs. the other families** (Sai Weng, wider frame) | framing, Divergence (Perspectival) | Relativism trap: "true but partial" used to excuse a narrow frame |
| T15 | **Factual error disguised as a perspective** | Divergence (Factual) | "Partial" used to cover "false" |
| T16 | **Absent vs. Unknown** (the neighbours vs. the old man) | missingness statuses | Treating "not considered" as "unknowable" |
| T17 | **[[The Self-Revising Harm Ontology]]** (AI quietly re-weights the ontology) | the model itself as an object of manipulation | Can the model detect changes to its own standards and perspectives? |
| T18 | **Luck vs. agency** (Sai Weng has no perpetrator) | Agent presence in the chain | "Who knows?" applied to deliberately caused harm |
| T19 | **Engineered assembly:** harmless parts, harmful whole (e.g. task decomposition) | CausalAssembly (origin: Engineered, individuallyInnocuous), factor-level vs. assembly-level Divergence | Judging factors one at a time and finding nothing wrong |
| T20 | **Exploited emergent storm:** an accidental alignment of factors that someone then uses | CausalAssembly (origin: Exploited), orchestrator, Unknown members | "Nobody built it, so nobody is answerable" |
| T21 | **Hidden outcome selection** (a variant of T09) | Outcome, Perspective (framing, resolution) | Benefits counted while some effects quietly fall outside the frame |
| T22 | **Hidden attribution:** one convenient factor named as "the cause" ("the user misused it") | Attribution vs. CausalAssembly, Unknown members | Other contributors escape notice |
| T23 | **The butterfly:** a small pivotal factor with a vast unforeseen effect | leverage, criticality, predictabilityHorizon, inclusionCriteria | Excluding by magnitude alone |
| T24 | **Adversarial perturbation at a critical point** (e.g. adversarial examples in ML) | sensitivity as assessed, CausalAssembly (Engineered) | Sensitivity used as a weapon |
| T25 | **Low-and-slow attack** kept below the assessment's sensitivity threshold | Perspective.sensitivity, assembly of sub-threshold factors | Attacking the Perspective itself |
| T26 | **"Our assessment found no harm"** | scopeAdequacy (never Complete), acknowledgedExclusions | A claim of completeness |
| T27 | **Unfinished harm:** a verdict on effects still unfolding | Outcome as a cut, provisional verdict, finality | A provisional verdict treated as final |

## Original wording
> "i would like to add an idea note specifically for stress testing the ontology.  you have mentioned in many cases observing that new structuring prevents certain traps especially with respect to ideas like the chineese farmer parable. I would like to centralize testing of the Ontology against challenging test cases"
- **Attribution:** Author

> "That one rule blocks the ethical trap at the level of the ontology itself."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5). Recorded here as a claim to be tested (T01), not a result.

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references:** the v1 stress tests (philosopher, Classical Council) in the same session; [[Claude_philosophers]] for council rosters; the cases' own sources as listed (legal cases unverified).

## Real-world examples
- See the test cases.

## Why it matters to the book
- The book's claims about harm will rest on this model. A suite of tests that can fail is what separates a framework from a rhetorical device.

## Open questions
- Who runs the tests: the author, Claude, councils, or all three? A test run by the party who designed the model has the self-evaluation problem from [[002 Scalability of Oversight and Control]].
- Should each test case get its own note once it's been run?
- Should a case be added for each verdict value (Mixed, Neutral, Contested)?

## Related
- [[HO-000 Harm as Perspective-Relative Assessment]]
- [[HO-II.b Assessment Horizon - the Sai Weng Trap]]
- [[HO-III.a Divergence and Integration - True but Partial]]
- [[HO-001 Harm by Habituation and Captured Assent]]
