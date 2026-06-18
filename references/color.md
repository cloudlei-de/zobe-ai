# Color intelligence

zobe.ai's first color law and the craft moves that make color read as *decided*.

## The law: monochrome base + ONE accent

A near-monochrome base plus exactly one signature accent is the backbone of every confident design. The accent earns its keep on **CTAs, focus rings, links, and one signature device** — never scattered as decoration. In strong systems the accent appears 70–150× in the source while no competing hue shows up at all.

Proven single-accent directions (pick the temperature that fits the brand):

| Base | Accent | Reads as |
|---|---|---|
| near-black / white | one decisive blue `#0071e3` (brighten to `#2997ff` on dark) | precise, product-grade |
| white | one brand red `#dc0000` used relentlessly, never decoratively | engineered, authoritative |
| near-black / white | one acid-lime / chartreuse `#E9F6C0` / `#f2f69b` | bold, editorial, high-energy |
| warm paper `#fbf9f2` / navy | one sun-yellow `#f7d070` | institutional but warm |
| white | one green `#65B330` | trustworthy, natural |
| off-white | one warm vermillion `#ff3d00` | confident, urban |

**Dual-axis** is allowed only as a deliberate system where one hue clearly dominates: e.g. a green identity family (`#6EDC14` / mint `#E1FFCD` bg / dark `#2C5808` text) with a violet (`#5F28FF`) that lives **only** in accents and shadows.

## Soften the extremes

Pure `#000`-on-`#fff` reads harsh and dated. Instead:

- **Text** → near-black: `#020202`, `#1d1d1f`, `#101010`, or a soft charcoal `#3C3D3F`.
- **Large light surfaces** → warm/cool off-white: `#f5f5f7` (cool) or `#fbf9f2` (warm "paper").
- Reserve pure `#000`/`#fff` for high-contrast moments (logo, full-bleed dark hero).

## Build each brand hue as a full ramp

Ship the accent as base + light-30/60 + dark-30/60 so **backgrounds, text, and borders all stay on-brand** — don't pair one accent hex with off-brand grays for everything else. On dark surfaces, **brighten the accent**. Use **alpha tints of the brand colors** for borders/scrims/hovers (e.g. `#996d5c80 / 4d / 33`, or a focus inset `0 0 0 1px #30148026`) rather than generic gray overlays.

## Accessibility

Engineer a **darker accent variant for WCAG button/text contrast** (e.g. a dedicated `#2F6600` next to a brighter display green). Always provide an `--accent-strong` token for accent text/buttons on light — `scripts/gen_tokens.py` derives and contrast-checks it for you.

## Don't

- Ship the default Gutenberg/WordPress rainbow (`#cf2e2e #ff6900 #fcb900 #00d084 #0693e3 #9b51e0`) — it leaks as cruft and screams "nobody curated the tokens."
- Let warm promo badges (`#c45500`/`#FF474D`) fight the brand accent — it cheapens the "premium" claim.
- Use accent-colored text below comfortable contrast at small sizes.
- Treat color as decoration. Color is identity + function (action, state, hierarchy) — nothing else.

## Quick recipe

1. Pick mode (light off-white / dark near-black / alternating).
2. Pick ONE accent; derive `--accent`, `--accent-strong` (WCAG), `--accent-tint` (bg), `--accent-on-dark`.
3. Ink = near-black; muted ink = ~55–65% toward bg; border = tonal hairline (alpha of ink).
4. Semantic status colors (product UI) at low opacity (10–20%) so they don't break the palette.
