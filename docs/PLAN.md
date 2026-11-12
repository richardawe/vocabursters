# Vocabursters: product plan

A spelling and grammar web app for Year 1 to Year 6 (ages 5 to 11), built from the *Weekly Vocabulary Tests: Y1 to Y6* lists. Parents install it on a phone, tablet or computer. There's no login, no account and no data leaves the device.

**The app is live at https://richardawe.github.io/vocabursters/** (source in [`app/`](../app), built by `scripts/build.py`, deployed to GitHub Pages on every push). It started as a mockup and is now the version families use. It's built mobile-first: on a phone it works like an app, with a bottom tab bar and full-screen games.

**Version 2 of this plan** adds ideas borrowed from Times Tables Rock Stars (section 6) and a dedicated mobile version (section 10).

---

## 1. Goals

**What success looks like**

1. A child practises their week's words for 10 to 15 minutes, 3 or more times a week, and wants to come back.
2. Friday test scores go up, and missed words are re-tested until they stick.
3. A parent can see in 30 seconds which words their child finds hard.
4. A 5-year-old who can't read yet can use it without help after the first go.

**Out of scope (for now)**

- Accounts, cloud sync, classrooms or teacher dashboards.
- Leaderboards against other children, chat, or any social features.
- Adverts, in-app purchases or loot boxes.

---

## 2. The source material

| Year | Words a week | Weeks | Words | What it covers |
|---|---|---|---|---|
| Y1 | 5 | 36 | 180 | Phonics (short vowels, digraphs), the common exception words, split digraphs, suffixes, days of the week |
| Y2 | 8 | 36 | 288 | Y2 spelling rules (dge, kn, wr, -le, -tion), y→ies, consonant doubling, contractions, possessives, homophones |
| Y3 | 10 | 36 | 360 | Prefixes, suffixes (-ous, -tion, -sion), Greek-origin ch, the Y3/4 statutory list, homophones, apostrophes |
| Y4 | 10 | 36 | 360 | Statutory list revision, -ation, -ious, Greek and Latin roots, silent letters, -ough, plurals, subject vocabulary |
| Y5 | 10 | 36 | 360 | -cious/-tious, -ant/-ent, -able/-ible, ie/ei, hyphens, homophones, the first 50 Y5/6 statutory words, word origins |
| Y6 | 10 | 36 | 360 | The second 50 Y5/6 statutory words, full revision, word building, commonly misspelt words, secondary-school vocabulary |
| **Total** | | **216** | **1,908** | **1,338 different words** (many come back for revision, which suits spaced practice) |

The lists are in [`data/words.json`](../data/words.json), extracted from the PDF and checked: every week has the right number of words.

**Data issues found while extracting**

- Three PDF line-break errors were fixed: `- ment` → `-ment` (Y4 W8), `re- elect` → `re-elect` and `ex- captain` → `ex-captain` (Y5 W14).
- Y6 W21 is labelled "Suffixes -ial, -ual" but includes *serious* and *obvious*, which are -ious words. Worth swapping for *partial* and *spatial*, or relabelling.
- The PDF says it was compiled from memory. Before launch, a teacher should check the Y3/4 and Y5/6 statutory weeks against the official DfE spelling appendix.
- Some words need special handling: *I* and *a* are single letters, *Monday*, *February*, *James's*, *Roman*, *Tudor* need capitals, *café* and *fiancé* need an é key, and Y2 to Y6 contain apostrophes and hyphens. The mockup handles all of these.
- Homophone and apostrophe weeks (*there/their*, *girl's/girls'*) can't be tested by saying the word alone. Every word in those weeks now has an example sentence in [`data/sentences.json`](../data/sentences.json). The full app needs one sentence for every word.

---

## 3. Who it's for

| | Years 1–2 (5–7) | Years 3–4 (7–9) | Years 5–6 (9–11) |
|---|---|---|---|
| Reading | Early readers; many can't read instructions | Read instructions, but slowly | Fluent |
| Hands | Imprecise taps; big targets needed | Fine | Fine; can type |
| Attention | 5–10 minutes | 10–15 minutes | 15–20 minutes |
| Motivated by | Characters, sounds, stickers, praise | Collecting, levelling up, a bit of challenge | Mastery, beating their own best, choice, not feeling babied |
| What it means for design | Every instruction has a speaker button. ABC keyboard. 2 extra bubbles, not 3. Lots of celebration | QWERTY keyboard. All games open | Same app, but quieter visuals are possible (calm mode). Harder words already raise the challenge |

