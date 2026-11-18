---
epoch: 1794988172008
mode: agent
backendId: claude
sessionId: "841afc39-c000-456b-b41a-2172cc5d1fea"
topic: "read harm ontology v3 handoff. rename chat to Harm Ontology…"
model: '{"baseModelId":"default","effort":"low"}'
tags:
  - copilot-conversation
usage: '{"usedTokens":113235,"contextWindow":1000000,"inputTokens":2,"outputTokens":5,"cacheReadTokens":110343,"cacheWriteTokens":2885,"updatedAt":1794990943841}'
---

**user**: read harm ontology v3 handoff.  rename chat to Harm Ontology v3 testing
<!-- copilot-message {"notes":["01_The Writer's Room/Handoff - Harm Ontology.md"]} -->
[Timestamp: 2026/11/18 00:49:32]

**ai**: I read the handoff. **I can't rename the chat.** Copilot names chats itself, and I have no tool that changes that. You can rename it from the Copilot chat history. Copilot also saves this conversation as a file, currently named `copilot/copilot-conversations/agent__read_harm_ontology_v3_handoff._rename_chat_to_Harm_Ontology@20261118_004932.md`. I can rename that file to something like `agent__Harm_Ontology_v3_testing@20261118_004932.md` if you want, but Copilot may keep writing to the old filename. Should I?

**Where things stand ([[Handoff - Harm Ontology]]):**
- The v3 design is drafted in [[Harm Ontology v3 - Draft Structure]]. No v3 `.ttl` file exists yet, and **nothing has been tested**.
- **Open item (2026-11-18):** "assessment-everywhere". This means treating almost every attribute as a judgement from a perspective, with "fact" as a status (an Observation that is settled). The risk you raised: naive queries quietly drop disputed or unassessed cases. Suggested fixes: shortcuts that carry a status, named query views, and SHACL as a safety net.
- **Test plan:** [[HO-002.a Assessment-Everywhere Test Strategy]] (CQ1–CQ8, plus CQ9). Pre-test steps 1–2 are done. **Next is step 3:** work out variant B in detail, **starting with the agreement rule** (what counts as "agree"). After that come the variant A baseline, a toy case, tooling, and a protocol for testing with non-experts.
- **Other next steps:** continue Migration Phase 0, or run the Horizon (R01) re-attribution test.
- **Cautions:** treat "blocks" claims as hypotheses, don't log pending items until they're tested, many references are unverified, and watch for momentum.

Since this chat is for v3 testing, I suggest we start with step 3: the agreement rule. Should I open HO-002.a and the draft structure and propose some options?
<!-- copilot-message {"tools":["Read (read): 01_The Writer's Room/Handoff - Harm Ontology.md"]} -->
[Timestamp: 2026/11/18 00:49:32]

**user**: yes
[Timestamp: 2026/11/18 00:50:10]

**ai**: Here's a proposal for the agreement rule. I haven't changed any notes yet.

## Starting point
Your rule v0 in [[HO-002.a Assessment-Everywhere Test Strategy]] is **"same verdict under the same procedure."** To run as a test, it has to settle five questions it doesn't yet answer.

### 1. Same claim: when are two assessments about the same thing?
- **A (recommended):** two assessments agree only if they share the same target, the same attribute, and the same scope (time window, Patient). Example: "severe for workers, 2010–2015" and "severe for the company" are *different claims*, not a disagreement.
- B: same target and attribute only. This is simpler, but it creates false disputes.

### 2. Same verdict: how do values compare?
- **Categorical values** (Harmful / Not harmful): exact match.
- **Graded or ordinal values** (severity, reversibility). Options:
  - (a) exact match
  - (b) **same band** (recommended): each procedure maps its scale onto a shared coarse band, and agreement is on the band
  - (c) within a tolerance
- **Recommendation:** use (b), and keep the original value on each assessment so no detail is lost. Otherwise the agreement rule quietly turns fine grades into a crude scale.

### 3. Same procedure: what counts as "the same"?
- **A (recommended):** the procedure has an identifier and a version. Assessments agree only under the same procedure *and version*. A different version means "not comparable", not "disputed".
- B: same procedure family (e.g. any clinical severity scale). This is looser and invites false settlement.
- This also makes `standardBasis` matter. Under v0, `Implicit` and `None` assessments **can never settle anything**, because they have no shared, checkable procedure. I think that's correct, but it's a strong consequence and you should decide it knowingly.

### 4. Who counts: which perspectives are in scope, and what about silence?
This is where silent omission comes back in.
- **Scope:** the perspectives in scope have to be **declared** for each view or query, never left implicit. Otherwise "settled" just means "settled among whoever we happened to include".
- **Abstention:** a perspective in scope that uses the procedure but hasn't assessed the claim:
  - (a) is ignored, so a single assessor settles the claim alone
  - (b) **blocks settlement** (recommended): the status becomes `PartiallyAssessed`, not Settled
- **Minimum number:** require at least 2 independent assessments to settle? (Recommended: yes. One assessment alone is `SingleSource`.)
- This suggests the status set needs widening:

| Status | Meaning |
|---|---|
| Settled(value) | ≥2 in-scope perspectives using the same procedure agree, none disagree, each has an evidence pointer |
| Disputed | at least two conflicting verdicts under the same procedure |
| Incommensurable | verdicts exist, but under different procedures or versions, so they can't be compared |
| SingleSource | only one assessment |
| PartiallyAssessed | some in-scope perspectives haven't assessed it |
| NotAssessed | no assessments |

The risk is that six statuses become a burden. They could collapse back into the original three for display (Settled / Disputed / NotAssessed), with the finer status available underneath. That's the version I'd test.

### 5. Time: which assessment counts?
- **Recommended:** for each perspective, use its **latest** assessment as of the query date. Settlement is recalculated, never stored as fixed. A newer dissent reopens the claim automatically, which is what CQ4 tests.
- An "as of" date parameter lets you ask "was this settled in 2012?" That fits Horizon well.

### Also needed: the evidence anchor
Under rule v0, a claim can be Settled only if **every** agreeing assessment has an evidence pointer. That's what keeps "settled" from being just a matter of opinion. Disagreement about the *evidence itself* (e.g. disputed Horizon logs) would be a separate Disputed claim about the Observation.

## Hard cases to put in the toy case
1. Two perspectives agree on the verdict for **different reasons** (same severity, different standards). Is that Settled? My suggestion: yes on the value, with the divergence in standards recorded.
2. A court ruling vs a later appeal from the same perspective type (same procedure, verdict reversed). This tests point 5.
3. A Horizon-like case: the institution's own procedure says "user error", an independent forensic procedure says "system error". Different procedures give **Incommensurable**, not Disputed. Is that what you want a naive "who caused it?" query to show? I suspect you'd rather see "Disputed". If so, point 3 needs an exception for causal questions.

## My recommendation
Agreement rule v1 = 1A + 2b + 3A + 4 (declared scope, abstention blocks settlement, ≥2 assessments) + 5 (latest assessment, recalculated as of a date) + evidence required, with the statuses collapsed to three for display. Hard case 3 is the real open question.

