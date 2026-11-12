# Vocabursters memory

The running record of where the project is. Update it at the end of every working session (newest log entry first). For the full product thinking see [`PLAN.md`](PLAN.md); for how to work in the repo see [`../CLAUDE.md`](../CLAUDE.md).

_Last updated: 2026-11-12_

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
  - **Store materials, all ready:** icons, splash screens, screenshots for every required size, the Play feature graphic, listing copy, form answers, and the privacy and support pages.
- **Site:** GitHub Pages is the only site, and it deploys **only from `main`**. `main` was created on 2026-11-12 from `claude/blissful-fermi-hmcnvp`. `claude/eager-faraday-o2i1u5` is old and no longer deploys. The privacy and support pages go live with the first `main` deploy.

## Next steps

1. Check https://richardawe.github.io/vocabursters/privacy.html and `/support.html` open. On GitHub, set `main` as the default branch (Settings → General) and, if Pages complains, allow `main` under Settings → Environments → github-pages.
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
| Open | Timed games on or off by default |
| Open | Family leaderboard for everyone, or opt-in per player |

## Log

- **2026-11-12**: built the App Store and Google Play apps (commit `3a659c6`).
  - Added the native projects, the `--native` build, and the native-only code in `app.html` (TTS, haptics, back button, splash, hidden install/print).
  - Added icons and splash screens, store screenshots and graphics, privacy and support pages, `store/LISTING.md`, `docs/STORE_RELEASE.md`, and the `android.yml` / `ios.yml` workflows.
  - Created `CLAUDE.md` and this memory file.
  - First CI runs passed: Android AAB/APKs, and the iOS simulator build on Xcode 26.6.
  - Created `main` from `claude/blissful-fermi-hmcnvp` and made it the only branch Pages deploys from (owner's choice), which puts the privacy and support pages online.
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
