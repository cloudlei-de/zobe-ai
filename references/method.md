# Method — the zobe.ai design process

The full procedure behind `SKILL.md` Step 1–6. Read this when running an intake or diagnosing an existing design.

---

## A. The intake (Step 2 in detail)

Goal: extract the few decisions that determine everything downstream, in one short round, using `AskUserQuestion`. Most slop comes from *assuming* these instead of asking.

Ask **4–6** questions. Skip any the brief already answers. Translate the question + option text into the user's language. Recommend the option that best fits the brief and put "(Empfohlen)/(Recommended)" first.

### The question bank

| # | Question | Why it matters | Good option set |
|---|---|---|---|
| 1 | **Brand archetype & personality** (3–5 words) | Archetype drives sharp-vs-soft, light-vs-dark, density, motion. Naming it first prevents a generic blend. | Editorial-studio · Corporate-institutional · Product-SaaS · Luxury/hospitality · Social-first/creator · Ecommerce/D2C |
| 2 | **Mode + the one accent** | The non-negotiable law is monochrome base + ONE accent. Lock it up front to kill the rainbow-palette tell. | Light (warm off-white) · Dark (near-black) · Alternating tiles · Accent cool (blue/cyan) · Accent warm (red/terracotta/yellow) · Accent electric (acid-lime) |
| 3 | **Shape language** | Must be committed, not accidental. Implies the shadow strategy. | Sharp / 0-radius / flat · Soft / tokenized 6–12px + pills · Hybrid (sharp blocks, pill buttons) |
| 4 | **Type mood** | A characterful face is the strongest anti-slop signal; the flavor sets the tonal register. | Geometric grotesque · Humanist corporate sans · Serif-display + hairline sans · Condensed all-caps · "I'll supply a brand font" |
| 5 | **Loudness / density** | The difference between a 160px shout and a quiet whisper. Calibrates padding, measure, headline size. | Poster-loud · Editorial-confident · Quiet-luxury · Corporate-comfortable |
| 6 | **Motion appetite** | Picks the easing strategy and prevents `transition: all .3s`. | Minimal · Restrained micro-interactions · Expressive scroll choreography · Tactile/spring |
| 7 | **Proof & imagery available** | Premium = specificity. Prevents stock-photo/vague-filler slop; enables logo walls and proof bands. | Bespoke photography · Client/partner logos · Hard metrics/years/ratings · Testimonials/awards · Nothing yet |
| 8 | **Language, audience & voice** | Copy must read native, not machine-translated; honor regional Sie/Du and locale needs. | German Sie · German Du · Bilingual DE+EN · English · Multi-locale |

**Rules for the intake:**
- One round, max 4 questions per `AskUserQuestion` call (the tool's limit) — prioritize 1–4, then a second round for 5–6 only if the brief is thin.
- If the user says *"skip the questions / just go"*, infer the answers, **state your assumptions explicitly** in 4–6 bullets, and proceed.
- If a project context exists (existing repo, brand guide, CLAUDE.md), read it first and pre-fill answers — only ask what's genuinely open.

---

## B. Lock the direction (Step 3)

Translate answers → one archetype from `references/archetypes.md`, then state the direction back in 3–5 lines. Template:

```
Direction: <archetype>
Palette:   <base off-white/off-black> + <accent name #hex> (+ optional secondary, dominant rule)
Type:      <display face> for headlines / <body face> for text
Shape:     <sharp 0-radius | soft Npx + pills>, <flat | one soft shadow>
Motion:    <token A: dur+curve>, <token B>  — appetite: <…>
Density:   <poster | editorial | quiet | corporate>
```

Get a one-word confirmation or adjust. Decide — don't present five options and ask the user to design it themselves.

---

## C. Tokens before build (Step 4)

Always emit a token set first. Minimum viable token system:

- **Color** — semantic names: `--bg`, `--surface`, `--ink` (near-black), `--ink-muted`, `--accent`, `--accent-strong` (WCAG-safe variant for button contrast), `--border` (tonal hairline). Build the accent as a small ramp (base / +light / +dark) so bg, text and borders stay on-brand.
- **Type** — a fluid scale via `clamp()`: micro → body → lead → h3 → h2 → h1 → display. Define display + body family, and the tracking rule (negative on display, wide-positive on labels).
- **Spacing** — a fluid scale (e.g. `clamp(12px, …, 16px)` up to section-scale) on an 8px base.
- **Radius** — ONE scale (or `0` for sharp). Tokenize it; never inline arbitrary radii.
- **Motion** — 1–2 easing tokens + 2 durations.

Use `assets/tokens.template.css` as the scaffold (Tailwind 4 `@theme` + plain CSS-var fallback). Build all code against these tokens.

---

## D. De-slop mode (the headline use case)

When the user hands you an existing design (code / screenshot / URL) that "looks AI-generated":

1. **Diagnose.** Walk the red-flag checklist in `references/anti-slop.md` against the artifact. List the specific tells you find, quoting the offending values (e.g. "`font-family: Inter` as the brand face", "three accent colors", "`shadow-lg` on every card", "`transition: all .3s`").
2. **Triage.** Rank fixes by visual impact: (1) type identity, (2) color discipline, (3) depth/shape, (4) hierarchy/spacing, (5) motion, (6) copy/imagery. Type + color + flatness usually do 80% of the lift.
3. **Confirm constraints.** Ask whether brand colors/fonts are fixed or open (one question).
4. **Rebuild.** Re-derive tokens, then refactor the code to use them. Keep the user's content/structure unless it's the problem.
5. **Show the diff.** Deliver a short *before → after* list: each slop tell removed and the craft move that replaced it.

The promise of de-slop mode: the *content* survives, the *taste* is upgraded.

---

## E. Output contract (Step 6)

Every delivery includes:
1. **Tokens** — the design-token block (CSS vars / Tailwind `@theme`).
2. **Code** — production HTML or React + Tailwind, using only the tokens.
3. **Rationale** — 2–4 bullets tying choices to the brief/archetype.
4. **Anti-slop pass** — 2–4 bullets naming the traps avoided (Step 5).
5. *(de-slop only)* the before → after diff.
6. *(optional)* next steps / what's still placeholder.

Keep prose tight. The work should speak; the rationale is a footnote, not an essay.
