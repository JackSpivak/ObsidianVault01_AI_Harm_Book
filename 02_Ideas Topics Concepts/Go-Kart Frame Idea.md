---
type: idea
status: seed
tags: [side-project/go-kart]
aliases: [Go Kart Frame, Gocart Frame]
created: 2026-11-04
---

# Go-Kart Frame Idea

> [!note] Off-topic for the book
> This is a personal side-project idea, not AI harm material. You can move it out of this vault if you want.

## Summary

This is an idea to design and build a go-kart frame (chassis). Web research gives the following starting points. They are **not** engineering specs, and the figures come from builds of mixed quality.

### Material and tubing
- **Mild steel (DIY):** One guide recommends ASTM A500 Grade B tubing at 1.25 in OD × 0.095 in wall for adult karts.[^alibaba] Another uses 1 in square tube with a 0.100 in wall and says square tube is easier to keep square.[^wcw] *(The low-authority sources are unverified.)*
- **4130 chromoly (racing):** Modern shifter karts mostly use 32 mm 4130 tubing.[^kartclass] It's stronger for its weight, but it needs TIG welding.[^garagewelding] It only saves weight if you use thinner or smaller tube.[^diyforum]
- **Mixed diameters:** One patent mixes 1.125 in and 1.25 in tube so the chassis isn't too stiff and can roll more in corners.[^patent]

### Geometry
- Racing-style reference: about a 48 in wheelbase and a 30 in front track.[^handmade] *(unverified)*
- CIK-FIA homologation classes chassis by wheelbase, front and rear widths, and the diameter and number of main tubes.[^fia] A seller site quotes a 1040 mm minimum wheelbase, but that comes from a seller, not the rulebook. *(unverified)*
- Ground clearance: about 3.5 in minimum.[^alibaba] Too much clearance raises the centre of gravity and the risk of rollover.[^diyframe]

### Stiffness and handling
- Karts have no suspension, so the frame flex does the suspension's job. The chassis needs torsional rigidity but also some flexibility.[^ijari]
- Torsional stiffness scales with the frame's horizontal width.[^wit]
- Caster changes camber as you steer (more negative on the outside front wheel). Ackermann lifts the inside rear tyre. Sources disagree on pro- vs anti-Ackermann.[^angri][^jetir]

### Building it
- Draw the frame full size, then build a plywood jig with 1×2 stops. Tack weld everything first, brace against weld distortion, and check that the diagonals match.[^kartfab][^wcw]
- Before you build, check the frame with FEA, e.g. beam elements in SolidWorks.[^rg1]

### Electric variant and safety
- Mount the battery low and central.[^xjd] One paper used a 47:53 front-to-rear weight split.[^rg2]
- Use a roll bar that runs from the front to above the driver's head.[^diyframe] Electrathon rules also require brakes, a roll bar, and an electrical disconnect.[^electrathon]

### Open questions
- [ ] Use: fun/yard kart, or a racing class (which rules apply)?
- [ ] Power: gas or electric?
- [ ] Material: mild steel (MIG) or chromoly (TIG)?

## Original wording

> "make a new note about an idea for a gocart frame deep exhaustive websearch"
> — **user (jspiv)**

- **Source:** Obsidian Copilot agent session, 2026-11-04 (copilot/copilot-conversations).
- **External references:** web searches run in that session; see Sources.
- The research content above is Claude's paraphrase (Claude: Opus 5.5, claude-opus-5-5). It isn't a quote from the conversation.

## Sources

[^alibaba]: Alibaba Product Insights, "DIY Go Kart Frame: Build A Safe Steel Chassis" — https://www.alibaba.com/product-insights/diy-go-kart-frame-build-a-safe-steel-chassis-step-by-step.html (low authority)
[^wcw]: WC Welding, "Go Kart Frame Build" — https://www.wcwelding.com/go-kart-frame.html
[^kartfab]: KartFab, "Go Kart Frame Plans" — https://kartfab.com/go-kart-plans/go-kart-frame
[^handmade]: Handmadelytics, "How to Build a Go-Kart" — https://handmadelytics.com/sewing/build-a-go-kart (unsourced figures)
[^patent]: US6022049A, "Go-kart chassis formed from tubular sections" — https://patents.google.com/patent/US6022049
[^kartclass]: KartClass, "Best Shifter Kart Chassis" — https://kartclass.com/blogs/technical-guides/best-shifter-kart-chassis-how-to-choose-the-right-frame-for-kz-and-kz2
[^garagewelding]: Garage Welding, "4130 Chrome-Moly vs Mild Steel" — https://garagewelding.com/chrome-moly-vs-mild-steel-automotive-chassis-welding/
[^diyforum]: DIY Go Karts forum, "Racing Kart chassis — Steel vs Chromoly?" — https://www.diygokarts.com/community/threads/racing-kart-chassis-steel-vs-chromoly.14158/
[^fia]: FIA Karting, Homologation Regulations 2023 — https://www.fiakarting.com/sites/default/files/2023-03/2023%20Karting%20Homologation%20Regulations%20(marked%20up)%2008.03.2023_0.pdf
[^wit]: WIT Press, "A study on torsional stiffness of the competition go-kart frame" — https://www.witpress.com/Secure/elibrary/papers/OP07/OP07018FU1.pdf
[^ijari]: IJARI, "Design, Development and Fabrication of a Go-Kart" — https://ijari.org/assets/papers/6/2/IJARI-ME-18-06-130.pdf
[^angri]: Angri Racing, "Kart Setup" — https://www.angriracing.com/kart-setup
[^jetir]: JETIR, "Design & Calculations of Ackermann Steering System" — https://www.jetir.org/papers/JETIR2501641.pdf
[^rg1]: ResearchGate, "Design and Fabrication of Electric Go-Kart" — https://www.researchgate.net/publication/345650481_Design_and_Fabrication_of_Electric_Go-Kart
[^rg2]: ResearchGate, "Design and Analysis of Electric Go Kart" — https://www.researchgate.net/publication/345416536_DESIGN_AND_ANALYSIS_OF_ELECTRIC_GO_KART
[^xjd]: XJD, "How to make an electric go kart" — https://www.xjd.com/t-how-to-make-a-electric-go-kart-step-by-step/
[^diyframe]: DIY Go Karts, "Go Kart Frame Design" — https://www.diygokarts.com/kart-plans/plans-frame-how-to-design.html
[^electrathon]: Wikipedia, "Electrathon" — https://en.wikipedia.org/wiki/Electrathon
