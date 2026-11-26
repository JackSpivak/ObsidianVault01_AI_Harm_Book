---
type: research
status: developing
tags: [ontology/harm, test, nonce, prompting, structure]
aliases: [Structured Prompt - Baseline and Control, Structured Prompt Additional Conditions]
created: 2026-11-25
test_date: 2026-11-25
ontology_tested: "Baseline (Interdisciplinary Harm Ontology v1.ttl, real names, full narrative, value labels) and CONTROL C (real names in IRIs, definitions only, labels stripped by the build)"
runs: "Ten runs: five texts under the structured prompt, on each of two files. One run per cell."
related_tests: "[[Nonce Test - Structured Prompt]], [[Nonce Test - Initial]], [[Nonce Test - Relational]]"
---

# Nonce Test: Structured Prompt, Baseline and Control

## Purpose
The structured-prompt test on NONCE B found that the property step was almost inert, because the value codes had no meaning in that file. This test runs the same structured prompt on the two files where the values should be readable: the baseline (full labels and narrative) and CONTROL C (real names in the IRIs). It asks whether the property step does real work once the values can be read.

## Part 1. Discussion that led here
- The NONCE B structured runs returned "unknown" for almost every property check. The likely cause was that the value codes carry no meaning in that file.
- A SPARQL check (rdflib, fixed queries) confirmed the cause. In NONCE B, 6 of the 72 value individuals have a label or definition. The check was then run on the baseline (72 of 72 have a label or definition) and on CONTROL C (6 of 72).
- The test therefore asks: with the values readable, does the structured prompt find anything the vague prompt misses, and does the structure change the matches?

## Part 2. Files and a flaw in CONTROL C
- **Baseline:** `Interdisciplinary Harm Ontology v1.ttl`, the original file. Real names, full narrative, value labels. 31 classes under `harm:Harm`.
- **CONTROL C:** `Interdisciplinary Harm Ontology v1 - CONTROL C (names kept, definitions only).ttl`. The build dropped `skos:prefLabel` from every node, including the values, and kept only `skos:definition` as narrative. Its class and value IRIs still carry real names, so a model can read the names. This means CONTROL C is not a clean "names kept, labels kept" file. Its value labels are missing, and its names are the only remaining signal.
- The query check found: baseline 72 of 72 values labelled or defined; CONTROL C 6 of 72.

## Part 3. Prompt
The same structured prompt used on NONCE B (see [[Nonce Test - Structured Prompt]]). The one change: Step 3 asks the model to read each value's own label or definition in the file, and the prompt names the root as `harm:Harm` (the baseline and CONTROL C use real IRIs). Texts and the five-step output format are unchanged.

## Part 4. Texts
Poem ("Whitey On The Moon"), T1 (systemic decline), T2 (rights denial), T3 (deprivation), and the control (factory discharge). The same texts as the earlier tests.

## Part 5. Protocol
- Each run was a separate subagent with one file and one text. Each was told not to read any other vault file, not to read the key, and not to use the web or training knowledge.
- The subagents share the vault's tools, so the instruction is the only barrier. Nothing in the outputs suggests other files were used, but this is not proven.

## Part 6. Session IDs (mapped to runs by content)

| Text | Baseline | CONTROL C |
|---|---|---|
| Poem | `ses_de9c5edcaffe5LVa7EDUG3fqAm` | `ses_de9c5bba5ffeKyUhRFkJGILsn6` |
| T1 | `ses_de9c5e490fferytH0NyIA2SNkA` | `ses_de9c5b219ffesL37CFLIyiwUA1` |
| T2 | `ses_de9c5db4bffeX1rUk2R13jevUw` | `ses_de9c5a865ffelxGyjZ7vpnv6XF` |
| T3 | `ses_de9c5d211ffeAhQvJOB2q920wD` | `ses_de9c59ee3ffe9mjg79diTFDdO2` |
| Control | `ses_de9c5c8beffeYhzalBWIT3OJNi` | `ses_de9c595a3ffeUwoRH3aw6TIm4z` |