What do you think, especially about hard case 3? Once you've decided, I can record rule v1 in HO-002.a under Author decisions.
<!-- copilot-message {"tools":["Glob (read)","Read (read): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md","Grep (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md"]} -->
[Timestamp: 2026/11/18 00:50:10]

**user**: does B make standard basis matter? is that what youre saying?  if yes, when and where do we enter/populate standardbasis? and what values does it take?
and what defines procedure family is this from a controlled list somewhere?
[Timestamp: 2026/11/18 00:57:44]

**ai**: **Short answer: no, it isn't B.** Two corrections to what I said earlier, and one gap I should own up to.

## 1. Which option makes `standardBasis` matter
I said that under **3A** (exact procedure and version), `Implicit` and `None` assessments can never settle anything. That isn't really specific to 3A. It follows from rule v0 itself: if agreement requires a shared, checkable procedure, then an assessment with no stated procedure has nothing to share. 3B only loosens what counts as "shared", so `None` still can't settle. In both cases `standardBasis` decides who is allowed to settle a claim. That's my inference, not something the vault already states.

## 2. Where and when `standardBasis` gets its value
**What the vault says:** the values are `Explicit | Implicit | None`, defined in [[HO-002.a Assessment-Everywhere Test Strategy]] (line 31) as "judgement against a stated standard, against a tradition's unstated default, or opinion". The vault doesn't yet say where the property lives or who fills it in. It isn't in [[Harm Ontology v3 - Draft Structure]].

**What I propose:** `standardBasis` sits on each **Assessment** and is **derived by script, not entered by hand**, because the draft structure already contains the inputs:
- **Explicit:** the assessment, or its PerspectiveSpecification, states an `appliedEvaluativeStandard` (draft structure line 98).
- **Implicit:** none is stated, so it is inherited from the PerspectiveType's `defaultEvaluativeStandard` (line 88; decided 2026-11-17 in [[PerspectiveStructure 0.02]]).
- **None:** no standard is stated and there's no tradition to inherit one from.

Deriving it follows your earlier principle. Its value is an Observation (anyone can check it from the data), not a judgement, so it doesn't add another layer of assessment. It also makes CQ5 testable without anyone hand-labelling 3 values.

One complication: a person may use their tradition's default *knowingly*. "Implicit" then means *not stated in this assessment*, not *unconscious*. If that difference matters to you, it's a fourth value (`InheritedAcknowledged`). I'd leave it out of the test.

## 3. "Procedure family": no, it isn't from any list
I made that term up in the last message. No controlled list exists. Worse, **"procedure" itself isn't defined in the vault.** The only place it appears is as a property of the Judgment subclass (draft structure line 113; [[HO-II.c Judgment as Assessment - Reasoning over Precedent]]), and there it means legal procedure. Rule v0 depends on an undefined term.

