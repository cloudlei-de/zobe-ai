#!/usr/bin/env python3
"""zobe.ai image brief — design direction + asset type → an art-directed, anti-slop prompt.

Provider-agnostic (works for /banana, Firefly, DALL·E, Midjourney, etc.). stdlib only.

Usage:
    python3 image_brief.py --type hero --archetype editorial-studio \\
        --subject "a quiet city intersection seen from above" \\
        --bg "#faf8f4" --ink "#1a1714" --accent "#ff3d00" --mode light

Emits: a positive prompt, a shared negative prompt, the recommended aspect/size,
and post-processing notes. Pair with references/imagery-generation.md.
"""
import argparse

ARCH = {
    "editorial-studio": ("shot on medium-format film, natural directional light, matte, fine grain",
                         "confident, art-directed, lots of negative space"),
    "corporate-institutional": ("candid documentary photograph, even natural light, neutral, realistic",
                                "trustworthy, precise, people doing real work"),
    "product-saas": ("clean studio render, bright even light, crisp, deep focus",
                     "modern, friendly, uncluttered, airy"),
    "luxury-event": ("editorial cinematic photograph, low-key warm tungsten light, textured",
                     "understated, atmospheric, exclusive"),
    "ecommerce": ("color-accurate studio packshot, soft key light, faint contact shadow, seamless ground",
                  "premium-mass, clean, aspirational"),
    "social-first": ("high-contrast editorial photograph, bold crop, sense of motion",
                     "high-energy, punchy, youthful"),
}

TYPE = {
    "hero":       ("16:9", "wide full-bleed composition, empty upper-left third reserved for headline text"),
    "background": ("16:9", "subtle textural field, very low contrast, nothing competing with foreground text"),
    "product":    ("4:5",  "single product centered, 3/4 front angle, consistent margin, soft contact shadow"),
    "lifestyle":  ("3:2",  "product in a real human context, environmental, candid"),
    "feature":    ("1:1",  "single clear subject, generous breathing room, centered"),
    "texture":    ("1:1",  "seamless tileable macro texture, flat even light, abstract"),
    "og":         ("1200x630", "social card composition, strong focal point left, room for wordmark"),
}

NEGATIVE = ("text, words, letters, captions, watermark, signature, logo, UI, "
            "extra fingers, deformed hands, distorted faces, lowres, blurry, jpeg artifacts, "
            "oversaturated, neon, rainbow gradient, purple-teal gradient, plastic 3d render, "
            "glossy cgi sheen, cluttered, busy, stock-photo cliché, fake bokeh")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", required=True, choices=list(TYPE))
    ap.add_argument("--archetype", default="product-saas", choices=list(ARCH))
    ap.add_argument("--subject", default="")
    ap.add_argument("--bg", default="#faf8f4")
    ap.add_argument("--ink", default="#1a1714")
    ap.add_argument("--accent", default="#ff3d00")
    ap.add_argument("--mode", choices=["light", "dark"], default="light")
    ap.add_argument("--ratio", default="")
    a = ap.parse_args()

    medium, mood = ARCH[a.archetype]
    ratio, comp = TYPE[a.type]
    ratio = a.ratio or ratio
    ground = a.bg if a.mode == "light" else a.ink

    subject = a.subject or {
        "hero": "an abstract on-brand scene that evokes the product",
        "background": "an abstract on-brand textural field",
        "product": "the product",
        "lifestyle": "the product in use in a real setting",
        "feature": "a single clear object representing the feature",
        "texture": "an abstract material surface",
        "og": "an abstract on-brand scene representing the product",
    }[a.type]

    palette = (f"strictly limited palette: {ground} ground, {a.ink} for darks, "
               f"a single {a.accent} accent used sparingly — no other colors")

    positive = (f"{subject}, {comp}, {medium}, {palette}, {mood}, "
                f"aspect ratio {ratio}, high resolution, intentional and editorial")

    print("── POSITIVE PROMPT " + "─" * 42)
    print(positive)
    print("\n── NEGATIVE PROMPT " + "─" * 42)
    print(NEGATIVE)
    print("\n── SPEC " + "─" * 53)
    print(f"aspect/size : {ratio}  (generate at ~2× the rendered size)")
    print(f"archetype   : {a.archetype}")
    print(f"palette     : bg {a.bg} · ink {a.ink} · accent {a.accent} · {a.mode}")
    print("\n── POST (see imagery-generation.md) " + "─" * 25)
    print("• grade to the palette (grayscale/duotone for mono systems; nudge WB to brand temp)")
    print(f"• if text sits on top, add a consistent scrim from {a.ink} (~45% alpha)")
    print("• export WebP/AVIF + srcset + sizes; set width/height; lazy-load below the fold; write alt")
    if a.type == "product":
        print("• remove background, place on the brand ground, reuse ONE angle/light across the whole set")
    if a.type == "og":
        print("• compose at exactly 1200×630 and place the wordmark; this is the social share card")
    print("\n── GENERATE (GPT Image 2 — needs OPENAI_API_KEY) " + "─" * 12)
    sz = {"hero": "1536x1024", "background": "1536x1024", "lifestyle": "1536x1024",
          "og": "1536x1024", "product": "1024x1536", "feature": "1024x1024",
          "texture": "1024x1024"}[a.type]
    print(f'python3 scripts/gpt_image.py --out asset.png --size {sz} --quality high \\\n'
          f'  --prompt "{positive}"')
    if a.type == "og":
        print("  (then crop the 1536×1024 down to exactly 1200×630 for the social card)")
    print("• no key? → hand this brief to the user, or wire an on-palette SVG/placeholder meanwhile")


if __name__ == "__main__":
    main()
