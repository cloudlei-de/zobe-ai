# zobe.ai — anti-slop design engine (Copilot instructions)

When a task involves visual design — a website, landing page, hero, UI, component, brand look,
color palette, or design system — or fixing an existing "AI-generated-looking" design, apply the
zobe.ai laws. Goal: design that looks **decided by a human with taste**, free of generic LLM
"slop" tells. Brand-agnostic — derive the look from the brief, never impose a default.

**The 10 laws:** (1) ONE accent on a near-monochrome base — no rainbow. (2) A characterful display
face; Inter/system-ui only as a quiet body workhorse. (3) Two-pole type tension — display huge +
negative tracking, labels tiny + UPPERCASE + wide tracking. (4) Flat depth; separate by background
and full-bleed imagery, not card-shadow soup. (5) One shape language (sharp 0-radius or one
tokenized soft scale). (6) 1–2 easing tokens, never a bare all-properties transition. (7) Near-
black ink, off-white surfaces; reserve pure #000/#fff. (8) Tokenize — fluid `clamp()` scales +
semantic color names. (9) Earn premium with specificity, not stock or filler. (10) Narrow reading
measure inside wide bands; steep hierarchy; one idea per section.

**Procedure:** frame the job → short intake → lock a direction → define design tokens first →
build on the tokens (never hardcode raw values) → self-audit against the red-flag checklist before
delivering.

Full guidance: `AGENTS.md` and the `references/` folder. Runnable helpers (token generator, slop
linter, image briefing/generation) live in `scripts/` — run `scripts/slop_audit.py` on the result
before declaring it done.
