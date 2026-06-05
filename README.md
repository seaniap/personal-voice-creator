# Personal Voice Creator

> An installable Claude skill that helps you build *your own* writing-voice skill — so Claude can write articles, letters, and posts that genuinely sound like you.

**Languages:** [English](README.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

---

## What it does

Generic AI writing sounds generic. **Personal Voice Creator** fixes that by guiding you through a short, conversational process and then packaging the result into a reusable skill:

1. **Choose your language** — Pick English, 繁體中文, or 日本語; the whole session runs in that language.
2. **Interview** — Claude asks questions about how you write, and weaves in situational prompts ("describe your work to a stranger at dinner") to capture your natural voice in the moment.
3. **Samples** — You share at least 3 pieces you've written across different contexts (a post, a business message, a longer piece). Cross-context patterns are the real voice markers.
4. **Test & calibrate** — Claude drafts sample pieces; you correct them until they sound like you.
5. **Package** — You get a `personal-voice.skill` file to install and use forever.

The magic is in step 3. Every "no, I'd phrase it this way" correction is captured, because that's where your real voice lives — in the gap between how you *think* you write and how you *actually* write.

## Quick start

### 1. Install the creator skill

Download [`dist/personal-voice-creator.skill`](dist/personal-voice-creator.skill), then in Claude go to **Settings → Skills** and upload it.

### 2. Run it

Start a chat and say something like:

> Help me build my personal voice skill.

Claude will interview you, ask for writing samples, draft test pieces, and calibrate based on your feedback.

### 3. Get your skill

At the end, Claude produces a `personal-voice.skill` file tailored to you. Install it the same way (**Settings → Skills**), then trigger it anytime with:

> Write this in my voice.

## What you'll need

- A Claude account with Skills enabled
- At least 3 real writing samples across different contexts (post, email, longer piece — the more varied, the better)
- 15–20 minutes for the interview and calibration

## Repository structure

```
.
├── README.md / README.zh-TW.md / README.ja.md   Docs (EN is canonical)
├── BUILD_LOG.md           How this project was made (story + lessons)
├── DESIGN.md              One-page design rationale
├── CLAUDE.md              Project memory for Claude Code
├── skill/
│   └── personal-voice-creator/    The skill source (edit here)
├── dist/
│   └── personal-voice-creator.skill   Built file (download this)
└── examples/              Sample walkthrough
```

## Building from source

If you edit the skill, rebuild the `.skill` file:

```bash
pip install pyyaml
python skill/personal-voice-creator/scripts/package_skill.py skill/personal-voice-creator dist
```

The packager validates the structure before zipping, so a broken skill won't build.

## Contributing

Issues and pull requests are welcome. Every PR runs an automated check that the skill still packages cleanly. See `CLAUDE.md` for project conventions.

## License

MIT — see [LICENSE](LICENSE).
