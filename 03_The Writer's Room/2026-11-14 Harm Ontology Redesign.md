---
type: session
status: archived
tags: [ontology/harm]
workstream: "[[Handoff - Harm Ontology]]"
harvested_through: "2026/11/15 01:22:16 (plus the closing turn)"
continued_in:
aliases: [Harm Ontology Redesign Session]
created: 2026-11-14
session_date: 2026-11-14
participants: [Author, "Claude: Opus 5.5 (claude-opus-5-5)"]
source: "Obsidian Copilot agent session \"philosopher adverse stress test harm ontology\" — copilot/copilot-conversations/agent__philosopher_adverse_stress_test_harm_ontology@20261114_071639.md"
topics: [harm ontology, stress test, councils, perspective, assessment, divergence]
---

# 2026-11-14 Harm Ontology Redesign

## Summary
- Two adversarial stress tests of the v1 harm ontology (an improvised philosopher test and the Classical Council) found that its top-level classes are rival *theories* of harm filed as *kinds* of harm. That made a single event both harm and not-harm.
- The discussion rebuilt the model in layers: neutral **Factors** bear **CausalRoles** that contribute to neutral **Effects**. Whether anything is harmful is decided only by an **Assessment** made under an **EvaluativeStandard**, taken from a **Perspective**.
- The Sai Weng parable (塞翁失马) showed that whoever sets the assessment horizon sets the verdict. That led to horizon, scope, patient and assessor as required parts of every judgment.
- Court judgments turned out to be a subclass of Assessment. That opens a path to reasoning over legal precedent.
- The photography metaphor produced a ten-property **Perspective**: all properties optional, extended by domain profiles, with explicit statuses for missing information.
- Main value-add over existing ontologies: **Divergence** between assessments is a first-class, typed object ("true but partial").

## Decisions made
All ten are logged in [[Decisions_Log]] on 2026-11-14:
- Theories of harm describe harm; they don't classify it.
- Factor and CausalRole.
- Phenomenality is a property with three values, applied to observability and experienceability.
- Effect is a separate, neutral class.
- Valence lives only in the Assessment.
- Assessment and Judgment, with `TheoryOfHarm` renamed to `EvaluativeStandard`.
- Perspective is a reusable class.
- Open world, domain profiles and explicit missingness.
- Reuse of expert domain vocabularies.
- Divergence is a first-class object.

