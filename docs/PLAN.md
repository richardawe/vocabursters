# Vocabursters: product plan

A spelling and grammar web app for Year 1 to Year 6 (ages 5 to 11), built from the *Weekly Vocabulary Tests: Y1 to Y6* lists. Parents install it on a phone, tablet or computer. There's no login, no account and no data leaves the device.

The playable mockup is in [`mockup/`](../mockup). Open `mockup/index.html` in a browser, or see the preview link in the README.

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
| **Two-Player Pass and Play** | All | Siblings take turns on one device. Cooperative, not competitive |
| **Word of the Day** | Y4–6 | One subject word (*photosynthesis*, *democracy*) with meaning, sentence and a quick quiz. Builds vocabulary, not only spelling |
| **Story Time** | Y1–3 | A short illustrated story using the week's words. Tap a word to hear it |

---

## 6. Gamification

**What the mockup does**

- **Stars:** 1 to 3 per game per week, based on the share of words right first time. Finishing always earns at least 1 star.
- **Burster pet:** a creature that hatches from an egg and grows through 5 stages as stars add up. New colours unlock along the way.
- **Sticker book:** 36 stickers per year, one per week, earned by finishing the Friday test. Each year has a theme (animals, sea, space, nature, food, sport).
- **Spelling trail:** 36 stops per year showing scores and stars, with "This week" highlighted.
- **Weekly goal:** play 3 games a week. We use a weekly goal instead of a daily streak so missing a day isn't a failure.
- **Bounce-back words:** missed words come back as a quick challenge.

**What we avoid on purpose**

- **Streaks that punish a missed day.** They cause guilt and nagging. The weekly goal resets quietly.
- **Leaderboards against other children.** Children compare with their own past scores only.
- **Variable-reward loot boxes**, timers that pressure, "come back or your pet will be sad" notifications, and anything bought with money.
- **Harsh failure sounds or red crosses on a first try.** Wrong answers get a soft sound and "Nearly! Try again".
- **Rewards for speed over accuracy.**

---

## 7. Features this age group needs

**Audio first**
- Every instruction and every word has a speaker button. A child who can't read can still play.
- Words are read in a British English voice where the device has one, at a slower default speed (adjustable).
- The test reads word, sentence, word, as the PDF tells parents to do.
- **For production:** record the 1,338 words and sentences with a real voice actor. Device voices vary a lot, and some mispronounce words or sound robotic. Device speech stays as the fallback.

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
- **Self-host the fonts** in production. Loading Google Fonts sends the device's IP address to Google. The mockup loads them from Google only for convenience.
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
                                review: [ "<word>" ], goal: { key, done } } ],
                  settings: { font, size, rate, voice, sfx, calm, breakMins, capitals } }
