# Spacing & layout intelligence

Contain the reading measure and let it breathe.

## Narrow text inside wide bands

Keep the **text measure** narrower than the **section band**. Content max-widths cluster around 1068–1280px; reading columns around 700–850px. The pattern: a **narrow text column for readability inside wide full-bleed media/section bands.** Long lines are a slop tell — keep body measure ≈ 60–80 characters (700–850px).

## Rhythm: 8px base or fluid clamp

- An **8px-based spacing scale** (8/12/16/24/32/40/48px), OR
- A **fluid `clamp()` scale** (e.g. `clamp(12px, …, 16px)` up to `clamp(40px, …, 120px)`).

So vertical rhythm breathes on large screens and compresses gracefully on mobile. **Never hardcode pixel section heights** — fixed `193/650px` heights and `margin-top:-145px` hacks are brittle.

## Density is archetype-driven

- **Editorial / luxury → LOW density.** One idea per section; work + whitespace carry the page.
- **Corporate → comfortable, info-rich but breathable** (alternating bands).
- **Ecommerce → tolerates tighter product grids** (but keep heroes airy).

## How to create depth & separation

- **Stack self-contained full-bleed tiles** (alternating light/dark) with consistent 44–69px tile padding — depth from rhythm, not cramming.
- **Background-color zones** — alternate white / a pale brand tint / near-white to separate sections.
- **Edge-to-edge photographic bands** (set inter-section gap to 0 for an immersive run).
- Use a **real grid** (12-col with 15px gutters; or explicit `grid-template-columns: repeat(3,1fr)` collapsing to `1fr`).
- **Generous heading margins** (20–30px top).

## Don't

- Everything center-aligned, same size, crammed — no hierarchy.
- Ignore the reading measure (lines too long).
- A generic stacked-band layout with zero asymmetry or editorial tension when the archetype wants confidence.
- Forget non-breaking spaces to prevent headline orphans.
- Scatter spacing values — untokenized spacing is a maintainability/slop smell.

## Quick recipe

1. `--measure: min(92vw, 720px)` for text; `--band: min(92vw, 1280px)` for sections; full-bleed for media.
2. Spacing scale on 8px or `clamp()`; section padding `clamp(48px, 8vw, 120px)`.
3. Pick density from archetype; one idea per section for editorial/luxury.
4. Separate sections by background zones / full-bleed imagery, not floating cards.
