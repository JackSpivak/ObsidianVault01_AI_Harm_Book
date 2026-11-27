---
fileClass: Idea
type: idea
status: seed
bookmark: HO-II.d.1
canonical_id: ho-perspective-structure-0-01
territory: new
tags: [ontology/harm]
aliases: [HO-II.d.1, PerspectiveStructure 0.01, PerspectiveType Structure v-0.01]
created: 2026-11-17
filed: 2026-11-17
---

# PerspectiveStructure 0.01

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-II.d Perspective - Ten Optional Properties|HO-II.d]] · Reviews: [[v-0.01 ClassicalCouncil Review of - PerspectiveStructure 0.01|HO-II.d.1.a Classical Council]] · Next version: [[PerspectiveStructure Proposal Draft 3.1|HO-II.d.3]]

> [!info] Base state
> The structure as it stood on 2026-11-17, before the council reviews. Each council review (HO-II.d.1.a–g) examines **this** version. Don't edit the structure in place; the next version gets a new note (0.02).

## Why this is distinct
- [[HO-II.d Perspective - Ten Optional Properties|HO-II.d]] models a Perspective as a single shot (the camera settings of one Assessment). This note models the **PerspectiveType**: the lens tradition (e.g. Public Health, Utilitarianism) with lineage, definitions, disciplines, scope defaults, relations, power and provenance. A Perspective *instantiates* a PerspectiveType.

## Anticipated direction
- Seven-council interdisciplinary review (Classical, Ethics, Legal, Logic, Physics, Sci-Fi, Cognitive), each looking for omissions, structural divergence, divergence in meaning, and domain vocabulary to populate the attributes.
- Then a consolidated PerspectiveStructure 0.02.

## Conceptual territory
- New. Extends HO-II.d; may absorb or extend `EvaluativeStandard` ([[HO-II.a Assessment and Evaluative Standard|HO-II.a]]). Integral quadrants and levels draw on Wilber's AQAL (from memory, unverified).

## Summary
- Two levels: PerspectiveType (tradition) and Perspective (shot). Type-level values act as defaults a shot may override.
- Eight attribute groups: Identity, Aim, Integral position, Scope, Epistemics, Relations, Consequence & power, Citation & provenance.
- Each attribute is marked object [O], annotation [A] or datatype [D]. Rule of thumb: anything you'll want to compare across perspectives (to compute Divergence) must be an object property, because reasoners ignore annotations.
- Social scope (size of group) and developmental altitude (inclusivity of the value structure) are split — the author accepted this distinction.
- Open decisions: adopt the two-level split? statement-level provenance from the start? include developmentalAltitude given that it's contested?

## Original wording

**Author's starting list:**
> "i want to develop a list of all relevant attributes of a thing called a perspective.
>
> Jack's starting list, for example:
> Domain of practice/applicability
> nameDomain (may have a differrent naming for the same perspective in differrent professions or disciplines
> divergence/convergence with other perspective
> keyThinkers/lineage (claimed inventor, major conttibutors, developers of the perspective)
> purpose what is this perspective for - is this different from applicability)
> objective (what is this perspective about)
> individual vs collective integral domain)
> interiority vs exteriority (integral domain)
> level (social scope - individual, family, community, tribe, cultuure, etc probably organized by the inclusivity of their value structure)
> spatialScope (blast radius, physical/spatial scope)
> systemicScope (relational distance of things and systems involved in applicability)
> temporalScope (radius of time horizon,  how far in the future or past count for applicabilityu)
> definition   (may have a differrent definition for the same perspective in differrent professions or disciplines)
> historicalNote/s
> importance (what is determined by or constrained by or results from the application of)
> applicableTo
>
> maybe this is enough of a starting place"
- **Attribution:** Author

> "I love your distinction between size and developmental scope
> lets use your proposals filling the gaps as a new starting point."
- **Attribution:** Author

> "i forgot citations (please redo including this and relevant additional provenance metadata attributes as a new attribute category)"
- **Attribution:** Author

> "Push back: your `level` mixes two things. *Social scope* (individual → family → tribe → culture) is about the size of the group. *Inclusivity of the value structure* is developmental altitude. A tribe-scale perspective can still have a world-centric value structure. Split them into `socialScope` and `developmentalAltitude`."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

