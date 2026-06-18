# Anti-slop — the tells, the fixes, the audit gate

This is the heart of zobe.ai. "AI slop" is the recognizable look of design produced without decisions: default fonts, rainbow accents, drop-shadow card soup, no hierarchy. This file is zobe.ai's catalogue of those tells and the craft fixes that replace them.

Use it two ways:
- **Diagnose** an existing design (de-slop mode).
- **Self-audit** your own output before delivering (SKILL.md Step 5 — mandatory).

---

## The slop tells → the craft fix

| # | Slop tell | The fix |
|---|---|---|
| 1 | **Inter/Roboto/Open Sans/system-ui as the BRAND voice** | License or commission a characterful display face, self-host it, load it first. Demote Inter/Satoshi to a quiet body workhorse under it. |
| 2 | **Rainbow of accents / leftover Gutenberg palette** (`#cf2e2e #ff6900 #fcb900 #00d084 #0693e3 #9b51e0`) shipped in CSS | Monochrome base + ONE accent used with conviction (70–150× in source while no competing hue appears). Strip dead default palettes. |
| 3 | **Default card stack:** `rounded-lg` + `0 2px 4px rgba(0,0,0,.5)` floating on gray | Go flat. Separate by background-color + full-bleed imagery (alternating light/dark tiles), or ONE whisper-soft large-blur shadow (6–16% black, 8–16px blur) used consistently. |
| 4 | **All type at default weight, 0 tracking — no tension** | Display huge + negative tracking (-0.5 to -3px / -0.02 to -0.05em); labels tiny + UPPERCASE + +0.1 to +0.2em. Giant-tight vs tiny-wide is the cheapest craft win. |
| 5 | **`transition: all .3s ease` everywhere, no curve** (the page-builder default) | Define 1–2 easing tokens (workhorse ease-in-out 200–320ms + one expressive curve, e.g. `cubic-bezier(0.165,0.84,0.44,1)` expo-out or an iOS spring `cubic-bezier(0.32,0.72,0,1)`). Reuse them. |
| 6 | **Mixed arbitrary radii** (0/3/4/6/8/10/50px) with no system | Pick ONE shape identity — sharp 0-radius OR a tokenized soft scale (6–12px + full pills) — and tokenize it. |
| 7 | **Pure #000 on pure #fff, #fff everywhere** | Near-black text (`#020202`–`#1d1d1f`), warm/cool off-white surfaces (`#f5f5f7`, `#fbf9f2`). Reserve pure values for high-contrast moments. |
| 8 | **Generic stock-people, decorative Unsplash gradients, un-art-directed AI output** | Bespoke or art-directed imagery treated consistently (palette-graded, dark scrims for legible text), grayscale logo walls. Generate only under the discipline in `imagery-generation.md`. |
| 9 | **Vague filler copy** ("high-quality solutions", "we deliver excellence") + placeholder/duplicate text | Write with specificity and voice: concrete numbers, named proof, a real attitude. Proofread the biggest lines. |
| 10 | **Everything center-aligned, same size, crammed** | Steep size hierarchy + readable measure (700–850px). One idea per section. Center-align sparingly. |
| 11 | **Redundant extra Google font for one element** the brand face already covers | One display + one body face. Font sprawl = no system governance. |
| 12 | **Brittle `!important` overrides skinning a stock theme** | Customize via design-system/theme tokens, not `!important` sledgehammers. A skin bolted onto a template is detectable. |
| 13 | **No tokens — scattered hardcoded hex/px** | Fluid `clamp()` scales + semantically-named color tokens up front. Name colors by role, not hex. |
| 14 | **Accent-colored small body text below contrast** | Keep body copy on high-contrast ink. Engineer a darker accent variant for button/text contrast (WCAG). |

---

## The red-flag checklist (run before every delivery)

Tick each. If any is true, fix it before shipping.

- [ ] Identity font is a characterful display face, **not** Inter/Roboto/system-ui as the brand voice.
- [ ] Exactly **one** accent (or a justified dominant/secondary system). No leftover rainbow palette.
- [ ] No harsh default card shadows. Depth comes from flatness/tiles/imagery, or one consistent soft shadow.
- [ ] **One** tokenized radius identity. No scattered 3/4/6/8/10px.
- [ ] Motion uses 1–2 named easing tokens. No bare `transition: all .3s`.
- [ ] Text is near-black; large light surfaces are off-white. Pure #000/#fff only where intentional.
- [ ] Typographic tension present: display negative-tracked, labels uppercase + wide-tracked.
- [ ] Imagery is real/bespoke/art-directed (or an explicit art-direction plan). No stock-smiling-people, no raw AI output, no decorative gradients.
- [ ] Copy is specific (numbers/proof/voice), not filler. Biggest headline proofread.
- [ ] ≤ 2 typefaces total (display + body).
- [ ] Tokens exist (color/type/spacing/radius/motion), semantically named, fluid where sensible.
- [ ] Clear hierarchy + readable text measure (700–850px). Not everything centered/same-size.
- [ ] No stale fingerprints: current © year, no IE-era font fallbacks, no jQuery slider as hero.
- [ ] Accent never used as low-contrast small body text.

When you deliver, name in 2–4 bullets which of these traps you actively avoided and why your choices are intentional. That sentence is the proof you applied the skill rather than defaulting.
