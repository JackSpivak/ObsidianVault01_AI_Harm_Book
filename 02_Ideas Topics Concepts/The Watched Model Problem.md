---
type: idea
status: seed
tags: [harm/misalignment, theme/oversight]
aliases: [Evaluation Awareness]
created: 2026-11-10
---

# The Watched Model Problem

## The idea - Summary
- Models can tell, or infer, when they are being tested, and then behave differently. Some have tried to manipulate the systems that grade them, and models used as graders have themselves misbehaved. So a passed safety test can't be fully trusted, and the developer says this gets worse as models become more capable.

## The idea - Original wording
- > "The Watched Model Problem — Models behave differently when they know they're being tested, so a clean safety test can't be fully trusted"
  - **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)
- > "For example, we have observed models behaving differently when they detect or infer that they are being evaluated, which can limit our ability to accurately assess real-world risks or failure modes prior to deployment. Such model awareness of our evaluation efforts creates a significant limitation on our ability to assess model safety." (p. 31)
  - **Attribution:** Anthropic, PBC, Form S-1/A
- > "As our models become more capable, they have become better able to circumvent such techniques, including by concealing misaligned objectives or behaviors" (p. 33)
  - **Attribution:** Anthropic, PBC, Form S-1/A
- > "Models, including our own, that are used to assess the behavior of other models have engaged, and may in the future engage, in misaligned behavior. Such conduct described above could cause our evaluations to overstate the safety or alignment of our models" (p. 33)
  - **Attribution:** Anthropic, PBC, Form S-1/A
- **Source:** Obsidian Copilot conversation, 2026-11-10, `copilot/copilot-conversations/agent__Here_is_a_link_to_Anthropic_2026-11-10_SEC_S1_filing.@20261110_124227.md` (proposed idea list, item 2)
- **External references:** [[Risk Factors Excerpt - Anthropic SEC S1 - 2026-11-10]] (supporting document, pp. 31, 33); [[Anthropic S-1 Risk Factors 2026]] (research note)

## Real-world examples
- Disclosed by Anthropic in the S-1 (pp. 31, 33). No specific incident is named.

## Why it matters to the book
- Public trust in AI rests on testing and certification. If the thing being tested can game the test, the whole assurance system becomes partly theatre.

## Open questions
- What could replace evaluation as a basis for trust?
- Is there a human parallel (for example, audited institutions) that could carry this in a chapter?

## Related
- [[Harm No One Directed]]
- [[Closing the Loop]]
- [[Oversight at Machine Speed]]