There are two distinct things that "procedure" could mean:
- **EvaluativeStandard:** *what counts* as harm (the rulebook; [[HO-II.a Assessment and Evaluative Standard]]).
- **Procedure / method:** *how you check* (a forensic audit, a clinical severity scale, a court's evidentiary process).

Two assessors can share a standard but use different methods, or the reverse. Options:
- **A:** treat "procedure" as just the EvaluativeStandard. This is simplest, but it merges what counts with how it's checked.
- **B (recommended for the test):** add a separate **Procedure** class (identifier, version, optional `implementsStandard → EvaluativeStandard`). Use it only for the toy case, with a handful of made-up procedures, and don't build a controlled list yet. Rule v0 then reads: same verdict, same Procedure, same version.
- **C:** B plus families from an external vocabulary (e.g. the ISO or clinical scale registries). That's premature, and I'd be naming registries from memory, unverified.

Under B, "procedure family" becomes unnecessary and option 3B drops out. That also resolves hard case 3 cleanly: institutional review vs independent forensic audit are two Procedures, so the status is Incommensurable unless we add a causal-question exception.

**Decisions for you:** (1) derive `standardBasis` by script, yes or no? (2) Procedure as a separate class for the test (option B)? Once you've answered, I can record both in HO-002.a under Author decisions, marked as test-only.
<!-- copilot-message {"tools":["Grep (read): 02_Ideas Topics Concepts"]} -->
[Timestamp: 2026/11/18 00:57:44]

**user**: i wonder if standardBasisType would be better so no one thinks they need to see some particular ISO standard for example
[Timestamp: 2026/11/18 01:00:17]

**ai**: You're right that there's a risk, but I don't think adding "Type" fixes it. The word that suggests ISO is **"standard"**, and `standardBasisType` still contains it. Two more problems:
- **"Type" already means something here.** In this model, names ending in "Type" are classes: PerspectiveType is a tradition. A property called `...Type` suggests there's a class behind it.
- **"Explicit" has the same problem.** It suggests a formal document has to exist somewhere.

**Rename both the property and its values**, so they describe *where the yardstick comes from*, not which document it's in:

| Option | Property | Values |
|---|---|---|
| **A (recommended)** | `judgementBasis` | `Stated` · `Inherited` · `Unstandardised` |
| B | `standardSource` | `Stated` · `Inherited` · `None` |
| C | `standardBasisType` | `Explicit` · `Implicit` · `None` (your suggestion) |

Why I'd pick A:
- **`Stated`** only means the assessor named their yardstick. That could be ISO, a professional code, a religious rule, or "my company's policy". No document is required.
- **`Inherited`** matches the derivation rule exactly (taken from the tradition's `defaultEvaluativeStandard`), so the name explains itself.
- **`Unstandardised`** is gentler than "opinion" and more accurate than "None". It also signals why these assessments can't settle anything.
- The word "standard" no longer appears in the property name.

Whichever name you choose, the definition (`skos:definition`) should say it outright: *"Records whether the assessor named their yardstick, inherited it from their tradition, or used none. It does not imply a formal or published standard."* That sentence matters more than the name.

Should I go with A? If so, I'll record it in HO-002.a together with the two open decisions: derive it by script, and Procedure as a separate class for the test.
[Timestamp: 2026/11/18 01:00:17]

**user**: i like a as well. however, if a judgement is the same as the product of executing the "assessment" would assessmentBasis be good to keep the wording consistent
[Timestamp: 2026/11/18 01:02:17]

**ai**: Yes, and there's a stronger reason than consistency: **"judgement" already means something narrower in this model.** In [[Harm Ontology v3 - Draft Structure]] (line 113), `Judgment` is a *subclass* of Assessment, the court-judgment profile from [[HO-II.c Judgment as Assessment - Reasoning over Precedent]]. A property called `judgementBasis` would suggest it only applies to court rulings. `assessmentBasis` avoids that and matches the class it sits on.

**One risk with the new name:** "basis" can be read as *evidence* basis ("what is this assessment based on?"). That would confuse it with the evidence pointer, which is a separate thing. The definition should rule that out:

> **`assessmentBasis`**: records whether the assessor named the yardstick they judged against (`Stated`), took it from their tradition's default (`Inherited`), or used none (`Unstandardised`). It does not imply a formal or published standard, and it says nothing about evidence; see the evidence pointer.

**A small spelling point:** `Unstandardised` is UK spelling. The Style Guide doesn't yet say whether to use US or UK English, and other identifiers (`Judgment`) use US forms. I'd use **`Unstandardized`** in the ontology for consistency, unless you prefer UK spelling.

If you agree, I'll record these in HO-002.a under Author decisions, all marked test-only:
1. `assessmentBasis: Stated | Inherited | Unstandardized`, with the definition above.
2. It's derived by script from `appliedEvaluativeStandard` / `defaultEvaluativeStandard`.
3. Procedure is a separate class for the test (option B), and rule v0 becomes "same verdict, same Procedure, same version".

Should I record all three, or only some?
[Timestamp: 2026/11/18 01:02:17]

**user**: yes
[Timestamp: 2026/11/18 01:04:04]

**ai**: I've recorded all three decisions in [[HO-002.a Assessment-Everywhere Test Strategy]], marked test-only.

**Changes:**
- **Summary:** `standardBasis` is now `assessmentBasis: Stated | Inherited | Unstandardized`, with a note of the old name.
- **CQ5 row:** uses the new property name; "Implicit" became "Inherited".
- **Author decisions:** new items 5–7:
  - 5: the property, why it was renamed, and its definition
  - 6: its value is derived by script
  - 7: Procedure is a separate class for the test, and rule v0 now reads "same verdict, same Procedure, same version"
- **Also added under the decisions:**
  - My inference that `Unstandardized` assessments can never settle a claim (labelled as an inference).
  - A list of what agreement rule v1 still has to decide, including hard case 3.
- **Original wording:** your two messages are quoted verbatim and my one line is attributed to me separately. The source is this session's transcript file.

**Not changed:**
- **[[Handoff - Harm Ontology]]** still says `standardBasis`. It gets overwritten when the session closes, so I'll update it then unless you want it changed now.
- **[[Decisions_Log]]:** nothing logged, because these are test-only decisions. That's in line with the handoff's "don't log until tested" caution.

**Next:** finish agreement rule v1. Hard case 3 is the main open question: when an institutional review and an independent forensic audit reach opposite verdicts, should a naive "who caused it?" query show them as **Incommensurable** or as **Disputed**?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:04:04]

**user**: disputed
[Timestamp: 2026/11/18 01:05:49]

**ai**: That makes sense, and I think it shows the rule should be **asymmetric** rather than having a special exception for causal questions.

## Why a causal-only exception is weak
If an institutional review and a forensic audit conflict over *severity*, the reason to show "Disputed" is the same: someone asking a naive question should see that people disagree. If the exception only covers causal questions, the same silent-omission problem comes back for every other attribute.

## Proposed rule v1 core: settling is hard, disputing is easy
- **To settle:** same verdict, same Procedure, same version, ≥2 assessments, each with evidence (as decided).
- **To dispute:** any two in-scope assessments with conflicting verdicts on the **same claim**, **whatever procedure they used**.
- **Incommensurable** is kept only for cases where the verdicts can't be lined up at all. For example, one scale has no shared band with the other, or the two assessments turn out to answer different questions. This becomes rare and always visible, not a place where conflicts get hidden.

This asymmetry fits the book's argument. The model should be slow to declare a fact and quick to show disagreement. Errors then lean towards *too much visible dispute*, never *quiet false consensus*. That's exactly the Horizon failure: an institutional procedure treated as settled fact.

## The detail that keeps "Disputed" useful
A dispute between two procedures and a dispute within one procedure are different things. The model already has a place to record the difference: the Divergence class (`divergesOn`, draft structure line 117). So:
- **Disputed** is shown to every query.
- The **Divergence** record says what the dispute is about: `divergesOn → Procedure` (method conflict), `→ EvaluativeStandard` (yardstick conflict), or `→ evidence`. Expert users can drill down. Naive users still see "Disputed".

## Effect on hard case 3 and the Horizon test
"Who caused the shortfalls?" returns **Disputed**, with the institution's review and the forensic audit side by side and a Divergence on Procedure. That's what the R01 test in the handoff expects.

## A cost to watch
An `Unstandardized` opinion can turn a well-supported claim into "Disputed". Is that right? Two options:
- **(a)** Yes, keep it. Every in-scope dissent counts, and `assessmentBasis` sits next to the status so readers can weigh it. The control lever is *scope*: who you declare to be in scope.
- **(b)** Only `Stated` and `Inherited` assessments can dispute a claim.

I'd pick **(a)**. Under (b), the model would decide in advance whose objections count, which is the kind of systematic omission HO-005 warns about. Scope is the honest place to make that choice, because it's declared.

Two decisions for you: (1) apply the asymmetric rule generally, not just to causal questions? (2) (a) or (b) for unstandardized dissent? Once you've answered, I'll add the decisions to HO-002.a.
[Timestamp: 2026/11/18 01:05:49]

**user**: a
[Timestamp: 2026/11/18 01:07:18]

**ai**: I've recorded both decisions in [[HO-002.a Assessment-Everywhere Test Strategy]] as test-only Author decisions:
- **Item 8:** hard case 3 shows as **Disputed**. The mechanism I proposed for it (a Divergence record with `divergesOn → Procedure`) is noted as my proposal, not yours.
- **Item 9:** **option (a)**. Unstandardized dissent counts, `assessmentBasis` appears next to the status, and declared scope controls who is included.

**Still need your answer on question 1:** should the asymmetric rule (settling is hard, disputing is easy) apply to **every attribute** or only to causal questions? I've listed it in the note as "proposed, awaiting author decision". I'd recommend every attribute.

After that, these parts of rule v1 are still open. I can take them one at a time or put them all forward as a single package:
1. Same-claim test (same target, attribute and scope)
2. Graded values compared through shared bands
3. Declared scope for each view or query
4. Abstention blocks settlement (status `PartiallyAssessed`)
5. At least 2 assessments to settle
6. Latest assessment per perspective, recalculated as of a date
7. Status set: six internal statuses, collapsed to three for display
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:07:18]

**user**: explain better
[Timestamp: 2026/11/18 01:08:37]

**ai**: Here's question 1 in plainer terms, with an example.

## The question
When two assessments **disagree**, when should the model label the claim **"Disputed"**?

You've already answered this for one case (hard case 3): **who caused the Horizon shortfalls?** The Post Office's internal review says "the sub-postmasters". An independent forensic audit says "the software". They used different methods, but you chose "Disputed", so anyone asking the question sees there's a conflict.

The question is whether that answer applies **only to "who caused it?" questions**, or **to every kind of question**.

## Example of the difference
Same two sources, a different question: **how severe was the harm to sub-postmasters?**
- The internal review uses a financial-loss method and says "moderate".
- An independent study uses a method that includes health, reputation and family impacts, and says "severe".

| | Rule for causal questions only | Rule for all questions |
|---|---|---|
| "Who caused it?" | **Disputed** ✔ | **Disputed** ✔ |
| "How severe?" | **Incommensurable**: the methods differ, so the model says it "can't compare" | **Disputed** ✔ |

Under the causal-only rule, a naive query for "severe harms" could treat this case as unknown, so the disagreement **disappears from view**. That's the silent omission you raised earlier, coming back for every attribute that isn't causal.

