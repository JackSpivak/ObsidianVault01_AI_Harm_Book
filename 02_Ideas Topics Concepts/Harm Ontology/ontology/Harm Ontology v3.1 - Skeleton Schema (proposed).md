---
type: outline
status: proposed
tags: [ontology/harm]
aliases: [Harm Ontology v3.1, v3.1 Skeleton Schema]
created: 2026-11-21
source: "[[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]]"
---

# Harm Ontology v3.1 — Skeleton Schema (proposed)

Placeholder for every change discussed since the v3 draft that is not yet logged. It holds three things: proposals, open questions and enhancements. It is also a **skeleton schema**: classes and properties only, with no narrative. Nothing here is adopted. Logged decisions remain in [[Decisions_Log]]; v3 is unchanged and remains the record of the 2026-11-20 revision.

> [!warning] Narrative migration deferred
> Migrating the narrative content (definitions, explanations, examples, hub and spoke text) is deliberately postponed. It waits until the backbone schema is finalised and tested for coverage, for example by comparing physics with Integral Theory. Do not carry narrative into v3.1 yet.

## Governing principles (from v3, unchanged)
- Theories of harm describe and judge; they do not classify. No intrinsic harmfulness; valence lives only in assessments.
- Open world, explicit missingness, profiles rather than domains.
- Three layers: schema (OWL, `ho:`), profiles (SHACL), vocabulary (SKOS). Layer-1 name "schema" is adopted but not yet logged.

## Naming rules under consideration (proposed)
- One IRI, one type and one unique label per layer ([[Handoff - Harm Ontology]], methodology rules 1–7).
- Classes are nouns; individuals of PerspectiveType carry the tradition's name, with the suffix `Perspective` as a candidate convention (for example `integralPerspective`, `physicsPerspective`).
- Three distinct terms for three distinct things (proposed, not logged):
  - **ConceptualTerritory**: the subject matter a discipline studies.
  - **Discipline**: the practice that studies, tests and applies principles.
  - **FieldOfApplication** (or **Setting**): where a practice is conducted.
- "Domain" in the ontology means only `rdfs:domain`. Prose may use "discipline" or "field" to blur deliberately. The rename of `nameByDomain` and `definitionByDomain` is pending.

## Skeleton schema (proposed additions to v3)

```text
PERSPECTIVE (abstract umbrella, unchanged from v3)
├── PerspectiveType                 (tradition; individuals such as integralPerspective, physicsPerspective)
│   └── structure: PerspectiveStructure 0.02 groups 0–12 and profiles   [see table below]
│       ├── foundationalCommitments → (open: range)   identity: what the perspective cannot give up  (2026-11-21, logged)
│       ├── CorePrinciples          (class, proposed)  generative rules that produce verdicts  (open: attachment property)
│       ├── heldBy → Discipline                        proposed; overlaps bearerRole / lineage (open)
│       ├── usedBy → Agent                             proposed; organisations using the perspective (new relation)
│       ├── informedBy → Theory                        proposed; carries a status (foundational · widelySupported · contested · fringe), assessed
│       ├── hasVocabulary → vocabulary scheme          proposed; replaces discipline-keyed schemes for traditions (open)
│       ├── anchoredIn → Discipline                    proposed; disciplines a tradition draws on
│       └── statedPurpose / use → Purpose              proposed; use is a node (a use of a perspective for a purpose)
│
├── PerspectiveSpecification        (unchanged from v3)
│
DISCIPLINE (proposed, new class)
├── studies → ConceptualTerritory                      proposed
├── practisedIn → FieldOfApplication                   proposed
├── heldBy → Agent (community of practitioners)        proposed
├── characteristicPerspective → PerspectiveType        proposed (one relation covering "has", "uses" and "embraces")
└── informedBy → Theory                                proposed; core and fringe theories both allowed

THEORY (proposed, new class)
├── developedBy / contributedBy → Person               proposed
└── status (assessed)                                  proposed

CONCEPTUAL TERRITORY (proposed, new class)              e.g. the physical world, harm, markets
FIELD OF APPLICATION (proposed, new class)              e.g. engineering, medicine, governance, business
```

### 0.02 groups that overlap the proposals (for the coverage test)
| Proposal | Already in 0.02 | Status |
|---|---|---|
| `heldBy` | `lineage`, `bearerRole`, `controlLocus` | overlap; decide reuse vs new |
| `usedBy` | `accountabilityLocus`, `authority` | partial gap |
| `informedBy` | `lineage`, `originatingCircumstance`, `transmissionMode` | theory not yet a node |
| `studies` | `objectOfAttention` (core) | overlap; decide reuse |
| `practisedIn` / `fieldOfApplication` | `fieldOfApplication` (group 5) | reuse; give it a target class |
| `foundationalCommitments` | group 0 core | reuse; give it a range (open) |