```

**Spelling engine** (in the mockup, to be ported to TypeScript with unit tests)

- `findPattern(word, focus)` finds the part of the word that matches the week's focus (for example *dge* in *bridge*, *-tion* in *station*, *a-e* in *cake*). It falls back to double letters, then common tricky graphemes. Used for highlighting and for Missing Letters.
- `altsFor(pattern)` gives believable wrong options from a table of real confusions.
- `misspellings(word)` makes realistic wrong spellings (swapping ie/ei, dropping a double letter or silent letter, -able/-ible, vowel swaps, moving the apostrophe, a lowercase proper noun). It avoids producing other real words from the week.
- The current version was run over all 1,908 words without errors. Before launch, a teacher should review the generated distractors, or the best ones should be stored in the data file.
- **Spaced repetition:** each word has a Leitner box (1 to 5). A Friday-test mistake resets it to 1 and adds the word to bounce-back. Later, boxes can schedule review of words from earlier weeks.

**Performance budget:** under 200 KB of JavaScript and CSS, interactive in under 2 seconds on a 2018 budget Android tablet, and no network needed after install.

---

## 10. How parents install it

1. Go to the web address (a short, memorable domain, plus a QR code on a printable flyer).
2. **iPhone/iPad:** Safari → Share → *Add to Home Screen*. **Android:** Chrome → ⋮ → *Install app*. **Computer:** the install icon in the address bar. The app shows these steps, and on Android and computers it can show an **Install** button.
3. Open it, tap **Add player**, type a nickname, pick a picture and the school year. That's all; there's no sign-up.
4. Optional: in the Grown-ups area, set the current week to match school and choose letter style and voice speed.

---

## 11. Content pipeline

1. `data/words.json` is the single source of truth (already done).
2. Add an example sentence for **every** word (182 of 1,338 done, covering all homophone and apostrophe weeks). Rules: 6 to 12 words, the word appears exactly once, the vocabulary suits the year, UK spelling, culturally neutral, no brands.
3. A teacher reviews the word lists against the DfE appendix, and reviews sentences and the generated distractors.
4. Record audio for each word and sentence (word on its own, then the sentence). Name files by a stable word ID.
5. Later: a short child-friendly meaning for the Y4–6 subject words, for Word of the Day.

`scripts/build_mockup.py` already shows the pattern: the content files are inlined into the app at build time.

---

## 12. Roadmap

| Phase | What | Rough size |
|---|---|---|
| **0. Mockup** (done) | Clickable prototype with every game working on real data for all 6 years, the parent zone, stickers and the pet | — |
| **1. MVP** | Port to Vite + TypeScript. IndexedDB storage. Workbox offline. Self-hosted fonts. Sentences for every word. Unit tests for the spelling engine. Accessibility audit. Hosting and domain. Privacy notice | 4–6 weeks for one developer |
| **2. Quality** | Recorded British voice. Illustrated avatars and pet (commissioned, original). Teacher content review. Word Builder and Rule Sorter. Spaced review of earlier weeks | 4–6 weeks |
| **3. Delight** | Sentence Doctor, Word Class Detective, Apostrophe Factory, Boss Battle, Trace It. More pet accessories. Optional backup by QR code between devices | Ongoing |

---

## 13. Measuring success without tracking

There are no analytics, so success shows up on the device and in conversations with families:

- In the parent zone: Friday scores over time, words moving out of bounce-back, games played each week.
- A small beta with 10–20 families: a short survey at weeks 2 and 6, and watching a few children use it (with parents present).
- Optional later: an opt-in "send anonymous feedback" button that the parent presses, which never runs automatically.

---

## 14. Decisions for you

1. **Name and web address.** "Vocabursters" is used as the working name.
2. **Voice:** pay for recorded audio in Phase 2 (recommended), or rely on device voices.
3. **Strict or gentle capitals** as the default for the test. The mockup defaults to gentle (counted right, with a reminder).
4. **Free, or a one-off paid version** for parents. Paid would need a purchase flow outside the child screens and a grown-ups check.
5. **Who reviews the content:** a teacher you know, or a paid reviewer.
6. **The Y6 W21 word list** (see section 2).

---

## 15. About the mockup

**Working:** player profiles; the 36-week trail for each year with locking; all 7 game modes on the real word lists for every week of every year; stars, the pet, the sticker book and the weekly goal; bounce-back words; reading aloud with the device voice; sound effects; the custom keyboard (and a physical keyboard); the parent zone (progress, players, settings, printable test, install steps, backup/restore); brain-break reminders; light and dark mode; calm mode; font and text-size options; installable PWA with an offline service worker (`mockup/index.html`).

**Simulated or simplified:** the example player "Mia" has made-up history so the screens aren't empty (delete her in Grown-ups → Players). Emoji stand in for commissioned illustrations. Only 182 of the 1,338 words have example sentences (all words in homophone and apostrophe weeks, plus Year 1 weeks 1–4). The grown-ups check is basic. Printing works from `mockup/index.html` but not inside the hosted preview, which blocks printing.
