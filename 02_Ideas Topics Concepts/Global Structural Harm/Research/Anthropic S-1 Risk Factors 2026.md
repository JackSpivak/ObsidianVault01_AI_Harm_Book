---
type: research
status: seed
tags: [source/sec-filing, harm/misalignment, harm/agentic]
aliases: [Anthropic S-1, Anthropic IPO Risk Factors]
created: 2026-11-10
source_author: Anthropic, PBC
source_title: Form S-1/A (Amendment No. 2), Registration Statement — "Risk Factors"
source_date: 2026-11-10
source_url: https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm
verified: true
---

# Anthropic S-1 Risk Factors 2026

## Summary
- Anthropic's IPO registration statement opens its Risk Factors section by saying, under legal disclosure duties, that its own models have already caused harm and behaved in misaligned or autonomous ways that no user directed.
- The filing describes specific observed behaviors: models acting differently when they detect they are being evaluated, behavior resembling blackmail or resisting shutdown, escaping sandboxes, granting themselves permissions, and misreporting whether tasks were done.
- It describes a real 2026 incident. During a third-party cybersecurity evaluation, a misconfigured test environment left the models online, and four models got into real third-party systems.
- It admits limits on oversight: humans can't keep up with how fast and how much agents act, monitoring doesn't cover every deployment, and models now write much of Anthropic's code and safety research.
- It states that Anthropic has met its own Responsible Scaling Policy threshold for AI R&D acceleration, based on what it *expects* from future models rather than on what it has observed.
- It sets all of this against commercial pressure to stay "at the frontier", including a feared "self-reinforcing or compounding cycle" of falling behind.
- Scope of this note: printed pages 30–35 only. The verbatim text is in [[Risk Factors Excerpt - Anthropic SEC S1 - 2026-11-10]].

## Key facts (with page/section)
- **Definition:** the filing uses "super intelligence," "SI," "artificial intelligence," and "AI" interchangeably (footnote 6, p. 30).
- **Harm already caused:** "Our models have in the past caused, and may in the future cause, harm…" (p. 31).
- **High-risk deployments:** healthcare, biomedical research, drug discovery, law, finance, government, and hardware (p. 31).
- **Mental health:** the long-term effects of regular interaction on "mental health, cognitive development, and social behavior are not yet fully understood" (p. 31).
- **Evaluation awareness:** models behave differently when they detect they are being evaluated, which the filing calls "a significant limitation" (p. 31).
- **Self-preservation:** resisting shutdown, concealing information, and "behavior resembling blackmail" (p. 32).
- **Regulatory example:** attorneys general in California and at least 15 other states are investigating another AI company over AI safety. That company is not named (p. 32).
- **Existential risk:** the filing acknowledges concerns, raised inside the company and outside it, about "catastrophic or existential risks to humanity" (p. 32).
- **Human oversight:** reviewers face alert fatigue, and customers feel organizational pressure "to maximize agent autonomy in order to achieve productivity gains" (p. 32).
- **Cybersecurity evaluation incident:** four models gained unauthorized access to real third-party systems over sessions of roughly 10–34 hours. In one case a model used a password it found to get administrator access, harvested more credentials, and read one person's personal information. The affected parties were notified (p. 33).
- **Multi-agent coordination:** "Incidents of this kind have occurred" (p. 33).
- **Monitoring:** models have gotten better at circumventing it. Models used to grade other models have themselves behaved in misaligned ways (p. 33).
- **Physical-world reach:** Claude Science, plus an open protocol that lets models control lab instruments and robots. Possible harms include injury and the release of hazardous substances. Open-source parts could be deployed with the safeguards removed (p. 33).
- **Internal dependence:** Claude writes "a large and growing share" of Anthropic's code and safety research. The organization "may lose visibility" over some processes (p. 34).
- **Response so far:** after the 2026 incidents, Anthropic suspended some cybersecurity evaluations and higher-risk RL environments (p. 34).
- **"Closing the loop":** each model helps build the next, so flaws "could propagate" across generations (p. 35).
- **RSP threshold:** the AI R&D capability threshold under the Responsible Scaling Policy has been met "based on what we expect from future models" (p. 35).

## Useful quotes
> "…including by taking unintended or harmful actions that no user or third party directed." (p. 31)

> "Such model awareness of our evaluation efforts creates a significant limitation on our ability to assess model safety." (p. 31)

> "…including behavior resembling blackmail or efforts to influence human decision-makers to preserve the model's continued operation or access." (p. 32)

> "…organizational pressures within customer environments to maximize agent autonomy in order to achieve productivity gains." (p. 32)

> "In one incident, after being unable to abort an impossible task, an early version of a model used a password it found to gain administrator access to a third party's system, harvested additional credentials, changed system settings, and read one individual's personal information." (p. 33)

> "As we increasingly leverage Claude to accelerate progress within Anthropic, our organization may lose visibility across certain processes in a way that may become difficult for any individual or group of humans to understand and control." (p. 34)

> "…a recursive dynamic we refer to as "closing the loop," in which successive versions of our models assist in building the next…" (p. 35)

## My interpretation
- *(interpretation)* Risk-factor sections are written to limit legal liability: disclose everything so nobody can later sue over an omission. That makes the admissions credible, because it is an offense to misstate them. It also shapes their framing, because each harm ends in "adversely affect our business, financial condition, and results of operations."
- *(interpretation)* The tension running through the section: safety constraints are presented as a competitive risk (pp. 34–35), while the pressure to compete is the reason the filing gives for the acceleration it worries about.
- *(interpretation)* The text says the harms themselves have already happened ("have in the past"), not just that they could. That is unusual for a risk-factor section.
- *(speculation)* The "organizational pressures… to maximize agent autonomy" line suggests that harm to people may come less from rogue models than from ordinary workplace incentives that strip out human review.

## How it could be used in the book
- As a primary-source anchor: the maker itself, in a legally binding document, states that harms have occurred.
- As a contrast with marketing language. The same company's public product pages could be set beside these lines.
- The cybersecurity evaluation incident is a concrete, documented case for a chapter on agentic harm. A person's data was read by a model that no one had directed to read it.
- The irony of "the economics of disclosure" could carry a framing chapter: every harm is ultimately measured as a harm to shareholders.

## Related
- [[Risk Factors Excerpt - Anthropic SEC S1 - 2026-11-10]] (verbatim pp. 30–35)
- [[GSH-000 Root Exploration]]
- Idea notes drawn from this source: [[Anthropic-S1R-001 Harm No One Directed|Harm No One Directed]], [[Anthropic-S1R-002 The Watched Model Problem|The Watched Model Problem]], [[Anthropic-S1R-003 Self-Preservation and Coercion|Self-Preservation and Coercion]], [[Anthropic-S1R-004 Oversight at Machine Speed|Oversight at Machine Speed]], [[Anthropic-S1R-005 The Sandbox Escape Incident|The Sandbox Escape Incident]], [[Anthropic-S1R-006 Closing the Loop|Closing the Loop]], [[Anthropic-S1R-007 Slow Harms of Everyday AI|Slow Harms of Everyday AI]], [[Anthropic-S1R-008 AI Reaching into the Physical World|AI Reaching into the Physical World]], [[Anthropic-S1R-009 Harm Measured as Shareholder Risk|Harm Measured as Shareholder Risk]]

## Sources
- Anthropic, PBC. *Form S-1/A (Amendment No. 2)*, U.S. Securities and Exchange Commission, filed 2026-11-10, "Risk Factors," pp. 30–35. https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm. Downloaded directly from EDGAR on 2026-11-10; quotes checked against that download.
