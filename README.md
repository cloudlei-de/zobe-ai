# zobe.ai — the anti-slop enterprise design skill

> A Claude Code / Claude skill that turns generic "AI slop" into intentional, enterprise-grade design.
> Brand-agnostic. Media-agnostic. Installable by anyone.

zobe.ai is a portable [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills). When invoked, it runs a short, opinionated **design intake** (it asks you about brand, color, type, density, motion, archetype), then designs — or **de-slops an existing design** — using zobe.ai's distilled design intelligence.

It does two things:

1. **Design from a brief** — greenfield UI/landing/brand work, grounded in real craft, not template defaults.
2. **De-slop an existing design** — paste code, a screenshot, or a URL and zobe.ai diagnoses the slop tells and rebuilds it with craft.

Output: **production code (HTML / React + Tailwind) and a portable design-token set** (colors, type scale, spacing, radii, motion).

---

## What problem it solves

LLMs left to their own devices produce a recognizable look: the same generic gradient, the same Inter-everywhere, emoji bullets, everything center-stacked, glassmorphic cards, `shadow-lg` on everything, and zero hierarchy. That's "AI slop." zobe.ai encodes *why* premium sites look premium and forces those decisions to be made on purpose.

---

## Install

A skill is just a folder with a `SKILL.md`. Pick the scope you want:

**Personal (all your projects):**
```bash
cp -R zobe-ai ~/.claude/skills/zobe-ai
```

**One project only:**
```bash
cp -R zobe-ai /path/to/project/.claude/skills/zobe-ai
```

**Claude.ai / Claude Desktop:** zip the `zobe-ai` folder and upload it under Settings → Capabilities → Skills.

That's it — no build step, no dependencies. Verify it's picked up with `/help` (Claude Code) or by typing `/zobe-ai`.

### Use it in any tool — Cursor, Codex, OpenCode & more

The same intelligence ships in portable, tool-native formats. All of them point at the same
`references/` and `scripts/`:

| Tool | What it reads | How to install |
|---|---|---|
| **Claude** (Code / Desktop / claude.ai) | `SKILL.md` | copy the folder to `~/.claude/skills/zobe-ai`, then `/zobe-ai` |
| **OpenAI Codex, OpenCode, Amp, Zed, Gemini CLI** | `AGENTS.md` | drop `AGENTS.md` (+ `references/`, `scripts/`) at your repo root, or merge into your existing `AGENTS.md` |
| **Cursor** | `.cursor/rules/zobe-ai.mdc` | copy `.cursor/rules/zobe-ai.mdc` into your project's `.cursor/rules/` |
| **GitHub Copilot** | `.github/copilot-instructions.md` | copy it into your repo's `.github/` |
| **Windsurf** | `.windsurfrules` | copy it to your project root |

The fastest path for any of them: clone this repo into (or next to) your project so `AGENTS.md`,
`.cursor/rules/`, `references/` and `scripts/` are all present, and your agent picks up the rules
automatically.

### Optional: image generation

The skill can generate on-brand imagery (hero, product shots, `og:image`) with **OpenAI GPT Image 2**. This is the only part that needs anything extra:

- a **paid OpenAI API key** in your environment: `export OPENAI_API_KEY="sk-..."` (get one at https://platform.openai.com/api-keys)
- Python 3 (already on macOS/Linux) — the scripts are stdlib-only, no `pip install`.

Without a key, everything else works; the skill just hands you art-directed prompts and on-palette placeholders instead of generating.

> The skill folder is named `zobe-ai` because skill identifiers must match `^[a-z0-9-]+$` (no dots). The brand is **zobe.ai**; the invocation is `/zobe-ai`.

---

## Use

Invoke explicitly:
```
/zobe-ai
```
…or just describe a design task and Claude will reach for it (the description is written to trigger on design / UI / landing-page / "make this look good" / "fix this design" requests).

Typical flows:

- `/zobe-ai` → *"Landing page for a B2B security SaaS, German, serious but modern."*
  → zobe asks 4–6 sharp questions → proposes a direction → builds tokens + code.
- `/zobe-ai` → *"Here's my current hero section [paste code]. It looks like AI slop. Fix it."*
  → zobe runs the slop diagnostic → rebuilds with a rationale for every change.

You can skip the intake any time by saying *"skip the questions, just go"* — zobe will infer and state its assumptions.

---

## What's inside

```
zobe-ai/
├── SKILL.md                          # Claude Agent Skill (operating instructions)
├── AGENTS.md                         # portable rules for Codex / OpenCode / Amp / Zed …
├── .cursor/rules/zobe-ai.mdc         # Cursor project rule
├── .github/copilot-instructions.md   # GitHub Copilot instructions
├── .windsurfrules                    # Windsurf rules
├── README.md                         # this file
├── references/
│   ├── method.md                     # the end-to-end design process zobe runs
│   ├── anti-slop.md                  # slop tells → craft fixes, red-flag checklist
│   ├── color.md                      # palette construction, contrast, restraint
│   ├── typography.md                 # type pairing, scale, tracking, hierarchy
│   ├── spacing-layout.md             # grid, rhythm, whitespace, composition
│   ├── shape-motion-imagery.md       # radii, shadows, motion, imagery treatment
│   ├── imagery-generation.md         # art-directing & generating imagery (GPT Image 2)
│   └── archetypes.md                 # preset design systems (incl. switchable looks)
├── scripts/
│   ├── gen_tokens.py                 # accent + mode → WCAG-checked token set
│   ├── slop_audit.py                 # lint files for slop tells, score 0–100
│   ├── image_brief.py                # asset + brand → art-directed image prompt
│   └── gpt_image.py                  # generate the image via OpenAI GPT Image 2
└── assets/
    └── tokens.template.css           # copy-paste design-token scaffold
```

`SKILL.md` stays lean; the `references/` files are loaded on demand so the skill scales without bloating context. The `scripts/` are stdlib-only Python 3 — they make zobe.ai's judgment executable (generate tokens, lint for slop) with zero install.

Quick taste:
```bash
python3 scripts/gen_tokens.py --accent "#0071e3" --mode light --report   # generate tokens
python3 scripts/slop_audit.py ./src --json                               # audit your code
```

---

## About

zobe.ai is a self-contained design intelligence. It ships no third-party assets — only its own laws, archetypes, tokens, and tooling. Bring your own fonts, imagery, and (for generation) an OpenAI API key.

## License

MIT — © 2026 cloudlei. See [LICENSE](./LICENSE).

You may use, modify, and redistribute the skill freely, including commercially. The only requirement is that the copyright notice and license text stay included.
