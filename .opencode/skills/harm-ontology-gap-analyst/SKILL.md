---
name: harm-ontology-gap-analyst
description: Performs focused inquiry into the adequacy of a harm ontology. Strictly requires explicit user input for 1) a discipline-based perspective, 2) an empirical target narrative/case text, and 3) a target ontology schema note or file. Never assumes or carries over inputs from previous context.
license: MIT
metadata:
  copilot-enabled-agents: opencode, codex, general
  copilot-builtin-version: "3"
---

# Harm Ontology Searchlight and Gap Analyst

## Intention Framing & Purpose

This skill performs focused inquiry into the adequacy of a harm ontology. It starts from a discipline-based perspective, generates the questions it would ask (its searchlight, with its competencies and blind spots), and tests whether those questions yield checkable findings in real-world reporting. It then operationalises the judging layer, benchmarks it against institutional practice, and identifies gaps in how the model represents the search, the findings, and the consequences or remedies. 

The process is iterative. **Success is measured by whether the model can represent a real assessment, not by the elegance of its internal structure.**

---

## Strict Input Protocol (No Context Carryover)

**This skill assumes nothing from prior conversation history or previous sessions.** When invoked, if any of the three required inputs are missing, unstated, or ambiguous, you must explicitly pause and prompt the user for them. Never reuse inputs from an earlier run.

1. **Input A: The Discipline-Based Perspective**
   - *Requirement:* The user must explicitly name or define the perspective, council, or analytical tradition to be used (e.g., *Classical Council*, *Military Strategist*, etc.). If unnamed, prompt the user.
2. **Input B: The Empirical Target Narrative / Case Text**
   - *Requirement:* The user must provide the specific text, filing, news story, or scenario to be analyzed. If missing, prompt the user to paste or attach the text.
3. **Input C: The Target Ontology Schema**
   - *Requirement:* The user must specify the exact ontology note, draft structure, or schema file in the vault to be evaluated against the narrative findings (e.g., `Harm Ontology v3 - Draft Structure` or a specific `.ttl` file). Never use a list of gaps or meta-notes as the ontology. If missing, prompt the user to name the ontology document.

---

## Workflow Steps

### Step 1: Elicit Inputs & Validate Completeness
- Verify that Input A, Input B, and Input C are explicitly provided in the current prompt or attachments. If any are missing, stop and prompt the user for the missing input(s).

### Step 2: Generate the Searchlight from Input A
- Articulate the perspective's core tradition, competencies, and blind spots.
- Derive 10–20 structured core investigative questions.

### Step 3: Translate Questions into Observable Harms using Input B
- Apply the searchlight questions to the empirical text provided in Input B.
- Reframe the inquiries into concrete, checkable statements of actual or potential harm found within that specific narrative.

### Step 4: Operationalize the Judging Layer & Benchmark
- Define the required assessment dimensions, instruments, and procedural workflows.
- Cross-reference against real-world institutional frameworks (e.g., EIA, CBA, PRA).

### Step 5: Gap-Map Findings against Input C (The Actual Ontology Schema)
- Compare the required findings, procedural steps, and assessment mechanics directly against the text/structure of **Input C** (the user's specified ontology schema).
- Identify genuine structural omissions in Input C (missing classes, properties, or attributes needed to represent the assessment).

### Step 6: Apply the Placement Test
- Test every identified missing element to ensure proper structural placement (e.g., procedural layer vs. perspective tradition).

---

## Validation Checklist

- [ ] All three inputs (Perspective, Narrative, Ontology) were explicitly supplied in the current prompt (no context carryover).
- [ ] Searchlight questions are derived strictly from Input A.
- [ ] Observable harms are grounded strictly in Input B.
- [ ] Gaps are identified strictly by comparing against the actual schema in Input C (never against past gap lists).