## Part 7. Results

**Accepted classes**

| Text | Baseline | CONTROL C |
|---|---|---|
| Poem | InterestSetbackHarm (bite, swelling); ExperientialHarm (parent, accepted because no child was) | CapabilityStructuralHarm; DeprivationHarm |
| T1 | SystemicCyberneticHarm (parent, with ExternalityCoordinationHarm accepted as its child); CapabilityStructuralHarm | ExternalityCoordinationHarm; CollectiveEnvironmentalHarm |
| T2 | harm:Harm (root, accepted by fallback) | none |
| T3 | PerfectionistTeleologicalHarm; DeprivationHarm | PerfectionistTeleologicalHarm; InterestSetbackHarm |
| Control | ExternalityCoordinationHarm is not accepted; CollectiveEnvironmentalHarm rejected on perpetrator; harm:Harm (root, fallback) | InterestSetbackHarm |

**Property checks**
- **Question: do the unknown counts fall once values are readable?** Answer: yes. Compared with NONCE B, most checks were now supported, contradicted or clearly unknown, rather than uniformly unknown.
- **Question: are some classes rejected on a property rather than on their definition?** Answer: yes. HedonicHarm was rejected because its acute trajectory conflicts with a ten-year debt; InterestSetbackHarm because the speaker perceives the losses; CollectiveEnvironmentalHarm because the text names one source.
- **Question: is the transparency property applied the same way across files?** Answer: no. On T2, the baseline and CONTROL C both rejected the rights classes on the transparency property, but the baseline accepted the root as a fallback and CONTROL C did not.

## Part 8. Interpretation
- **Question: does the property step do any work once values are readable?** Answer: yes. Readable values turn most checks into decisions, which confirms the NONCE B result: the structure is only usable when its values carry meaning.
- **Question: are the contradictions facts about the text?** Answer: no, they are interpretations. Rejecting a class because the speaker perceives a loss depends on reading `UnperceivedObjective` as "the victim is not aware of the harm," while the property's own definition says "objective harms occurring outside awareness." Whether a perceived loss can still be objective is a modelling choice the ontology has not settled, and the runs made it differently.
- **Question: does the structured prompt change which families of harm are found in the poem?** Answer: no. Across the baseline and CONTROL C, the poem's bodily and financial harms fall in the same families (experiential or interest-setback in one, capability or deprivation in the other). The structure changes which class within a family is chosen, not which family is found.
- **Question: is the rule for accepting a parent when no child fits applied consistently?** Answer: no. The root class was accepted in one T2 run and not in the other, so the fallback rule was applied differently across runs.
- **Question: can CONTROL C tell us whether labels matter separately from names?** Answer: not cleanly. Its names remain in the IRIs, so the model can read meaning from the names alone, and its value labels were lost in the build. Its results need caution. (CONTROL C2 was built to address this; see Part 11.)
- **Question: do the mappings improve on a vague request?** Answer: we cannot say yet. We have no expert judgment of which classes are correct for these texts, so the structure changes decisions and makes them traceable, but we cannot say the changes are improvements.

## Part 9. Limitations
- One run per cell. The T2 fallback difference and any single class choice could be variance.
- CONTROL C is not a clean control (see Part 2).
- Contradicted properties depend on the model's reading of each value; the reading was not checked against an expert.
- Subagent isolation is not proven (see Part 5).
- No outcome measure: we cannot test the pragmatic criterion (whether the mapping leads to a better judgment) without expert ground-truth cases.

## Part 10. Next steps
1. Rebuild CONTROL C with value labels kept, so it isolates names from narrative. Then rerun the structured prompt on it.
2. Write a small set of expert ground-truth judgments for the five texts, so the classes can be scored against something other than the model's agreement with itself.
3. Settle how `UnperceivedObjective` should be read, and record that as a design decision, since the runs disagreed on it.
4. Repeat each cell two or three times to measure variance.

