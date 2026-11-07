# Vocabursters

Weekly spelling and grammar games for Year 1 to Year 6 (ages 5 to 11). It's built from the *Weekly Vocabulary Tests: Y1 to Y6* lists: 216 weeks and 1,908 words, following the National Curriculum in England spelling appendix.

It's a web app that parents add to the home screen. There's no login, and progress stays on the device.

- **Plan:** [`docs/PLAN.md`](docs/PLAN.md) covers goals, game ideas, gamification, features for the age group, privacy, the technical plan, the roadmap and decisions still to make.
- **Playable mockup:** open [`mockup/index.html`](mockup/index.html) in a browser. To test installing and offline use, serve the folder over HTTP: `python3 -m http.server -d mockup 8000`.

## What's here

| Path | What it is |
|---|---|
| `data/words.json` | All 216 weekly word lists, extracted from the PDF and checked |
| `data/sentences.json` | Example sentences, including every homophone and apostrophe word |
| `mockup/src/app.html` | Mockup source (HTML, CSS and JS in one file) |
| `mockup/index.html` | Built standalone app: installable, works offline |
| `mockup/vocabursters.html` | Built page body used for the hosted preview |
| `mockup/manifest.webmanifest`, `sw.js`, icons | Files that make the app installable and work offline |
| `scripts/build_mockup.py` | Inlines the data into the mockup. Run it after editing `data/` or `mockup/src/` |

## Rebuild

```sh
python3 scripts/build_mockup.py
```
