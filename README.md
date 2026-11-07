# Vocabursters

Weekly spelling and grammar games for Year 1 to Year 6 (ages 5 to 11). It's built from the *Weekly Vocabulary Tests: Y1 to Y6* lists: 216 weeks and 1,908 words, following the National Curriculum in England spelling appendix.

It's a web app that parents add to the home screen. There's no login, and progress stays on the device.

- **Plan:** [`docs/PLAN.md`](docs/PLAN.md) covers goals, game ideas, gamification, features for the age group, privacy, the technical plan, the roadmap and decisions still to make.
- **Playable mockup:** open [`mockup/index.html`](mockup/index.html) in a browser. To test installing and offline use, serve the folder over HTTP: `npm run serve` (or `python3 -m http.server -d mockup 8000`).
- **Mobile:** on a phone the app has a bottom tab bar, full-screen games and a keyboard docked at the bottom; on tablets and computers the tabs move to the top. Add it to the home screen to use it like an app.
- **App Store / Google Play (optional):** the Capacitor setup wraps the same app in native shells. Run `npm install`, then `npm run android` (needs Android Studio) or `npm run ios` (needs Xcode). See section 10 of the plan for caveats.

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
| `package.json`, `capacitor.config.json` | Native iOS/Android app shells via Capacitor (generated `android/` and `ios/` folders are not committed) |

## Rebuild

```sh
python3 scripts/build_mockup.py
```