The mockup adapts automatically: the keyboard defaults to ABC for Years 1–2, Bubble Burst uses fewer decoy letters for younger children, and the Friday test length follows the year (5, 8 or 10 words).

---

## 4. The weekly loop

This copies the paper routine in the PDF so the app fits what families already do:

1. **Start of the week: learn.** *Look, Say, Cover, Write, Check* introduces each word with its tricky part highlighted.
2. **Midweek: practise.** Short games (Bubble Burst, Missing Letters, Spot the Spelling, Word Jumble, Homophone Hero). Each takes 2 to 4 minutes.
3. **Friday: test.** The app reads each word, uses it in a sentence, then says it again, just as the PDF tells parents to do. The score is out of 5, 8 or 10.
4. **Next week: bounce-back words.** Missed words are added to the next test (up to 3) and to a separate bounce-back round until they're spelled correctly. This is the PDF's "re-test missed words the following week".
5. Finishing the Friday test unlocks the next week and earns that week's sticker.

The parent can move the current week or year at any time in the Grown-ups area, for example to match school or to go back and fill gaps.

---

## 5. Game modes

### Built in the mockup

| Game | Years | How it plays | Why it works |
|---|---|---|---|
| **Look, Say, Cover, Write, Check** | All | See the word with its tricky part highlighted and hear it in a sentence. The word is hidden, the child types it, then sees a letter-by-letter comparison | The method UK schools already use. Highlighting the week's pattern teaches the *rule*, not only the word |
| **Bubble Burst** | Y1–3 best | Hear the word and pop floating letter bubbles in order. There are decoy letters. After 2 wrong taps the right bubble glows | Phoneme-to-letter mapping with movement and sound. Gives a pre-reader a way to succeed |
| **Missing Letters** | All | The word is shown with the tricky part blanked (`?regular`). Choose from 4 options (`irr`, `ir`, `er`, `ur`) | Targets exactly the grapheme being taught that week. Distractors are the real confusions (ai/ay/a, tion/sion/cian, able/ible) |
| **Spot the Spelling** | All | Hear the word, then pick the correct spelling from 4. The wrong ones are realistic misspellings (necessery, recieve) | Trains visual memory of the correct form. In homophone weeks one distractor is the other homophone |
| **Word Jumble** | All | Put shuffled letter tiles in order. Wrongly placed letters turn red | Letter order and sequencing. Low pressure |
| **Homophone Hero** | Homophone weeks | A sentence with a gap; pick *their / there / they're*. A wrong answer shows how the other word is used | Grammar in context, which is where homophones are learned |
| **Friday Test** | All | Dictation with the on-screen keyboard. Marked at the end with a gentle letter-by-letter check | The real outcome measure, matching the paper test |

### Added in version 2

| Mode | Years | How it plays | Why it works |
|---|---|---|---|
| **Smart practice** | All | 10 words picked across every unlocked week, weighted towards words the child gets wrong or hasn't tried. Mixes Spot the Spelling, Missing Letters and Word Jumble | Adaptive practice. Words come back until they're secure, not just in the week they were taught |
| **Speed round** | Y2–6 best | 60 seconds: tap the correct spelling from 3, as many times as possible. Sets the child's **Speller status** | Builds instant recognition of the correct spelling. A personal-best target is very motivating |
| **Bubble Battle** | All | A 60-second race against 3 computer rivals who play at about the child's speed. Live race lanes show positions | The thrill of live competition, with no strangers and no internet needed |
| **Word map** | All | A heat map with one square per word for the whole year, coloured secure, getting there, tricky or not tried. Tap a square to hear the word | Children see their progress at a glance, and it leads straight into "Practise my tricky words" |

### More ideas for later

