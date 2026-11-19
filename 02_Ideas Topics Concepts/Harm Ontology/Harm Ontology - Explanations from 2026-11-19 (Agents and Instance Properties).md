---
type: reference
status: developing
tags: [ontology/harm]
aliases: [Agents and Instance Properties explanations, 2026-11-19 explanations]
created: 2026-11-19
---

# Harm Ontology: explanations from 2026-11-19 (agents and instance properties)

> [!warning] Status
> A reference note that preserves explanations given in the session "read" (2026-11-18 to 19) so a new chat doesn't have to rebuild them. **Nothing here is decided or logged.** It is not a bookmarked idea note and is not in [[_Harm Ontology Bookmark Index]]; the proposed HO-007 awaits the author's confirmation (see [[Handoff - Harm Ontology]]). Legal, linguistic and BFO/OBO statements are **from memory and unverified**. Statements about how Protégé behaves are from general knowledge and were **not tested**.

## 1. Why instances show no properties to fill in
- **Properties are not attached to classes in OWL.** `rdfs:domain` and `rdfs:range` are axioms about how a property is used. If you assert `x p y` and `p` has domain `C`, a reasoner **infers** that `x` is a `C`; it does not make `p` a field of `C`.
- **"only" restrictions** (for example `PerspectiveType SubClassOf (divergesFrom only PerspectiveType)`) say what values a link may have. They show on the class page but create no entry fields, and under open-world semantics they force nothing to exist.
- **Any individual can carry any property assertion**, and nothing pre-lists properties for it. Annotation properties behave the same way.
- **What instances do inherit:** their class memberships (and so the class's restrictions), and, through sub-properties, super-property assertions. So the property group tree helps display, not data entry.
- **Protégé Desktop has no instance entry form** (general knowledge; check the installed version). "Properties of this class" lists come from older frame-based editors.
- **In this sample specifically:** the editor-first mini gave only PerspectiveType and PerspectiveSpecification their attributes. Assessment has only `assessedBy` and Person is a stub range target, so the draft structure's Assessment and CausalAssessment properties (`assesses`, `takenFrom`, `forAffectedEntity`, `verdict`, `declaredScope`, `attributedCause`, `leftOut` and the rest) were never modelled.
- **The altitude and congruence attributes sit on PerspectiveType** (a tradition), not on a person. A person appears as the `assessor` (an Agent) of a PerspectiveSpecification.

**Ways to guide data entry (none verified):**
1. Give every class its properties by domain and range, from the draft structure's `props:` lines; find them via the class's usage list (I believe it lists domain axioms; nothing prompts you).
2. State expected properties as restrictions, for example `Assessment SubClassOf (assesses some …)`: visible, but open-world.
3. **SHACL profile shapes** (the layer 2 job of the 2026-11-17 three-layers decision): the standard way to say which properties instances should have, required or optional, in order. Form tools such as TopBraid read them; I know of no native Protégé form.
4. Template individuals that are duplicated (I believe Protégé has "duplicate individual").
5. Spreadsheet entry via the Cellfie plugin, if present.

## 2. Who or what can be an agent
- **"Agent" has several English senses:** an intentional agent (acts for reasons: the philosophical and legal core); a legal agent (acts for a principal); a causal agent ("agent of erosion", "chemical agent": anything that brings about an effect). Linguistics (from memory) separates the **agent** (usually animate doer) from a **force** or **instrument** ("the storm destroyed the roof").
- **So sentience is not required in the loose causal sense; the strict sense needs more.** The ontology should say which sense it means.
- **Three separable axes:** causal capacity (anything); purposive action (animals, organizations, AI systems may have it); capacity to answer for the act (needs sentience plus autonomy, or legal personhood for organizations). Which entity has which is **assessed** ("standing is assessed", 2026-11-18).
- **Inanimate things are Factors, not agents.** Flood water, windblown debris and a power grid are Factors playing a CausalRole (Conduit, ProximateCause). The toy case already modelled a grid as a Conduit Factor and an affected entity.
- **The lion at the zoo:** a purposive participant in the mauling and a causal agent in the fuller sense, but not an answerable party. Law would look to the keeper or zoo (possibly strict liability for dangerous animals; from memory, unverified). The person who fell in is an affected entity and may also be a participating factor (contributory fault).
- **One entity, several roles:** a Person, the lion or a grid can be a Factor, a participant and an affected entity in one event. v3 already says Factor and AffectedEntity are not disjoint.
- **Existing v3 pieces:** `hasAgent → Agent (?)` on Factor, `answerableAgent (?)` on CausalRole, `orchestrator → Agent (?)` on FactorAssembly, `assessor → Agent` on PerspectiveSpecification, and `Agent (?)`: UnitaryIntentionalAgent · CollectiveAgent · AutonomousSystem (?). `hasAgent` is separate from `answerableAgent`, which matches the three axes.

## 3. Participation in events
- v3 has only `Factor participatesIn FactorAssembly` ([[HO-003 Causal Assembly - the Perfect Storm]]). There is **no Event class** (Factor kinds include Act and Process; [[PerspectiveStructure 0.02]] has `originatingCircumstance → Event` as a stub) and no participation of an Agent in anything.
- **Proposed chain (not decided):** `Agent —participatesIn→ Event —participatesIn→ FactorAssembly`, with roles in the participation (principal, accessory, conspirator, vicarious party; from legal memory, unverified) and joint participation by several agents in one event.
- **Foundational case:** robbers participating in a robbery that causes an assessed loss of a pecuniary interest.
- **Participation is not responsibility.** Whether someone is answerable stays with the pending ResponsibilityAssessment ([[HO-005 Assessed Membership and Systematic Omission]]).
- **Reuse candidate:** the OBO Relation Ontology "participates in" (continuants in processes), from memory, unverified.

## 4. Assessing organizations
- `assessor → Agent` on PerspectiveSpecification should cover organizations: contracted audit firms, independent testing agencies (UL-type), regulators assessing safety, competence or compliance.
- Ties to the toy test's `assessorOrganisation`, the independence rule for settling a claim (two strictly independent organisations), and questions of authority and capture.

## 5. Proposed bookmark shape (not confirmed)
- One root **HO-007** with tiers, matching the index's tiered pattern: **I** what counts as an agent (the three axes); **II** participation in events and roles; **III** assessing organizations.
- Candidate **`HO-007-premise`:** "agency is a role in an assessed participation, not an intrinsic kind" (a hypothesis, parallel to HO-premise on harm).
- Alternatives: two or three separate top-level bookmarks.
- Test cases to add to HO-002, after approval: the robbery; the lion in the zoo; the storm with flood and debris; assessor independence and capture.
- The author's three questions are open: one bookmark with tiers or separate; add the test cases to HO-002 now; is "participation" the right word for the middle tier.

## 6. The three layers and the editor-first requirement
- **Three layers** ([[Decisions_Log]] 2026-11-17): ontology/schema (OWL, `ho:`), profiles (SHACL, `hosh:`), vocabulary (SKOS, `hov:` hubs plus discipline schemes). "Schema" is the author's 2026-11-18 name for layer 1 (not logged).
- **Namespaces name things; `owl:imports` loads files.**
- **Editor-first requirement (author, 2026-11-18):** the model must be readable and maintainable in Protégé, not through scripts or generated pages. Details and findings: [[Harm Ontology v3 Three-Layer Mini Example Brief]].
- **Property groups** (the 12 display groups of 0.02 plus the PerspectiveSpecification facets) are proposed as abstract super-properties plus an annotation (tier, group); not approved.

## Original wording
> "i don't see domain and range or groupings into superproperties"
- **Attribution:** Author
- **Source:** session "read", 2026-11-19 (`copilot/copilot-conversations/agent__read@20261118_125642.md`)

> "i believe, although i am not sure, that this is because the root classes (person, assessment) actually do not have properties attached.  they are only mentioned by domain and range in properties and in owl:Restrictions (for example, on PerspectiveType)"
- **Attribution:** Author
- **Source:** same session

> "in general, how can instances inherit the right object and annotation properties if none are explicitly specified for their respective root classes"
- **Attribution:** Author
- **Source:** same session

> "i am not interested in the script approach at all.  it is a miserable way to interact with the data if someone wanted to maintain or extend the ontology in an editor"
- **Attribution:** Author
- **Source:** same session

> "certainly law is heavilly dependent on the notion of participation in an event.  foundational example: (human/person robbers participating in an event (robbery) that causes assessed harm (loss of pecuniary interest)"
- **Attribution:** Author
- **Source:** same session

> "Can inanimate objects be "agents" of a storm in the sense that they are responsible for conveying the harm of the harmful event?  Does agency require "sentience" as a capacity for individual autonomous decision?  Or is this simply a way that we most commonly use the word agency in english?"
- **Attribution:** Author
- **Source:** same session

> "i like option 1 as well, but i still don't have a sense of what this will look like literally in an ontology editor like Protege or how to tie all this together."
- **Attribution:** Author (on narrative placement, before opening the first mini example)
- **Source:** same session

> "sorry, mistake.  it does not look great it looks awful. very difficult to visualize and navigate/understand."
- **Attribution:** Author (correcting an earlier "looks great" after opening the first mini example in Protégé)
- **Source:** same session

- **External references:** [[Harm Ontology v3 - Draft Structure]]; [[HO-003 Causal Assembly - the Perfect Storm]]; [[HO-005 Assessed Membership and Systematic Omission]]; [[PerspectiveStructure 0.02]]; [[Harm Ontology v3 Three-Layer Mini Example Brief]]; [[Decisions_Log]].

## Related
- [[Handoff - Harm Ontology]]
- [[Harm Ontology v3 Three-Layer Mini Example Brief]]
- [[Harm Ontology v3 Provisional Release Brief]]