## The rule I'm proposing (the "asymmetric" rule)
- **Calling something a fact (Settled) is hard.** Several sources must give the same answer using the *same* method, with evidence.
- **Calling something Disputed is easy.** Any two in-scope sources giving conflicting answers is enough, *whatever method they used*.
- **"Incommensurable"** is kept only for real non-comparisons. For example, one source answers a different question altogether, or uses a scale that can't be lined up with the other.

In one sentence: **the model should be slow to declare facts and quick to show disagreement.** If it gets things wrong, it should show too much dispute, never a quiet false consensus.

## What you're deciding
- **All questions (recommended):** "Disputed" works the same way for severity, reversibility, patient type, and so on.
- **Causal questions only:** narrower, but disagreements about other attributes can drop out of view.

Which do you choose?
[Timestamp: 2026/11/18 01:08:37]

**user**: recommended
[Timestamp: 2026/11/18 01:10:07]

**ai**: I've recorded it in [[HO-002.a Assessment-Everywhere Test Strategy]] as Author decision 10, test-only, with the severity example. The asymmetric rule now applies to every attribute.

## Next open item: when are two assessments about the same claim?
This has to be settled first, because the rule above only works if we know when two assessments are answering the same question.

**Example:** two sources on Horizon:
- Source 1: "The harm was **severe** for **sub-postmasters**, **1999–2015**."
- Source 2: "The harm was **minor** for **the Post Office as a company**, **2015**."

Is that a dispute? No. They're about different people and different periods, so both can be true. If the model compared them anyway, it would show a **false dispute**.

**Proposal:** two assessments are about the same claim only if they match on:
1. **What** is assessed (the same Effect, Factor, etc.)
2. **Which attribute** (severity, cause, reversibility…)
3. **Scope**: the same Patient and an overlapping time period

If any of the three differ, they're separate claims, and each gets its own status.

**A harder case:** source 1 says "severe for sub-postmasters" and source 2 says "minor for *some* sub-postmasters". One group contains the other. The options are:
- **(a)** treat them as different claims (simple, but it can hide a real conflict)
- **(b)** treat them as the **same claim, shown as Disputed** whenever the groups or periods overlap (recommended, in line with "quick to show disagreement")

Do you agree with the three-part match and with (b)?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:10:07]

**user**: should we really be using the language patient here?  wouldn't impactedParty be better (and not say harmed party since they could be impacted beneficcially?_
[Timestamp: 2026/11/18 01:12:31]

**ai**: Good catch. I agree the name should change, but I'd suggest something other than `impactedParty`.

## What's wrong with "Patient"
- **Philosophy:** "moral patient" usually means *an entity whose interests count* or *that can be wronged*. That builds standing into the name, which contradicts the decision that **standing is assessed** (2026-11-18).
- **Everyday reading:** most people hear "hospital".
- **In its favour:** in linguistics, "patient" just means *whatever undergoes the action*, with no positive or negative charge. That's probably why it was chosen. But few readers will hear it that way.

## Why not `impactedParty`
- **"Party"** suggests a person or legal entity: someone who could sign a contract or join a lawsuit. It sounds odd for a river, an ecosystem, an electric grid or a future generation, all of which are on the inclusive list.
- **"Impact"** is fairly neutral, but in everyday speech it often leans negative ("the impact of the cuts").
- You're right that "harmed party" is out. Since 2026-11-14, valence lives only in the assessment ([[Decisions_Log]]), so the name has to cover beneficial effects too.

## Options
| Name | Neutral valence | Fits non-persons | Notes |
|---|---|---|---|
| **AffectedEntity** (recommended) | ✔ | ✔ | Matches the existing property `affects` (Effect `affects` → AffectedEntity), so the model reads naturally |
| ImpactedEntity | mostly | ✔ | Similar, but "impact" leans slightly negative |
| ImpactedParty | mostly | ✘ | "Party" suggests a person or legal entity |
| Patient (keep, clearly defined) | ✔ in linguistics | ✔ | Familiar to philosophers, confusing to everyone else |

I'd keep **"patient"** and **"moral patient"** as alternative labels (`altLabel`), so people coming from philosophy can still find it.

## What the rename would involve
- "Patient" appears **about 70 times across 19 notes**, including the draft structure, HO-002.a, the council reviews and the v1 `.ttl`. It's also in the Patient decision in [[Decisions_Log]].
- That makes this a **design decision**, not a test-only one. It should be logged.
- To keep the momentum low, I suggest:
  1. You choose the name now.
  2. I log it and use the new name in the v3 test files and in HO-002.a from now on.
  3. The full rename across the other notes and the `.ttl` goes on the migration plan's list. I'll propose those edits as a list first, as the vault rules require.
- Subtypes keep their names (SentientIndividual, Household, NaturalSystem…). Only the umbrella class changes, along with `patientStanding`, which would become `affectedStanding` or `standing`.

Do you want **AffectedEntity**? Once you've chosen, I'll come back to the same-claim question, using the new name.
<!-- copilot-message {"tools":["Grep (read): 00_Claude_Admin/Decisions_Log.md","Grep (read): 02_Ideas Topics Concepts/Harm Ontology"]} -->
[Timestamp: 2026/11/18 01:12:31]

**user**: yes to all
[Timestamp: 2026/11/18 01:13:38]

**ai**: Patient is now **AffectedEntity**. Here's what changed:

- **[[Decisions_Log]]:** new 2026-11-18 entry. Patient becomes AffectedEntity (altLabels "patient" and "moral patient"), and `patientStanding` becomes `affectedStanding`. Subtype names don't change. The entry quotes your reasons verbatim. It replaces the class name in the earlier "inclusive types" entry, but that decision itself still stands.
- **[[HO-002.a Assessment-Everywhere Test Strategy]]:** every non-quote "Patient" now reads AffectedEntity: the CQ7 row, the model section (renamed, with a pointer to the log) and the test-case table. Verbatim quotes are untouched.
- **Migration list:** the full rename across the other notes and the v1 `.ttl` (about 70 occurrences in 19 notes) is added as item 10 in the migration-plan running list. I'll propose those edits as a list before making them.

You said "yes to all", so I picked **`affectedStanding`** rather than plain `standing`. Plain `standing` could be confused with legal standing (locus standi). Say if you'd prefer the shorter name.

## Back to: when are two assessments about the same claim?
Proposal: two assessments are about the same claim only if they match on:
1. **What** is assessed (the same Effect, Factor…)
2. **Which attribute** (severity, cause…)
3. **Scope**: the same **AffectedEntity** and an overlapping time period

**Harder case:** "severe for sub-postmasters" vs "minor for *some* sub-postmasters".
- **(a)** treat them as different claims (simple, but it can hide a real conflict)
- **(b)** treat them as the **same claim, shown as Disputed** when the groups or periods overlap (recommended: quick to show disagreement)

Do you agree with the three-part match and with (b)?
<!-- copilot-message {"tools":["Read (read): 00_Claude_Admin/Decisions_Log.md","Read (read)","Grep (read): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md","Edit (edit): 00_Claude_Admin/Decisions_Log.md","Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md","Edit (edit)"]} -->
[Timestamp: 2026/11/18 01:13:38]