| Idea | Years | What it is |
|---|---|---|
| **Word Builder** | Y3–6 | Drag prefix + root + suffix tiles together (*un + help + ful*). Teaches morphology for the prefix/suffix and Greek/Latin weeks |
| **Rule Sorter** | Y2–6 | Sort words into baskets by rule: *-tion / -sion / -cian*, *-able / -ible*, "double the consonant or not" |
| **Sentence Doctor** | Y3–6 | Find and fix the misspelt or wrong word in a sentence. Proofreading, which is what KS2 SATs test |
| **Word Class Detective** | Y4–6 | Tag words in a sentence as noun, verb, adverb, preposition, conjunction. Uses the Y6 "grammar words" week |
| **Apostrophe Factory** | Y2–6 | Turn "the coats belonging to the girls" into *the girls' coats*. Covers possession and contraction |
| **Speedy Burst** | Y4–6 | Timed version of Spot the Spelling against the child's own best time. Off by default, never compared with others |
| **Boss Battle** | All | A Friday test framed as a friendly monster that loses a health bar for each right word |
| **Trace It** | Y1 | Trace letters with a finger to build handwriting and letter formation |
| **Two-Player Pass and Play** | All | Siblings take turns on one device, as a duel version of Bubble Battle |
| **Seasonal events** | All | A themed fortnight (for example "Spooky Spellings") with a special sticker and hat. Content ships with app updates, so no server is needed |
| **Word of the Day** | Y4–6 | One subject word (*photosynthesis*, *democracy*) with meaning, sentence and a quick quiz. Builds vocabulary, not only spelling |
| **Story Time** | Y1–3 | A short illustrated story using the week's words. Tap a word to hear it |

---

## 6. Gamification

### Ideas borrowed from Times Tables Rock Stars

Times Tables Rock Stars (TTRS) is the times-tables app many UK primary schools use. Families will recognise how it works, and children are already motivated by it. We borrow its **mechanics**, not its rock-music theme, names or art. Vocabursters keeps its own bubble world and characters.

| TTRS idea | Vocabursters version | Notes |
|---|---|---|
| Speed test that sets a "Rock Status" title | **Speed round** sets a **Speller status**: Bubble Blower → Fizzer → Popper → Splasher → Burster → Supersonic → Word Wizard → Spelling Legend | Based on seconds per right answer in 60 seconds. The next level always shows how many right answers it needs |
| Certificates for reaching a new status | **Certificate** card on level-up, kept in the Me tab | The full app can print them from the parent zone |
| Coins per right answer, spent on avatar items | **Coins** (1 per right answer, bonuses for tests, personal bests and battles), spent in the **shop** on hats, glasses, extras and backgrounds for the Burster pet | No real money, ever. Buying needs two taps so children don't spend by accident |
| Heat maps of each fact for children and teachers | **Word map** heat map in the child's app and the parent zone | Tap a square to hear the word |
| Live multiplayer games and leaderboards | **Bubble Battle** against computer rivals, plus a **family leaderboard** of players on the same device (coins this week, resets on Monday) | No online play with strangers. That keeps the no-login, no-data promise and the Children's Code simple |
| Questions that adapt to each child | **Smart practice** picks words from the child's own history | Uses the same per-word box as bounce-back words |
| Apps for phones and tablets | **Mobile version** (section 10) | Installable web app now. App-store versions via Capacitor are optional |

**What we do differently from TTRS:** there are no accounts or school logins, nothing about the child goes online, and timed games can be switched off by a parent. Speed suits some children and stresses others, so all the learning works without a timer.

### What the mockup does

- **Stars:** 1 to 3 per game per week, based on the share of words right first time. Finishing always earns at least 1 star.
- **Coins and the shop:** see the table above. 14 items in 4 slots, from 15 to 120 coins.
- **Speller status, certificates and Bubble Battle:** see the table above.
- **Burster pet:** a creature that hatches from an egg and grows through 5 stages as stars add up. New colours unlock along the way.
- **Sticker book:** 36 stickers per year, one per week, earned by finishing the Friday test. Each year has a theme (animals, sea, space, nature, food, sport).
- **Spelling trail:** 36 stops per year showing scores and stars, with "This week" highlighted.
- **Weekly goal:** play 3 games a week. We use a weekly goal instead of a daily streak so missing a day isn't a failure.
- **Bounce-back words:** missed words come back as a quick challenge.

