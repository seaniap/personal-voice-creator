# CLAUDE.md — Project Memory for Claude Code

This file gives Claude Code the context it needs every time it works on this repo. Read it before making changes.

## What this project is

`personal-voice-creator` is a **meta-skill**: an installable Claude skill that guides any person through building their *own* `personal-voice.skill` — a skill that makes Claude write in their authentic personal style.

The user runs the creator, gets interviewed, provides writing samples, calibrates through test drafts, and ends up with a packaged `.skill` file they can install and reuse.

## Repository layout

```
.
├── README.md / README.zh-TW.md / README.ja.md   Docs in 3 languages (EN is canonical)
├── BUILD_LOG.md           The making-of record — local dev branch only, never on main
├── DESIGN.md              One-page design rationale
├── CLAUDE.md              This file
├── LICENSE                MIT
├── .github/
│   ├── workflows/validate.yml      CI: packages the skill on every PR to catch breakage
│   └── ISSUE_TEMPLATE/             Bug report + feature request templates
├── skill/
│   └── personal-voice-creator/     THE SOURCE OF TRUTH — edit the skill here
│       ├── SKILL.md
│       ├── references/
│       └── scripts/package_skill.py
├── dist/
│   └── personal-voice-creator.skill   Built artifact for download (rebuild after edits)
└── examples/                       Sample walkthrough / sample output
```

## Conventions — do not break these

- **The skill source lives in `skill/personal-voice-creator/`.** Never edit files inside `dist/` directly; they are build outputs.
- **Exactly one `SKILL.md` per skill.** claude.ai and the Skills API reject multiple SKILL.md files on upload. Supporting docs must be named `references/<topic>.md`, never `SKILL.md`.
- **Keep the packager dependency-light.** `scripts/package_skill.py` must stay self-contained (only PyYAML). Do not reintroduce imports from an external `scripts` package.
- **After editing the skill, rebuild the artifact:**
  ```bash
  python skill/personal-voice-creator/scripts/package_skill.py skill/personal-voice-creator dist
  ```
- **Three READMEs stay in sync.** If you change behavior, update README.md, README.zh-TW.md, and README.ja.md together. English is canonical.
- **Append to BUILD_LOG.md** when a change is interesting enough to mention in the eventual blog post. Work on the `dev` branch when updating it.

## Branch workflow

- **Develop on `dev`**, merge to `main` when ready, then push `main` to GitHub.
- `dev` is local-only — never push it to remote.
- **BUILD_LOG.md is tracked on `dev` but not on `main`.** After every `git merge dev`, check whether BUILD_LOG.md was pulled in and remove it before pushing:
  ```bash
  git rm --cached BUILD_LOG.md
  git commit -m "chore: remove BUILD_LOG.md from merge"
  ```

## Commit message style

Use conventional-commit prefixes: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`. Keep the subject line short and factual.

## Design philosophy

KISS. This project is a few Markdown files and one script. Resist over-engineering — no heavyweight build system, no full SDD. The CI exists for exactly one reason: catch a broken skill structure before it ships.
