# Imagery & generation — art direction that turns "AI image slop" into owned assets

Generated imagery is allowed — but it is held to the same bar as every other decision. Default text-to-image output (over-glossy 3D blobs, fake bokeh, purple/teal gradients, uncanny people, garbled text) is the *visual* form of AI slop. This file is the discipline that makes generated imagery read as **bespoke, on-system, and intentional**.

Rule of thumb: **the model generates pixels; zobe.ai art-directs them.** A locked palette, a consistent treatment, and a tight brief are what separate "looks AI-made" from "looks commissioned."

---

## When to generate vs. source vs. draw

| Need | Best source | Why |
|---|---|---|
| Logo / wordmark / favicon | **Design it** (type + vector) | Never generate a logo — gen produces garbled, untrademark­able marks. |
| Icons, diagrams, simple motifs | **Vector / SVG** (hand or code) | Crisp, tiny, recolorable to tokens. Gen rasterizes + drifts off-style. |
| Hero / background / texture | **Generate** (abstract/textural) or bespoke photo | Great gen use-case: art-directed atmosphere, no text, no faces. |
| Product shots | **Real photo** if the product exists; else generate from a reference | A real product needs a real (or reference-conditioned) image — pure gen invents the wrong product. |
| People / lifestyle / context | Generate **with care**, or license real | Highest slop/uncanny risk; demand tight specs, inspect hands/faces. |
| Charts / real data | **Never gen** — render from data | Generated "charts" are fiction. |

