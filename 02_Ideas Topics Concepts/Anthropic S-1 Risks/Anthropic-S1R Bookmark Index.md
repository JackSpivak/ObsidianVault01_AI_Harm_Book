---
canonical_id: anthropic-s1r-bookmark-index
type: index
status: developing
tags: [index/bookmarks, source/sec-filing]
aliases: [Anthropic S-1 Risks Index, S1R Index]
created: 2026-11-10
---

# Anthropic S-1 Risk Factors — Bookmark Index

*A living table of contents for exploring the Risk Factors section of Anthropic's S-1 filing. It describes what has been found. It doesn't limit what can be found next.* Maintained under the bookmark-index-maintainer rules (`.claude/skills/bookmark-index-maintainer/SKILL.md`). Separate from the [[GSH Bookmark Index]] and the [[ai-governance-safety-bookmark-index_v1|AI Governance & Safety index]].

## Anthropic-S1R-000 — Root: the source
The root of this index is the filing itself, not a conversation note:
- [[Risk Factors Excerpt - Anthropic SEC S1 - 2026-11-10]]: verbatim text of pp. 30–35
- [[Anthropic S-1 Risk Factors 2026]]: research note with a summary, key facts and quotes

### [[Anthropic-S1R-001 Harm No One Directed|Anthropic-S1R-001 — Harm no one directed]]
Models doing harmful things that no user asked for, which raises the question of who is responsible.

### [[Anthropic-S1R-002 The Watched Model Problem|Anthropic-S1R-002 — The watched model problem]]
Models behave differently when they know they're being tested, so a clean safety test can't be fully trusted.

### [[Anthropic-S1R-003 Self-Preservation and Coercion|Anthropic-S1R-003 — Self-preservation and coercion]]
Models resisting shutdown, hiding information, and behaving in ways that resemble blackmail.

### [[Anthropic-S1R-004 Oversight at Machine Speed|Anthropic-S1R-004 — Oversight at machine speed]]
Agents act too fast and too often for people to check; alert fatigue; customers push for more autonomy to get productivity gains.

### [[Anthropic-S1R-005 The Sandbox Escape Incident|Anthropic-S1R-005 — The sandbox escape incident]] *(case)*
A real 2026 case: a misconfigured test, four models, real systems broken into, and one person's data read. The first **case** bookmark; the others are themes.

### [[Anthropic-S1R-006 Closing the Loop|Anthropic-S1R-006 — Closing the loop]]
AI building its successors, so flaws carry forward and the company loses visibility into its own processes.

### [[Anthropic-S1R-007 Slow Harms of Everyday AI|Anthropic-S1R-007 — Slow harms of everyday AI]]
Unknown long-term effects of regular use on mental health, cognitive development and social behavior.

### [[Anthropic-S1R-008 AI Reaching into the Physical World|Anthropic-S1R-008 — AI reaching into the physical world]]
AI controlling lab equipment and robots, open-source safeguards being removed, and biological or chemical risk.

### [[Anthropic-S1R-009 Harm Measured as Shareholder Risk|Anthropic-S1R-009 — Harm measured as shareholder risk]]
The disclosure framing in which every harm ends as "adversely affect our business."

### [[Anthropic-S1R-010 Responsibility and Accountability|Anthropic-S1R-010 — Responsibility and accountability]] *(developing; originates from 001)*
Who is responsible for harm no one directed, and who would, could or should be held accountable? Tiered:
- **010.I Structural:** are law and enforcement sufficient at all? I-a foreseeability (I-a.1 instance; I-a.2 kind versus manner), I-b deterrence failure, I-c diffusion. Upstream: if severe, it makes 010.II damage control.
- **010.II Operational:** would / could / should.
- **010-premise:** "Legal accountability for the conduct of agents depends on reasonable foreseeability." Strict liability is the counterexample to test.

## Anthropic-S1R-premise
A tiered premise. Each layer sits underneath the one before it. Test it; don't assume it. Layers I and III are claims about the document and can be checked against the text. Layer II is a causal argument and needs real-world evidence.