**user**: do any of the attributes use patient
[Timestamp: 2026/11/18 01:14:33]

**ai**: Yes, a few. Here's everything in the ontology files, sorted by type (from a grep of `ontology/` and [[PerspectiveStructure 0.02]]):

## Properties (attributes) that use "patient"
| Where | Attribute | Proposed new name |
|---|---|---|
| [[Harm Ontology v3 - Draft Structure]] line 104 | `forPatient` (on Assessment: whose harm the verdict is about) | `forAffectedEntity` |
| Draft structure line 71 | `patientStanding` | `affectedStanding` (already decided) |
| Draft structure line 59 | `affects → Patient` | name unchanged; only the target becomes AffectedEntity |
| Draft structure line 88; PerspectiveStructure 0.02 line 171 | `moralCircle ↔ Patient` | name unchanged; only the link target changes |
| v1 `.ttl` lines 875–883 | `hasPatientOntology`, `PatientOntologyValue` (v1's "Attribute 15") | handle during migration: becomes AffectedEntity type, with the old IRIs deprecated, not edited in place |

## Two places that should probably not change
- **v1 `.ttl` lines 258–259:** "a patient's survival odds" (the Loss of Chance example). That's a real **medical** patient, so it stays.
- **PerspectiveStructure 0.02 line 121:** `standingOfSubjects {agent · patient · datum}`. This is the classic philosophical pair *agent* (one who acts) and *patient* (one acted on). It describes how a tradition sees subjects, not our class. Options:
  - **(a)** keep "patient" here (recommended, because it's the standard term in that pair)
  - **(b)** change it to "affected", for consistency

## Everything else
The rest are mentions in prose: the draft structure's class tree (lines 67–72) and notes, the crosswalk pilot, the migration plan, and the HO notes. Those go in the planned rename list.

**Decisions for you:**
1. Rename `forPatient` to `forAffectedEntity`?
2. Keep "patient" in `standingOfSubjects`, (a) or (b)?

After that we can go back to the same-claim question.
<!-- copilot-message {"tools":["Grep (read): 02_Ideas Topics Concepts/Harm Ontology","Grep (read): 02_Ideas Topics Concepts/Harm Ontology/ontology","Grep (read): 02_Ideas Topics Concepts/Harm Ontology/PerspectiveStructure 0.02.md"]} -->
[Timestamp: 2026/11/18 01:14:32]

**user**: yes are you making this change in Harm Ontology v3 as well or only in the test version
[Timestamp: 2026/11/18 01:15:45]

**ai**: I've added `forPatient` → `forAffectedEntity` to the AffectedEntity entry in [[Decisions_Log]] and to the migration rename list.

## Your question: v3, or only the test version?
**So far, neither.** The plan we agreed was:
- **The test version:** use the new names. But no test files exist yet (`ontology/tests/` is empty), so there's nothing to change there yet.
- **HO-002.a:** already updated.
- **[[Harm Ontology v3 - Draft Structure]]:** **not changed yet.** It went on the deferred rename list with everything else.

## I'd change that
The draft structure isn't just another note. It's the **v3 design** itself, and the test files will be built from it. Since the rename is logged as a design decision, leaving the draft with the old names means:
- the source of truth would contradict [[Decisions_Log]]
- the test files would be built from a note that uses names we've already retired

**Proposal:** update the draft structure **now**: about 8 lines (59, 67, 70–72, 88, 104, 128, 153), plus an "applied decisions" line like the existing one at line 138. Keep the full rename across the **other 18 notes and the v1 `.ttl`** deferred to migration, as planned. The v1 `.ttl` should never be edited in place anyway: its old IRIs get deprecated.

**Two things to confirm:**
1. Update the draft structure now?
2. Your "yes" covered `forPatient`. For `standingOfSubjects {agent · patient · datum}` in [[PerspectiveStructure 0.02]], should I keep "patient", as the standard philosophical pair (a), or change it to "affected" (b)?
<!-- copilot-message {"tools":["Edit (edit): 00_Claude_Admin/Decisions_Log.md","Edit (edit)"]} -->
[Timestamp: 2026/11/18 01:15:45]

**user**: change to affected
[Timestamp: 2026/11/18 01:16:55]

**ai**: I've made the change and logged it:
- **[[PerspectiveStructure 0.02]] line 121:** now reads `standingOfSubjects ★ {agent · affected · datum}`, with a dated note that it replaces "patient".
- **[[Decisions_Log]]:** added to the AffectedEntity entry.

Line 171 of that note still says `moralCircle ↔ Patient`. That's a link target, so it changes together with the draft structure.

**Still open: should I update [[Harm Ontology v3 - Draft Structure]] now?** That's about 8 lines (`affects → AffectedEntity`, the class tree, `affectedStanding`, `moralCircle ↔ AffectedEntity`, `forAffectedEntity`, `experienceability`, and the "patients" line in the notes), plus an "applied decisions" line. I'd also fix line 171 of PerspectiveStructure 0.02 at the same time. The other 17 notes and the v1 `.ttl` stay deferred to migration. Should I go ahead?
<!-- copilot-message {"tools":["Read (read): 02_Ideas Topics Concepts/Harm Ontology/PerspectiveStructure 0.02.md","Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/PerspectiveStructure 0.02.md","Edit (edit): 00_Claude_Admin/Decisions_Log.md"]} -->
[Timestamp: 2026/11/18 01:16:55]

**user**: yes
[Timestamp: 2026/11/18 01:18:21]

**ai**: I've updated [[Harm Ontology v3 - Draft Structure]], and a grep shows "Patient" now appears only in the labels that record the old name.

**Changes in the draft structure:**
- `affects → AffectedEntity` (Effect props)
- The class tree reads **AffectedEntity**, with "formerly Patient", the altLabels "patient" and "moral patient", and the rename date. Proposed items now use `affectedStanding` and "Factor and AffectedEntity not disjoint".
- `moralCircle ↔ AffectedEntity` (PerspectiveType)
- `forAffectedEntity` (Assessment)
- Box A: "experienceability (relative to the affected entity)"
- A new **Revision 2026-11-18** callout listing the applied decision, like the existing 2026-11-17 one.
- The "assessment everywhere" warning callout now says AffectedEntity and `assessmentBasis` (marked test-only).
- The open list: "…as affected entities"

**[[PerspectiveStructure 0.02]] line 171:** `moralCircle ↔ AffectedEntity`.

**Something I noticed:** the draft's **Open** list still includes "future generations, AI systems and relationships as affected entities". The 2026-11-18 decision already confirmed them as types. If that item is about something still unresolved, such as their *standing*, it should be reworded. If not, it could move off the Open list. I've left it as it is. Should I reword it, remove it, or leave it?

**Back to the same-claim question:** should two assessments count as the same claim when they match on **what** is assessed, **which attribute** and **scope** (AffectedEntity plus an overlapping time period)? And when groups overlap ("severe for sub-postmasters" vs "minor for *some* sub-postmasters"), should that be **(b) the same claim, Disputed** (recommended), or (a) separate claims?
<!-- copilot-message {"tools":["Read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md","Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md","Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/PerspectiveStructure 0.02.md","Grep (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md"]} -->
[Timestamp: 2026/11/18 01:18:21]

**user**: leave
[Timestamp: 2026/11/18 01:20:43]

**ai**: I'll leave it as it is.

The same-claim question is still waiting for your answer:

1. **Three-part match:** two assessments are about the same claim only if they share **what** is assessed, **which attribute**, and **scope** (AffectedEntity plus an overlapping time period). Do you agree?
2. **Overlapping groups**, e.g. "severe for sub-postmasters" vs "minor for *some* sub-postmasters":
   - **(a)** treat them as separate claims
   - **(b)** treat them as the same claim, shown as **Disputed** (recommended, because it shows the disagreement instead of hiding it)
[Timestamp: 2026/11/18 01:20:43]

**user**: 1
[Timestamp: 2026/11/18 01:21:36]

**ai**: I've recorded the three-part match in [[HO-002.a Assessment-Everywhere Test Strategy]] as Author decision 11 (test-only).

I read your "1" as agreeing with question 1, so question 2 is still open. I've listed it in the note as open. The question is what to do when the groups overlap.

**Example:** source A says the harm was "severe for sub-postmasters". Source B says it was "minor for *some* sub-postmasters".
- **(a) Separate claims:** each gets its own status, and the model shows no conflict. That's simple, but a reader never learns that B partly contradicts A.
- **(b) Same claim, Disputed** (recommended): because the groups overlap, the model flags the conflict. A Divergence record notes that the scopes differ (whole group vs subgroup), so an expert can see the dispute might come from the difference in scope rather than real disagreement.

Do you choose (a) or (b)?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:21:36]

**user**: b
[Timestamp: 2026/11/18 01:22:51]

**ai**: I've recorded it in HO-002.a as Author decision 12 (test-only): overlapping scopes count as the same claim, shown as Disputed, with a Divergence record noting the scope difference.

## Next open item: comparing graded values
Some attributes are graded (severity, reversibility). Two sources rarely use the same scale. When do their answers count as the **same verdict**, which matters for Settled, or as **conflicting**, which matters for Disputed?

**Example (made up):**
- Source A, financial method: severity **7 out of 10**
- Source B, clinical method: severity **"serious"** on a 4-step scale (mild, moderate, serious, critical)

Do they agree?

**Options:**
- **(a) Exact match only:** the scales differ, so they can never agree. Settling then becomes almost impossible, and every pair looks like a conflict.
- **(b) Shared bands** (recommended): each Procedure maps its scale onto a shared coarse scale, e.g. **Low / Medium / High / Extreme**. A's 7/10 maps to High and B's "serious" maps to High, so they **agree**. Each original value is kept on its assessment, so no detail is lost.
- **(c) Tolerance:** answers within some distance count as agreeing. That only works when both scales are numeric, so it doesn't fit here.

**One consequence of (b):** someone has to decide each mapping, e.g. that "serious" equals High. That mapping is itself a judgement. Under the assessment-everywhere approach it should be **recorded with the Procedure and open to challenge**, not hidden. For the toy case, I'd make the mappings up and label them as such.

Do you choose (a), (b) or (c)?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:22:51]

**user**: b
[Timestamp: 2026/11/18 01:23:58]

**ai**: I've recorded it in HO-002.a as Author decision 13 (test-only): shared bands, original values kept, and the mapping recorded with the Procedure and open to challenge.

## Next open item: declared scope
**Rule v0 says:** a claim is Settled when every perspective *in scope* agrees. But who decides which perspectives are in scope?

**Example:** "What caused the Horizon shortfalls?"
- If the scope is **only the Post Office's own reviews**, every assessment says "user error", so the claim is **Settled**.
- If the scope also includes **the forensic audit and the sub-postmasters**, the claim is **Disputed**.

Same data, opposite answers. Whoever picks the scope picks the result. If the scope is left unstated, "Settled" really means "settled among whoever we happened to include". That's silent omission again.

**Options:**
- **(a) Implicit:** every perspective in the data is in scope. It's simple, but the result depends on what happened to be entered, and nobody sees that.
- **(b) Declared and shown** (recommended): every query or view **declares its scope**, meaning which perspectives are included. The result **displays that scope** next to each status, e.g. "Settled *among: Post Office reviews*". If no scope is given, the default is **everything in the data**, and the result says so.
- **(c) Declared, not shown:** scope is declared but only visible to experts. That brings back the original risk.

(b) also fits two earlier decisions: *Assessment `declaredScope`* (draft structure line 106) and your option (a) on unstandardized dissent, where scope is the place to decide who counts.

Do you choose (a), (b) or (c)?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:23:58]

**user**: b
[Timestamp: 2026/11/18 01:25:12]

**ai**: I've recorded it in HO-002.a as Author decision 14 (test-only): scope is declared, shown next to each status, and defaults to everything in the data, with the result saying so.

## Next open item: silence (abstention)
Say a perspective is **in scope** and uses the right Procedure, but **hasn't assessed** this claim. Does its silence stop the claim from being Settled?

**Example:** three forensic auditors are in scope and all use the same audit procedure. Two say "software fault" and the third hasn't looked at this branch yet.
- **(a) Silence is ignored:** two agree, nobody disagrees, so the claim is **Settled**.
- **(b) Silence blocks settlement** (recommended): the status is **PartiallyAssessed** ("2 of 3 agree, 1 not assessed"). It still counts as agreement so far, but it isn't called a fact.

**Why I recommend (b):** under (a), adding *more* perspectives to the scope can never weaken a Settled claim unless they actively disagree. Gaps disappear without a trace. (b) keeps those gaps visible, in line with "slow to declare facts".

**The cost:** with a wide scope, almost nothing will ever be fully Settled. Two things ease that. Scope is declared (decision 14), so you can narrow it on purpose and openly. And PartiallyAssessed still shows agreement so far.

Do you choose (a) or (b)?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:25:12]

**user**: b
[Timestamp: 2026/11/18 01:25:53]

**ai**: I've recorded it in HO-002.a as Author decision 15 (test-only): silence blocks settlement, and the status is PartiallyAssessed.

## Next open item: minimum number of assessments
Can a **single** assessment settle a claim?

**Example:** only one forensic audit exists, and it says "software fault". No other perspective in scope uses that procedure, so nobody is silent and nobody disagrees. Under the rules so far, it would count as **Settled**.

- **(a) One is enough:** an Observation with evidence under a checkable procedure is Settled on its own.
- **(b) At least 2 independent assessments** (recommended): one alone is **SingleSource**. That says "uncontradicted, but nobody has checked it".

**Why I recommend (b):** a "checkable procedure" only means something if someone has actually checked it. A single audit, even a good one, is one view. That matters for Horizon: for years the only "procedure" applied was the Post Office's own. My summary of that is from memory and unverified until we research it.

**A related point:** what does "independent" mean? Two auditors employed by the same firm, or one report quoted by another, aren't really two. Options:
- treat "independent" as **different PerspectiveSpecifications** (simple, but it can be gamed)
- also require **no shared assessor or organisation** (stricter)

For the toy case, I'd use the stricter version and tag each assessment with its organisation.

Do you choose (a) or (b)? And should the toy case use the stricter definition of independence?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:25:53]