If no generator is wired and no assets exist: ship the on-palette **SVG/placeholder** (see the host project's bespoke vector motif) and hand the user the briefs below.

---

## The AI-image slop tells → the fix

| Slop tell | Fix |
|---|---|
| Over-glossy, plasticky **3D blobs / "AI render" sheen** | Specify a real medium: "matte studio photograph", "risograph print", "technical line drawing", "long-exposure photo". Name lens/film if photographic. |
| **Fake shallow depth-of-field** bokeh on everything | Only ask for DOF when it's motivated; for product/editorial prefer "deep focus, everything sharp". |
| **Garbled text** baked into the image | Never ask for text in the image. Put ALL copy in real HTML over the image. Negative-prompt "text, letters, watermark, signature". |
| **Uncanny hands/faces**, 6 fingers | Prefer crops that avoid hands/faces; if people are needed, generate, then *inspect and regenerate*. Consider hands out of frame, back-views, silhouettes. |
| **Generic purple→teal gradient** background | Lock the background to a brand token (`--bg`/`--ink`) or a flat/textured on-palette field. Forbid rainbow/neon gradients in the negative prompt. |
| **Inconsistent style** across a set | Reuse ONE style sentence + ONE seed/style-reference across the whole batch. Generate as a family, not one-offs. |
| Wrong **aspect / low-res / visible upscaling** | Generate at target ratio and 2× the rendered size; export crisp WebP. |
| Reads like **stock** (smiling people, handshake, lightbulb idea) | Be specific and unexpected; tie subject to the real product. Stock clichés are slop even when "real". |

---

## The prompt formula

```
[subject + what it's doing] , [composition & crop] , [medium/style] ,
[lighting] , [palette: name the brand colors + hex] , [mood] ,
[lens/film if photographic] , [aspect ratio] .
Negative: text, watermark, signature, logo, extra fingers, deformed hands,
distorted faces, lowres, jpeg artifacts, oversaturated, neon, rainbow gradient,
cluttered, busy, stock-photo cliché, plastic 3D render.
```

- **Lock the palette in words AND hex** (e.g. "warm off-white #faf8f4 ground, near-black #1a1714, a single vermillion #ff3d00 accent — no other colors").
- **Leave negative space** for the headline that will sit on top ("composition with empty upper-left third for text").
- **Match the medium to the archetype** (table below).
- **Generate at 2× target**, target aspect ratio, then post-grade.

---

## Per-archetype image style (matches `archetypes.md`)

- **editorial-studio** — bold, art-directed; full-bleed, generous negative space; one accent prop; deep focus; "shot on medium format, natural directional light, muted, grain". Black-and-white or monochrome-graded photography is a power move.
- **corporate-institutional** — documentary realism; people *doing the work*, real environments; even, honest light; restrained; "candid documentary photograph, natural light, neutral". No stock smiling.
- **product-saas** — clean product/UI renders on seamless or soft-gradient-of-ONE-brand-hue; crisp, bright, even light; lots of air; subtle on-palette ambient shapes (not blobs).
- **luxury-event / hospitality** — atmospheric, warm-graded, low-key lighting, shallow only where motivated; texture (linen, stone, dusk); "editorial, cinematic, warm tungsten, restrained".
- **ecommerce / D2C** — consistent packshots on a seamless ground that matches `--bg`; soft contact shadow; plus aspirational lifestyle in a real setting; color-accurate.
- **social-first / creator** — high-energy, high-contrast, bold crops, motion; on near-black with one electric accent; punchy.

---

## Product imagery — the consistency kit

Products live or die by *set consistency*. For a catalog/feature set, fix and reuse:

1. **One background** = the site's `--bg` (or seamless white→`--bg`). Same for every SKU.
2. **One camera angle + framing** (e.g. 3/4 front, centered, same margin).
3. **One light setup + shadow** (e.g. soft top-left key, faint contact shadow).
4. **One treatment** (same grade, same crop ratio).
5. If the product is real → photograph it, or generate from a **reference image** (image-to-image / edit), then **remove background** and place on the brand ground. If MCP editing tools are available (background removal, crop, color match), use them to normalize the set.

Never let promo/badge colors fight the brand accent (a flagged D2C slop tell).

---

## Integration & post (this is half the craft)

- **Grade to the palette.** For a B/W or monochrome system, convert to grayscale or duotone (or `mix-blend-mode: luminosity`) so photos fold into the system. For color, nudge white balance toward the brand temperature.
- **Consistent scrim for legible text** over imagery: a tonal overlay from `--ink` (e.g. `rgba(26,23,20,.45)`) or a gradient scrim — same recipe everywhere.
- **Export discipline:** WebP/AVIF, `srcset` + `sizes`, 2× for retina, explicit `width`/`height` (or aspect-ratio box) to prevent layout shift, `loading="lazy"` below the fold, meaningful `alt`.
- **Social:** an `og:image` at **1200×630**, on-brand, with the wordmark — generated/composed to match.
- **Don't** drop a raw generation in at full saturation next to a restrained palette — it will look pasted-in. Always treat the set as one.

---

## Tooling — generating with GPT Image 2

zobe.ai generates imagery with **OpenAI GPT Image 2** via `scripts/gpt_image.py`.

> **⚠️ Requires an OpenAI API key.** GPT Image 2 is a paid OpenAI model. The user needs an
> `OPENAI_API_KEY` (https://platform.openai.com/api-keys) exported in the environment:
> `export OPENAI_API_KEY="sk-..."`. **Tell the user this up front, before attempting generation** —
> don't silently fail. If the key is missing, the script exits with a clear message and you fall
> back to briefs + on-palette placeholders.

The two scripts compose:

1. **Brief** — `scripts/image_brief.py` builds the art-directed positive + negative prompt for the asset (tuned to the locked archetype/palette).
2. **Generate** — `scripts/gpt_image.py` calls GPT Image 2 with that prompt:
   ```bash
   python3 scripts/gpt_image.py --prompt "<positive prompt>" --out public/hero.png \
     --size 1536x1024 --quality high
   ```
   - Sizes: `1024x1024` · `1536x1024` (landscape) · `1024x1536` (portrait) · `auto`.
   - **Product / image→image:** `--edit reference.png --prompt "on a seamless #faf8f4 ground"` conditions on a real reference so the *actual* product is rendered, not a hallucinated one.
   - `--background transparent` (png/webp) for product cut-outs.
3. **Post-process** — grade to the palette, add the consistent scrim, export WebP + `srcset`, set dimensions, write `alt` (see the checklist above). Use any connected MCP image-editing tool (background removal, crop, recolor) to normalize a product set.

Always state that GPT Image 2 was used (and that it consumed API credits), and run every generated image through the **integration & post** checklist before declaring it done. If no key is available, emit the briefs, wire on-palette SVG/placeholders, and tell the user exactly what to generate and where each asset goes.