**The structure (verbatim):**
```text
                                ┌──────────────────────┐
                                │   PerspectiveType     │  the tradition / lens
                                │ (e.g. Public Health,  │
                                │  Utilitarianism)      │
                                └──────────┬───────────┘
                                           │ ◄── instantiates [O]
                                ┌──────────┴───────────┐
                                │  Perspective (shot)   │  HO-II.d: one assessment's
                                │                       │  camera settings; may override
                                └──────────────────────┘  type-level defaults

PerspectiveType
│
├── 1 IDENTITY ─────────────────────────────────────────────────────────
│   ├── name ........................ [A]  rdfs:label
│   ├── nameByDomain ................ [A]  skos:altLabel (+ domain qualifier)
│   ├── definitionByDomain .......... [A]  skos:definition (+ domain qualifier)
│   ├── historicalNote .............. [A]  skos:historyNote
│   └── lineage ..................... [O] → Person          (role: originator | contributor | developer)
│
├── 2 AIM ──────────────────────────────────────────────────────────────
│   ├── objectOfAttention ........... [O] → Entity / Phenomenon class
│   ├── purpose ..................... [A]  free text for now  (→ [O] Purpose later?)
│   └── domainOfApplicability ....... [O] → Domain          (applicableTo = its instances)
│
├── 3 INTEGRAL POSITION ────────────────────────────────────────────────
│   ├── quadrant .................... [O] → {UL · UR · LL · LR}   (individual/collective × interior/exterior)
│   ├── socialScope ................. [O] → SocialLevel  {individual · family · community · tribe · culture · species …}
│   └── developmentalAltitude ....... [O] → Altitude     {egocentric · ethnocentric · worldcentric · …}
│
├── 4 SCOPE (type-level defaults) ──────────────────────────────────────
│   ├── spatialScope ................ [O] → ScopeBand  (or [D] radius + unit)
│   ├── systemicScope ............... [O] → ScopeBand  (relational distance)
│   └── temporalScope ............... [D]  pastHorizon / futureHorizon (xsd:duration)
│
├── 5 EPISTEMICS ───────────────────────────────────────────────────────
│   ├── assumption .................. [A]  (→ [O] Axiom if you want to compare across types)
│   ├── method ...................... [O] → Method / Instrument
│   ├── unitOfMeasure ............... [O] → Unit  {QALY · dollars · rights violated · narrative …}
│   └── observabilityLimit .......... [O] → Phenomenality value   (HO-I.c)
│
├── 6 RELATIONS (to other PerspectiveTypes) ────────────────────────────
│   ├── divergesFrom / convergesWith  [O] → PerspectiveType  (reified: divergenceType per HO-III.a)
│   ├── specializes / generalizes ... [O] → PerspectiveType  (transitive)
│   └── complements ................. [O] → PerspectiveType  (symmetric)
│
├── 7 CONSEQUENCE & POWER ──────────────────────────────────────────────
│   ├── importance .................. [A]  what it determines / constrains
│   ├── authority ................... [O] → Institution      (who is *bound* by it)
│   ├── whoseInterests .............. [O] → Party / Patient
│   ├── blindSpot ................... [O] → Entity / HarmType (HO-005)
│   ├── knownCritique ............... [A]  (+ [O] critiquedBy → PerspectiveType)
│   └── status ...................... [O] → {dominant · contested · marginal · emerging}
│
└── 8 CITATION & PROVENANCE  (NEW) ─────────────────────────────────────
    │
    ├── 8a  SOURCES: what the perspective rests on
    │   ├── foundationalWork ........ [O] → Source (bibo:Document)   seminal text(s)
    │   ├── keyReference ............ [O] → Source                   major secondary works
    │   ├── citation ................ [O] → Source                   general dct:references
    │   └── Source  (its own class)
    │       ├── title · creator · date · publisher · url/doi ... [A]/[D]  (dct:/bibo:)
    │       ├── sourceType .......... [O] → {primary · secondary · legal · grey · interview …}
    │       └── accessedOn .......... [D]  xsd:date
    │
    ├── 8b  RECORD PROVENANCE: who made this entry, how
    │   ├── wasAttributedTo ......... [O] → Agent {Author · Claude (model + version) · …}  prov:
    │   ├── wasGeneratedBy .......... [O] → Activity (session / conversation)              prov:
    │   ├── wasDerivedFrom .......... [O] → Source / prior entry                           prov:
    │   ├── created / modified ...... [D]  xsd:date                                        dct:
    │   └── originalWording ......... [A]  verbatim quote (+ its own wasAttributedTo)
    │
    └── 8c  TRUST: how much to believe it
        ├── verificationStatus ...... [O] → {verified · unverified · fromMemory · disputed · retracted}
        ├── evidenceLabel ........... [O] → {fact · interpretation · speculation}
        ├── confidence .............. [D]  0–1 or ordinal          (HO-II.e)
        └── canonStatus ............. [O] → {seed · developing · stable · canon}

[O] object property: links to another thing; the reasoner can query and compare it
[A] annotation property: human-readable metadata; the reasoner ignores it
[D] datatype property: a literal value (number, duration, date)
```
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5), building on the Author's list above.

- **Source:** Obsidian Copilot agent session "Name this chatWhat is Perspective", 2026-11-17 (`copilot/copilot-conversations/agent__Name_this_chatWhat_is_Perspective@20261117_094622.md`).
- **External references:** PROV-O, Dublin Core, BIBO, SKOS (namespaces from memory, unverified); Wilber's AQAL (from memory, unverified).

## Real-world examples
- Candidate PerspectiveTypes: Public Health, Utilitarianism, Tort Law, Integral Theory.

## Why it matters to the book
- A harm dispute is often a dispute between lenses that don't know they are lenses. A PerspectiveType record makes a lens's lineage, blind spots, authority and interests explicit.

## Open questions
- Adopt the two-level split (PerspectiveType / Perspective)?
- Statement-level provenance from the start (each claim its own node, e.g. RDF-star or named graphs)?
- Include developmentalAltitude, given that it's contested?

## Related
- [[HO-II.d Perspective - Ten Optional Properties]]
- [[HO-II.a Assessment and Evaluative Standard]]
- [[HO-III.a Divergence and Integration - True but Partial]]
- [[HO-005 Assessed Membership and Systematic Omission]]
- [[Claude_philosophers]] (the councils)