## Part 11. CONTROL C2 (names and labels kept, definitions only)

CONTROL C2 was rebuilt to fix the label flaw in CONTROL C: all 72 value individuals carry a label or definition, real names are kept, and only `skos:definition` remains as narrative. Structure is intact (879 triples). The file is `Interdisciplinary Harm Ontology v1 - CONTROL C2 (names and labels kept, definitions only).ttl`. The original CONTROL C is kept unchanged.

**Session IDs (C2, mapped by content)**

| Text | Session |
|---|---|
| Poem | `ses_de9c2a208ffeVAgBNV6k51z48L` |
| T1 | `ses_de9c29853ffevS9dvpgVlgSvuM` |
| T2 | `ses_de9c28ec5fferCRSoRLv5doYT3` |
| T3 | `ses_de9c28535ffeptnYzgP1d8J5pQ` |
| Control | `ses_de9c27bc7ffeWoQ4JDbQwUIxbz` |

**Accepted classes across the three files**

| Text | Baseline (full narrative) | CONTROL C (labels stripped) | CONTROL C2 (labels kept, definitions only) |
|---|---|---|---|
| Poem | InterestSetbackHarm; ExperientialHarm (parent) | CapabilityStructuralHarm; DeprivationHarm | PrivateTortiousHarm; ExperientialHarm (parent). InterestSetbackHarm rejected on UnperceivedObjective |
| T1 | SystemicCyberneticHarm (parent) with ExternalityCoordinationHarm; CapabilityStructuralHarm | ExternalityCoordinationHarm; CollectiveEnvironmentalHarm | ExternalityCoordinationHarm; SystemicCyberneticHarm |
| T2 | harm:Harm (root, by fallback) | none | none. Root not accepted; flagged as a judgment call |
| T3 | PerfectionistTeleologicalHarm; DeprivationHarm | PerfectionistTeleologicalHarm; InterestSetbackHarm | PerfectionistTeleologicalHarm; DeprivationHarm |
| Control | harm:Harm (root, by fallback) | InterestSetbackHarm | CollectiveEnvironmentalHarm |

**What C2 shows**
- **Question: do labels restore decidability?** Answer: yes. As in the baseline, most property checks now resolve, and the unknowns that dominated the NONCE B and CONTROL C runs largely fall away.
- **Question: does the narrative change the structured decisions, or only the labels?** Answer: the narrative changes them. C2 and the baseline differ only in narrative (scope notes, examples, history notes, notes and citations). Their accepted sets agree on one text out of five (T3). On the poem, T1 and the control they diverge. This is the opposite of the NONCE B conclusion, which could not test it because labels were absent.
- **Question: is the control's result the same as the baseline's?** Answer: no. On the control, C2 accepts CollectiveEnvironmentalHarm, which the baseline rejected on its perpetrator property. The same property is read differently when the narrative differs, which suggests the narrative shapes how the value is understood.
- **Question: is the parent fallback stable across files?** Answer: no. The baseline accepts the root for T2; C and C2 do not. The same rule produced different results across files.
- **Question: are the property rejections determined by the text alone?** Answer: no. C2 rejects InterestSetbackHarm because the speaker perceives the losses, and it accepts PrivateTortiousHarm on the same text. The decision depends on how `UnperceivedObjective` and related values are read, not on the text alone.

**Limits.** One run per cell. Baseline and C2 differ in narrative, so any difference is the narrative plus variance; the design cannot separate them. No expert ground truth, so we still cannot say which set is better.

## Related
- [[Nonce Test - Structured Prompt]]: the NONCE B structured runs, and the design of the prompt.
- [[Nonce Test - Initial]]: the first nonce test.
- [[Nonce Test - Relational]]: the hierarchy test.
- [[Design Decision - Vocabulary Placement - Narrative, OWL Classes or Mixed]]: the design question these tests inform.
