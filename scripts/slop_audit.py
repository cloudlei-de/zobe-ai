#!/usr/bin/env python3
"""zobe.ai slop audit — scan CSS/HTML/JSX/TSX for AI-slop design tells.

Usage:
    python3 slop_audit.py <file-or-dir> [<file-or-dir> ...] [--json] [--quiet]

Exit code 0 = clean (score >= 80), 1 = slop detected. stdlib only, no deps.
Pairs with references/anti-slop.md — each finding maps to a rule there.
"""
import argparse
import json
import re
import sys
from pathlib import Path

EXTS = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".jsx", ".tsx",
        ".vue", ".svelte", ".astro", ".js", ".ts"}

GUTENBERG = ["#cf2e2e", "#ff6900", "#fcb900", "#00d084", "#0693e3", "#9b51e0",
             "#c65bcf", "#abb8c3", "#eb144c"]
DEFAULT_FONTS = ["inter", "roboto", "open sans", "open-sans", "system-ui",
                 "helvetica neue", "arial", "lato", "montserrat", "poppins", "nunito"]
GENERIC_FALLBACKS = {"sans-serif", "serif", "monospace", "system-ui", "ui-sans-serif",
                     "ui-serif", "ui-monospace", "-apple-system", "blinkmacsystemfont",
                     "segoe ui", "helvetica neue", "arial", "inherit", "initial", "cursive"}
FILLER = [r"high[- ]quality solutions", r"we deliver excellence", r"cutting[- ]edge solutions",
          r"innovative solutions", r"lorem ipsum", r"best[- ]in[- ]class", r"world[- ]class solutions",
          r"take it to the next level", r"empower(?:ing)? your business"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]")


class Finding:
    __slots__ = ("rule", "severity", "where", "detail")

    def __init__(self, rule, severity, where, detail):
        self.rule, self.severity, self.where, self.detail = rule, severity, where, detail


def lineno(text, idx):
    return text.count("\n", 0, idx) + 1