**user**: b
[Timestamp: 2026/11/18 01:26:39]

**ai**: I've recorded it in HO-002.a as Author decision 16 (test-only): settling needs at least 2 independent assessments, and a lone assessment is SingleSource.

**Still open, a quick one:** what does "independent" mean?
- **Loose:** any two different PerspectiveSpecifications count, even if they come from the same firm.
- **Strict** (recommended): they must also share **no assessor or organisation**. A report that only repeats another report doesn't count.

For the toy case, should I use the strict definition, with each assessment tagged with its organisation?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:26:39]

**user**: recommended
[Timestamp: 2026/11/18 01:28:06]

**ai**: I've recorded it in HO-002.a as Author decision 17 (test-only): independence needs different perspective specifications **and** no shared assessor or organisation.

## Next open item: time (which assessment counts?)
Perspectives change their minds. Courts get overturned, and auditors revise their findings. When a perspective has several assessments of the same claim over time, which one counts?

**Example (made up):** a court rules "user error" in 2010, and an appeal court rules "software fault" in 2021.

**Proposal:**
- **Latest wins, per perspective:** only each perspective's most recent assessment counts, so in 2026 that court perspective says "software fault".
- **Recalculated, never stored:** statuses are worked out each time a query runs. A new dissent automatically reopens a Settled claim (CQ4).
- **"As of" date:** a query can ask "what was the status **in 2012**?" It then uses only assessments made by that date, and returns "user error", possibly Settled.
- **Earlier assessments are kept, never deleted**, so CQ4 can trace the sequence of changes and what triggered each one.

**One question inside this:** does "latest" mean the date the assessment was **made**, or the date it was **recorded in our data**? They differ when we enter a 2010 ruling in 2026.
- **(a) Only the date it was made** (recommended for the test). It's simpler.
- **(b) Both dates.** This lets you ask "what did *we* know in 2024?" That's useful later, but heavier.

Do you agree with the proposal, and do you choose (a) or (b)?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:28:06]

**user**: recommended
[Timestamp: 2026/11/18 01:29:10]

**ai**: I've recorded it in HO-002.a as Author decision 18 (test-only): latest assessment per perspective, recalculated at query time, an "as of" date, history kept, and the date the assessment was made. Adding the recorded date is deferred.

**Two items left:** the evidence requirement and the status set. They're closely linked, so here they are together.

## 1. Evidence requirement
**Proposal:** a claim can be Settled only if **every** agreeing assessment has an **evidence pointer**: the document, log, dataset or record it relies on. Without evidence, agreement is only shared opinion.
- If the **evidence itself** is contested (e.g. disputed Horizon logs), that's a **separate claim**, about the Observation, with its own status. A dispute over evidence then shows up visibly instead of quietly undermining the main claim.

## 2. Status set
Our decisions have produced more statuses than the original three:

| Status | Meaning | Decided in |
|---|---|---|
| Settled(value) | ≥2 independent in-scope assessments, same Procedure and version, same band, each with evidence, no dissent, nobody silent | 7, 13, 15–17 |
| Disputed | conflicting verdicts on the same claim, under any procedure | 10, 12 |
| Incommensurable | verdicts that can't be lined up at all | 10 |
| PartiallyAssessed | agreement so far, but some in-scope perspectives are silent | 15 |
| SingleSource | one uncontradicted assessment | 16 |
| NotAssessed | no assessments | — |

There's one gap: assessments that **agree but can't settle**, because they use different procedures or have no evidence. I'd call that **Corroborated**: "agree, but not under the conditions needed to settle".

**Display question:** seven statuses is a lot for someone asking a naive question.
- **(a) Show all seven** everywhere.
- **(b) Two layers** (recommended): naive views show three, **Settled / Disputed / Open**, where Open covers Corroborated, PartiallyAssessed, SingleSource, NotAssessed and Incommensurable. Each item can be opened to see its detailed status. Counts per status appear in every view (the earlier mitigation 4).

**My concern about (b):** grouping five statuses under "Open" can hide the difference between "nobody has looked" and "people agree, unofficially". The non-expert test (step 5) should check whether that misleads people. If it does, show all seven instead.

Do you agree with the evidence requirement? And do you choose (a) or (b) for display?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md","Grep (read): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:29:10]

**user**: b
[Timestamp: 2026/11/18 01:30:27]

**ai**: I've recorded the last two items in [[HO-002.a Assessment-Everywhere Test Strategy]] (test-only), so **agreement rule v1 is complete**:
- **Decision 20:** your choice of **(b)**. The detailed statuses (now including Corroborated) are shown in two layers: Settled / Disputed / Open. The non-expert test will check whether "Open" misleads people.
- **Decision 19:** the evidence requirement. You didn't answer this one directly. I recorded it because it's already part of the CQ3 pass criteria you agreed earlier. Say if you'd like it changed.

## Agreement rule v1 in one paragraph
A claim is identified by its target, attribute and scope, and overlapping scopes count as the same claim. It's **Settled** only when at least 2 strictly independent, in-scope assessments, using the same Procedure and version, agree at the level of shared bands. Each one needs evidence, and nobody in scope can disagree or be silent. It's **Disputed** whenever two in-scope assessments conflict, under any procedure, including unstandardized ones. Everything else is **Open**, with a detailed status underneath. Only each perspective's latest assessment counts, statuses are recalculated at query time, and the scope is always shown.

## A reflection before moving on
That's 18 decisions in one sitting, mostly by accepting my recommendation. The handoff warns about **momentum**, so I'll flag it. The rule is now strict enough that in Horizon **almost nothing may ever reach Settled**. That might be honest, or it might make the model useless. The toy case should show which. It may be worth reading decisions 5–20 in the note once, slowly, before we build on them.

## Next steps (pre-test steps 3–4)
1. **Finish designing variant B:** where Procedure, the evidence pointer, the band mapping and the status calculation live in the classes.
2. **Variant A baseline:** write down the current draft as it stands, for comparison.
3. Then the **toy case** (about 3 factors, 2 effects, 3 perspectives, with a timeline built in).

Do you want to review the decisions first, or go on to the variant B design?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:30:27]

**user**: b design
[Timestamp: 2026/11/18 01:31:44]

**ai**: Here's a draft design for variant B. It's in chat only; I haven't written it to any note yet. I've built it from decisions 3 and 5–20 and the attribute triage in the handoff.

## 1. What changes, in one line
Entities (Factor, Effect, AffectedEntity, FactorAssembly) become **thin**: an identifier and label, plus an observable core where the triage allows one. **Everything else lives on Assessments.** Statuses are **worked out from those assessments**, never entered by hand.

## 2. Classes