## Structural and naming changes pending (not decided)
1. `nameByDomain` / `definitionByDomain` → `…ByDiscipline`, or another name.
2. `fieldOfApplication` gets a target class (setting), not free text.
3. Layer-1 rename from "ontology" to "schema" to be logged.
4. Whether `hov:hubs` is renamed, and whether each hub becomes its own scheme.
5. Whether `int:` is keyed to a discipline or to the Integral perspective.
6. The `observabilityLimit` attribute in 0.01 has no matching 0.02 property; confirm whether Box A covers it.
7. Group numbering: 0.02 says "twelve display groups" but numbers 0–12.

## Open questions
- Does a perspective's core principles attach through a new property or through `foundationalCommitments`? (See the 2026-11-21 entry in [[Decisions_Log]].)
- Is a discipline's perspective the same kind of thing as a tradition's? Working answer: yes, it is a PerspectiveType, and the discipline uses it.
- Do disciplines hold perspectives, or do communities of practitioners hold them and disciplines use them?
- Should "use" be one relation or two: `practisedIn` (settings) and `usedBy` (agents)?
- Should a theory's status be an Assessment with `assessedBy`, or a fixed value?
- Statement-level provenance (RDF-star or named graphs), an attribute-space model for comparing traditions, and whether the ontology is an instance of its own PerspectiveType (carried from 0.02).

## Enhancements beyond v3 (proposed)
- Separate `ResponsibilityAssessment`, `ValenceAssessment` and `CausalAssessment` (pending, HO-005).
- Event class and participation for agents (HO-007, proposed 2026-11-19).
- v4 Chain class bounded by a horizon (HO-006).
- Organisations as assessors (`assessor` as organisations, HO-007).

## Test plan before any logging
1. **Coverage test: physics vs Integral.** See the section below.
2. **Overlap test.** Resolve each row of the 0.02 overlap table: reuse, rename or add.
3. **Naming test.** Check each new name in a Protégé tree next to its neighbours, and against the methodology rules.
4. Only after 1–3 pass, log decisions and then consider narrative migration.

## Coverage test: physicsPerspective and integralPerspective (proposed, structure only)

**Method.** Create two individuals of PerspectiveType, `physicsPerspective` and `integralPerspective`. Each carries the full PerspectiveStructure 0.02 slots, with values for structure only. No narrative is entered; the Physics Council review (v-0.01) is not used as a source for values yet, because the migration is deferred and the council reviews are not independent evidence.

**Each discipline is a separate individual**, not a subtype: `Physics` (Discipline) and `Integral` (the Integral practice, to be confirmed), linked to their perspectives by `characteristicPerspective`. This follows the rule that subclasses are for kinds of tradition only.

**For each 0.02 slot, record one of:**
- a value (structure only, for example `physicsPerspective.foundationalCommitments` is present, with a placeholder value)
- a missingness status: Unknown, NotApplicable, Undisclosed, Disputed or Pending (HO-II.e)
- or "gap" if neither fits.

**Three checks:**
1. **Applies to both.** Every slot is either applicable or NotApplicable, with a reason, for both individuals.
2. **Physics-only needs.** Any slot physics needs that Integral cannot express is listed as a gap to resolve.
3. **Integral-only needs.** Any slot Integral needs that physics cannot express is listed as a gap to resolve.

**Expected findings to test (hypotheses, not claims):**
- Integral's group 3 (interiority, collectivity, moralCircle, developmentalAltitude) may be NotApplicable or Unknown for physics, which would be a real divergence, not a gap.
- Group 11 (assessments of the tradition) should apply to both, but physics may need an assessment of its own epistemic standing (group 6) that Integral does not.
- Group 9 (power) may be sparse for physics and rich for Integral's organisational use.

**Outcome.** A table with one row per 0.02 slot, and one column per individual, showing the value, the missingness status or the gap. Findings are recorded here, and only confirmed ones are considered for logging.

**Status.** Not run. Waiting for the author's go-ahead to create the two individuals in a test file.

## Deferred
- Narrative migration (definitions, explanations, examples, hub and spoke text) into the schema.
- Compendium generation from the `.ttl`.
- Protégé domains and ranges for every class (waiting on the skeleton).

## Sources
- [[PerspectiveStructure 0.02]], [[PerspectiveStructure 0.01]]
- [[2026-11-20 Harm Ontology Sample Review and Methodology]]
- [[HO-II.d.3 Hub and Spoke Pattern]]
- [[Decisions_Log]] (2026-11-21 entry)
