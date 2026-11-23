---
name: perspective-critical-reading
description: Reads a narrative as a holder of a named perspective would, and reports the critical questions that perspective asks, the observable findings it can see, and the blind spots it cannot. Use when the user asks to read, question or critique a text from a discipline, council, tradition or other perspective (for example "from a military strategist's perspective", "Classical Council perspective", "Vajrayana Buddhist view"). Does not map to any ontology; for that use harm-ontology-gap-analyst.
license: MIT
metadata:
  copilot-enabled-agents: opencode, codex, general
  copilot-builtin-version: "1"
---

# Perspective Critical Reading

## Purpose

Read a text as a particular perspective would, and say what that perspective asks, finds and misses. The skill's value lies in two outputs that a general reader does not produce:

1. **Perspective-shaped questions**: questions that the perspective's own concepts make natural when applied to the text.
2. **Blind spots**: what the perspective cannot see in the text. These are often the most useful output.

This skill does not decide whether harm occurred, and it does not map to an ontology. It produces questions and findings for the user to judge.

## Inputs

Both inputs must be explicit in the current request. Do not reuse inputs from earlier conversation.

- **Input A, Perspective:** the discipline, council, tradition or lens to read from. If unnamed, ask.
- **Input B, Text:** the narrative, article, filing or scenario, pasted or named as a vault note. If missing, ask.

## Ordering rule (required)

The questions that come from the perspective must be written **before** the text is read in detail, so that the two sources can be told apart later.

1. **Step 1, perspective only.** Using Input A alone, state:
   - the perspective's core concepts and its canonical sources, marked *from memory, unverified* unless a source has been retrieved;
   - 6 to 10 core questions the perspective asks of any situation;
   - what the perspective typically treats as out of frame.
   Record these in the reply under the heading **Core questions (from the perspective alone)**.
2. **Step 2, the text.** Only now read Input B. Apply the core questions to it and write **Questions the text prompts**. Each one should quote or cite the passage that prompted it.
3. **Step 3, findings.** List observable statements in the text that the perspective's questions make visible. Each finding cites the passage. Separate **stated** (the text says it) from **inferred** (the reader concludes it).
4. **Step 4, blind spots.** List what the perspective cannot see in this text, and what questions it would not ask. Name the people, costs, causes or evidence that fall outside its frame. Also name what the text omits that a different perspective would consider essential.

## Provenance tags (required)

Tag every claim so the reader can tell where it came from:

- **[P]** from the perspective's concepts (Step 1), unverified unless a source was retrieved.
- **[T]** from the text, with the quoted passage.
- **[I]** the reader's inference, with the reasoning.
- **[K]** general background knowledge that is not in the text and not verified.

A question that refers to a detail of the text is **narrative-shaped**. Mark it so, and keep it separate from the Step 1 questions.

## Output format

```text
Perspective: <name>
Text: <title or source, date>

Core questions (from the perspective alone) [P]
1. ...

Questions the text prompts [P→T]
1. ... ("quote")

Findings
- Stated [T]: ...
- Inferred [I]: ...

Blind spots
- Outside the frame: ...
- Omitted by the text, essential to this perspective: ...

Caveats
- Canonical sources and background are unverified [K] unless retrieved.
- Narrative-shaped questions: <list>.
```

## Rules

- Do not present the perspective as authoritative. Say it is a reconstruction, and say when a tradition would dispute a formulation.
- Do not decide that harm occurred. Report what the perspective would ask and what it would find.
- Do not invent quotations or sources. If the text does not contain a detail, say so.
- If the text has no outcome data, say that the findings are potential, not observed.
- If Input A is a tradition with known internal disagreement, name the disagreement rather than choosing one side silently.

## Validation checklist

- [ ] Input A and Input B are both explicit in the request.
- [ ] Step 1 (core questions) appears before the text is applied.
- [ ] Every question that refers to the text is marked narrative-shaped and cites a passage.
- [ ] Every claim carries a provenance tag.
- [ ] Blind spots are listed, not only findings.
- [ ] No ontology is referenced as an input, and no gap or mapping is claimed.

## Relation to other skills

- **harm-ontology-gap-analyst**: takes findings from this kind of reading and tests them against an ontology. Use it only when an ontology note is named as an input.
