# Design Rationale

A one-page explanation of why this project is built the way it is. (Deliberately not a full SDD — see the last section.)

## The problem

Generic AI writing sounds generic. People want Claude to write in *their* voice — but a static prompt like "write in my style" doesn't carry enough signal, and most people can't articulate their own style on demand.

## The core insight

The truest signal of someone's voice is not how they describe themselves — it's:
1. Their real writing samples, and
2. The corrections they make when they see a draft that's *almost* right.

So the design centers on a **calibration loop**, not a questionnaire. The interview is just enough to get a first draft; the value accrues in the "no, I'd say it this way" feedback.

## Why a meta-skill

We could have shipped one person's voice skill. Instead we ship the *process* that produces a voice skill, so anyone can run it. The creator skill encodes the facilitation workflow: interview → draft reference files → ingest samples → test & calibrate → package.

## Architecture in one breath

- `SKILL.md` — the facilitation workflow Claude follows
- `references/interview-guide.md` — the question bank
- `references/template-*.md` — templates for the files the process produces
- `scripts/package_skill.py` — self-contained validator + packager

The output is a separate, standalone `personal-voice.skill` with its own `identity.md`, `voice-style.md`, and accumulated `calibration-notes.md`.

## Key design decisions

- **Self-contained packager.** The original packager imported from an external `scripts` module and failed for anyone without the full toolkit. The distributed version validates inline and depends only on PyYAML.
- **Samples weighted over self-report.** The workflow explicitly tells the facilitator to trust writing samples more than interview answers.
- **Calibration notes are a first-class artifact.** They persist into the generated skill so the voice keeps sharpening with use.

## Why no full SDD

The entire codebase is a handful of Markdown files and one Python script. A formal software design document (or a strict spec-driven process) would be heavier than the thing it describes — a violation of KISS. Project context for ongoing development lives in `CLAUDE.md` instead, because that file actually gets read on every session. This page exists only to record intent for future maintainers and for the blog write-up.
