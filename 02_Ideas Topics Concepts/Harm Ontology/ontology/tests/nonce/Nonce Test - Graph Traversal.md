---
type: research
status: developing
tags: [ontology/harm, test, nonce, traversal, sparql]
aliases: [Nonce Test Graph Traversal, Traversal Test]
created: 2026-11-25
test_date: 2026-11-25
ontology_tested: "Interdisciplinary Harm Ontology v1.ttl (baseline: full narrative, value labels)"
runs: "Two stages, five texts. Stage 1: five candidate-proposal runs. Stage 2: five decision runs on fixed query results. One run per cell."
related_tests: "[[Nonce Test - Graph Queries (for review)]], [[Nonce Test - Structured Prompt - Baseline and Control]]"
---

# Nonce Test: Graph Traversal

## Purpose
Test whether querying the ontology's relations (fixed SPARQL, run by rdflib on the TTL) changes what the model finds, compared with reading the file as text. This record covers the traversal condition only. The model-only comparison and expert judgments come later.

## Design
- **Stage 1 (candidates, no queries).** For each text, the model read the baseline file and listed every class whose `skos:definition` the text could plausibly trigger, with parents and children as separate rows. No harm was decided.
- **Candidate selection (my choice).** For stage 2 I kept the strong triggers and their parents from stage 1, so the result set stayed readable. This is a selection I made, and it shapes what stage 2 could assess (see Limitations).
- **Stage 2 (queries and decisions).** Fixed queries ran on the selected nodes, and the rows were written to files outside the vault (`%TEMP%\nonce_build\stage2\`). For each node: direct parent, direct children, ancestors, and every triple on the node with its value's label and definition. Each stage-2 model read only its result file and the text, and reported one row per HarmDetermination.

## Texts
Five texts were run, each as its own separate test. The table labels them as follows. Every quote in the results comes from its own text, and I checked each one against it.

- **Poem:** "Whitey On The Moon" (the full poem from the original naive run).
- **T1 (systemic decline):** "Every year more families left the district because the school was weaker, and every departure made the school weaker still, until the building closed. No one decided this, and no single act caused it."
- **T2 (rights denial):** "The official told her that the rules did not apply to people like her. Nothing was taken from her, yet her standing as someone entitled to the same protection was denied."
- **T3 (deprivation):** "A young man was kept from the training his talent called for. No blow was struck. The life he would have grown into never came to be."
- **Control (factory discharge):** "The factory's discharge has spread across the river valley. Each household's small loss adds to a total that no one carries alone."

T1, T2, T3 and the control are the short texts from the relational test. They were not part of the poem, and they were not run together with it.

## Stage 1 session IDs

| Text | Session |
|---|---|
| Poem | `ses_de9abee1affe8ZfIjv3rQYBOsW` |
| T1 | `ses_de9abe982ffeXUtM479ls94rlF` |
| T2 | `ses_de9abe4d1ffeAVKgo6nPM0TDwp` |
| T3 | `ses_de9abe070ffeA3vGk97phh2FRH` |
| Control | `ses_de9abdc1fffe4vVxCk6bsXfNmE` |

## Stage 2 session IDs

| Text | Session |
|---|---|
| Poem | `ses_de9ab0f60ffex82Q9TiiNAHnXo` |
| T1 | `ses_de9ab0e9affe0DbX2KpL2KBIMN` |
| T2 | `ses_de9ab0dceffeuvB29uKBnCww1A` |
| T3 | `ses_de9ab0d0cffeXxVa3Zt47wo4EU` |
| Control | `ses_de9ab0c30ffeV5wjyih38U8CxT` |

## Results: accepted HarmDeterminations

Expert and provenance columns are left blank. They are filled after review.

| Text    | #   | HarmDetermination                                                            | Text example(s)                                                           | Harm type (class)                             | Node IRI                             | Node name                     | Parent / child                                         | Model confidence                                  | Key property evidence                                                                                                                                     | Expert verdict | Expert-preferred class | Provenance of quoted definition |
| ------- | --- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------ | ----------------------------- | ------------------------------------------------------ | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------- | ------------------------------- |
| Poem    | 1   | Suffering from the bite, the illness and the distress                        | "Her face and arms began to swell"; "Junkies making me a nervous wreck"   | Experiential, subjective harm                 | `harm:HedonicHarm`                   | HedonicHarm                   | Child of ExperientialHarm (parent not needed)          | High (category); medium (trajectory, perpetrator) | DirectPrimaryVictim, ActualizedHarm, SomaticBiologicalSubstrate supported. AcuteTrajectory partly supported; the ten-year debt points the other way.      |                |                        |                                 |
| T1      | 1   | Collective-action trap: each departure worsens the school for those who stay | "every departure made the school weaker still"; "No one decided this"     | Negative externality and coordination failure | `harm:ExternalityCoordinationHarm`   | ExternalityCoordinationHarm   | Child of SystemicCyberneticHarm                        | High (trap); medium (victim, duty-bearer)         | NonLinearAmplifying and StructurallyAlignedEmergent supported; DiffuseCollectivePerpetrator supported ("no single act")                                   |                |                        |                                 |
| T1      | 2   | Slow, diffuse erosion of a shared institution                                | "Every year more families left"; "until the building closed"              | Collective environmental harm                 | `harm:CollectiveEnvironmentalHarm`   | CollectiveEnvironmentalHarm   | Child of WelfareInterestHarm (separate branch from #1) | Medium                                            | SlowAccumulativeTrajectory, DiffuseThreshold supported. Whether a school counts as a shared ecosystem is not settled.                                     |                |                        |                                 |
| T1      | 3   | Structural privation of a functioning school                                 | "the school was weaker … until the building closed"                       | Teleological deprivation                      | `harm:TeleologicalDeprivationHarm`   | TeleologicalDeprivationHarm   | Standalone                                             | Low                                               | No active injury fits. The "ought naturally to possess" step is not in the text.                                                                          |                |                        |                                 |
| T2      | 1   | Denied equal standing under the rules                                        | "the rules did not apply to people like her"; "her standing … was denied" | Kantian (dignitary) harm                      | `harm:KantianDeontologicalHarm`      | KantianDeontologicalHarm      | Child of DeontologicalRightsHarm; sibling of #2        | Medium                                            | NormativeWrongful, NormativeStatusSubstrate supported. UnperceivedObjective unknown.                                                                      |                |                        |                                 |
| T2      | 2   | Rights violation with no loss                                                | "Nothing was taken from her, yet…"                                        | Injuria sine damno                            | `harm:InjuriaSineDamnoHarm`          | InjuriaSineDamnoHarm          | Child of DeontologicalRightsHarm; sibling of #1        | Medium                                            | Zero loss stated in the text. Severity and remedy unknown.                                                                                                |                |                        |                                 |
| T3      | 1   | Loss of the future life he would have grown into                             | "The life he would have grown into never came to be."                     | Deprivation                                   | `harm:DeprivationHarm`               | DeprivationHarm               | Child of TeleologicalDeprivationHarm; sibling of #2    | Medium                                            | CounterfactualBaseline, IrreversibleHysteresis supported. SomaticBiologicalSubstrate partly contradicted by "No blow was struck"; kept on its definition. |                |                        |                                 |
| T3      | 2   | Blocked development of a talent                                              | "kept from the training his talent called for"                            | Teleological harm (perfectionist)             | `harm:PerfectionistTeleologicalHarm` | PerfectionistTeleologicalHarm | Child of TeleologicalDeprivationHarm; sibling of #1    | Medium-high                                       | OpportunityCapabilitySubstrate supported. UnperceivedObjective unknown.                                                                                   |                |                        |                                 |
| Control | 1   | Setback to household resources, aggregated over the valley                   | "Each household's small loss adds to a total that no one carries alone"   | Welfare and interest-based harm               | `harm:WelfareInterestHarm`           | WelfareInterestHarm           | Parent (accepted because no child was)                 | Medium                                            | Counterfactual and perception values unknown.                                                                                                             |                |                        |                                 |

## Rejected candidates

- **Poem:** InterestSetbackHarm and WelfareInterestHarm (UnperceivedObjective contradicted). CapabilityStructuralHarm and ExternalityCoordinationHarm (DiffuseRepresentativeClass contradicted). TeleologicalDeprivationHarm (UnperceivedObjective contradicted). SystemicCyberneticHarm (definition not triggered).
- **T1:** CapabilityStructuralHarm (not clearly triggered). InterestSetbackHarm and DeprivationHarm (definition not triggered). WelfareInterestHarm and SystemicCyberneticHarm (parents not needed).
- **T2:** DignitaryRelationalHarm, InterestSetbackHarm, WelfareInterestHarm (definition not triggered). Harm (parent, not needed). EpistemicTestimonialHarm, FiduciaryBetrayalHarm and several others were not assessed (not in the query results).
- **T3:** CapabilityStructuralHarm (definition not triggered). InterestSetbackHarm (borderline; vital stakes not named). Parents not needed.
- **Control:** CollectiveEnvironmentalHarm and ExternalityCoordinationHarm (DiffuseCollectivePerpetrator contradicted, because the text names one factory).

## Observations

- **Inconsistent verdicts on the same node and property.** InjuriaSineDamnoHarm was rejected on `UnperceivedObjective` in the earlier structured run on this file, and accepted here, where that property was unknown. The same property was contradicted in one run and unknown in another.
- **The same property read differently across texts.** DiffuseCollectivePerpetrator was contradicted for the control ("the factory") and supported for T1 ("no single act caused it").
- **Coverage depends on the candidate selection.** Several rejections in stage 2 are "not assessed," because I did not include those nodes in the query results. That is a selection effect I introduced.
- **Reading of the query results is the model's.** The queries return rows; the decisions are the model's reading of those rows.

## Limitations
- One run per cell.
- Candidate selection was mine, not the model's and not a fixed rule. Nodes outside the selection were never assessed.
- Provenance of quoted definitions has not yet been checked by script. The quotes are from the query rows, so they should match, but this is not yet verified.
- No expert verdicts yet. Without them the table measures the traversal's internal consistency and output, not correctness.

## Next steps
1. Fill the expert columns (verdict, preferred class) for each row.
2. Run the provenance check on each quoted definition against the file.
3. Add unmapped harms, which the expert identifies, as a separate list. These measure coverage.
4. Run the model-only condition on the same candidate set, so the comparison is like for like.

## Related
- [[Nonce Test - Graph Queries (for review)]]: the fixed queries used in stage 2.
- [[Nonce Test - Structured Prompt - Baseline and Control]]: the earlier structured-prompt results on the same file.
- [[Nonce Test - Initial]]: the first nonce test.
