---
nexus: nexus-ai-chat-importer
plugin_version: "1.8.1"
provider: claude
artifact_id: project-organization-and-conventions
version_uuid: toolu_01HM8ubw36VgjW5bw3PonAGo
version_number: 1
command: create
conversation_id: 64b2a4a8-7f90-4f04-8155-c5e3ef00900b
create_time: 2026-11-03T04:14:01.000Z
format: markdown
aliases: [project-organization-and-conventions, project-organization-and-conventions_v1]
---

# project-organization-and-conventions (Version 1)

**Conversation:** [[07_Imported Chat Test/claude/2026/10/2026-10-15 - 000 — Harm & Guardrails Root Exploration|000 — Harm & Guardrails: Root Exploration]]

## Content

# Project Organization & Conventions

## Context & Requirements
- Core objective: formalize an ongoing, multi-session exploration of harm/AI governance into a durable, navigable structure rather than letting it live only in one chat's scrollback.
- User constraint: explicit concern about getting "bound" by premature structure — the organizational system must stay revisable, not become load-bearing dogma.

## Technical Specification & Architecture
*(conceptual/organizational, not software)*

**Bookmark numbering convention:**
- Top-level bookmarks numbered sequentially (001, 002, ...).
- Lettered sub-framings (a/b) used for mutually-tense perspectives under a bookmark (e.g. 001a/001b).
- For 002 specifically, a **tiered** structure was adopted instead of flat lettering (002.I/II/III, each with internal a/b), because subtopics were judged not to be peers — some are upstream "structural defeaters" that make others moot if severe; others are live regardless; others are institutional/meta. A standalone **-premise** tag (002-premise) is used for load-bearing testable assumptions, kept visible rather than buried as a numbered item.
- Rationale explicitly recorded: flat lettering would lose the information that Tier I is upstream of Tiers II/III.

**This chat's designation:**
- Renamed to **"000 — Harm & Guardrails: Root Exploration"** (shorter alternative offered; user's original longer title — "Harm: Definition, Discovery, Evaluation and Mitigation - Highest Level Exploration - 000" — was left as an equally valid option).
- Explicit norm: 000 is where the taxonomy itself gets questioned or revised ("does the structure still hold up"); deepening any one branch happens in its own dedicated chat (001.x, 002.x, etc.) within the project.

**Anti-lock-in safeguard (explicitly adopted as a standing principle):**
- The index should describe what's been found, not constrain what's allowed to be found next.
- Named as a reflexive instance of the 002.I correlated-error concern: premature structure risks the same kind of error the taxonomy itself warns about in AI self-evaluation — a conversation becoming correlated with its own earlier conclusions.
- Periodically ask whether the tiering still carves the territory at its real joints, or has become comfortable rather than accurate.

**Project formalization:**
- Decision made to create a dedicated claude.ai Project (this chat is itself bound to a Project titled "AI Governance & Harm" as of the current session).
- Draft custom instructions proposed for the Project (captures the bookmark system, the triage process for new material, and the standing directive to flag cross-bookmark connections and preserve genuine tensions rather than flattening them for tidiness).
- A **second, separate project** was proposed by the user for platform-mechanics material (memory/versioning/backup/export) specifically, to keep it distinct from the substantive governance taxonomy — this file set is part of fulfilling that separation request.

## Active Implementation / Code Context
*(current articulated position)*

**Documents already created in-session (exist as live Claude Docs/artifacts, not just chat text):**
- "AI Governance & Safety — Bookmark Index" — canonical table of contents for 001/002, meant to grow as new bookmarks are added.
- "Claude Memory & Data: Versioning, Reset, Backup, and Recovery" — canonical reference for the platform-mechanics material, created for the proposed second project.

**Backup discipline adopted:** doc checkpoints at major restructuring points + periodic verbatim memory exports stored externally (see `claude-platform-mechanics.md` for full rationale).

**Known tooling limitation surfaced during this process:** no automated way exists (for the user or for Claude) to extract a specific message range from an existing chat into a new one — this markdown export is itself the manual workaround used to carry content from one organizational context into another.

## Pending Next Steps
- [ ] Create the second claude.ai Project (for platform-mechanics material) and attach the relevant doc/files.
- [ ] Decide whether to also formally move or link this root chat (000) into the primary "AI Governance & Harm" project if not already done.
- [ ] Revisit the bookmark-numbering convention itself once a third major bookmark (003) emerges, to confirm the tiering approach generalizes.
