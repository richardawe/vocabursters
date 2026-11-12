# Vocabursters memory

The running record of where the project is. Update it at the end of every working session (newest log entry first). For the full product thinking see [`PLAN.md`](PLAN.md); for how to work in the repo see [`../CLAUDE.md`](../CLAUDE.md).

_Last updated: 2026-11-12 (pre-submission polish)_

## Current state

- **Web app:** live at https://richardawe.github.io/vocabursters/.
  - It is an installable PWA that works offline.
  - All 7 weekly game modes run on the real word lists for Years 1–6.
  - Other features:
    - Smart practice and the Speed round;
    - Bubble Battle against computer rivals;
    - the Word map;
    - the shop, pet and stickers;
    - the parent zone (progress, players, settings, printable test, backup/restore).
  - Every word and sentence is recorded in the Kokoro `af_heart` voice.
- **Store apps:** built on branch `claude/blissful-fermi-hmcnvp`, **not yet submitted**.
  - **Projects:** iOS (iPhone + iPad) and Android (phones + tablets) Capacitor 8 projects are committed.
  - **Android:** the release AAB and debug APK compiled in a cloud session. They have not been run on a device or emulator.
  - **iOS:** compiles in the `ios.yml` GitHub workflow (simulator build, Xcode 26.6 on `macos-26`). First run passed on 2026-11-12. Not yet signed or run on a device.
  - **CI:** the first `android.yml` and `ios.yml` runs both passed (2026-11-12).
  - **Pre-submission polish (branch `claude/blissful-fermi-hmcnvp`, not merged into `main`):**
    - Capacitor `loggingBehavior` is `none`.
    - Android backup is off (`allowBackup="false"`, `fullBackupContent="false"`, data-extraction rules excluding cloud backup and device transfer).
    - iOS App-Bound Domains are declared (`WKAppBoundDomains = [localhost]`).
    - The support page has a TODO for the real support email.
  - **Store materials, all ready:** icons, splash screens, screenshots for every required size, the Play feature graphic, listing copy, form answers, and the privacy and support pages.
- **Site:** live at https://richardawe.github.io/vocabursters/ and deploying **only from `main`**, which is the default branch. The Pages source must stay **GitHub Actions**: "Deploy from a branch" shows the README instead of the game. The `github-pages` environment allows `main`. The game, `privacy.html` and `support.html` were all checked live on 2026-11-12. `claude/eager-faraday-o2i1u5` is old and unused.

## Next steps

0. Before submitting:
   - Owner decides whether to merge the polish branch into `main`. That republishes the site; only `support.html`'s hidden comment changes on the web.
   - Owner chooses the support email (TODO in `app/site/support.html`).
   - On the first TestFlight build, check that the app loads with App-Bound Domains on.
   - Decide whether iOS should also be excluded from iCloud device backup. WKWebView `localStorage` lives in `Library/WebKit`, which iCloud backs up by default. That is not yet changed, and the privacy policy says data stays "only on the device".
1. Owner: start the store steps in `docs/STORE_RELEASE.md` (Apple and Google accounts, then add signing secrets, then run the workflows on `main`).
2. Owner tasks (see `docs/STORE_RELEASE.md`):
   - **Apple:**
     - enrol in the Developer Program;
     - register the bundle ID;
     - create the app in App Store Connect;
     - add the API key and Team ID secrets;
     - run the iOS workflow;
     - test with TestFlight;
     - fill in the listing and submit.
   - **Google:**
     - create the developer account;
     - make the upload key and add the secrets;
     - run the Android workflow;
     - set up the app and fill in the forms;
     - run internal testing, then a closed test (12 testers × 14 days for new personal accounts);
     - release to production.
   - Choose a public support email (optionally add it to `app/site/support.html` at `SUPPORT_CONTACT`).
3. Test on real devices: a cheap Android phone, an Android tablet, an older iPhone and an iPad. Check:
   - sound with the silent switch;
   - the native text-to-speech fallback;
   - the back button;
   - rotation on tablets;
   - backup/restore.
