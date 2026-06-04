# Example Walkthrough

This is what running `personal-voice-creator` looks like, using the project author's own session as a worked example.

## The interview (abbreviated)

- **Anti-goal:** doesn't want to sound like he's showing off, reading from a script, or being preachy.
- **Structure:** mostly plans first (pyramid structure), occasionally writes by feel.
- **Audiences:** social friends (natural, warm) · clients (composed, CEO-level courtesy) · Japanese friends (JLPT N2, conversational, no stiff literary forms).
- **Habits:** conclusion first, then explanation; small concrete examples over big abstractions; occasional English/Japanese mixed in; prefers visual/diagram-style explanation for complex things.

## Sample ingestion

Five real Medium articles were read. Observed patterns the author hadn't stated himself:
- Technical posts open with an overall architecture picture, then break it down.
- Non-technical posts cite a definition first (often in English), then explain it with an everyday analogy.
- Tone stays even and unhurried — no exclamation-mark hype.

## Calibration (the valuable part)

A test social post was drafted. Corrections that defined the voice:

| Draft | Correction | Why |
|-------|-----------|-----|
| "It's a little embarrassing to admit…" | removed; start on the point | rarely uses self-deprecating openers |
| "I'm not going to work in Japan" | "I'm really not going to work in Japan" | prefers a firmer negative |
| "the invisible glass" | "the invisible wall" | stronger word choice |
| "not papering over it with a translation tool, it just disappears" | "that feeling is something a translation tool can't give you" | original had a muddled subject |

A test business email's first draft sounded too casual ("had a chat with a few marketing leads"); the rewrite ("spoke recently with several marketing leads") landed the composed, CEO-level tone.

## The resulting skill

```
personal-voice/
├── SKILL.md
└── references/
    ├── identity.md
    ├── voice-style.md
    └── samples/
        └── calibration-notes.md
```

Packaged into `personal-voice.skill` and installed via Settings → Skills. From then on, "write this in my voice" produces text that reads like the author wrote it.

---

> Your own run will look different — that's the point. The interview and your samples make the skill yours.
