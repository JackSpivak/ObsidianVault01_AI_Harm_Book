---
type: session
status: developing
tags: [handoff, ontology/harm]
aliases: [Harm Ontology Handoff]
created: 2026-11-15
updated: 2026-11-15
workstream: Harm Ontology
latest_session: "[[2026-11-14 Harm Ontology Redesign]]"
---

# Handoff — Harm Ontology

*Rolling, forward-facing note. Overwrite it at each session close; history lives in the session notes and in git. Attach this note to start a new chat.*

## Status
- The v3 **design** is drafted and logged. No v3 `.ttl` exists yet.
- **Migration Phase 0** is partly done: v1 `.ttl` repaired and validated, tooling ready.
- **Nothing in the model has been tested yet.**

## Where we are
- **Design:** [[Harm Ontology v3 - Draft Structure]] is the consolidated model. Its rationale is in the HO notes ([[_Harm Ontology Bookmark Index]]) and [[Decisions_Log]] (2026-11-14 and 2026-11-15).
- **Key commitments:**
  - harm is judged, never intrinsic
  - Factor → CausalRole / CausalAssembly → Effect → Outcome
  - Assessment taken from a Perspective
  - Divergence is first-class
  - deliberately asymmetric in time
  - scope never Complete
- **Files:** `02_Ideas Topics Concepts/Harm Ontology/ontology/` (repaired v1 `.ttl` v1.0.1, v3 draft structure, migration plan).
- **Tooling:** conda environment `harm-ontology` (`~/anaconda3/envs/harm-ontology/python.exe -I …`, rdflib, pyshacl). Scripts go in `~/harm-ontology-scripts/` (outside the vault).

## Pending (proposed, not decided; see [[HO-005 Assessed Membership and Systematic Omission]])
- Splitting Assessment into Causal / Valence / Responsibility.
- Causal standards (but-for, NESS, INUS…) as a second family of standards.
- Reifying `participatesIn` as a claim.
- HO-003's "jointly sufficient" becoming "as assessed".
- An evidence anchor against the regress ("everything is a view").

## Next step (choose one)
1. **Migration Phase 0, continued:** pick the authoritative source for each part. Open `# Master Formal Ontology of Harm (Part 1…)` (never read), compare v1 and v2, and extract inventories by script.
2. **First re-attribution test:** research the UK Post Office Horizon case, with sources, and model it roughly as a sequence of causal assessments ([[HO-002 Ontology Stress-Test Suite]] R01). The results should decide the pending items.

## Cautions
- Claims that the structure "blocks" traps are **hypotheses**. Run tests, don't assert.
- **Don't log the pending items** until tested.
- Many references are **from memory, unverified**: legal cases, Wilber, NESS/INUS, the vocabularies, Lorenz, Meadows, and the war ending of the Sai Weng parable.
- Both early stress tests ran against **v1**, not v2. Re-check findings against v2.
- Old **root files** (`Interdisciplinary_Harm_Ontology_Compendium.md`, `Interdisciplinary Harm Ontology.ttl`) are untouched and awaiting an archive decision. Ask before moving or deleting.
- Watch for **momentum**: the author values reflection over quick agreement.

## Sub-workstreams
- **PerspectiveType consolidation (HO-II.d.1):** [[Handoff - PerspectiveStructure 0.02]]. Seven council reviews are done and their citations verified; the 0.02 consolidation is next.

## Read first
- This note, then [[Harm Ontology v3 - Draft Structure]] and [[Harm Ontology Migration Plan]].
- Open individual HO notes only as needed.

## Previous sessions
- [[2026-11-14 Harm Ontology Redesign]] (transcript: `copilot/copilot-conversations/agent__philosopher_adverse_stress_test_harm_ontology@20261114_071639.md`; read selectively, don't reopen the chat)