## How the thinking moved
- **"Accounts" → TheoryOfHarm → EvaluativeStandard.** The author saw that accounts *describe* harm rather than classify it.
- **"Phenomena" dropped.** The word implied that harm must be experienced. The author then showed that causes *can* be phenomena (the shooting chain), which corrected Claude's overstatement. Phenomenality became a property with three values, and observability was separated from experienceability.
- **Fixed cause and effect classes → Factor plus roles.** The chain example showed that every middle link is both cause and effect. Roles became things in their own right (the author's proposal). Claude later rolled the open questions back to "events", and the author corrected it: Factor had been chosen for good reason.
- **Effects became neutral.** The author's point was that an effect can itself become a *beneficial* factor. Harmfulness moved entirely into the Assessment.
- **Horizon.** The author raised the dependency on timescale, illustrated by the Sai Weng parable. Claude found an ethical trap in both directions: too short is short-sighted, and too long becomes an excuse ("who knows?").
- **Assessment ≈ judgment.** The author asked whether the two are the same. They are not identical, but Judgment is a subclass that adds authority, procedure, ratio and finality. Finality is law's way of closing the horizon.
- **Perspective as a camera.** The author listed six elements (standpoint, direction, timestamp, utility, domain of intent, standard). Claude added exposure, framing, resolution, sensitivity and operator.
- **Real-world sparsity.** The author: not every property applies, some domains need more, and many values will be unknown. The result is open world, SHACL "addressed, not known", and missingness statuses.
- **Value-add.** The author linked divergence to Wilber's "true but partial" and the blind men and the elephant.

## Concepts introduced
- **Factor:** neutral base (Act, Process, Omission, Condition, Structure, Risk) → idea note: y
- **CausalRole:** a role borne by a factor in one chain, with its own properties → y (with Factor)
- **Effect (neutral) with cascades:** → y
- **Phenomenality ×2 (observability, experienceability):** → y
- **Valence-in-assessment / no intrinsic harmfulness:** → y (premise)
- **Assessment horizon (Sai Weng trap):** → y
- **Assessment ⊃ Judgment / precedent reasoning:** → y
- **Perspective (ten properties, fitness):** → y
- **Missingness statuses:** → y
- **Divergence / Integration:** → y
- **Harm by habituation and captured assent** (from the Classical Council) → y

## Open questions
- Does Condition split into physical state, status and disposition?
- Is Agent a top-level class, and can an AI system be an agent?
- Does a structure cause harm, or only provide the setting?
- Future generations, AI systems and relationships as patients.
- Should Assent/Judgment become a new object of harm?
- Consent: does it cancel harm, reduce it, or change the verdict only under some standards?
- How the legal layer is modelled, and when.
- Should v2 replace v1? What happens to the root `.ttl`?
- Is causal share measurable, or only ordinal?
- Which role types belong in the set?

## Original wording
> "In this sense, Accounts do not actually classify (or subclassify) harms. I think they describe harm."
- **Attribution:** Author

> "each of these stages in the chain of causation and effect are phenomenon"
- **Attribution:** Author

> "the benefit of this approach is that the roles can have appropriate properties like"
- **Attribution:** Author

> "how about phenomenal, nonPhenomenal or conditionallyPhenomenal"
- **Attribution:** Author

> "just as a given role may be harmful or helpful depending on the circumstance, so can be an effect. especially if the state induced in the obeject of harm itself becomes a beneficial agent in a causation chain."
- **Attribution:** Author

> "there is an ethical trap in almost all framings of harm (i believe) and there is a dependency that i don't know if we have represented it anywhere in the ontology."
- **Attribution:** Author

> "The parable shows that **whoever sets the horizon sets the verdict.**"
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

> "this would be a wonderful fortuitous and significant overlap with the domain of law and regulation if it is and would make an entire body of precident directly inferable and (reason-able)"
- **Attribution:** Author

> "if you think of a perspective literally - as in photography - each perspective has:"
- **Attribution:** Author

> "in real world instances these properties might be left blank (null) or better \"unknown\" especially by default"
- **Attribution:** Author

> "i actually like what i think might provide an actual value-add for this ontology relative to others which define harm outright."
- **Attribution:** Author

> "**AI's typical harm is not a loss you suffer but a self you are trained into:** your habits shaped, your assent handed over, your desires grown."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5), voicing the Classical Council's Moderator's Summary

## External references
| Reference | Used for | Status |
|---|---|---|
| Sai Weng / 塞翁失马, *Huainanzi* | The horizon problem | Web search (standard), result pages not opened; whether the war ending is original is unverified |
| Wilber, "true but partial" | The divergence principle | From memory, unverified |
| *Clapper* (2013), *Spokeo* (2016), *TransUnion* (2021) | Legal standards on horizon, modality and concreteness | From memory, unverified |
| Ashley, HYPO / CATO | Factor-based legal case reasoning | From memory, unverified |
| BFO, PROV-O, OWL-Time, SHACL, STIX, ATT&CK, CVSS, AIID, CSET, MIT AI Risk Repository | Candidate vocabularies to reuse | From memory, unverified |
| [[Claude_philosophers]] | Council rosters and format | Read in the session |

## Artifacts touched
- **Read:** root `Interdisciplinary_Harm_Ontology_Compendium.md` (v1, in full); root `Interdisciplinary Harm Ontology.ttl` (lines 1–565, rest searched only); [[Interdisciplinary_Harm_Ontology_Compendium v2]] (beneficiary attribute only); [[Claude_philosophers]]; [[structured-inquiry-book-notes]] (council section).
- **Both stress tests were run against v1**, not v2.
- **Edited:** [[Decisions_Log]] (10 rows); created the [[Session]] template and this note.

