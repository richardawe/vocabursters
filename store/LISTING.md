# Store listing copy and form answers

Copy and paste these into App Store Connect and the Google Play Console. The steps for where each one goes are in [`docs/STORE_RELEASE.md`](../docs/STORE_RELEASE.md).

| | |
|---|---|
| App name | **Vocabursters** |
| Bundle ID / package name | `app.vocabursters.spelling` (permanent once uploaded) |
| Privacy policy URL | https://richardawe.github.io/vocabursters/privacy.html |
| Support URL | https://richardawe.github.io/vocabursters/support.html |
| Marketing URL (optional) | https://richardawe.github.io/vocabursters/ |
| Price | Free, no in-app purchases, no adverts |
| Primary category | Education (both stores) |
| Copyright | 2026 followed by your name, or your company's name if you publish as a company |

---

## Text for both stores

**Subtitle (App Store, max 30 characters)**
```
Weekly spelling, Year 1 to 6
```

**Short description (Google Play, max 80 characters)**
```
Fun weekly spelling games for Year 1 to Year 6, with a recorded voice.
```

**Promotional text (App Store, max 170 characters, can change without review)**
```
Every weekly spelling list from Year 1 to Year 6, turned into quick games. No adverts, no accounts, no data collected. Works offline.
```

**Keywords (App Store, max 100 characters, comma-separated, no spaces)**
```
spelling,phonics,KS1,KS2,homework,primary,words,test,curriculum,homophones,school,learn,kids,English
```

**Full description (both stores, max 4000 characters)**
```
Vocabursters turns your child's weekly spelling list into short, friendly games. It covers every week of the National Curriculum in England spelling appendix, from Year 1 to Year 6: 216 weekly lists and over 1,300 words.

EVERY WEEK, SEVEN WAYS TO PLAY
• Look, Say, Cover, Write – the classic method, with the tricky part of each word highlighted
• Spot the Spelling – pick the right spelling from realistic mistakes
• Missing Letters, Word Scramble and more
• A Friday-style practice test, with words they found hard coming back later

HEAR EVERY WORD
Every word and example sentence is read aloud in a clear recorded voice. The recordings are inside the app, so it works without the internet.

STAYS MOTIVATING
• Stars, coins and a 14-item shop
• A pet that grows as your child plays
• A sticker book and a weekly goal
• Speed rounds with Speller levels and certificates
• Bubble Battle against friendly computer rivals
• A Word map that shows which words are secure

MADE FOR FAMILIES
• Up to several players on one device, each with their own year and week
• A Grown-ups area to set the school week, check progress and change settings
• Calm mode, dyslexia-friendly font choices, text size, and light or dark mode
• Brain-break reminders
• Back up progress with a code and move it to another device

PRIVATE BY DESIGN
No accounts, no adverts, no in-app purchases, no tracking and no chat. Progress is saved only on your device, and children's names never leave it. We collect no data at all.

Free, with no catches.
```

**What's new (first release)**
```
First release of Vocabursters on the App Store and Google Play.
```

---

## Screenshots (in `store/screenshots/`)

| Store slot | Folder | Size |
|---|---|---|
| App Store: iPhone 6.9" display | `ios-iphone-6.9in/` | 1320 × 2868 |
| App Store: iPad 13" display | `ios-ipad-13in/` | 2064 × 2752 |
| Google Play: Phone | `android-phone/` | 1080 × 2160 |
| Google Play: 7-inch tablet | `android-tablet-7in/` | 1200 × 1920 |
| Google Play: 10-inch tablet | `android-tablet-10in/` | 1600 × 2560 |
| Google Play: Feature graphic | `google-play/feature-graphic-1024x500.png` | 1024 × 500 |
| Google Play: App icon | `google-play/icon-512.png` | 512 × 512 |
| App Store: icon | Comes from the build; spare copy at `app-store-icon-1024.png` | 1024 × 1024 |

The order in each folder is: home, Look-Say-Cover-Write, Spot the Spelling, Bubble Battle, Word map, pet, Grown-ups progress. They use the example players "Mia" and "Leo". To retake them after changing the app, run `npm run build:native && node scripts/store_screenshots.js`.

---

## Apple: App Privacy ("nutrition label")

- **Do you or your third-party partners collect data from this app?** → **No, we do not collect data from this app.**
- Result shown on the store: **Data Not Collected**.

## Apple: Age rating questionnaire

Answer **None** or **No** to every item: violence, sexual content, profanity, horror, drugs, gambling, contests, unrestricted web access, user-generated content, messaging, advertising, medical and health. Expected rating: **4+**.

- **Made for Kids:** optional. If you choose it, pick the age band **6–8** (Apple allows one band). The app already meets the Kids Category rules: no adverts, no analytics, no links out, no purchases, and an adult check before the Grown-ups area. Once an app is in the Kids Category it must keep meeting those rules.

## Apple: other questions

- **Export compliance / encryption:** already answered in the app (`ITSAppUsesNonExemptEncryption = NO`), so App Store Connect won't ask.
- **Content rights:** "Yes, it contains third-party content, and I have the rights". The fonts are under the SIL Open Font Licence, and the voice was made with Kokoro under Apache 2.0.
- **EU Digital Services Act trader status:** a free app with no money involved and published as an individual is usually **not a trader**. If you publish as a business, choose **trader**, and your contact details will be shown in the EU.
- **Sign-in required?** No.

**App Review notes (paste into "Notes")**
```
Vocabursters is a free spelling practice app for children aged 5 to 11 (UK Years 1 to 6). No account or sign-in is needed: tap "Add player", type any nickname, choose a picture and a school year. Or tap "Look around with example players" to see the app with sample progress.

The Grown-ups area is behind a parental gate that asks a multiplication question (for example 7 × 14); type the answer to continue.

All content (216 weekly word lists, over 1,300 words and sentences, and their audio recordings) is bundled in the app and works fully offline. The app makes no network requests, collects no data, and has no adverts, purchases, external links or third-party SDKs. Native features used: haptic feedback, the system text-to-speech engine for spoken instructions, and the splash screen.
```

---

## Google Play: App content forms

| Form | Answer |
|---|---|
| Privacy policy | https://richardawe.github.io/vocabursters/privacy.html |
| App access | **All functionality is available without special access.** Add an instruction: "The Grown-ups area asks a multiplication question; type the answer to continue." |
| Ads | **No**, the app does not contain ads |
| Content rating (IARC) | Category: **Reference, News, or Educational**. Answer **No** to everything. Expected: PEGI 3 / Everyone / USK 0 |
| Target audience and content | Age groups: **5 and under**, **6–8** and **9–12** (Years 1 to 6 are ages 5 to 11). Appeal to children: yes. This puts the app under the **Families Policy**, which it already meets |
| Data safety | **Does your app collect or share any of the required user data types?** → **No**. Data encrypted in transit: not applicable (no data sent). Way to request deletion: not applicable (nothing collected; deleting the app deletes everything) |
| News app | No |
| Government app | No |
| Financial features | None |
| Health | None |
| Advertising ID | **No**, the app does not use an advertising ID |
| Teacher Approved (optional) | Opt in after launch, under Families → Teacher Approved |

**Store settings:** App category: **Education**. Tags: Education, Educational games, Language learning. Contact email: required, and shown publicly. **Countries:** start with the United Kingdom (the word lists follow England's curriculum), then add others if you like.