def scan_text(path, text):
    f = []
    low = text.lower()

    # Rule 2: leftover Gutenberg rainbow palette
    hits = [c for c in GUTENBERG if c in low]
    if len(hits) >= 3:
        f.append(Finding("rainbow-palette", "high", str(path),
                         f"default Gutenberg/WP palette present ({', '.join(hits[:4])}…) — strip it, commit to one accent"))

    # Rule 1 / 11: default font as identity + font sprawl
    fams = re.findall(r"font-family\s*:\s*([^;{}]+)", low)
    fams += [m for m in re.findall(r"--font[-\w]*\s*:\s*([^;{}]+)", low)]
    named = set()
    for decl in fams:
        for part in decl.split(","):
            name = part.strip().strip("'\"").strip()
            if name and name not in GENERIC_FALLBACKS and not name.startswith("var("):
                named.add(name)
    brandish = [n for n in named if n not in DEFAULT_FONTS]
    if named and not brandish:
        f.append(Finding("default-font-identity", "high", str(path),
                         f"only default fonts as the brand voice ({', '.join(sorted(named)[:3])}) — add a characterful display face"))
    if len(named) > 2:
        f.append(Finding("font-sprawl", "med", str(path),
                         f"{len(named)} typefaces ({', '.join(sorted(named)[:4])}…) — discipline is 1 display + 1 body"))

    # Rule 3: harsh shadows
    for m in re.finditer(r"box-shadow\s*:\s*([^;{}]+)", low):
        val = m.group(1)
        alpha = re.search(r"rgba?\([^)]*?[,/]\s*0?\.([3-9]\d?)\s*\)", val)
        if alpha or re.search(r"0\s+2px\s+4px", val):
            f.append(Finding("harsh-shadow", "med", f"{path}:{lineno(text, m.start())}",
                             f"heavy/opaque shadow `{val.strip()[:48]}` — go flat or use one ~6-16% large-blur shadow"))
            break
    tw_heavy = len(re.findall(r"\bshadow-(lg|xl|2xl)\b", low))
    if tw_heavy >= 3:
        f.append(Finding("shadow-soup", "med", str(path),
                         f"{tw_heavy}× shadow-lg/xl/2xl — depth should come from layout/imagery, not card stacks"))

    # Rule 5: transition:all / no easing curve
    for m in re.finditer(r"transition\s*:\s*all\b[^;{}]*", low):
        if "cubic-bezier" not in m.group(0):
            f.append(Finding("transition-all", "med", f"{path}:{lineno(text, m.start())}",
                             "`transition: all` with no chosen curve — define 1-2 easing tokens"))
            break
    if re.search(r"\btransition-all\b", low) and "ease-[" not in low and "cubic-bezier" not in low:
        f.append(Finding("transition-all", "low", str(path),
                         "Tailwind `transition-all` without a custom easing — pick a real curve"))

    # Rule 6: mixed border-radii
    radii = set()
    for m in re.finditer(r"border-radius\s*:\s*([0-9.]+)px", low):
        v = float(m.group(1))
        if v > 0:
            radii.add(v)
    radii.discard(9999.0)
    if len(radii) > 3:
        f.append(Finding("radius-sprawl", "med", str(path),
                         f"{len(radii)} distinct radii ({sorted(radii)[:6]}) — tokenize ONE radius identity"))

    # Rule 7: pure black/white
    pure = len(re.findall(r"#000(000)?\b", low)) + len(re.findall(r"#fff(fff)?\b", low))
    if pure >= 6:
        f.append(Finding("pure-bw", "low", str(path),
                         f"{pure}× pure #000/#fff — soften ink to #1d1d1f-ish and surfaces to off-white"))

    # Rule 12: !important skin
    bangs = low.count("!important")
    if bangs >= 8:
        f.append(Finding("important-skin", "med", str(path),
                         f"{bangs}× !important — likely a stock theme skinned with overrides, not a token system"))

    # Rule 8: stock/decorative imagery
    if "unsplash.com" in low:
        f.append(Finding("stock-imagery", "low", str(path),
                         "Unsplash asset referenced — use bespoke, palette-graded imagery"))

    # Rule 9: filler copy
    for pat in FILLER:
        m = re.search(pat, low)
        if m:
            f.append(Finding("filler-copy", "med", f"{path}:{lineno(text, m.start())}",
                             f"filler/placeholder copy: “{text[m.start():m.start()+40].strip()}…” — write with specificity"))

    # Emoji as UI
    if path.suffix in {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}:
        em = EMOJI.findall(text)
        if len(em) >= 3:
            f.append(Finding("emoji-ui", "low", str(path),
                             f"{len(em)} emoji in markup — avoid emoji as bullets/icons in serious design"))

    # Stale fingerprints
    m = re.search(r"©\s*20(1\d|2[0-3])\b", text)
    if m:
        f.append(Finding("stale-year", "low", f"{path}:{lineno(text, m.start())}",
                         f"stale copyright {m.group(0)} — update to current year"))
    if re.search(r"\.eot\b|format\(['\"]embedded-opentype", low):
        f.append(Finding("stale-fonts", "low", str(path), "IE-era font fallbacks (.eot) — dead weight"))
    return f


def collect(paths):
    out = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            for sub in p.rglob("*"):
                if sub.is_file() and sub.suffix.lower() in EXTS and "node_modules" not in sub.parts:
                    out.append(sub)
        elif p.is_file():
            out.append(p)
    return out


SEV_WEIGHT = {"high": 18, "med": 9, "low": 3}
SEV_COLOR = {"high": "\033[91m", "med": "\033[93m", "low": "\033[90m"}


def main():
    ap = argparse.ArgumentParser(description="Scan files for AI-slop design tells.")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="only print the score line")
    args = ap.parse_args()

    files = collect(args.paths)
    if not files:
        print("No matching files found.", file=sys.stderr)
        return 1

    findings = []
    for fp in files:
        try:
            findings += scan_text(fp, fp.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue

    score = max(0, 100 - sum(SEV_WEIGHT[f.severity] for f in findings))
    tty = sys.stdout.isatty()

    if args.json:
        print(json.dumps({"score": score, "files": len(files),
                          "findings": [{"rule": f.rule, "severity": f.severity,
                                        "where": f.where, "detail": f.detail} for f in findings]}, indent=2))
        return 0 if score >= 80 else 1

    if not args.quiet:
        if not findings:
            print(f"✓ {len(files)} file(s) scanned — no slop tells found.")
        for f in sorted(findings, key=lambda x: -SEV_WEIGHT[x.severity]):
            c = SEV_COLOR[f.severity] if tty else ""
            r = "\033[0m" if tty else ""
            print(f"{c}[{f.severity.upper():4}] {f.rule}{r}  {f.where}\n        {f.detail}")
    verdict = "CLEAN" if score >= 80 else ("RISKY" if score >= 55 else "SLOP")
    print(f"\nscore: {score}/100  →  {verdict}   ({len(findings)} findings, {len(files)} files)")
    return 0 if score >= 80 else 1


if __name__ == "__main__":
    sys.exit(main())
