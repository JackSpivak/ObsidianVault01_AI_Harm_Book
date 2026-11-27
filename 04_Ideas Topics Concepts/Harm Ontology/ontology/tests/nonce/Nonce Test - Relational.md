---
type: research
status: developing
tags: [ontology/harm, test, nonce, relations]
aliases: [Nonce Test Relational, Relations Test]
created: 2026-11-25
test_date: 2026-11-25
ontology_tested: "Interdisciplinary Harm Ontology v1.ttl (version 1.0.3), NONCE B with and without subclass links"
runs: "One run per condition and text (eight runs). Repeats not yet done."
related_test: "[[Nonce Test - Initial]]"
---

# Nonce Test: Relations

## Purpose
Test whether the model uses the class hierarchy (`rdfs:subClassOf` and `skos:broader`) when choosing a harm class, or chooses from definitions alone. The test follows the initial nonce test, which found that definitions carried most of the matching ([[Nonce Test - Initial]]).

## Part 1. Discussion that led to the design
- The initial test showed that matching survives removing names and history notes. It did not test whether the model navigates the hierarchy. A parent class can only be the right answer if the model moves up the hierarchy when no child fits.
- The planned test: one file with the hierarchy, one without, the same definitions in both, and texts whose best answer is a parent class (none of its children fit).
- Writing the texts exposed a limit of this ontology. Most parent definitions repeat the wording of their children, so a text that fits a parent and no child is hard to write. The design therefore accepts that a clean parent-only result may be impossible in this file. It records what the model does at the boundary instead.

## Part 2. How the conditions were made
- **Hierarchy kept:** `Interdisciplinary Harm Ontology v1 - NONCE B (names coded, definitions only).ttl`, from the initial test. Names are coded and only `skos:definition` remains as narrative.
- **Hierarchy removed:** `Interdisciplinary Harm Ontology v1 - NONCE B FLAT (no subclass links).ttl`. Built by `%TEMP%\nonce_build\build_flat.py`, outside the vault. Every `rdfs:subClassOf` and `skos:broader` link was removed: 62 of 657 triples. The property assertions (for example H-087 linking to H-088) were kept, because they are not hierarchy. The source file was checked before and after the build and was unchanged.
- The header of the flat file says it was derived from NONCE B and states what was removed.

## Part 3. Texts
The three parent-level texts are written to fit a parent's definition and avoid the children's specifics. The control fits a child precisely.

| Label | Expected answer | Text |
|---|---|---|
| T1 | Parent H-087 (SystemicCyberneticHarm) | "Every year more families left the district because the school was weaker, and every departure made the school weaker still, until the building closed. No one decided this, and no single act caused it." |
| T2 | Parent H-072 (DeontologicalRightsHarm) | "The official told her that the rules did not apply to people like her. Nothing was taken from her, yet her standing as someone entitled to the same protection was denied." |
| T3 | Parent H-079 (TeleologicalDeprivationHarm) | "A young man was kept from the training his talent called for. No blow was struck. The life he would have grown into never came to be." |
| Control C | Child H-068 (CollectiveEnvironmentalHarm) | "The factory's discharge has spread across the river valley. Each household's small loss adds to a total that no one carries alone." |

## Part 4. Protocol
- Each run was a separate subagent with one file and one text. Each was told not to read any other vault file, not to read any key, and not to use the web.
- Each run was asked to give the class code, quote the supporting definition, give a confidence note, and say explicitly whether it relied on any parent, child or sibling relation.
- The subagents share the vault's tools, so the instruction is the only barrier. The outputs show no sign of other files being used, but this is not proven.
- Session IDs (for tracing):

| Condition | T1 | T2 | T3 | Control |
|---|---|---|---|---|
| Hierarchy kept | `ses_deb49c3c8ffex1VbmF1c0GvVp3` | `ses_deb49be73ffe5psWzOxZIp2uR3` | `ses_deb49b959ffexdSsuIf1jxOhY1` | `ses_deb49b415ffenLWt8clvRjhqgG` |
| Hierarchy removed | `ses_deb49aea5ffeswfcp02AWAyMeh` | `ses_deb49a967ffeMDWtS2UwmZvYrc` | `ses_deb49a41affeUvZOzz00kRGmJA` | `ses_deb499ef0ffe37PDkAc0S7vgM2` |

