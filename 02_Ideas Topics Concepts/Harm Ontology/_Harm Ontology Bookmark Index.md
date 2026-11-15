---
canonical_id: harm-ontology-bookmark-index
type: index
status: developing
tags: [index/bookmarks, ontology/harm]
aliases: [Harm Ontology Bookmark Index, HO Index]
created: 2026-11-14
---

# Harm Ontology — Bookmark Index

*A living table of contents for designing the perspective-relative harm ontology. It describes what has been found. It doesn't limit what can be found next.* Maintained under the bookmark-index-maintainer rules (`.claude/skills/bookmark-index-maintainer/SKILL.md`). Registered in the [[_Master Bookmark Index]]. Prefix `HO-`.

## Bookmarks
Click the arrow beside an item to open or close its branch.

- [[HO-000 Harm as Perspective-Relative Assessment|HO-000 — Root: harm as perspective-relative assessment]]: theories of harm describe harm rather than classify it. Neutral factors, roles and effects are judged by assessments taken from perspectives.
	- **HO-I — Core model** (tier, no page of its own): what exists in a harm situation (neutral of verdicts).
		- [[HO-I.a Factor and CausalRole|HO-I.a — Factor and CausalRole]]: neutral factors (Act, Process, Omission, Condition, Structure, Risk) bear roles in specific causal chains.
		- [[HO-I.b Effect and Cascades|HO-I.b — Effect and cascades]]: neutral effects with patient-specific properties. Effects can bear roles and lead to further effects.
		- [[HO-I.c Phenomenality - Observability and Experienceability|HO-I.c — Phenomenality]]: Phenomenal / NonPhenomenal / ConditionallyPhenomenal, applied separately to observability and experienceability.
	- **HO-II — Judging layer** (tier): how anything comes to count as harmful or beneficial.
		- [[HO-II.a Assessment and Evaluative Standard|HO-II.a — Assessment and evaluative standard]]: each assessment is one judgment, made under a standard (formerly "theory of harm").
		- [[HO-II.b Assessment Horizon - the Sai Weng Trap|HO-II.b — Assessment horizon: the Sai Weng trap]]: whoever sets the horizon sets the verdict.
		- [[HO-II.c Judgment as Assessment - Reasoning over Precedent|HO-II.c — Judgment as assessment]]: a court judgment is an assessment with authority, procedure, ratio and finality.
		- [[HO-II.d Perspective - Ten Optional Properties|HO-II.d — Perspective]]: the photographic model (position, time, optics, purpose, operator).
		- [[HO-II.e Missingness Statuses and Domain Profiles|HO-II.e — Missingness and domain profiles]]: open world, SHACL "addressed, not known", Unknown / NotApplicable / Undisclosed / Disputed / Pending.
	- **HO-III — Meta layer** (tier): relations between judgments, and to other vocabularies.
		- [[HO-III.a Divergence and Integration - True but Partial|HO-III.a — Divergence and integration]]: typed disagreement between assessments. The main value-add.
		- [[HO-III.b Reusing Expert Domain Vocabularies|HO-III.b — Reusing expert vocabularies]]: map by default, reference identifiers, import only small cores.
- [[HO-001 Harm by Habituation and Captured Assent|HO-001 — Harm by habituation and captured assent]]: AI's typical harm may be the self you are trained into, not a loss you suffer.
- [[HO-002 Ontology Stress-Test Suite|HO-002 — Ontology stress-test suite]]: the one place where the model is tested against hard cases (Pass / Partial / Fail / Untested). It turns design claims into tests.
- [[HO-003 Causal Assembly - the Perfect Storm|HO-003 — Causal assembly: the perfect storm]]: factors `participatesIn` a jointly sufficient assembly. Engineered or exploited assemblies of harmless parts are an attack vector.
- [[HO-004 Criticality, Leverage and the Limits of Scope|HO-004 — Criticality, leverage and the limits of scope]]: time makes the model asymmetric (settled past, open future). Scope can never be asserted complete; inclusion by leverage, not only magnitude; sensitivity as an attack vector.
- [[HO-005 Assessed Membership and Systematic Omission|HO-005 — Assessed membership and systematic omission]]: which factors count as causes is itself assessed, and omission is the norm. Re-attribution cases as the test method. Revises HO-003 (pending).

## Ontology files
- [[Harm Ontology v3 - Draft Structure]]: the consolidated v3 model.
- [[Harm Ontology Migration Plan]]: v1/v2 → v3 (phases 0–5).
- `ontology/Interdisciplinary Harm Ontology v1.ttl`: repaired, validated v1 (1.0.1).

## Premises
- [[HO-premise No Intrinsic Harmfulness|HO-premise — No intrinsic harmfulness]]: valence (harmful or beneficial) lives only in assessments. HO-I.b, HO-II.a, HO-II.b and HO-III.a all depend on it.

## Cross-references
- **HO-II.b and HO-III.a:** horizon is one of the axes a Divergence can turn on (the neighbours vs. the old man).
- **HO-II.c and HO-II.b:** legal finality is law's way of closing the horizon.
- **HO-001 and [[_AI Governance & Safety Bookmark Index|002.II.a]]:** rubber-stamping is captured assent in an oversight setting.
- **HO-000 and [[_AI Governance & Safety Bookmark Index|003]]:** 003 covers building tooling for an ontology; this index covers the ontology's design.
- **HO-I.b and HO-II.e:** Effects with Undisclosed values held by the party with most to lose (the shadowban pattern).
- **This index and [[The Self-Revising Harm Ontology]]** (unfiled story device): a model where harm is only ever judged, never intrinsic, is exactly what an AI could quietly re-weight.

- **HO-003 and HO-I.a / HO-III.a:** assemblies are made of Factors, and factor-level vs. assembly-level verdicts are a new kind of Divergence.
- **HO-004 and HO-II.b:** the predictability horizon is a principled limit on the Sai Weng horizon.
- **HO-004 and HO-003:** the most dangerous pattern is an assembly of individually innocuous, sub-threshold factors placed at critical points.
- **HO-005 and HO-003:** HO-005 revises HO-003's "jointly sufficient" to "as assessed" (pending tests).
- **HO-002 and every other entry:** each design claim in this index should eventually have a test case in HO-002. [[The Self-Revising Harm Ontology]] is test T17.

## Summary
Created 2026-11-14 from the harm ontology redesign session ([[2026-11-14 Harm Ontology Redesign]]). Its decisions are logged in [[Decisions_Log]].

## Original wording
- **Author:** "i am almost certain that we will be expecting and need an entirely new bookmark index for ideas related to this ontology endeavor.  perhaps we could execute that now."
- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14 (`copilot/copilot-conversations/agent__philosopher_adverse_stress_test_harm_ontology@20261114_071639.md`).