4. Then Phase 1 of the roadmap (PLAN.md §13):
   - Vite + TypeScript;
   - IndexedDB;
   - unit tests for the spelling engine;
   - accessibility audit;
   - more example sentences (only 182 of 1,338 words have one).

## Decisions

| Date | Decision |
|---|---|
| 2026-11 | Name **Vocabursters**. Free, with no adverts, accounts, purchases or tracking. Progress lives only on the device |
| 2026-11 | Voice: **Kokoro `af_heart`** (American English, chosen by ear over the British voices). The device voice is the fallback and reads instructions that contain a child's name |
| 2026-11 | Capital letters: gentle by default (a wrong capital counts as right, with a reminder); parents can switch to strict |
| 2026-11 | Word lists and sentences checked; they ship as they are |
| 2026-11 | Delivered as an installable web app on GitHub Pages **and** on the App Store and Google Play |
| 2026-11-12 | Store apps: Capacitor 8, one build per platform for phones and tablets. Phones are portrait-only, tablets can turn. Voice bundled for offline use. iOS uses Swift Package Manager |
| 2026-11-12 | GitHub Pages deploys only from `main`; work happens on branches and is merged into `main` to publish |
| 2026-11-12 | Package / bundle ID `app.vocabursters.spelling` (permanent once uploaded) |
| 2026-11-12 | Store builds run in GitHub Actions, so no Mac is needed. Signing comes from repo secrets; build numbers come from the workflow run number |
| 2026-11-12 | Listings: category Education; Apple "Data Not Collected", 4+, Kids Category optional (6–8); Google: all children's age groups (Families Policy), no data collected or shared |
| 2026-11-12 | Device backups off on Android (Auto Backup and device transfer); the in-app backup code is the only way to move progress |
| 2026-11-12 | iOS web view limited to App-Bound Domains, with `localhost` (bundled app) as the only domain |
| Open | Timed games on or off by default |
| Open | Family leaderboard for everyone, or opt-in per player |

## Log

- **2026-11-12**: pre-submission polish (no app ID change, no cap init, no new platforms, no IAP or accounts).
  - `loggingBehavior` set to `none`.
  - Android Auto Backup and device-to-device transfer turned off, so nicknames in `localStorage` stay on the device. This makes the Play Data safety answer "no data collected" unambiguous.
  - iOS `WKAppBoundDomains = [localhost]` added to match `limitsNavigationsToAppBoundDomains: true`.
  - Support email TODO added.
  - Android rebuilt and checked; native and web smoke tests passed.
- **2026-11-12**: built the App Store and Google Play apps (commit `3a659c6`).
  - Added the native projects, the `--native` build, and the native-only code in `app.html` (TTS, haptics, back button, splash, hidden install/print).
  - Added icons and splash screens, store screenshots and graphics, privacy and support pages, `store/LISTING.md`, `docs/STORE_RELEASE.md`, and the `android.yml` / `ios.yml` workflows.
  - Created `CLAUDE.md` and this memory file.
  - First CI runs passed: Android AAB/APKs, and the iOS simulator build on Xcode 26.6.
  - Created `main` from `claude/blissful-fermi-hmcnvp` and made it the only branch Pages deploys from (owner's choice). The owner set the default branch, the environment rule and the Pages source (GitHub Actions). Live site checked: the game plays on phone and tablet sizes, and the privacy and support pages are up.
- **2026-11-07**: switched the recorded voice to Kokoro `af_heart`.
  - Re-recorded 1,338 words and 183 sentences.
  - Clips moved to `audio/<voice>/`; the service worker deletes old voice caches.
- **2026-11-07**: shipped the installable web app on GitHub Pages (PWA, offline service worker, self-hosted fonts, auto-updates).
- **2026-11-07**: added the TTRS-inspired mechanics and the mobile version:
  - coins and the shop;
  - Speller status and the Speed round;
  - Bubble Battle;
  - the Word map and Smart practice;
  - phone and tablet layouts.
- **2026-11-07**: wrote the plan, word data and a playable mockup.
