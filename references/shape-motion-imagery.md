# Shape, motion & imagery intelligence

## SHAPE — commit to one language

- **Editorial / agency / event → hard 0-radius** as a deliberate stance. Sharp reads architectural and confident.
- **SaaS / consumer → consistently soft** — a fluid radius `clamp(6→12px)` workhorse + capsule pills (980px / 9999px) for buttons.
- **Tokenize ONE radius identity.** Scattered 0/3/4/6/8/10px is flagged cruft.
- **Borders = thin 1px hairlines**, often tonal (an alpha of the ink, or a soft grey like `#e8e8ed`), not heavy strokes.

## SHADOWS — default to flat

- Create depth **without `box-shadow`** — alternating tiles, full-bleed imagery, color blocks.
- Where used, **whisper-soft only:** e.g. `#2a20200f` (~6% warm black), `0 0 16px rgba(0,0,0,.16)`, or a single `0 0 10px #00000033`. Brand-colored focus rings work well (e.g. mint `0 0 0 5px #E1FFCD`).
- **Never** the harsh default card stack (`0 2px 4px rgba(0,0,0,.5)`).

## MOTION — govern with 1–2 easing tokens, reuse everywhere

Crafted systems define one or two curves and reuse them across every transition:

- One workhorse **300ms ease-in-out** for nearly everything (calm, corporate).
- Two tokens — e.g. **160ms / 320ms** (product clarity).
- An expressive **expo-out** `cubic-bezier(0.165, 0.84, 0.44, 1)` or **0.7s ease-out-expo** for hero reveals.
- An **iOS spring** `cubic-bezier(0.32, 0.72, 0, 1)` + `active:scale-[0.97]` for tactile product UI.

**Match appetite to archetype:** calm uniform → corporate; spring press → product/app; GSAP scroll line-reveals / SPA page transitions → editorial; heavy expo + marquees → social.

**Signature micro-interactions earn memorability:** a smooth button color-invert on hover, a pill that inverts, a highlighter-marker headline. Pick ONE signature move. Always respect `prefers-reduced-motion`. Don't: `transition: all .3s` with no curve (lifeless); parallax/scroll-jacking gimmicks.

## IMAGERY — bespoke and on-system

- Real work / venue / install / product photography, **color-graded to the palette** (warm amber tones, dark scrims `#2c2c2c` for legible white text, navy `rgba(0,40,100)` overlays).
- **Grayscale/monochrome SVG logo walls** for credibility.
- `mix-blend-mode: luminosity` to fold photography into a B/W system.
- **Optimized WebP via CDN with full `srcset`** (up to 3840w for retina/large screens).

**Don't:** generic stock smiling-people, decorative Unsplash gradients, or un-art-directed AI output. If no real imagery exists, either generate it under the discipline in `imagery-generation.md` or propose an art-direction plan — never fake it.

## Quick recipe

1. One radius token (`0` or a `clamp(6→12px)` scale + pill for buttons).
2. Hairline tonal borders (alpha of ink). Default flat; if elevation needed, one soft 8–16px / 6–16% shadow.
3. Two easing tokens + one signature micro-interaction. `prefers-reduced-motion` guard.
4. Real or art-directed, palette-graded imagery; grayscale logo wall; WebP + srcset.