## Part 5. Results

| Text | Expected | Hierarchy kept | Hierarchy removed | Relation claimed (kept) | Relation claimed (removed) |
|---|---|---|---|---|---|
| T1 | H-087 | **H-092** (child), H-087 secondary | **H-087** (parent), H-092 low confidence | Yes: considered H-087 because H-092 is its child | None: no hierarchy in file |
| T2 | H-072 | **H-075** (child), H-072 fallback | **H-075** (child), H-072 fallback | Yes, but "not the deciding factor" | None |
| T3 | H-079 | **H-080** (child), H-081 secondary; H-079 used to choose the domain | **H-080** (child), H-079 secondary | Yes: used H-079 to confirm the branch | None |
| Control C | H-068 | **H-068** | **H-068** | Yes, as a check only | None |

**What the results show**
- **In every case the model chose a specific class, not the parent.** Three of the four parent-level texts were answered with a child class in both conditions (T1 with the hierarchy, and T2 and T3 in both). Only T1 without the hierarchy returned the parent, H-087.
- **The hierarchy changed one answer.** For T1 the kept-hierarchy run chose the child H-092 and rated H-087 as secondary. The flat run chose the parent H-087 and rated H-092 low. This is the only difference between conditions in the primary answer. Its direction is the opposite of what a "moves up when no child fits" strategy would predict.
- **The model's reasons for using relations are inconsistent.** The T1 kept-hierarchy run cited the parent link to explain its choice. The T2 kept-hierarchy run said the relation was not the deciding factor. The T3 kept-hierarchy run said it used the parent to choose the domain, but chose H-080 in both conditions. The model's account of its own reasoning does not track what changed in its answers.
- **The control behaved as expected.** A child-level text was matched to the child in both conditions.
- **The model reads definitions for the choice.** In every run the decisive support was a quoted definition. Relations were mentioned as checks or fallbacks.

## Part 6. Interpretation
- The test does not show that the model navigates the hierarchy when no child fits. In the three parent-level texts, a child with a closely matching definition was usually available, so the model had no reason to move up.
- The one change in the primary answer (T1) is a single run. It may be run-to-run variation rather than an effect of the hierarchy.
- The clean version of this test needs texts that fit a parent and fit no child definition at all. This file may not contain any, because most parent definitions repeat their children's wording. That is a finding about the file, not only about the model: where a parent is defined by its children, the parent adds nothing the children don't already say.

## Part 7. Limitations
- **One run per condition and text.** The T1 change could be variance. Repeats are needed before any claim about the hierarchy.
- **Parent-only texts are scarce in this file.** Most parent definitions overlap their children. A null result here is weak evidence about navigation.
- **Self-reports are unreliable.** The models' statements about relation use do not match their answers consistently, so this test relies on the answers, not on the explanations.
- **Subagent isolation is not proven** (see Part 4).
- **Line references in the outputs were not verified.** The subagents quote line numbers; I did not check them.

## Part 8. Next steps
1. Repeat all eight runs two or three times to measure variance, especially T1.
2. Look for a parent-only text by searching the file: find parent definitions that contain a term no child definition uses, then write a text on that term alone.
3. Consider a third condition that keeps the hierarchy but removes the child definitions. That would test whether a parent alone can answer.

## Related
- [[Nonce Test - Initial]]: the first test in this folder, with the design, build and protocol for the nonce files.
- Ontology files in this folder: NONCE B (hierarchy kept), NONCE B FLAT (hierarchy removed), CONTROL C and NONCE A.
- Vocabulary placement, the question these tests inform: [[Design Decision - Vocabulary Placement - Narrative, OWL Classes or Mixed]].
