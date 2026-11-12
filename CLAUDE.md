# Vocabursters: working notes for Claude

Free weekly spelling games for Year 1 to Year 6 (ages 5–11), following the National Curriculum in England spelling appendix. It ships as an installable web app on GitHub Pages and as native App Store and Google Play apps (Capacitor 8).

**Read [`docs/MEMORY.md`](docs/MEMORY.md) first.** It holds the project history, decisions, current state and next steps, and it must be kept up to date (see the last section). [`docs/PLAN.md`](docs/PLAN.md) is the full product plan.

## Layout

| Path | What it is |
|---|---|
| `app/src/app.html` | **The whole app**: one file of HTML, CSS and plain JS, with no framework or bundler. `__WORDS__` / `__SENTENCES__` / `<!--FONTS-->` are placeholders filled in by the build |
| `app/public/` | Icons, PWA manifest, service worker (`sw.js`), self-hosted fonts, recorded voice (`audio/af_heart/{w,s}/*.mp3` + `audio/manifest.json`) |
| `app/site/` | Web-only pages: `privacy.html`, `support.html` (the store listings link to them) |
| `data/words.json`, `data/sentences.json` | 216 weekly lists (6 years × 36 weeks); example sentences for 182 words |
| `scripts/build.py` | `python3 scripts/build.py` builds `dist/` (GitHub Pages). `--native` builds `native-www/` (Capacitor `webDir`) |
| `scripts/generate_voice.py` | Records missing clips with Kokoro (setup is in the file's docstring) |
| `scripts/make_store_icons.js` + `npm run assets` | Icon and splash sources in `assets/`, then every native size |
| `scripts/store_screenshots.js` | Store screenshots and the Play graphics, written to `store/` |
| `ios/`, `android/` | Native projects (committed). `capacitor.config.json` holds the shared config |
| `store/LISTING.md`, `docs/STORE_RELEASE.md` | Store copy and form answers; step-by-step submission guide |
| `.github/workflows/` | `pages.yml` (deploy), `android.yml`, `ios.yml` (build on push; sign and upload when run by hand) |

## Commands

```sh
python3 scripts/build.py && python3 -m http.server -d dist 8000   # web app at localhost:8000
npm ci && npm run cap:sync                                         # native-www/ + copy into ios/ and android/
cd android && ./gradlew assembleDebug bundleRelease                # needs ANDROID_HOME (Android SDK 36, JDK 21)
npm run build:native && node scripts/store_screenshots.js          # retake store screenshots
```

## Rules and gotchas

- **Native-only behaviour is gated in `app.html`** on `NATIVE` (set from `window.Capacitor.isNativePlatform()`). Plugins are reached with `plugin("Name")`, which calls `Capacitor.registerPlugin`, because there is no bundler. `capacitor.js` is added only to the native build. Any change must keep the web app working when `NATIVE` is false.
- In the apps: TextToSpeech (`NTTS`), Haptics, App (Android back button) and SplashScreen are used. There is no service worker, no install prompts, no offline-download panel and no print.
- **After adding a Capacitor plugin**, run `npx cap sync`. It updates `ios/App/CapApp-SPM/Package.swift` (iOS uses Swift Package Manager, not CocoaPods) and the Android gradle files.
- **Privacy is a hard rule:**
  - no analytics, adverts, accounts, network calls with user data, external links or third-party SDKs;
  - progress lives in `localStorage` only.
  - The store listings declare "Data Not Collected", and Apple's Kids Category and Google's Families Policy depend on it.
- Bundle ID / package name `app.vocabursters.spelling` is permanent once uploaded to a store.
- Never commit signing material. `.gitignore` blocks `*.jks`, `*.p8`, `*.p12`, `android/keystore.properties`. CI reads signing details from GitHub secrets (names in `docs/STORE_RELEASE.md`).
- Generated folders that are not committed: `dist/`, `native-www/`, `node_modules/`, `android/app/src/main/assets/public`, `ios/App/App/public`.
- Voice clips live in `audio/<voice>/`. Changing the voice means changing the folder and the cache name, so devices don't mix voices.
- Pages deploys only from `main` and `claude/eager-faraday-o2i1u5` (`pages.yml`).
- No Mac and no Android emulator (no KVM) in cloud sessions:
  - iOS is checked by the `ios.yml` workflow on `macos-26`;
  - test native code paths in Playwright with a fake `window.Capacitor` + `window.androidBridge` (see `scripts/store_screenshots.js`).
- If Maven Central returns 429 errors in a cloud session, retry Gradle with `--max-workers=2`.
- Writing style for user-facing text: British English, plain and friendly, short sentences, child-safe.

## Keep the memory up to date

At the end of any session that changes the project, update `docs/MEMORY.md`:
- add a dated line to the **Log**;
- refresh **Current state** and **Next steps**;
- record new decisions under **Decisions**.

Also update `docs/PLAN.md` §15–16 if decisions or status changed. Commit the memory update with the work.
