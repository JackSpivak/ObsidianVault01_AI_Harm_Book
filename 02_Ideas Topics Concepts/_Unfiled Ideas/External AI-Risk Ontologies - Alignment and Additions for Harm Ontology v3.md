---
fileClass: Idea
type: idea
status: seed
bookmark: draft
canonical_id:
territory: new
tags: []
aliases: [AIRO Alignment, External Ontologies Landscape, AIRO vs Harm Ontology]
created: 2026-11-16
---

# External AI-Risk Ontologies - Alignment and Additions for Harm Ontology v3

> [!todo] Feeds the migration plan
> Phase 2 crosswalk and the AIRO/VAIR to-do in [[Harm Ontology Migration Plan#Open to-dos]]. The comparison so far rests on search summaries, not on loading the files.

## Why this is distinct
- It surveys the published, open AI-risk and legal ontologies and sets out where [[Harm Ontology v3 - Draft Structure|Harm Ontology v3]] should **align** with them (reuse) and where it **adds** something they lack. [[HO-III.b Reusing Expert Domain Vocabularies]] states the reuse principle; this note names the actual vocabularies.

## Anticipated direction
- A machine-readable comparison: load the AIRO and DPV-RISK Turtle files (stored outside the vault) with rdflib in the `harm-ontology` environment and compare by meaning against the v1 `.ttl` and v3 skeleton.
- Crosswalk rows (`owl:equivalentClass`, `skos:closeMatch`, `skos:broadMatch`) from v3 to AIRO / DPV / VAIR IRIs.
- A clear statement of what v3 contributes beyond AIRO, possibly a book argument or publishable contribution.

## Conceptual territory
- New. It extends [[HO-III.b Reusing Expert Domain Vocabularies]] with named targets, and builds on the research in [[Advantages of a Harm Ontology vs Strict LLM Training]] and [[The Governance Gap - Training-Governed vs Ontology-Governed Harm]].

## Summary
- Several respected, open ontologies exist, most of them from one research community built around AIRO. None models harm the way this project does: AIRO models *risk management* (ISO 31000: risk source → consequence → impact), not what harm *is* or how it is *judged*.

### Landscape (as of 2026-11-16)
| Resource | Standing | Machine-readable | Covers |
|---|---|---|---|
| **AIRO**, ADAPT Centre (Golpayegani, Pandit, Lewis 2022) | Peer-reviewed, open, v1.0 | OWL/Turtle, w3id.org/airo, repo `DelaramGlp/airo` | Risk, RiskSource, Consequence, Impact (subclass of Consequence), ImpactArea, AISubject; EU AI Act + ISO 31000/31073 |
| **VAIR** | Draft, "no official standing" | Yes | Term taxonomy that fills AIRO |
| **W3C DPV**: RISK + AI extensions (v2.3, February 2026) | W3C Community Group report, not a W3C Standard | Yes | Consequences and impacts including "harm", positive consequences (benefits); has absorbed AIRO/VAIR; models the AI Act's risk definition |
| **AI Incident Database**: CSET harm taxonomy, GMF | Widely used | Database snapshot (formats unconfirmed) | Harm types and severity; goals, methods and failures |
| **MIT AI Risk Repository** | Widely cited | Spreadsheet/database, not OWL | 1,700+ risks; 7 domains / 24 subdomains; causal taxonomy |
| **LKIF-Core** | Established in AI & Law | OWL | Basic legal concepts; tort/harm only a planned extension |
| **IBM Risk Atlas Nexus** | Open source (unconfirmed this round) | Unconfirmed | Combines frameworks; reuses AIRO |

### Potential additions (what v3 offers that AIRO lacks)
Likely, pending a real comparison of the files:
1. **Theories of what harm is**: hedonic, interest-based, rights-based, flourishing/capabilities ([[Capability Approach - Sen and Nussbaum]]), Kantian, held as evaluative standards (HO-II.a).
2. **Legal doctrine inside the model**: *injuria sine damno*, *damnum absque injuria*, tort vs crime, remedial duty-bearers, judgment as assessment (HO-II.c). LKIF-Core leaves tort as future work.
3. **Fact separated from verdict**: no intrinsic harmfulness ([[HO-premise No Intrinsic Harmfulness]]); assessments from perspectives (HO-II.d) with horizons (HO-II.b); divergence as part of the record (HO-III.a). AIRO assumes consequences are negative.
4. **AI-specific mechanisms**: habituation and captured assent (HO-001), causal assemblies (HO-003), criticality and leverage (HO-004), phenomenality (HO-I.c), near-zero-cost replication.
5. **Missingness statuses** (HO-II.e) and narrative lineage (history notes, citations across disciplines).

### Alignments (where v3 should reuse, not reinvent)
| v3 element | Candidate external match | Likely mapping |
|---|---|---|
| Factor (Risk kind) | `airo:Risk`, `dpv:Risk` | close / broader |
| Factor / CausalRole (source) | `airo:RiskSource` | close |
| Effect | `airo:Consequence`, `airo:Impact`, DPV consequences/impacts | close; Impact narrower |
| Patient / affected party | `airo:AISubject`, DPV data-subject / stakeholder terms | close |
| Effect domain | `airo:ImpactArea` | close |
| Beneficial assessments | DPV positive consequences (Benefit) | related; v3 puts valence in the assessment, DPV in the term |
| Controls, mitigations, AI system, purpose, deployer | AIRO / DPV-AI | **import or reference**: v3 doesn't model these itself |
| LegalResponse, agents, rights, roles | LKIF-Core | reference |
| Severity and harm types for incidents | CSET taxonomy, MIT domains | `skos:` mapping for incident data |

All mappings are provisional until the files have been compared.

### Where AIRO/DPV are stronger
- Regulatory alignment (EU AI Act, ISO), institutional uptake through DPV, AI-system modelling and stable published identifiers.

## Original wording
> "what existing, respected, standardized, published, available ontologies available and in current use
>
> does this Interdisciplinary harm ontology add anything to the AIRO (AI Risk Ontology), is there an existing open source published compendium or machine readable version available for comparson"
- **Attribution:** Author

> "None that I found models harm the way your ontology does. AIRO models *risk management* (in the ISO 31000 sense: risk source → consequence → impact), not what harm *is* or how it gets *judged*. That's where your work adds something."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

> "AIRO assumes a consequence is negative. Your v3 says nothing is harmful in itself: judgments are made from perspectives, with time horizons, and disagreement between judgments is modelled as part of the record (HO-000, HO-II, HO-III.a). I found nothing like that in AIRO, VAIR or DPV."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

> "please record this as an idea note reflecting potential additions, external links, alignments to the Harm Ontology v3.   Include reflecting on this in the migration plan"
- **Attribution:** Author

- **Source:** Obsidian Copilot agent session, 2026-11-16 (`copilot/copilot-conversations/agent__are_you_able_to_find_a_conversation_segment_in_which@20261115_182550.md`).
- **External references** (from web search results; pages not opened, so details are unverified):
	- AIRO: [w3id](https://w3id.org/AIRO) · [parsed Turtle mirror](https://akswnc7.informatik.uni-leipzig.de/dstreitmatter/archivo/w3id.org/AIRO/2024.09.16-052348/AIRO_type%3Dparsed.ttl) · [paper (Zenodo)](https://zenodo.org/records/6821845) · [paper (IOS Press)](https://ebooks.iospress.nl/pdf/doi/10.3233/SSW220008) · [OECD catalogue](https://oecd.ai/en/catalogue/tools/airo-ai-risk-ontology) · [HART vocabulary](https://rsaniei.github.io/hart)
	- [VAIR](https://w3id.org/vair)
	- DPV: [DPV 2.3](https://w3c.github.io/dpv/2.3/dpv/) · [AI extension](https://w3c.github.io/dpv/2.3/ai) · [RISK extension](https://w3id.org/dpv/risk) · [EU AI Act](https://w3c.github.io/dpv/2.0/legal/eu/aiact)
	- AIID: [taxonomies](https://incidentdatabase.ai/taxonomies/) · [CSET v1](https://incidentdatabase.ai/taxonomies/csetv1) · [editors paper](https://arxiv.org/pdf/2409.16425)
	- [MIT AI Risk Repository paper](https://futuretech.mit.edu/publication/the-ai-risk-repository-a-meta-review-database-and-taxonomy-of-risks-from-artificial-intelligence)
	- LKIF-Core: [CEUR paper](https://ceur-ws.org/Vol-321/paper3.pdf) · [Wikipedia](https://en.wikipedia.org/wiki/Legal_Knowledge_Interchange_Format)

## Real-world examples
- DPV's absorption of AIRO/VAIR shows these vocabularies are converging into one community standard.

## Why it matters to the book
- If v3 adds the judgment layer that existing AI-risk ontologies lack, that addition is part of the book's argument: today's AI-risk standards record harm as a fixed consequence, not as a contested judgment.

## Open questions
- Does `airo:Consequence` or `dpv:Harm` build in negative valence by definition? If so, v3 can only map to it as `skos:closeMatch`, not `owl:equivalentClass`.
- Import AIRO's AI-system classes, or only reference their IRIs (HO-III.b: import only small cores)?
- Should v3 be offered back to the DPV community group as a judgment/assessment extension?

## Related
- [[Harm Ontology v3 - Draft Structure]]
- [[Harm Ontology Migration Plan]]
- [[HO-III.b Reusing Expert Domain Vocabularies]]
- [[Advantages of a Harm Ontology vs Strict LLM Training]]
- [[The Governance Gap - Training-Governed vs Ontology-Governed Harm]]
