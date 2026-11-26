---
type: research
status: developing
tags: [ontology/harm, test, nonce, epistemics]
aliases: [Nonce Test v1, Nonce Test Results, nonce-test-initial, Nonce Test - Interdisciplinary Harm Ontology v1 - Design, Build and Results]
created: 2026-11-25
test_date: 2026-11-25
ontology_tested: "Interdisciplinary Harm Ontology v1.ttl (version 1.0.3)"
runs: "Single run per condition (four runs). Repeats not yet done."
---

# Nonce Test: Interdisciplinary Harm Ontology v1

## Purpose
Test whether a language model maps a text onto an ontology by reading the ontology's definitions, or by drawing on what it already knows about harm. The test asks: when the class names are hidden and the narrative is reduced, do the mappings hold?

## Part 1. Discussion that led to the design
- **The naive run.** A fresh chat, with the v1 TTL loaded and the instruction to use only what the ontology provides, mapped a mixed text (war reporting, poems, song lyrics) onto the ontology. The results were judged good. Three open questions followed:
  1. v1 had harm classes explicitly, so the run may have been reading class names.
  2. It was unclear whether the TTL carried narrative (SKOS definitions, descriptions, notes) on the harm classes.
  3. The instruction "map the text to the ontology" was casual and set no process. The model may have predicted matches rather than run a logical query.
- **The epistemic concern.** Structured SPARQL queries over SKOS-stored richness need prior knowledge of the case. A query can find only the richness the querier already knows to ask about. This was tested against the naive run to see whether the same trap is avoided.
- **Checking question 2.** The v1 file carries `skos:definition`, `skos:altLabel`, `skos:scopeNote`, `skos:historyNote` and `skos:example` on the harm classes. The narrative was therefore present in the naive run.
- **The nonce idea.** If the model reads definitions, replacing class names with neutral codes should not change its matches. If it draws on training, names or theorists outside the file would start to appear.
- **Design change.** Building the first two files showed that a single "names removed" file also removed definitions, so it could not separate the effect of names from the effect of narrative. A two-by-two design was adopted:

