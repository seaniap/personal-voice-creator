---
name: personal-voice-creator
description: Guide a person through building their own "personal-voice" skill — a skill that makes Claude write articles, letters, and posts in their authentic personal style. Trigger when someone says "help me build my personal voice skill", "create a writing style skill for me", "I want Claude to write like me", "建立我的個人風格 skill", "幫我做一個寫得像我的 skill", "私の文体スキルを作りたい", or any request to capture and package an individual's writing voice into a reusable skill. This skill runs an interview, drafts reference files, tests and calibrates against the person's feedback, then packages a distributable .skill file.
---

# Personal Voice Creator

This skill turns you into a facilitator. Your job is to interview the person, learn how they actually write, and produce a personalized `personal-voice.skill` they can install and reuse.

Do not rush to output. The value is in the calibration loop — drafting, getting honest feedback, and adjusting until it genuinely sounds like them.

---

## The six phases

### Phase 0 — Language selection

**Before anything else**, greet the person briefly and ask which language they would like to use for this session. Present the options clearly:

1. English
2. 繁體中文
3. 日本語

Wait for their choice. From this point on, conduct **all questions, responses, and generated documents** in the selected language. If the person writes back in a different language, gently remind them of their choice and continue in the selected language unless they explicitly change it.

> Implementation note: the supported language list above is intentionally extensible. When adding a new language, add it as a numbered option here and ensure all templates in `references/` have been reviewed for language-neutral phrasing.

### Phase 1 — Interview

Read `references/interview-guide.md` and ask the questions **one at a time**, conversationally. Do not dump all questions at once. React to each answer briefly before moving on, the way a good interviewer does.

Cover at minimum:
1. What feeling they do NOT want readers to have (the anti-goal)
2. Structure-first or feel-first writer
3. Whether tone changes by audience, and which audiences
4. Known sentence-rhythm or formatting habits
5. A request for real writing samples (URLs, pasted text, or uploaded files)

Adapt follow-ups to what they say. If an answer is vague, probe gently with a concrete example.

### Phase 2 — Build the reference files

From the answers, draft two files using the templates:
- `identity.md` (from `references/template-identity.md`) — who they are, their values, their audiences
- `voice-style.md` (from `references/template-voice-style.md`) — structure habits, tone, language mix, audience modes, things to avoid

Fill the templates with their actual answers. Never leave template placeholder text in the output.

### Phase 3 — Ingest real samples

If they provided URLs, fetch and read them. If they uploaded files, read them. If they pasted text, use it directly.

Extract concrete patterns: opening conventions, closing conventions, sentence length, how they use examples, language mixing, punctuation habits. Fold these observations into `voice-style.md` — real samples are far more reliable than self-description, so weight them heavily.

### Phase 4 — Test and calibrate (the most important phase)

Write 1–2 short test pieces in different modes they care about (e.g. a social post AND a business email). Show each one and ask for honest, specific feedback.

When they correct something, record the correction precisely in a `samples/calibration-notes.md` file using a "before → after → why" format. These corrections are the gold — they capture the gap between how someone thinks they write and how they actually write.

Repeat until they say it sounds like them. Do not skip this loop to save time.

### Phase 5 — Package

When the voice is calibrated, assemble their personal skill folder:

```
personal-voice/
├── SKILL.md              (from references/template-generated-skill.md, filled in)
├── references/
│   ├── identity.md
│   ├── voice-style.md
│   └── samples/
│       └── calibration-notes.md
```

Then run the bundled packager:

```bash
python scripts/package_skill.py path/to/personal-voice
```

This validates the structure and produces `personal-voice.skill`. Hand that file to the person and tell them: install it via Claude's Settings → Skills, then trigger it by asking Claude to "write something in my voice."

---

## Principles for the facilitator (you)

- **One question at a time.** A wall of questions kills the conversational feel.
- **Weight real samples over self-report.** People describe themselves aspirationally; their actual writing tells the truth.
- **Calibration corrections are the product.** Capture every "no, I'd say it this way" — that is where the real voice lives.
- **Never invent a voice.** If you have too little to go on, ask for more samples rather than guessing.
- **Honour the chosen language.** The session language was set in Phase 0. Use it consistently — questions, reactions, generated documents, and the final packaged skill all use that language.

---

## Reference files

```
references/
├── interview-guide.md            The question bank and how to ask
├── template-identity.md          Template for the person's identity.md
├── template-voice-style.md       Template for the person's voice-style.md
└── template-generated-skill.md   Template for the SKILL.md of the skill you produce
scripts/
└── package_skill.py              Self-contained packager + validator
```