## Follow-ups
- [ ] Harvest the concepts into idea notes and a new bookmark index (planned in this session).
- [ ] Re-check the stress-test findings against v2.
- [ ] Verify the external references.
- [ ] Decide whether v1 is archived.
- [ ] Update the draft model tree to match the decisions.

## Addendum: rest of the session (2026-11-14 late → 2026-11-15)

### How the thinking moved
- **Stress-test suite.** The author asked for one place to test the ontology → [[HO-002 Ontology Stress-Test Suite]]. Claude's "this blocks the trap" claims were recorded as hypotheses.
- **Effects aren't single things.** By the same logic as factors, "the effect" is a perspective's selection → **Outcome** class.
- **Perfect storm.** Cause inferred from an assembly of participating factors; engineered or exploited assemblies of harmless parts are an attack vector → **CausalAssembly**, `participatesIn` ([[HO-003 Causal Assembly - the Perfect Storm]]).
- **Symmetry attempted, then abandoned.** Claude proposed Ramification and Attribution as mirror images. The author objected that every state influences all later states, scope is necessarily limited, magnitude is insufficient (the butterfly effect, critical points), and sensitivity is itself an attack target. Then the author's key point: the irreversibility of time makes symmetry impossible. → No Ramification class; Attribution and Outcome as bounded selections; scope never Complete; leverage and criticality ([[HO-004 Criticality, Leverage and the Limits of Scope]]).
- **Membership is assessed.** The author saw that factors are assessed for inclusion in the assembly. Claude answered quickly, then admitted momentum when the author asked, and added caveats (regress, evidence anchor). Omission is the norm → re-attribution cases as the test method ([[HO-005 Assessed Membership and Systematic Omission]], pending).
- **Process.** Cost of long chats; transcripts as the raw archive; session = conversation; rolling handoff notes; incremental harvest; closing checklist.
- **Ontology files.** No v3 artifact existed → [[Harm Ontology v3 - Draft Structure]]. Migration goals → [[Harm Ontology Migration Plan]]. The v1 `.ttl` was repaired (prefixes) and validated with a new conda environment.

### Decisions made (addendum)
- 2026-11-14: Outcome; CausalAssembly; temporal asymmetry; scope, humility and criticality.
- 2026-11-15: transcripts as archive; incremental harvest; sessions, handoffs and closing; ontology tooling; `.ttl` as single source of truth.

### Original wording (addendum)
> "I am concerned that similarly we have effects as a unitary construct."
- **Attribution:** Author

> "it may be inherently true that the structure of reality, because of the irreversability of time makes our aesthetic desire for a symmetrical structure impossible. an assembly of causes produce an infinitely rammifying chain of events  - very much not a mirror image"
- **Attribution:** Author

> "you responded rapidly.  do you simply agree or does this require more reflection."
- **Attribution:** Author

> "I agreed quickly, and some of that speed was momentum."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

### Artifacts touched (addendum)
- **Created:**
  - HO-002 to HO-005
  - `ontology/` folder: repaired v1 `.ttl`, v3 draft structure, migration plan
  - [[Handoff]] template; [[Handoff - Harm Ontology]]
- **Edited:**
  - [[Session]] template (fields, closing checklist)
  - bookmark-index-maintainer skill (incremental harvest)
  - [[Decisions_Log]]
  - Harm Ontology and AI Governance & Safety indices; [[_Master Bookmark Index]]
- **Installed:** conda environment `harm-ontology`.

## Related
- [[Handoff - Harm Ontology]]
- [[003 Harm Ontology from Outlines]]
- [[002 Scalability of Oversight and Control]] (002.II.a rubber-stamping)
- [[The Self-Revising Harm Ontology]]
- [[Interdisciplinary_Harm_Ontology_Compendium v2]]