**What we avoid on purpose**

- **Streaks that punish a missed day.** They cause guilt and nagging. The weekly goal resets quietly.
- **Leaderboards against children outside the family.** Children compare with their own past scores, computer rivals and, if they choose, brothers and sisters on the same device.
- **Variable-reward loot boxes**, timers that pressure, "come back or your pet will be sad" notifications, and anything bought with money.
- **Harsh failure sounds or red crosses on a first try.** Wrong answers get a soft sound and "Nearly! Try again".
- **Rewards for speed over accuracy in the learning games.** Speed only counts in the optional Speed round and Bubble Battle, and a parent can turn both off in Settings ("Timed games").

---

## 7. Features this age group needs

**Audio first**
- Every instruction and every word has a speaker button. A child who can't read can still play.
- Words and sentences are read by one recorded voice for every child, at a slightly slower speed (adjustable). Instructions use the device's own voice (British English where the device has one).
- The test reads word, sentence, word, as the PDF tells parents to do.
- **Recorded voice (done):** all 1,338 words and every example sentence are recorded with Kokoro's voice "Heart" (`af_heart`), so every child hears the same clear pronunciation. Heart was chosen by ear over all 8 British Kokoro voices, using 8 accent tests built from the word lists; the British voices sounded foreign (one was described as "Italian"). Heart has an American accent (short *a* in *bath*, a sounded *r*), but reads British spellings correctly (*draught* is said like *draft*, and *cheque*, *programme* and *pyjamas* come out right). Words spelt the same but said differently are fixed by hand (for example *lead* the metal). The clips are about 40 kbps MP3, a few KB each. Device speech stays as the fallback.

**The on-screen keyboard**
- A custom keyboard means **no autocorrect, predictive text or spell-check giving the answer away**. This is the most important integrity feature.
- ABC layout for Years 1–2, QWERTY for older children (the parent can change it).
- Large keys, a capital-letter key, apostrophe and hyphen keys when the year needs them, and é for *café*.
- A physical keyboard also works on computers.

