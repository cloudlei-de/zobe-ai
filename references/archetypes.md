# Archetypes — intake answers → concrete recipe

Six design archetypes zobe.ai works in. Map the intake's archetype/personality answer to one, then follow its recipe. Each recipe is a starting system, not a straitjacket — adjust to the brand's accent and voice.

---

## 1. editorial-studio (agency / creative portfolio)
**When:** design studios, film/production agencies, photographers, architects — credibility *is* visual taste; the work is the hero.

- **Palette:** black/white (or near-black `#020202` / off-white) + ONE accent (chartreuse, electric yellow, acid-lime).
- **Type:** characterful geometric display face at 80–160px with hard negative tracking (-2 to -7px) vs tiny wide uppercase eyebrows.
- **Spacing:** generous, low-density, big section padding, work-led grids.
- **Shape:** sharp, 0-radius, flat, near-shadowless.
- **Motion:** scroll line-reveals with Expo easing (`cubic-bezier(0.165,0.84,0.44,1)`), one accent-colored highlight sweep.
- **Imagery:** real portfolio work, full-bleed video reels, grayscale logo walls.

## 2. corporate-institutional (authority / standards / B2B trust)
**When:** universities, associations, standards/safety bodies, industrial OEMs, insurers, regulatory-adjacent tech — trust > flash.

- **Palette:** white/warm-paper + deep navy or charcoal ink + ONE accent (cyan, brand red, sun-yellow).
- **Type:** licensed humanist/geometric sans — headings often LIGHT weight (300) for elegance, sentence case, surgical letter-spacing on uppercase labels (~1.7px).
- **Spacing:** ~1150px container, 8px rhythm, comfortable-corporate density, alternating bands.
- **Shape:** squared CTAs (0-radius) or tight 3px, 1px hairline borders, near-flat.
- **Motion:** one signature 300ms ease-in-out everywhere.
- **Imagery:** documentary real photography + accreditation badges + concrete proof numbers. Optional signature device (e.g. a marker-highlight headline).

## 3. product-saas (modern B2B/B2C software)
**When:** SaaS, apps, platforms, fintech — modern, trustworthy-but-human, conversion clarity.

- **Palette:** white/off-white + a brand hue shipped as a full ramp (base / light-30 / light-60 / dark-30 / dark-60) — e.g. green `#6EDC14` + mint `#E1FFCD` bg + dark `#2C5808` text; one functional accent for actions (e.g. blue `#0071e3`).
- **Type:** custom geometric grotesque on a fluid clamp scale; semibold headings lh ~1.05–1.2; fluid body `clamp(14→16px)`.
- **Spacing:** narrow reading column (708–734px) inside wide section bands (1440px); fluid clamp spacing.
- **Shape:** soft fluid radius `clamp(6→12px)` + pills (980px/9999px); thin 1px light borders; whisper-soft shadows (~6% warm black).
- **Motion:** 1–2 easing tokens (160/320ms ease-in-out); spring press feedback; Lottie/number-counter ambient motion.
- **Imagery:** real product UI, customer logos, trust badges.

## 4. luxury-event / hospitality (understated exclusivity)
**When:** boutique venues, galas, hospitality, high-end events, premium lifestyle — exclusivity via taste and detail, not loudness.

- **Palette:** warm sand/cream (`#f5efe0`) + muted terracotta/mocha (`#996d5c`) + near-black; OR clean white + near-black + one bold accent (e.g. hot-pink `#FF366F`).
- **Type:** serif display + hairline sans (weight 100), OR a custom condensed all-caps. Wide uppercase tracking (.1–.3em) on eyebrows/buttons.
- **Spacing:** very low density, one idea per section, lots of negative space.
- **Shape:** hairline-border pills that invert on hover; 0-radius editorial blocks; near-shadowless.
- **Motion:** quiet fade/slide reveals, hover inversions, no parallax.
- **Imagery:** bespoke warm-graded atmospheric photography.
- **Copy:** specificity flexes (exact materials, named numbers). Avoid gold-on-black cliché — glamour through editorial calm.

## 5. ecommerce / D2C (premium-mass retail)
**When:** D2C brands, fashion/lifestyle retail, premium-mass catalogs — product + trust drive sales, brand wants to read above generic storefront templates.

- **Palette:** white + hard near-black text + ONE brand accent (teal `#006969`, green `#65B330`) for CTAs/footer/stars; keep promo badges from fighting the brand color.
- **Type:** light-weight geometric heading (weight 400) + clean sans body; uppercase +2px tracking reserved for select labels.
- **Spacing:** full-bleed photographic bands edge-to-edge; moderate product-grid density.
- **Shape:** consistent soft radius (10px) OR light 5px; flat/shadowless; thin borders.
- **Motion:** subtle hover-lift + reveal, restrained.
- **Imagery:** clean studio packshots + aspirational lifestyle.
- **Copy:** heritage + hard numbers and one genuinely punchy brand line.

## 6. social-first / creator-bold (youth-culture energy)
**When:** creator agencies, music/entertainment, youth brands — energy, attitude, motion are the product.

- **Palette:** near-black canvas + white + ONE loud accent (acid-lime).
- **Type:** single bold geometric grotesque pushed to ~160px UPPERCASE display with negative tracking; weights restrained to ~600 max; tiny wide uppercase labels.
- **Spacing:** centered editorial column (~1160px) over full-bleed black, airy.
- **Shape:** hard 0-radius, flat brutalist-leaning.
- **Motion:** heavy premium `0.7s ease-out-expo` (scroll-triggered), marquee tickers, reveals that even tween letter-spacing.
- **Imagery:** 16:9 work thumbnails, blue-chip grayscale logo wall on black.
- **Copy:** punchy capitalized attitude. **Watch contrast** of accent-on-black for small body text.

---

## Optional: the zobe.ai starter preset
A ready-to-use, opinionated system for when the user wants a strong starting point fast — a *preset*, not a default.

- **Accent:** one warm electric yellow `#F2F29D` (or any single accent the brand prefers). **Base:** stark black/white, near-black `#020202` for dark sections.
- **Type:** a characterful geometric grotesque (display) + a quiet sans (body). Tight negative tracking (-1 to -6px) on display; uppercase micro-labels +0.1em.
- **Two flavors:**
  - *Editorial:* sharp 0-radius, flat, bottom-border-only forms, `cubic-bezier(0.87,0,0.13,1)`, a full-bleed page-transition overlay.
  - *Product:* dark-only, surfaces `#151515`/`#1F1F1F`, soft `rounded-[7.5px]`/`rounded-xl`, frosted glass `backdrop-blur-md`, iOS-spring `cubic-bezier(0.32,0.72,0,1)` + `active:scale-[0.97]`, status colors at 10–20% opacity.