| | Full narrative | Definitions only |
|---|---|---|
| **Real names** | Baseline (the naive run's file) | CONTROL C |
| **Coded names** | NONCE A | NONCE B |

## Part 2. How the alternative files were made
- **Source.** `Interdisciplinary Harm Ontology v1.ttl`, version 1.0.3. 1,086 triples in total.
- **Build.** A Python script run with rdflib in the `harm-ontology` conda environment. The script lives outside the vault, in `%TEMP%\nonce_build\build_nonce.py`. It does not write any scratch files into the vault.
- **Codes.** Every node in the `harm:` namespace (classes, properties, individuals, values) was given a code, `H-001` to `H-125`. Codes follow the order in which each name first appears in the file, so they carry no alphabetical hint. The key maps each code to its original name.
- **What was removed, by file:**
  - In every file: `skos:prefLabel`, `skos:altLabel` and `skos:changeNote` (names and file history).
  - In NONCE B and CONTROL C: `skos:note`, `skos:scopeNote`, `skos:historyNote`, `skos:example` and `dcterms:bibliographicCitation`. Only `skos:definition` remains as narrative.
  - Structure is kept in every file: `rdfs:subClassOf`, `skos:broader`, domain and range, and property assertions. The relations test depends on this.
- **Leak scan.** The build checks whether any original name still appears as a whole word. The scan found only the English word "Harm" in both NONCE files. It appears in ordinary definitions, such as "Harm to a person's reputation...". I did not rewrite it, because that would change the content under test. CONTROL C was not scanned, because its names are kept by design.
- **Residuals.** The `harm:` prefix remains. Names inside definitions and scope notes can remain, for example "Teleological Harm".

| File | Names | Narrative | Triples |
|---|---|---|---|
| Interdisciplinary Harm Ontology v1 (Baseline) | real | full | 1,086 |
| NONCE A | coded | full | 861 |
| NONCE B | coded | definitions only | 657 |
| CONTROL C | real | definitions only | 657 |

The three files derived from the source are in this folder. The baseline is the original file in `ontology/`. The key, `KEY - do not load for the test.csv`, must not be loaded when running the test.

## Part 3. Protocol
- **Prompt, used identically in all four runs:**
  > Using only the things and relations provided in the loaded ontology, and explicitly using no context, content, or weights based on training within your model, map the text below onto the ontology and provide an analysis, including a tabular output of the harms found in the text.
- **Isolation.** Each run was a separate subagent with one ontology file and the text. Each was told not to read any other vault file, not to read the key, and not to use the web. Subagents share the vault's tools, so these instructions are the only barrier; the outputs show no sign of other files being used, but this is not proven.
- **Text.** The poem "Whitey On The Moon", one of the texts from the original naive run. The original run also included war reporting and song lyrics, so these results are not directly comparable with the naive run. Full text, as run (the source chat export ran the lines together, so the line breaks below are not the original layout):
> We have a poem here, it's called "Whitey On The Moon"It was inspired by some whiteys on the moonSo I wanna give credit where credit is due[Verse]A rat done bit my sister NellWith whitey on the moonHer face and arms began to swellAnd whitey's on the moonI can't pay no doctor billsBut whitey's on the moonTen years from now I'll be payin' stillWhile whitey's on the moonThe man just upped my rent last nightCause whitey's on the moonNo hot water, no toilets, no lightsBut whitey's on the moonI wonder why he's upping me?Cause whitey's on the moon?Well I was already giving him fifty a weekWith whitey on the moonTaxes taking my whole damn checkJunkies making me a nervous wreckThe price of food is going upAnd as if all that shit wasn't enough:A rat done bit my sister NellWith whitey on the moonHer face and arm began to swellAnd whitey's on the moonWas all that money I made last yearFor whitey on the moon?How come I ain't got no money here?Hmm! Whitey's on the moonY'know I just 'bout had my fillOf whitey on the moonI think I'll send these doctor billsAirmail specialTo whitey on the moon
- **Session IDs** (for tracing the subagent transcripts):
  - Baseline: `ses_deb62792dffevZch84kB7WdO7r`
  - NONCE A: `ses_deb626e96ffeA60lL0nmduOog4`
  - NONCE B: `ses_deb6264f0ffeVbjcaH0VDJjrzK`
  - CONTROL C: `ses_deb625ba7ffe37I2iEEEDJXwa8`

## Part 4. Results
Harm mappings (decoded against the key where a code was used):

| Harm in text | Baseline | NONCE A (coded) | NONCE B (coded, definitions) | CONTROL C (names, definitions) |
|---|---|---|---|---|
| Rat bite: pain and swelling | InterestSetbackHarm (HedonicHarm alternative) | H-009 HedonicHarm; H-044 PrivateTortiousHarm rejected as low | H-041 InterestSetbackHarm, with H-009 | HedonicHarm |
| Medical debt, lost earnings | InterestSetbackHarm | H-041 | H-041 | InterestSetbackHarm |
| Emotional distress | HedonicHarm | H-009 | H-009 | HedonicHarm |
| Rent rise, no water, toilets or lights | InterestSetbackHarm, or CapabilityStructuralHarm | H-082 CapabilityStructuralHarm; H-030 rejected | H-059 ProbabilisticRiskHarm, with H-044 | ExpectationRelianceHarm and DeprivationHarm |
| Taxes, rising food prices | InterestSetbackHarm | H-041; H-068 CollectiveEnvironmentalHarm (low) | H-068 (low) | no class supported |
| Group blame ("whitey on the moon") | unmapped | unmapped | unmapped | unmapped |
| Causal attribution to the moon | unmapped | unmapped | unmapped | unmapped |
| Narrator's distress about Nell | not separately mapped | H-027 considered, rejected | not mapped | not mapped |

**What held across all four runs**
- The core classes were stable. Distress mapped to HedonicHarm (H-009 in the coded files). Financial and health setbacks mapped to InterestSetbackHarm (H-041 in the coded files).
- Group-directed blame and the causal attribution to the moon were left unmapped in every run. The file has no class for them, and no run invented one.
- No run named a theorist, a harm class or a concept that is absent from its file.
- NONCE A's rejections cite scope notes and definitions, for example rejecting H-030 because the text describes no sensory interference.

**Where the runs diverged**
- Housing and utilities were the least stable region. Each run chose a different class (CapabilityStructuralHarm, ProbabilisticRiskHarm, ExpectationRelianceHarm, DeprivationHarm, PrivateTortiousHarm). These classes are not interchangeable, so the ambiguity is in the file, and each run resolved it differently.
- The taxes and food-price row was matched by some runs and not by others.

**What the results suggest**
- Removing the real names did not change the core matches (Baseline against NONCE A).
- Removing the history and scope notes did not change the core matches either (NONCE A against NONCE B). The definitions carried most of the matching. The notes contributed mainly to rejections.
- There is no sign of training leaking in as names or theorists. The results are still consistent with a model drawing on training to choose between close matches; the test cannot separate that case.

## Part 5. Limitations
- **One text, one run per condition.** The housing divergence could be run-to-run variance rather than a condition effect. Repeats are needed.
- **Subagent isolation is not proven.** See the isolation note in Part 3.
- **Relations are untested.** No run needed a parent class as the answer, so nothing here shows the model follows `subClassOf` links.
- **Some details in the outputs are unverified.** NONCE A describes H-100 as a concept scheme, but the key shows H-100 is `CausationMechanismValue`. Line counts reported by the subagents differ from one another, and they were not checked.
- **The leak scan is shallow.** It checks whole-word matches for original names. It does not check paraphrases of the names or the content of the definitions.
- **The text is one poem.** The original naive run used more texts, so these results can't be compared with it directly.

## Part 6. Next steps
1. Repeat each of the four conditions twice more to measure variance.
2. Build the relations test: a text whose only supporting evidence sits at a parent class, so the answer depends on following `subClassOf`.
3. Run the same protocol on the full original text set, to compare with the naive run.
4. Decide whether the nonce script should be copied into `ontology/scripts/` so the build can be reproduced.

## Related
- Ontology files in this folder: NONCE A, NONCE B, CONTROL C (see Part 2).
- Baseline: `../Interdisciplinary Harm Ontology v1.ttl`
- Vocabulary placement, the question this test informs: [[Design Decision - Vocabulary Placement - Narrative, OWL Classes or Mixed]]
- Session record of the discussion: [[2026-11-24 Harm Ontology Common Schema and DUL Alignment Session]]