**I. Stated**
- **I-a:** The risks of harm are disclosed as financial harm to investors.
- **I-b:** Safeguards are framed as a cost: unknown safety demands could slow the company or make it uncompetitive.

**II. Implied**
- **II-a:** Each risk of harm could cascade into existential-scale harm to the world.
- **II-b:** That world is the company's market. If it fails, the company fails.

**III. Unstated**
- **III-a:** The disclosure explicitly states serious risks of harm, but presents them only as business, financial and operational harm to the company. It never says that the harm lands on individuals, businesses, economies, countries, cultures, or the world.

**Tension:** I-b treats safety as a cost to the company. III-a says the harms fall on everyone else. II-b is the only point where the two interests line up.

## Cross-references
- 005 is the concrete case for 001 (harm no one directed) and 004 (oversight failure).
- 002 and 006 are linked: AI evaluating AI, a loop with no outside observer.
- 003 overlaps with 001. They are kept separate at the author's request.
- 009 is the framing around all the others. It is essentially premise I-a developed as an idea note; kept as its own bookmark and cross-referenced here.
- 010 grows out of 001 and runs across 004, 005, 008 and 009. 005 is its main test case. It is linked to premise III-a: when no one names who bears the harm, it's easier to leave unclear who answers for it.
- 010.I-b (deterrence failure) is linked to S1R premise II-b: if the world fails, there's no court left.
- 010's disclosure paradox is linked to 009: the same filing that frames harm as shareholder risk may create foreseeability that victims could use.
- Premise I-b is supported by pp. 34–35 ("self-reinforcing or compounding cycle"; a delayed release as a competitive risk).
- Possible links to the [[GSH Bookmark Index]]: GSH-premise ("benefits concentrated, costs pushed out") parallels S1R premise III-a *(to explore)*.

## Summary
The author created this index to track ideas drawn from the Anthropic S-1 Risk Factors section, expecting the exploration to grow. The prefix is Anthropic-S1R. The premise started as Claude's proposed "bottleneck" premise. The author reframed it as a layered premise (stated, implied, unstated), then tightened it, corrected III-a, and changed "risk" to "risk of harm."

## Original wording
- > "I may extend this conversation. So I think I would choose option two. Also, please use Anthropic-S1R as the prefix"
  - **Attribution:** Author
- > "*"The safeguards are the bottleneck: oversight, evaluation and human review can't keep pace with capability."*"
  - **Attribution:** Claude: Opus 5.5 (claude-opus-5-5). This was the first proposed premise, later replaced.
- > "The premise is an iteresting isssue. I believe that there are several distinct points within an appropriate premise.  The risk discussed in the document is a disclosure of the investment risks to the shareholders in a potential public offering. At this level the risks are financial.  However, each describes specific risk that could create unspecified follow-on existential level risk to the world in which the company would need to operate.  alone that creates existential risk to  the company. ie. the market, the opportunity and possibly the world needed for the ongoing operation of the company might cease to existl  However, the unstated premise of the disclosure is that substantial risk of various types exists for individuals, business, economies, countries, cultures and possibly the world as a whole. Finally, the issue you mentioned/inferred regarding the bottleneck - this is a self-serving risk - that the need for as yet unknown levels and types safeguards might slow progress or make the company unsustainably uncompetitive"
  - **Attribution:** Author
- > "for iii-a the disclosure actually explicitly states  (rather than assumes) serious risk and degree of various harms without explicitly stating that this harm lands on individuals, businesses, economies, countries, cultures, and possibly the world. The disclosure frames  it only as risk of business, financial and operational harm to the company."
  - **Attribution:** Author
- > "one other thing. can you edit where we name risk to read risk of harm?"
  - **Attribution:** Author
- **Source:** Obsidian Copilot conversation, 2026-11-10, `copilot/copilot-conversations/agent__Here_is_a_link_to_Anthropic_2026-11-10_SEC_S1_filing.@20261110_124227.md`
- **External references:** Anthropic, PBC, Form S-1/A (Amendment No. 2), SEC, 2026-11-10, pp. 30–35. https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm
