# Harm Ontology v0.03.1: Master Index

The single bookmark index for v0.03.01 work. Every v0.03.01 note is listed here. The older index in the parent `Harm Ontology` folder now points here.

Status key: **Settled** = logged in the decisions log · **Proposed** = drafted, awaiting author confirmation · **Scratch** = working file, not part of the design.

## 1. Design foundations
- [[Harm Ontology v0.03.01 Design Guide - Vision, Principles, Commitments, Rationale|Design Guide: vision, principles, commitments, rationale]] · Proposed
  - Core premise: harm is an assessment, never an intrinsic property. Three layers: neutral backbone, judging layer, discipline modules.

## 2. Design notes and decisions
- [[Harm Ontology v0.03.01 Design Notes - Harmfulness, Imagined Harm and Causal Chains|Design notes: harmfulness, imagined harm and causal chains]] · Proposed
  - Temporal split (AssessedHarm past or present, AssessedImaginedHarm future); harmfulness as assessment; causal chains as occurrent structures; modular TBox over a shared ABox.
- [[Harm Ontology v3.1 - Feature Roadmap and Change Ledger|Change ledger (features S1 to S41, K1 to K5, and others)]] · Proposed
  - Open items with status, blockers and source. Inherited from v3.1; new v0.03.01 items should be added here.

## 3. Core model: neutral backbone (Layer 1)
- [[Harm Categories Causal Chain Methodology Part 1|Causal chain methodology, part 1: the extended progression]] · Scratch (source of candidate roles, not schema)
- [[Harm Categories Causal Chain Methodology Part 2|Part 2: how standards name the chain]] · Scratch (contains errors; see corrections in the crosswalk work)
- [[Harm Categories Causal Chain Methodology Part 3|Part 3]] · Scratch
- [[Harm Categories Causal Chain Methodology Part 4 philosophy|Part 4: philosophy]] · Scratch

## 4. Judging layer (Layer 2)
- [[Proposed Class Tree and DUL Alignment|Proposed class tree with DUL alignment, definitions and descriptions]] · Proposed (IRI reference only; DUL links marked provisional where unchecked)
- Not yet filed as separate v0.03.01 notes. The consolidated candidate requirements (R1 to R23) and the candidate tree live in chat and need to be filed here once the wording is confirmed.

## 5. Discipline modules (Layer 3)
- Not yet started for v0.03.01. Earlier discipline work is in the parent `Harm Ontology` folder and will be linked here when reviewed.

## 6. Test cases
- [[Model Structure Test Note - Competency Questions and Coverage|Model structure test note: competency questions, case tests, coverage matrix]] · Proposed
- Scratch: Fire door case, dinner party case, dealer case, 2008 crisis extraction test (`Scratch - 2008 Crisis Extraction Test Sketch.md.bak`, a non-.md scratch file; not part of the note graph).

## Naming rules in use (proposed)
- **Assessment** is the act of judging; **Determination** is its output, versioned and persistent.
- **Harm** (realised) and **Harmfulness** (source-side) are always qualified as Assessed, Determination or Imagined where relevant.
- **Causal boundary** is the set of stop nodes of a chain, with reasons. **Temporal horizon** bounds the time an assessment considers. The two are not interchangeable.
