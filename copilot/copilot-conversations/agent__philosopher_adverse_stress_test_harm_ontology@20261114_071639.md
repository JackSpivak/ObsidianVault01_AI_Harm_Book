---
epoch: 1794665799072
mode: agent
backendId: claude
sessionId: "e70339de-8f8c-4d0d-9527-1167eb96620d"
topic: "philosopher adverse stress test harm ontology"
model: '{"baseModelId":"default","effort":"low"}'
tags:
  - copilot-conversation
usage: '{"usedTokens":86016,"contextWindow":1000000,"inputTokens":2,"outputTokens":3,"cacheReadTokens":84592,"cacheWriteTokens":1419,"updatedAt":1794665870250}'
---

**user**: philosopher adverse stress test harm ontology
<!-- copilot-message {"notes":["Interdisciplinary_Harm_Ontology_Compendium.md","Interdisciplinary Harm Ontology.ttl"]} -->
[Timestamp: 2026/11/14 07:16:39]

**ai**: 

# Philosopher's adversarial stress test: Interdisciplinary Harm Ontology

**Scope:** I read all of `Interdisciplinary_Harm_Ontology_Compendium.md`. In `Interdisciplinary Harm Ontology.ttl` I read lines 1–565 in full and searched the rest only for property declarations. My verdict: the ontology is rich and well sourced, but its main sorting principle is incoherent. Below are the objections, most serious first.

---

## 1. The top-level classes are rival theories of what harm is, not kinds of harm

Meta-categories I–IV (experiential, welfare/interest, rights-based, flourishing/deprivation) are **competing answers to the same question**. They aren't distinct regions of harm, and their own definitions contradict each other:

- `ExperientialHarm` says: "what you do not experience cannot harm you"; it "excludes unperceived or posthumous setbacks."
- `WelfareInterestHarm` says: harm occurs "even if the victim never perceives the loss."

**Test case:** a covert AI system profiles a user who never finds out. Under I this is *not harm*. Under II it *is*. The ontology files both views as sibling subclasses of one `harm:Harm`, so it holds that this event both is and isn't harm. OWL won't flag this, because no classes are declared disjoint. But the meaning breaks: the parent definition ("a relational setback to … experience, … interests, … rights, … flourishing, or … equilibrium") is a disjunction of rival theories, not a concept.

**Fix:** move the theories out of the class tree. Model them as a separate SKOS scheme of *accounts* (e.g. `harm:assessedUnder harm:HedonicAccount`). Then one harm event can be assessed under several theories, and the verdicts can disagree. That disagreement is philosophically honest, and it's useful material for the book.

## 2. Kinds of harm, legal causes of action, remedies and mechanisms sit side by side as siblings

These are four different kinds of thing:

| Entry | What it actually is |
|---|---|
| `HedonicHarm`, `DeprivationHarm` | Philosophical **theories** |
| `PrivateTortiousHarm`, `WrongfulDeathConsortiumHarm`, `PublicCriminalHarm` | Legal **causes of action / jurisdictional classes** |
| `ParensPatriaePaternalisticHarm` | A **justification for state intervention**: harm *prevention*, not harm |
| `OpportunityCostChoiceHarm`, `ExternalityCoordinationHarm` | **Mechanisms** |