**Reading and accessibility**
- **Andika** is the default font: a literacy font with the single-storey *a* and *g* children are taught to write. Lexend and Atkinson Hyperlegible are offered for children who find them easier, including some dyslexic readers.
- Text size options, light and dark mode, and calm mode (no bobbing, pulsing or confetti), which also follows the device's reduced-motion setting.
- Buttons are 52 to 72px tall. Keyboard keys are 52px tall and as wide as the screen allows (about 33px on a small phone, like a phone's own keyboard). Colour is never the only signal: ✓/✗ icons and words go with green and red.
- Screen reader labels on buttons, with a live region for feedback.

**Wellbeing**
- A brain-break reminder after 10 to 30 minutes (parent setting) suggests standing up, stretching and having a drink.
- Feedback praises effort ("Well done for trying!") as well as results.

**For parents (behind a grown-ups check)**
- Progress for each child: test history, average score, tricky words (most often wrong), bounce-back words.
- Set the year and current week, and lock weeks ahead.
- A printable paper test for any week, with a fold-over answer line. This keeps the paper routine.
- Several children on one device, each with their own picture, year and keyboard.
- Backup and restore by copying a code, for example to move to a new tablet.
- Install instructions for iPhone, Android and computers.

---

## 8. Privacy, safety and compliance

The app is for children, so it should meet the **UK Age Appropriate Design Code (Children's Code)** and **UK GDPR** from day one. The simplest way to do that is to **collect nothing**.

- All progress stays in the browser's storage on the device. No server, no accounts, no analytics by default.
- A child's name is a nickname typed by a parent and never leaves the device.
- No adverts, third-party trackers, external links in child screens, chat or user-generated content.
- The **grown-ups check** (a multiplication question) protects settings, deletion and backup. Before launch, consider a stronger check such as "type the number in words", since many Year 5–6 children can do the multiplication.
- A short, plain-English privacy notice in the app and on the website.
- If analytics are ever wanted, use an opt-in, cookieless, aggregate-only tool, and only after a Data Protection Impact Assessment.
- **Fonts are self-hosted (done).** The app never contacts Google Fonts, so no device IP addresses are sent to a third party, and the fonts work offline.
- Set a strict Content Security Policy and serve over HTTPS.

---

## 9. Technical plan

**Delivery: a Progressive Web App (PWA).** One codebase works on iPhone, iPad, Android, Chromebook, Windows and Mac. Parents install it from the browser with "Add to Home Screen". There's no app store review, no fees, and it works offline after the first visit.

| Area | Choice | Why |
|---|---|---|
| Framework | **Vite + TypeScript + Preact** (or Svelte) | Small bundle (fast on old tablets), typed data model, components for each game |
| Styling | CSS custom properties (design tokens, as in the mockup) | Light/dark and font switching in one place |
| Storage | **IndexedDB** (via `idb-keyval`) with a `localStorage` fallback | Survives longer than localStorage, holds audio caches. Ask for `navigator.storage.persist()` so the browser doesn't clear it |
| Offline | **Workbox** service worker: precache the app shell, word data, fonts and audio | Works on a plane or with no Wi-Fi |
| Speech | Pre-recorded audio clips (Opus/MP3, ~5 KB each, ~15 MB total, downloaded per year) + Web Speech API fallback | Consistent British pronunciation |
| Sound effects | Web Audio API tones (as in the mockup) | No files to download |
| Hosting | Static hosting: **GitHub Pages**, Netlify or Cloudflare Pages | Free, HTTPS, no server to secure |
| Testing | Vitest for the spelling engine; Playwright for every game end to end; axe for accessibility; Lighthouse PWA checks in CI | The mockup already has a Playwright drive-through of every game |

**Data model** (already used by the mockup)

```
words.json      { years: [ { year, wordsPerWeek, intro, weeks: [ { week, focus, words[] } ] } ] }
sentences.json  { "<word>": "<example sentence containing the word>" }
device state    { profiles: [ { id, name, avatar, year, week, kb, pet,
                                stars: { "<y>-<w>": { learn, burst, missing, spot, scramble, homophone, test } },
                                tests: [ { y, w, score, total, missed[], date } ],
                                words: { "<word>": { r, x, box, last } },   // right, wrong, Leitner box
                                review: [ "<word>" ], goal: { key, done },
                                coins, owned: [ "<itemId>" ], wear: { hat, eyes, neck, bg },
                                speed: { best, top, runs: [ { date, n, avg } ], reached: { "<statusIndex>": date } },
                                battles: { played, won }, wk: { key, coins } } ],   // wk = coins this week, for the family board
                  settings: { font, size, rate, voice, sfx, calm, breakMins, capitals, timed } }
```

**Spelling engine** (in the mockup, to be ported to TypeScript with unit tests)

- `findPattern(word, focus)` finds the part of the word that matches the week's focus (for example *dge* in *bridge*, *-tion* in *station*, *a-e* in *cake*). It falls back to double letters, then common tricky graphemes. Used for highlighting and for Missing Letters.
- `altsFor(pattern)` gives believable wrong options from a table of real confusions.
- `misspellings(word)` makes realistic wrong spellings (swapping ie/ei, dropping a double letter or silent letter, -able/-ible, vowel swaps, moving the apostrophe, a lowercase proper noun). It avoids producing other real words from the week.
- The current version was run over all 1,908 words without errors. Before launch, a teacher should review the generated distractors, or the best ones should be stored in the data file.
- **Spaced repetition:** each word has a Leitner box (1 to 5). A Friday-test mistake resets it to 1 and adds the word to bounce-back. Later, boxes can schedule review of words from earlier weeks.

**Performance budget:** under 200 KB of JavaScript and CSS, interactive in under 2 seconds on a 2018 budget Android tablet, and no network needed after install.

---

## 10. The mobile version

Most children will use Vocabursters on a parent's phone or a family tablet, so the app is designed for phones first. There are two ways to deliver it, and the first is already built.

### A. Installable web app (live on GitHub Pages)

The same code gives a different layout by screen size:

| | Phone (under 760px wide) | Tablet and computer |
|---|---|---|
| Navigation | **Bottom tab bar** (Home, Practise, Battle, Word map, Me) within thumb reach, clear of the iPhone home bar | The same five tabs as a floating bar at the top |
| Games | **Full screen**: no tab bar or header, just the progress bar and a ✕ button | Centred, up to 760px wide |
| Keyboard | **Docked to the bottom of the screen** like a real phone keyboard, with the Check/Next button above it | Under the question |
| Feedback | Sounds plus a **short vibration** for right and wrong answers (Android; iPhone browsers don't allow vibration) | Sounds |

Other mobile details:
- Safe areas for notches and the home bar.
- No double-tap zoom on game buttons.
- Pull-to-refresh is disabled so a swipe can't reload mid-game.
- Pop-up messages sit above the tab bar.
- The browser scrolls focused buttons clear of the tab bar.
- Dark mode follows the phone.
- Pinch-zoom still works for accessibility.

It installs from the browser (section 11) and works offline. Tested at iPhone size (390 × 844), iPad size (820 × 1180) and desktop size, in light and dark mode.

### B. App Store and Google Play versions (built, November 2026)

Some parents expect to find an app in the store, as they do for TTRS. The same app is wrapped in native iOS and Android projects with **Capacitor 8**, with no rewrite. The steps to sign, submit and list it are in [`STORE_RELEASE.md`](STORE_RELEASE.md), and the listing copy, form answers and screenshots are in [`store/`](../store/LISTING.md).

- **One build for each platform covers phones and tablets.** Phones are portrait-only, because games dock a keyboard at the bottom. iPads and Android tablets can turn either way.
- **Fully offline.** `python3 scripts/build.py --native` builds `native-www/` with every voice clip bundled, no service worker and no install prompts.
- **Native features** (in `app.html`, only active in the apps):
  - instructions are spoken by the system text-to-speech engine, which fixes Android's web view having no speech;
  - haptics on iPhone as well as Android;
  - the Android back button closes a game or goes back to Home instead of quitting;
  - the splash screen;
  - printing is replaced by a note to print from the website.
- **Builds:**
  - `.github/workflows/android.yml` builds an AAB and APKs on every push; when run by hand it signs them and can upload to a Play testing track.
  - `.github/workflows/ios.yml` builds for the simulator on every push; when run by hand it archives, signs and uploads to TestFlight. No Mac is needed.
  - The Android release AAB has been compiled here. The iOS build is checked by the macOS workflow.
- **Store rules for children's apps:** Apple's Kids Category and Google Play's Families Policy. There are no adverts, analytics, links out or purchases, and there is an adult check before the Grown-ups area. The listings declare **Data Not Collected** / no data collected.
- **Costs:** the Apple Developer Program is $99 a year and Google Play has a one-off $25 fee. New personal Play accounts need a 14-day closed test with 12 testers before production. Every update goes through store review, which the web app avoids.

---

## 11. How parents install it

1. Go to the web address (a short, memorable domain, plus a QR code on a printable flyer).
2. **iPhone/iPad:** Safari → Share → *Add to Home Screen*. **Android:** Chrome → ⋮ → *Install app*. **Computer:** the install icon in the address bar. The app shows these steps, and on Android and computers it can show an **Install** button.
3. Open it, tap **Add player**, type a nickname, pick a picture and the school year. That's all; there's no sign-up.
4. Optional: in the Grown-ups area, set the current week to match school and choose letter style and voice speed.

---

## 12. Content pipeline

1. `data/words.json` is the single source of truth (already done).
2. Add an example sentence for **every** word (182 of 1,338 done, covering all homophone and apostrophe weeks). Rules: 6 to 12 words, the word appears exactly once, the vocabulary suits the year, UK spelling, culturally neutral, no brands.
3. A teacher reviews the word lists against the DfE appendix, and reviews sentences and the generated distractors.
4. Record audio for each word and sentence with `scripts/generate_voice.py` (Kokoro, done for all current content; re-run after adding words, and only new clips are recorded). Files are named by a hash of the word.
5. Later: a short child-friendly meaning for the Y4–6 subject words, for Word of the Day.

`scripts/build.py` follows this pattern: the content files are inlined into the app at build time.

---

## 13. Roadmap

| Phase | What | Rough size |
|---|---|---|
| **0. Mockup** (done) | Clickable prototype with every game working on real data for all 6 years, the parent zone, stickers and the pet. Version 2 adds coins and shop, Speller status, Speed round, Bubble Battle, Word map, Smart practice and the mobile layout | — |
| **1. MVP** | Port to Vite + TypeScript. IndexedDB storage. Workbox offline. Self-hosted fonts. Sentences for every word. Unit tests for the spelling engine. Accessibility audit. Testing on real phones (cheap Android, older iPhone, iPad). Hosting and domain. Privacy notice | 5–7 weeks for one developer |
| **2. Quality** | A recorded British voice, if a better open-source one appears (a human recording is the other option). Illustrated avatars, pet and shop items (commissioned, original). Teacher content review. Word Builder and Rule Sorter. Spaced review of earlier weeks. **App Store and Google Play versions** via Capacitor, if wanted | 6–8 weeks |
| **3. Delight** | Sentence Doctor, Word Class Detective, Apostrophe Factory, Boss Battle, Trace It. More pet accessories. Optional backup by QR code between devices | Ongoing |

---

## 14. Measuring success without tracking

There are no analytics, so success shows up on the device and in conversations with families:

- In the parent zone: Friday scores over time, words moving out of bounce-back, games played each week.
- A small beta with 10–20 families: a short survey at weeks 2 and 6, and watching a few children use it (with parents present).
- Optional later: an opt-in "send anonymous feedback" button that the parent presses, which never runs automatically.

---

## 15. Decisions

**Decided (November 2026)**

1. **Name:** Vocabursters. Web address: https://richardawe.github.io/vocabursters/ (GitHub Pages, deployed on every push).
2. **Voice:** recorded with **Kokoro** (open-source, Apache 2.0), voice `af_heart` (American English, chosen by ear over the British voices), for every word and example sentence. Device voices are only a fallback, and still read instructions that contain a child's name.
3. **Capital letters:** gentle. A wrong capital counts as right, with a reminder. Parents can switch to strict in Settings.
4. **Price:** free.
5. **Content:** word lists and sentences have been checked, so the lists ship as they are (including Y6 W21).
6. **Delivery:** an installable web app from GitHub Pages, working on all devices.
7. **App stores:** also ship on the App Store and Google Play, for phones and tablets (section 10 and `STORE_RELEASE.md`).

**Still open**

8. **Timed games on or off by default.** The mockup has them on, and a parent can switch them off.
9. **Family leaderboard:** keep it, or make it opt-in per player. Some families prefer siblings not to compare.

---

## 16. Current status

**Working:** the phone layout (bottom tabs, full-screen games, docked keyboard, vibration) and tablet/desktop layout (top tabs); player profiles; the 36-week trail for each year with locking; all 7 weekly game modes on the real word lists for every week of every year; Smart practice; the Speed round with Speller status and certificates; Bubble Battle against computer rivals; the Word map heat map; coins and a 14-item shop; the family leaderboard; stars, the pet, the sticker book and the weekly goal; bounce-back words; the recorded Kokoro voice for every word and sentence, downloadable for offline use, with the device voice as a fallback; sound effects; the custom keyboard (and a physical keyboard); the parent zone (progress, players, settings, printable test, install steps, backup/restore); brain-break reminders; light and dark mode; calm mode; font and text-size options; an installable PWA on GitHub Pages with an offline service worker, self-hosted fonts and automatic updates; native iOS and Android apps (phone and tablet) with store icons, screenshots, a privacy policy, listing copy and build/upload workflows, ready to submit (not yet submitted).

**Simplified:** the app starts with no players. Example players "Mia" and "Leo" (with made-up history) appear only if a parent taps *Look around with example players*, and can be deleted in Grown-ups → Players. Bubble Battle rivals are computer players, not real children. Emoji stand in for commissioned illustrations. Only 182 of the 1,338 words have example sentences (all words in homophone and apostrophe weeks, plus Year 1 weeks 1–4). The grown-ups check is basic. Printing works in the app but not inside the claude.ai preview, which blocks printing.
