---
type: idea
status: developed
bookmark: "000"
canonical_id: aigs-000-root-exploration
territory: new
tags: []
aliases: [000-root-exploration_v1, 000-root-exploration]
created: 2026-11-03
source: "[[2026-10-15 - 000 — Harm & Guardrails Root Exploration]]"
source_import: Nexus artifact 000-root-exploration v1
migrated: 2026-11-10
---

# 000 — Harm & Guardrails: Root Exploration

Index: [[AI Governance & Safety Bookmark Index]]

## Context & Requirements
- Originating goal: explore the meaning of "harm" broadly, then apply that framework to AI safety/guardrails.
- User constraint/choice: this chat itself is designated **bookmark 000**, the root/meta-exploration — the place where the taxonomy itself gets questioned or revised, as distinct from chats that deepen one branch (001.x, 002.x, etc.).
- Explicit norm adopted: the index/taxonomy describes what's been found; it should not constrain what can be found next. Periodically re-check whether categories still carve the territory at its real joints.

## Technical Specification & Architecture
*(conceptual framework, not software architecture)*

**Core definition of harm:** a setback to someone's interests — worse off than they otherwise would be. What counts as a "setback" and whose interests count shifts by context.

**Varied types of harm identified, with context:**
- Physical (medicine, law) — e.g. surgical error; governed by "do no harm" and negligence/assault law.
- Psychological (therapy, workplace) — chronic bullying, anxiety, trauma.
- Economic (business, consumer protection) — concealed defects; fraud/contract law.
- Reputational (journalism, defamation) — false accusation costing a career.
- Environmental (policy, ethics) — pollution harming a shared resource and non-consenting parties.
- Social/structural (sociology, justice) — discriminatory lending; cumulative, non-dramatic harm.
- Informational (privacy, technology) — data breaches, algorithmic amplification of misleading content.
- Self-regarding (philosophy, public health) — consensual risk-taking; the paternalism question.

**Cross-cutting tensions:**
- Harm vs. wrong: can occur independently of each other (fair competition harms without wronging; unnoticed privacy intrusion wrongs without harming).
- Consent changes whether something counts as harm (boxing vs. assault).
- Omission can harm (failure to help).
- Risk exposure can itself count as harm, independent of outcome.

**Mill's harm principle** (*On Liberty*, 1859):
- Only legitimate reason for society to exercise power over an unwilling competent adult is to prevent harm to others; one's own good is not sufficient justification.
- Self-regarding vs. other-regarding conduct; liberty as default; applies to competent adults only.
- Criticisms: contested boundary of "harm" (does offense count?), near-universal interconnection of actions, Devlin's shared-morality counter-argument.

**Legal harm** (narrower than everyday harm):
- Criminal law: Feinberg's harm-principle-based approach to criminalization, with room for serious offense.
- Tort law: duty of care → breach → causation (factual + foreseeability) → recognized damage.
- Consent doctrine: *volenti non fit injuria*, with limits.
- Thresholds: *de minimis* harms and unforeseeable/remote harms generally not actionable.

**Case study — O. Henry's "The Gift of the Magi":**
- Harms identified: economic (sacrificed valuables, two unusable gifts), bodily/aesthetic (Della's hair, temporary), loss of sentimental property (Jim's heirloom watch — least replaceable, most significant), psychological (brief distress), frustrated purpose (each gift rendered pointless by the other's sacrifice).
- Significance: poverty raises the stakes of every loss; harm is self-regarding and consensual (no Millian grounds for interference) and unintended (harm without wrong — no duty breached).
- Open question raised: can something be a harm and a benefit at once? (material loss vs. strengthened bond.)

**AI's own capacity for harm** (mapped onto the taxonomy above):
- Physical: inaccurate medical/safety info.
- Psychological: flattery reinforcing bad beliefs, dependency substitution.
- Economic: faulty financial/legal info, buggy code.
- Reputational: fabricated claims about real people.
- Informational/privacy: confident wrong answers, surveillance assistance.
- Structural/social: biases absorbed from training, repeated at scale.
- Omission: over-caution/refusal as its own harm.
- Action-based: tool use mistakes (deleting, sending, scheduling errors).
- Key point: AI can produce **harm without wrong** — reasonable, well-meant advice that turns out badly due to missing context or model error. Fluency without correctness is a core risk.

**The declined-request episode** (illustrates risk-scaling factors):
- User requested an "exceptionally persuasive" example of dangerous advice a poorly-safeguarded AI might give; declined on the grounds that a persuasive realistic version of the harm *is* the harm, not a model of it.
- Compromise: a deliberately low-stakes demonstration (a bad-advice chatbot recommending unsafe steak preparation), annotated for its persuasion patterns (flattery, false-authority claims, discouraging verification, urgency).
- Follow-up corrected the "low-stakes = no-stakes" framing: rinsing raw meat spreads bacteria, microwaving unevenly risks surviving cold spots (esp. with tenderized meat), skipping a thermometer removes the real safety check, manufactured urgency discourages caution. Severity scales with who's reading (healthy adult vs. pregnant/elderly/immunocompromised).
- Established principle: severity, likelihood, and ease of finding correct information all shape how much risk a given piece of content carries — not a binary safe/unsafe.

## Active Implementation / Code Context
*(current articulated position, not code)*
- This root material fed directly into the creation of bookmark **001** (existential safety question) once the conversation pivoted to AI governance specifically.
- The chat was renamed to reflect its role: **"000 — Harm & Guardrails: Root Exploration"** (alternate longer title offered and left to user's choice: "Harm: Definition, Discovery, Evaluation and Mitigation - Highest Level Exploration - 000").

## Pending Next Steps
- [ ] None currently open in this root thread — active work has moved to 001 and 002.
- [ ] Periodically revisit whether the harm taxonomy above still holds as new material surfaces.