| Class | Role | New or changed |
|---|---|---|
| **Assessment** | one judgement about one attribute of one target | gets new properties (below) |
| **Procedure** | *how* something is checked: id, version, `implementsStandard → EvaluativeStandard`, `usesScale`, `hasBandMapping` | new (decision 7) |
| **BandMapping** | maps a Procedure's scale onto the shared bands (e.g. "serious" → High) | new (decision 13); **can itself be assessed**, so it's open to challenge |
| **Band** (vocabulary) | Low · Medium · High · Extreme | new SKOS concept scheme |
| **Evidence** | pointer to a document, log, dataset or record | new (decision 19) |
| **Observation** | *defined*, not asserted: any Assessment with a Procedure **and** Evidence | new (status, not kind) |
| **Claim** | thin, **generated** node: target + attribute + scope. The thing a status attaches to | new; see question A |
| **ScopeDeclaration** | the set of perspectives included in a view or query; default is "all in data" | new (decision 14) |
| **Divergence** | **generated** whenever a claim is Disputed; `divergesOn` Procedure, EvaluativeStandard, scope or evidence | existing, now produced automatically |
| **CausalRole** | folded into CausalAssessment as a structured part | removed as a separate class (proposed in HO-002.a) |

## 3. New properties on Assessment
- `assesses` → target (existing) · `aboutAttribute` → which attribute (severity, cause…) · `value` (the raw value, as given)
- `band` → Band (**derived** through the Procedure's BandMapping)
- `usesProcedure` → Procedure · `hasEvidence` → Evidence
- `forAffectedEntity` (existing) · `scopePeriod` (time interval) → together with target and attribute these make up the claim
- `assessedAt` (the date it was made, decision 18) · `assessor` → Agent · `assessorOrganisation` → Agent
- `repeats` → Assessment (marks a copy, so it doesn't count as independent; decision 17)
- `assessmentBasis` (**derived**: Stated / Inherited / Unstandardized, decision 6)

## 4. How a status is worked out (for each claim, scope and as-of date)
1. Gather the assessments for this claim, **including overlapping scopes** (decision 12), that are in the declared scope and dated on or before the as-of date.
2. For each perspective, keep only its **latest** assessment (decision 18).
3. Any conflicting bands or verdicts → **Disputed**, and generate a Divergence.
4. Otherwise, if none can be lined up → **Incommensurable**.
5. Otherwise, all agree. Then:
   - no assessments at all → **NotAssessed**
   - only 1, or no 2 that are independent → **SingleSource**
   - different Procedures or versions, or any without Evidence → **Corroborated**
   - an in-scope perspective using the Procedure is silent → **PartiallyAssessed**
   - otherwise → **Settled(band)**
6. Display: Settled / Disputed / Open, plus counts per status and the scope label (decisions 14 and 20).

This step order is my proposal. For example, it puts Disputed ahead of everything else, in line with "quick to show disagreement".

## 5. Three design questions for you

**A. Should Claim be a real node?**
- **Yes, generated by script** (recommended). Statuses, Divergences and shortcuts need something to attach to. Without a Claim node, every query has to rebuild the claim from four joins, which is exactly the expert-only trap you warned about.
- No: compute the claim only inside queries.

**B. Shortcuts vs "never stored" (a tension I created):**
Mitigation 1 asks for a status shortcut on every node. Decision 18 says statuses are never stored.
- **Recommended:** a script regenerates **snapshot** shortcuts, each stamped with its scope ("all in data") and date. These are read-only and rebuilt on every run. Live queries with other scopes or dates are always computed.
- Alternative: no stored shortcuts at all, only named views. That's purer, but naive queries then find nothing on the nodes.

**C. How to name the attribute an assessment is about:**
- **A small vocabulary of attribute concepts** (`hoa:severity`, `hoa:reversibility`…) (recommended). It's clean, and SHACL can check it.
- Point at the old property IRIs themselves. That's shorter, but it mixes classes and data in an awkward way (OWL "punning").

Do you agree with the design, and with A, B and C? Once you've answered, I'll save it as a "Variant B design" section in HO-002.a, or as its own note in `ontology/` if you'd rather keep HO-002.a short.
[Timestamp: 2026/11/18 01:31:44]

**user**: recommended
[Timestamp: 2026/11/18 01:33:37]

**ai**: I've saved the design as a new section, **"Variant B design"**, in [[HO-002.a Assessment-Everywhere Test Strategy]], just above the AffectedEntity model. It's marked test-only and records that it was my proposal, which you accepted.

**What the section covers:**
- **Principle:** entities are thin, and statuses are derived.
- **Classes:** the 10-row table, with your choices built in:
  - **Claim** as a node generated by script
  - **Attribute concepts** in an `hoa:` vocabulary
  - **Snapshot shortcuts**, stamped with their scope and date, which resolve the conflict with "never stored"
- **New Assessment properties.**
- **The 6-step status calculation.**

I also updated the "agreement rule v1" line to say the design is done.

I put it in HO-002.a rather than a new note, so it stays next to the decisions it's built on. That makes the note long. If you'd prefer a separate design note in `ontology/`, I can move it there.

## Next: variant A baseline (pre-test step 4)
Variant A is the draft as it stands: attributes stored directly on entities, with no Claim, Procedure or status calculation. The baseline would set out:
1. how each CQ would be answered in A, and what's missing
2. the predicted failures (e.g. CQ2 quietly drops disputed severity, and CQ3 can't be answered)

This would be a short section in HO-002.a, written **before** any modelling, so the comparison isn't biased by the results. Should I draft it?
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:33:37]

**user**: yes
[Timestamp: 2026/11/18 01:35:02]

**ai**: I've added the variant A baseline to HO-002.a as **"Variant A baseline"**. It's labelled as my predictions, written before any modelling, to be checked against the toy case.

**The predictions in brief:**
- **Fails outright:**
  - CQ2 "severe": disputed and unassessed effects drop out silently
  - CQ3 "agreement": no rule exists, so the query can't be written
  - CQ7 "type": a fixed class, which can't be disputed and has no `Unclassified`
- **Partly works:**
  - CQ1 causes: but the asserted `causes` property gives a silent single answer
  - CQ4 time: asserted attributes have no history
  - CQ5 basis
  - CQ6 omission: causes only
  - CQ9 responsibility
- **Simplest in A:** CQ8.
- **Most of A's failures are silent.** That's the risk you raised.

I added two cautions. First, I designed B, so this baseline may be unfair to A. The non-expert run is the check on that. Second, I found a gap that affects **both** variants.

## The gap: Effect has no occurrence date
CQ8 asks "**when** did Effect X occur?", but the draft structure gives Effect only `temporalStatus` (has it happened yet?) and `temporalTrajectory` (how it develops). There's **no date**. CQ8 can't serve as a fair control until this is fixed.

**Options:**
- **(a) Observable core plus an assessed reading** (recommended): add `occurredDuring` (a time interval) as the observable core, such as the dates of recorded shortfalls. Also allow assessments of it, because *when harm began* is often disputed. In Horizon, did the harm begin with the first shortfall, the first prosecution, or the first suspicion? That matches how the triage handles `temporalTrajectory`.
- **(b) Fully assessed:** treat the date only as an assessment. That's consistent with B, but it makes the control question harder in B, so it would unfairly count against B.
- **(c) Reword CQ8** to avoid dates. That's easiest, but it removes a real control.

Do you choose (a), (b) or (c)? If you choose (a), I'll add it to both variants in HO-002.a, and as a proposed item in the draft structure, not a decided one.
<!-- copilot-message {"tools":["Edit (edit): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md"]} -->
[Timestamp: 2026/11/18 01:35:02]