`ParensPatriae…` is the clearest category mistake. Compulsory schooling is not a harm. Worse, the ontology has no place for **paternalism itself as a harm** (overriding someone's autonomy), even though `KantianDeontologicalHarm` cites exactly that as an example in the TTL file (line 322). The same act appears once as a harm and once as protection from harm.

## 3. Harm and wrong are run together

The rights-based category says "A person is harmed simply by being wronged." That erases Feinberg's harm/wrong distinction, which the ontology itself relies on in `hasNormativeStatus`. `InjuriaSineDamnoHarm` is *by definition* a wrong without harm ("zero physical pain, financial loss, or emotional distress"), yet it is filed as a subclass of `Harm`. The label contradicts its own position in the tree. Meanwhile, `DignitaryRelationalHarm` is filed under *Experiential* but tagged `NormativeWrongful`, so it sits in two places at once.

**Fix:** make `Wrong` a separate top concept and model harm and wrong as two relations that can overlap: harmful wrongs, harmless wrongs, and harms that wrong no one.

## 4. The counterfactual baseline carries most of the weight but is never defended

Classes II and IV and most of the attribute bindings depend on comparing what happened with what would otherwise have happened. That comparison has well-known problems, none of which the ontology handles:

- **Pre-emption and overdetermination.** If system A harms you, but backup system B would have done the same, the counterfactual test says A did no harm. `OverdeterminedCausation` exists as a value, but nothing reconciles it with the counterfactual baseline.
- **Non-identity problem.** It is listed under "Domains of Applicability" and then never addressed. Harms to future generations (filed under `NonSentientSystem`, see §6) fail the counterfactual test, because those people would not exist otherwise.
- **Omissions.** On a pure counterfactual account, every failure to help counts as harm. `DeprivationHarm` is subtitled "Harm by Omission," and nothing separates harming from failing to benefit.
- **Missing alternative.** Non-comparative accounts (Shiffrin, Harman) define harm as being *in* a bad state, not worse off than a baseline. They are absent, and they handle the cases above better.

## 5. Meta-category V is not a kind of harm

`SystemicCyberneticHarm` sorts harms by **causal structure** (feedback, emergence, scale). That is exactly what attribute Domain B (`hasFeedbackDynamics`, `hasScalabilityAsymmetry`) and `hasIncentiveAlignment` already describe. So the tree sorts by *theory of harm* in I–IV and by *how harm is produced* in V. One structural feature is encoded twice, which guarantees overlap. Algorithmic hiring bias could go in V.3, II.7, III.3 or IV.3, and there is no rule for choosing.

**Manipulation** has the same problem. It appears in `KantianDeontologicalHarm`, `OpportunityCostChoiceHarm` and `EpistemicPollutionHarm`, with no criterion to tell them apart.

## 6. Who can be harmed, and who does the harming, is muddled

- `NonSentientSystem` puts "future unconceived generations" next to rivers. Future people aren't non-sentient; they don't exist yet. That is a completely different problem.
- **AI systems as possible moral patients are missing.** For a book about AI harm, that is a notable gap, whatever your view on model welfare.
- `NonAgenticAutonomousSource` lumps "natural forces" together with "autonomous AI systems." That builds in a contested answer to the **responsibility gap**: it treats AI like weather. A book on AI harm probably wants that question kept open.

## 7. The gap that matters most for your book: emptied-out agency

The excerpt you attached (002.II.a) describes "nominal human authority ≠ meaningfully exercised authority." **No class captures this.** The nearest candidates each miss it:

- `PerfectionistTeleologicalHarm` relies on a contested "natural function," and it has no mechanism for how this happens.
- `OpportunityCostChoiceHarm` requires *suboptimal* choices. A rubber-stamping human may approve good outputs and still be harmed.
- `KantianDeontologicalHarm` requires coercion, deception or manipulation. Automation bias involves none of them, because the person *chose* to rely on the system.

The missing concept is harm through **consensual, beneficial-seeming dependence**: deskilling, eroded judgment, hollowed-out accountability. Arguably this is the signature harm of AI, and the ontology has nowhere to put it. I'd treat it as a candidate core concept for the book, not just a gap in the ontology.

Related omissions:
- harm to groups *as groups* (cultural erasure; Young's structural injustice is cited only through Galtung)
- complicity
- consent as something that cancels harm (*volenti*)
- offsetting benefits
- homogenization of thought or culture

## 8. Technical defects in the TTL file

- **Broken prefixes (serious):** `owl:`, `rdf:`, `rdfs:` and `skos:` all point to `<http://w3.org>`, so `owl:Class`, `rdfs:Class` and `skos:Concept` all resolve to wrong IRIs. `harm:` is `<http://example.org>`, which is also the ontology's own IRI, while the Compendium says `http://example.org/ontology/harm#`. No reasoner will read this file correctly.
- **Properties are attached directly to classes** (OWL "punning"). Subclasses therefore don't actually inherit anything. Inheritance would need `owl:Restriction` / `owl:someValuesFrom`.
- **Bindings that contradict their own examples:**
  - `ProbabilisticRiskHarm` is tagged `BlackBoxOpaque`, but carcinogen exposure isn't opaque.
  - `HedonicHarm` is tagged `UnitaryIntentionalAgent` + `AcuteTrajectory`, which excludes slow, unintended grief.
  - The rights-based category defaults to `ActualizedHarm`, which excludes Thomson's risk-imposition, even though Thomson is cited in II.5.
  - `EpistemicTestimonialHarm` is tagged `UnperceivedObjective`, but hermeneutical injustice is often acutely *felt*.

## 9. Citations to check (from my memory, all unverified)

- Brignull's *Deceptive Patterns* is a 2023 book. He coined "dark patterns" in 2010.
- Hohfeld's 1913 work is a *Yale Law Journal* article. The book *Fundamental Legal Conceptions* came out posthumously in 1919.
- Simon (1971) didn't coin the phrase "attention economy." The coinage is usually credited to Goldhaber (1997).
- Devlin is a *legal moralist*, not a parens patriae theorist. Citing him there supports the category confusion in §2.
- Bork's consumer welfare standard is an odd thing to cite *for* diffuse harm, since critics argue it narrowed what antitrust counts as harm.
- The tort-law "Austin" in the `InjuriaSineDamnoHarm` history note (Compendium only) has no citation.

---

## Recommendation

Rebuild the ontology around three independent axes instead of one tree:

1. **Accounts:** how harm is assessed (hedonic, comparative, non-comparative, rights-based, flourishing-based). Model these as a SKOS scheme, not as OWL classes.
2. **Phenomena:** what happened (pain, loss, exclusion, deception, eroded agency, and so on).
3. **Legal vehicles and remedies:** causes of action, doctrines, duty-bearers.

Keep the 19 attributes; they are the strongest part.

**Possible next steps:**
- Save this stress test as a session note in `01_The Writer's Room/`.
- Draft "agency hollowing / consensual dependence harm" as an idea note.
- Fix the TTL prefixes.
- Log the three-axis decision in `Decisions_Log.md` if you adopt it.
<!-- copilot-message {"tools":["Read (read): Interdisciplinary_Harm_Ontology_Compendium.md","Read (read): Interdisciplinary Harm Ontology.ttl","Grep (read): Interdisciplinary Harm Ontology.ttl"]} -->
[Timestamp: 2026/11/14 07:16:39]