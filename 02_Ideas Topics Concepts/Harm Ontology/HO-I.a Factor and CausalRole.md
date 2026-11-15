---
fileClass: Idea
type: idea
status: developing
bookmark: HO-I.a
canonical_id: ho-factor-causal-role
territory: new
tags: [ontology/harm]
aliases: [HO-I.a, Factor, CausalRole]
created: 2026-11-14
filed: 2026-11-14
---

# HO-I.a — Factor and CausalRole

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-000 Harm as Perspective-Relative Assessment|HO-000]] · Tier HO-I (core model)

## Why this is distinct
- It separates **what a thing is** (a Factor) from **what part it plays** in one particular chain (a CausalRole). It uses "Factor" rather than "Event" because omissions, risks and structures are not events.

## Anticipated direction
- Factor types: Act, Process, Omission, Condition (possibly split into physical state, status and disposition), Structure, Risk.
- Role types: Trigger, Enabler, Amplifier, Conduit, ProximateCause, DistalCause, ContributingCause.
- Role properties: causal necessity (but-for, sufficient, overdetermined, contributory), proximity, causal share, isDistributed, foreseeability, answerable agent.
- Possible alignment with BFO's Role class.

## Conceptual territory
- New. v1 had causation only as one attribute (`hasCausationMechanism`). The chain-of-factors approach resembles factor-based legal reasoning (HYPO/CATO; from memory, unverified).

## Summary
- A Factor is neutral. It bears a CausalRole in a specific chain, contributing to an Effect. One factor can play different roles in different chains: an engagement loop can be the *amplifier* of one person's radicalisation and the *trigger* of another's sleep loss. Making roles things in their own right lets them carry their own properties. Each property sits where it belongs: `isContinuous` on the Factor, `isPosthumous` on the Effect.

## Original wording
> "A perpetrator shoots a victim.  The victim dies.
>
> causation:
>  aiming and  pulling the trigger > operation of gun mechanism > explosion in shell propels bullet > bullet strikes skin > bullet enters body > damages (harmful effect - also phenomenon) skin/muscle/organs/bone > loss of beneficial life functions > death of victim"
- **Attribution:** Author

> "so maybe a starting point aligned with your view might be to consider if a role is to be a thing in itself or a property of a thing."
- **Attribution:** Author

> "the benefit of this approach is that the roles can have appropriate properties like
>
> isPosthumous
> isDistributed
> isContinuous"
- **Attribution:** Author

> "im sorry. this is rolling back too far.  didnt we make a decision to speak of factors rather than events for good reason?"
- **Attribution:** Author

> "Here's a simple test: **does it stay true if you remove the harm chain?**"
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references:** BFO (Basic Formal Ontology) Role (from memory, unverified).

## Real-world examples
- The shooting chain: Act (trigger pull) → Process (gun mechanism) → … → Effect (death).

## Why it matters to the book
- AI harm chains are long, spread across many actors, and full of links nobody observes. Roles make it possible to say *what part* each actor's contribution played.

## Open questions
- Is the list of role types complete?
- Is causal share measurable, or only ordinal?
- Does a Structure cause harm, or only provide the setting for agents?

## Related
- [[HO-I.b Effect and Cascades]]
- [[HO-I.c Phenomenality - Observability and Experienceability]]
