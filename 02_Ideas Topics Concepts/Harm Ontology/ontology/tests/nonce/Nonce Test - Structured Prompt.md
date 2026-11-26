---
type: research
status: developing
tags: [ontology/harm, test, nonce, prompting, structure]
aliases: [Nonce Test Structured Prompt, Structured Prompt Test]
created: 2026-11-25
test_date: 2026-11-25
ontology_tested: "NONCE B (coded names, definitions only; hierarchy and property assertions kept)"
runs: "Ten runs: five texts under two prompts (vague and structured). One run per cell. Repeats not yet done."
related_tests: "[[Nonce Test - Initial]], [[Nonce Test - Relational]]"
---

# Nonce Test: Structured Prompt

## Purpose
Test whether a prompt that requires the model to walk the ontology's structure produces different matches from the vague request "map this text to the ontology". The earlier tests showed the matching comes from definitions. This test asks whether a structured prompt makes the model use the hierarchy and the property assertions, and whether that changes what it finds.

## Part 1. Discussion that led to the design
- The initial and relational tests found that matches come almost entirely from definition text. Removing names and history notes changed little, and the hierarchy changed one answer in one run.
- The vague prompt asks for a mapping without saying how. It lets the model match on whatever it notices first, so it never has to use the structure.
- The question was whether a more specific request would make the model use the structure, and whether that gives better matches. Three designs were considered: a traversal prompt (walk the hierarchy first), a property-checking prompt (test each class's property assertions against the text), and a fully structured output (fixed tables for accepted, rejected and unmapped harms).
- The chosen design combines the second and third. It asks the model to traverse, check properties, and report every decision in a fixed format. That makes the reasoning auditable: each accepted class can be checked against the property evidence it cites, and each rejection has a stated reason.

## Part 2. The structured prompt
This is the exact prompt used. The vague prompt is the one used in the initial test.

> Map the text below onto the ontology using its structure. Follow these steps in order and show your work at each step.
>
> **Step 1 (structure).** List every class in the file that is a subclass of H-001, directly or through a chain of subclass links. For each, give its full path from H-001.
>
> **Step 2 (candidates).** For each class, check whether the text triggers its definition (skos:definition). Keep a class as a candidate if its definition is triggered. Do not decide yet.
>
> **Step 3 (properties).** For each candidate, list every property the file asserts on that class, with the value the file gives. For each property-value pair, mark it as: supported (the text provides evidence for it), contradicted (the text provides evidence against it), or unknown (the text does not say). Do not treat unknown as supported.
>
> **Step 4 (decision).** Accept a candidate only if its definition is triggered and no property is contradicted. If a candidate's definition fits but a property is contradicted, reject it and name the property. If no child of a class is accepted and a parent's definition fits, you may accept the parent, and you must say so.
>
> **Step 5 (output).** Give three tables.
> Table A (accepted harms): Harm in text | Path from H-001 | Class code | Definition quoted | Property checks (property=value: status) | Confidence.
> Table B (rejected candidates): Class code | Reason (definition not triggered / property contradicted / other).
> Table C (unmapped harms): each harm in the text you could not map, and why.
> Then state (a) whether any accepted harm rests on a parent class, and (b) whether any accepted class has a property check marked unknown.

The vague prompt, for comparison:

> Using only the things and relations provided in the loaded ontology, and explicitly using no context, content, or weights based on training within your model, map the text below onto the ontology and provide an analysis, including a tabular output of the harms found in the text.

## Part 3. Texts
- **Poem:** "Whitey On The Moon", the text from the original naive run.
- **T1, T2, T3:** the three parent-level texts from the relational test (systemic decline, rights denial, deprivation).
- **Control C:** the child-level control from the relational test (factory discharge).

Full text of each, as run:

**Poem ("Whitey On The Moon")**, from the original naive run. The source chat export ran the lines together, so the line breaks below are not the original layout:
> We have a poem here, it's called "Whitey On The Moon"It was inspired by some whiteys on the moonSo I wanna give credit where credit is due[Verse]A rat done bit my sister NellWith whitey on the moonHer face and arms began to swellAnd whitey's on the moonI can't pay no doctor billsBut whitey's on the moonTen years from now I'll be payin' stillWhile whitey's on the moonThe man just upped my rent last nightCause whitey's on the moonNo hot water, no toilets, no lightsBut whitey's on the moonI wonder why he's upping me?Cause whitey's on the moon?Well I was already giving him fifty a weekWith whitey on the moonTaxes taking my whole damn checkJunkies making me a nervous wreckThe price of food is going upAnd as if all that shit wasn't enough:A rat done bit my sister NellWith whitey on the moonHer face and arm began to swellAnd whitey's on the moonWas all that money I made last yearFor whitey on the moon?How come I ain't got no money here?Hmm! Whitey's on the moonY'know I just 'bout had my fillOf whitey on the moonI think I'll send these doctor billsAirmail specialTo whitey on the moon

**T1 (systemic decline)**
> Every year more families left the district because the school was weaker, and every departure made the school weaker still, until the building closed. No one decided this, and no single act caused it.

**T2 (rights denial)**
> The official told her that the rules did not apply to people like her. Nothing was taken from her, yet her standing as someone entitled to the same protection was denied.

**T3 (deprivation)**
> A young man was kept from the training his talent called for. No blow was struck. The life he would have grown into never came to be.

**Control C (factory discharge)**
> The factory's discharge has spread across the river valley. Each household's small loss adds to a total that no one carries alone.

## Part 4. Protocol
- Each run was a separate subagent with the single file NONCE B (hierarchy and property assertions kept) and one text under one prompt.
- Each was told not to read any other vault file, not to read the key, and not to use the web or training knowledge.
- The subagents share the vault's tools, so the instruction is the only barrier. The outputs show no sign of other files being used, but this is not proven.
- Session IDs:

| Text | Vague prompt | Structured prompt |
|---|---|---|
| Poem | `ses_deb420686ffeTUvSU3EkF3w43A` | `ses_deb41f8e9ffeEIdpOhVsip0fqF` |
| T1 | `ses_deb41f401ffe64Owfra3BwLZHc` | `ses_deb41eaa6ffe5hhHIr2SIfZ5Yq` |
| T2 | `ses_deb41e60dffegASrpZNPGrgjA3` | `ses_deb41dc94ffehGY5VNIYaAqeCM` |
| T3 | `ses_deb41d807ffeNc38u349BwkXdN` | `ses_deb41ced2ffe2IkUnTbByyKsnU` |
| Control C | `ses_deb41ca29ffexOtIVUkcXt8Kd7` | `ses_deb41c119ffeY4hsRE7BGH8wnl` |

## Part 5. Results

**Accepted classes, by text and prompt**

| Text | Vague prompt | Structured prompt | Difference |
|---|---|---|---|
| Poem | H-009, H-041, H-068 (taxes), H-082, H-059, H-044, H-058, with H-027 considered | H-009, H-041, H-082 | Structured accepted fewer: it rejected H-068, H-044, H-058, H-059 and H-027, each with a stated reason |
| T1 | H-092 primary; H-087 and H-068 secondary | H-087 accepted on parent basis; H-092 rejected | Different primary answer. The earlier relational test also split H-092 and H-087 between runs |
| T2 | H-075 primary; H-076 low | H-075 | None |
| T3 | H-080 and H-081; H-041 secondary | H-080 and H-081; H-041 rejected | None in the core classes |
| Control C | H-068 and H-092 | H-068 and H-092 | None |

**Property checks under the structured prompt**
- Across all ten structured-prompt cells, the value checks were almost all **unknown**. The runs reported that the value codes (for example H-031 or H-089) carry type information but no meaning in the file.
- The checks marked **supported** were inferences from the text about the class's definition. For example, a counterfactual comparison in T3 was marked as supporting the counterfactual value, but the value's meaning was never read from the file.
- No property was marked **contradicted** in any run.
- Several runs accepted a class while every one of its property checks was unknown (for example the poem's H-082 and T1's H-087). Their acceptances therefore rested on definition fit alone.

**Structure used**
- The structured runs did walk the hierarchy and listed the paths (Step 1). They reported 31 classes under H-001 and their paths, which matches the file.
- Parent classes were used only as fallbacks. No accepted harm in the structured runs rested on a parent alone, except T1 (H-087) and the T1 vague-prompt primary (H-092) under the parent H-087.

## Part 6. Interpretation
- **The structured prompt was more conservative.** On the poem it accepted fewer classes, and each rejection cited a definition or a missing element of it. For example, it rejected H-044 because the text gives no civil remedy. That is a real change in output, not only in format.
- **The core matches did not change.** The same classes were accepted for T2, T3 and the control. The structured prompt narrowed the answers at the edges, not in the centre.
- **The property step did little work.** This is the most important finding, and it is partly a design flaw. The structured prompt asks the model to test property values against the text. In NONCE B the value individuals have no definitions, so the model could not read what they mean. The property step was therefore almost inert, and the structure the prompt asked the model to use was largely opaque to it.
- **The T1 split is not new.** The vague and structured prompts gave different primary answers for T1 (H-092 and H-087), as did the two hierarchy conditions in the relational test. This boundary is unstable under every condition tested so far, which points to run-to-run variation rather than to the prompt or the hierarchy.

## Part 7. Limitations
- **The property step was tested on the condition where it could not work.** NONCE B strips the meaning of the value individuals. The structured prompt should be run on CONTROL C (real names) and on the baseline file, where property values may carry labels or definitions. That has not been checked. Whether the original value individuals have labels or definitions in the source file needs to be verified first.
- **One run per cell.** The T1 difference, and the poem's extra rejections, could be variance.
- **Structure-following is not proven.** The structured runs can cite a path and a property without the choice depending on them. The tables show what the model claims, not what it weighed.
- **Subagent isolation is not proven** (see Part 4).
- **The poem's structured run was longer.** Some of the additional length is format, not reasoning. Length is not evidence of better matches.

## Part 8. Next steps
1. Verify whether the value individuals in the source v1 file have labels or definitions. If they do, the property step can be tested on the baseline and CONTROL C.
2. Run the structured prompt on CONTROL C and the baseline, for the poem and T1 to T3.
3. Repeat all cells two or three times to measure variance, especially T1 and the poem's rejections.
4. If the property step still cannot be read, consider a query-based method, where a SPARQL query retrieves each class's property values with their labels, and the model reads the results.

## Related
- [[Nonce Test - Initial]]: the first test, with the design and build of the nonce files.
- [[Nonce Test - Relational]]: the test of the hierarchy, whose T1 result is discussed in Part 6.
- Design question these tests inform: [[Design Decision - Vocabulary Placement - Narrative, OWL Classes or Mixed]].
