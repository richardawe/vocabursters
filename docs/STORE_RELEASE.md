# Releasing Vocabursters on the App Store and Google Play

This is the step-by-step guide to signing, submitting and listing the iOS and Android apps. The listing text, screenshots and form answers are in [`store/LISTING.md`](../store/LISTING.md).

**What's already done in the repo**

- `ios/` and `android/` are native Capacitor projects. They wrap the same app as the website, with every word recording bundled so they work offline.
- Phones are portrait-only. iPads and Android tablets can turn either way. One build covers phone and tablet on each platform.
- In the apps:
  - no install prompts or offline-download panel;
  - the system text-to-speech engine reads instructions (Android's web view has no speech of its own);
  - haptics work on iPhone too;
  - the Android back button closes a game or goes back to Home;
  - the print button is hidden, with a note to print from the website.
- Icons and splash screens are generated for every size, in light and dark.
- The privacy policy and support pages are in `app/site/` and published with the website.
- Store screenshots are in `store/screenshots/` for iPhone 6.9", iPad 13", Android phone and 7" and 10" tablets, plus the Play feature graphic.
- Two GitHub Actions workflows build the apps on every push:
  - `android.yml` builds an AAB and APKs;
  - `ios.yml` builds for the simulator.
  - Run either by hand to sign the build and upload it to the store.

**Two things to know first**

1. **You don't need a Mac.** The iOS workflow runs on GitHub's macOS machines. Without a Mac you can't run the iOS simulator yourself, so test on your own iPhone or iPad through TestFlight (step A6).
2. **New personal Google Play accounts can't publish straight to production.** Google requires a **closed test with at least 12 testers for 14 days in a row** first. Organisation accounts (which need a D-U-N-S number) skip this. Plan for about three weeks on Android.

---

## 0. Before either store (about 15 minutes)

1. **Put the privacy and support pages online.** The stores check these links.
   - Merge this branch into the branch GitHub Pages deploys from (`main` or `claude/eager-faraday-o2i1u5`, see `.github/workflows/pages.yml`).
   - Then check that https://richardawe.github.io/vocabursters/privacy.html and https://richardawe.github.io/vocabursters/support.html open.
2. **Decide on a support contact.** Both stores ask for a contact email, and Google shows it publicly.
   - Consider a separate address such as a new Gmail for the app.
   - If you want it on the support page, add it where `SUPPORT_CONTACT` is marked in `app/site/support.html`.
3. **Check the package name.** It is `app.vocabursters.spelling`, and it **can never change** after the first upload. To change it, edit `appId` in `capacitor.config.json`, then run `npx cap sync` (and update the bundle ID in Xcode / `android/app/build.gradle`).

---

## A. Apple App Store (iPhone and iPad)

### A1. Join the Apple Developer Program ($99 a year)
1. Go to https://developer.apple.com/programs/enroll/ and sign in with your Apple ID (turn on two-factor authentication).
2. Enrol as an **Individual** (quick; your own name shows as the seller) or as an **Organisation** (needs a D-U-N-S number; the company name shows).
3. Approval usually takes from a few hours to two days.
4. Once approved, open https://developer.apple.com/account → **Membership details** and copy your **Team ID** (10 characters).

### A2. Register the bundle ID
1. Go to https://developer.apple.com/account/resources/identifiers → **+** → **App IDs** → **App**.
2. Description: `Vocabursters`. Bundle ID: **Explicit**, `app.vocabursters.spelling`.
3. Leave every capability unticked → **Continue** → **Register**.

### A3. Create the app in App Store Connect
1. Go to https://appstoreconnect.apple.com → **Apps** → **+** → **New App**.
2. Fill in:
   - Platforms: **iOS**
   - Name: **Vocabursters** (if the name is taken, try "Vocabursters Spelling")
   - Primary language: **English (U.K.)**
   - Bundle ID: `app.vocabursters.spelling`
   - SKU: `vocabursters`
   - User access: **Full Access**

### A4. Create an App Store Connect API key (this lets GitHub sign and upload)
1. In App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → **Team Keys** → **+**.
2. Name it `GitHub Actions` and set Access to **Admin**. Admin is needed so the workflow can create the signing certificate and profile for you.
3. Download the `.p8` file. **You can only download it once**, so keep it safe.
4. Note the **Key ID** (next to the key) and the **Issuer ID** (at the top of the page).

### A5. Add the Apple secrets to GitHub
In the repo on GitHub, go to **Settings** → **Secrets and variables** → **Actions** → **New repository secret** and add:

| Secret | Value |
|---|---|
| `APPLE_TEAM_ID` | Team ID from A1 |
| `APP_STORE_CONNECT_KEY_ID` | Key ID from A4 |
| `APP_STORE_CONNECT_ISSUER_ID` | Issuer ID from A4 |
| `APP_STORE_CONNECT_KEY_P8` | The whole contents of the `.p8` file, including the `-----BEGIN PRIVATE KEY-----` lines |

### A6. Build, upload and test with TestFlight
1. Go to GitHub → **Actions** → **iOS app (App Store)** → **Run workflow**.
2. Choose the branch, set the version to `1.0.0` → **Run**. It takes about 10–15 minutes.
3. The build appears in App Store Connect → your app → **TestFlight** after 5–30 minutes of processing.
4. Under **Internal Testing**, create a group, add yourself, and install the **TestFlight** app on your iPhone and iPad. Play through the app on both devices:
   - add a player;
   - play each game;
   - check sound with the silent switch on and off;
   - check the Grown-ups area;
   - check backup and restore;
   - check portrait and landscape on the iPad.
5. Each run gets a new build number automatically. Run the workflow again after any fix.

### A7. Fill in the App Store listing
Under your app's **Distribution** tab → **iOS App 1.0**, use the copy in `store/LISTING.md`:
1. **Screenshots:**
   - iPhone 6.9" display: drag in `store/screenshots/ios-iphone-6.9in/`.
   - iPad 13" display: drag in `store/screenshots/ios-ipad-13in/`.
2. **Promotional text, Description, Keywords, Support URL, Marketing URL.**
3. **Build:** click **+** and choose the TestFlight build.
4. **General app information:** Copyright, and **Age Rating** (questionnaire in LISTING.md: all None, giving 4+). If you want the Kids Category, tick **Made for Kids** and choose **6–8**.
5. **App Review Information:** no sign-in required. Paste the review notes from LISTING.md, and add your phone number and email (only Apple sees these).
6. **Version release:** "Manually release this version" lets you pick the launch moment.

In the sidebar:
- **App Information:**
  - Category **Education** (secondary: **Word** or **Family**);
  - Content Rights: yes, has rights;
  - EU DSA trader status.
- **App Privacy:**
  - Privacy Policy URL;
  - **Get Started** → "No, we do not collect data" → **Publish**.
- **Pricing and Availability:**
  - Price **Free** (USD 0.00);
  - choose countries (all, or start with the UK).

### A8. Submit for review
1. Click **Add for Review** → **Submit to App Review**.
2. Review usually takes **1–2 days**. You'll get an email, and the status changes to "Ready for Distribution".
3. **If it's rejected**, the message says which guideline was broken. The likeliest one for an app built on web technology is **4.2 Minimum Functionality**. Reply in Resolution Center and point out that:
   - all content and audio is bundled, and the app works offline;
   - it uses native haptics and text-to-speech;
   - it is a complete educational product.

   Then resubmit.
4. Once approved, click **Release** (or it releases itself if you chose automatic). The app usually appears in search within 24 hours.

---

## B. Google Play (Android phones and tablets)

### B1. Create a Google Play developer account ($25 once)
1. Go to https://play.google.com/console/signup.
2. Choose **Yourself** (personal) or **An organisation** (needs a D-U-N-S number; skips the 12-tester rule).
3. Pay the $25 fee and complete **identity verification** (ID document). This can take a few days.
4. Verify a phone number and the contact email. Personal accounts also need an Android device in the Play Console mobile app to verify.

### B2. Make the upload key (one time, keep it forever)
Run this on any computer with Java installed (or Android Studio's terminal):
```sh
keytool -genkeypair -v -keystore vocabursters-upload.jks -alias upload \
  -keyalg RSA -keysize 4096 -validity 10000
```
- Choose a strong password and answer the name questions (anything sensible).
- **Back up `vocabursters-upload.jks` and the password** somewhere safe, such as a password manager. Never commit it; `.gitignore` already blocks `*.jks`.
- Google holds the real app-signing key (**Play App Signing**). If you lose this upload key, Google support can reset it.

### B3. Add the Android secrets to GitHub
Turn the key into text:
```sh
base64 -i vocabursters-upload.jks | tr -d '\n' > upload.b64     # macOS / Linux
# Windows PowerShell: [Convert]::ToBase64String([IO.File]::ReadAllBytes("vocabursters-upload.jks")) > upload.b64
```
Then add these repository secrets:

| Secret | Value |
|---|---|
| `ANDROID_KEYSTORE_BASE64` | Contents of `upload.b64` |
| `ANDROID_KEYSTORE_PASSWORD` | Keystore password |
| `ANDROID_KEY_ALIAS` | `upload` |
| `ANDROID_KEY_PASSWORD` | Key password (the same as the keystore password unless you set another) |

Delete `upload.b64` afterwards.

### B4. Build the signed release
1. Go to GitHub → **Actions** → **Android app (Google Play)** → **Run workflow** → version `1.0.0`.
2. When it finishes, download the artifact `vocabursters-android-…`. It contains:
   - `app-release.aab`: the file you upload to Google Play;
   - `app-release.apk`: a signed APK you can install directly on an Android phone or tablet to test (allow "install unknown apps" on the device).

### B5. Create the app in the Play Console
1. Go to **Create app**.
2. Fill in:
   - App name: **Vocabursters**
   - Default language: **English (United Kingdom) – en-GB**
   - **App** (not game)
   - **Free**
3. Tick the declarations and click **Create app**.

### B6. Complete "Set up your app" (Dashboard)
Work through each task with the answers in `store/LISTING.md`:
- **Privacy policy**
- **App access**: give the parental-gate instruction
- **Ads**: none
- **Content rating**: IARC questionnaire
- **Target audience and content**: 5 and under, 6–8, 9–12. This makes the Families Policy apply.
- **Data safety**: no data collected or shared
- **Government app**, **Financial features**, **Health**, **Advertising ID**: all No
- **Store settings**: category **Education**, contact email
- **Main store listing**:
  - name, short description and full description;
  - icon `store/google-play/icon-512.png`;
  - feature graphic `store/google-play/feature-graphic-1024x500.png`;
  - phone screenshots from `android-phone/`;
  - 7-inch tablet screenshots from `android-tablet-7in/`;
  - 10-inch tablet screenshots from `android-tablet-10in/`.

### B7. Testing tracks
1. **Internal testing** (instant, up to 100 testers):
   - Go to **Testing** → **Internal testing** → **Create new release**.
   - Accept **Play App Signing** when asked, upload `app-release.aab`, and enter the release notes.
   - Click **Save** → **Review release** → **Start rollout**.
   - On the **Testers** tab, add your own email, then open the opt-in link on your Android phone and tablet to install from Play.
2. **Closed testing**, required for new personal accounts:
   - Go to **Testing** → **Closed testing** → **Create track** (or use "Alpha").
   - Add **at least 12 testers** (a Google Group or a list of emails, such as family, friends or other parents), then upload the same AAB.
   - Testers must **opt in and keep the app installed for 14 days in a row**.
   - When 14 days are up, the Dashboard shows **Apply for production**. Answer the short questions about your testing.

### B8. Release to production
1. Go to **Production** → **Countries / regions**: add the United Kingdom (and others if you like).
2. Go to **Create new release** → **Add from library** (reuse the tested AAB) → release notes → **Review release** → **Send for review** / **Start rollout**.
3. The first review usually takes **from a few days to about a week**. Apps for children get extra checks under the Families Policy.
4. Once approved, the app goes live on the store. Search for it, or share `https://play.google.com/store/apps/details?id=app.vocabursters.spelling`.

### B9. Optional: let GitHub upload to Play for you
After the first manual upload (Google requires the first AAB to go in by hand):
1. In the Play Console, go to **Setup** → **API access** and link a Google Cloud project.
2. Create a **service account** in Google Cloud and download its **JSON key**.
3. Back in the Play Console, go to **Users and permissions**, invite the service account's email and give it the **Release apps to testing tracks** and **Release to production** permissions for Vocabursters.
4. Add the JSON contents as a GitHub secret named `PLAY_SERVICE_ACCOUNT_JSON`.
5. From then on, choose a **track** when you run the Android workflow and it uploads the AAB itself. Testing tracks go up as a draft for you to roll out.

---

## C. Releasing updates

1. Make the change in `app/src/app.html` (or the word data), then push.
2. Both workflows rebuild automatically. Download the Android APK artifact to try it.
3. Run **iOS app** and **Android app** by hand with a **higher version**, such as `1.0.1` or `1.1.0`. Build numbers go up automatically.
4. On iOS:
   - App Store Connect → **+ Version or Platform** → **iOS** → `1.0.1`;
   - pick the new build, write "What's new", and click **Add for Review**.
5. On Android:
   - **Production** → **Create new release** → upload the new AAB (or let the workflow do it, B9);
   - write release notes and click **Send for review**.
6. Screenshots only need updating if the app looks different. Run `npm run build:native && node scripts/store_screenshots.js`.

## D. Building on your own computer (optional)

```sh
npm ci
npm run android     # builds the app bundle, syncs it, opens Android Studio (Run ▶ on a phone or emulator)
npm run ios         # same for Xcode (Mac only); pick your Team under Signing & Capabilities, then Run ▶
```
- For a local signed Android release, put `storeFile`, `storePassword`, `keyAlias` and `keyPassword` in `android/keystore.properties` (ignored by git), then run `cd android && ./gradlew bundleRelease`.
- After changing icons, run `node scripts/make_store_icons.js && npm run assets`.

## E. Costs and timeline at a glance

| | Apple | Google |
|---|---|---|
| Fee | $99 a year | $25 once |
| Account approval | Hours to 2 days | A few days (ID check) |
| Testing before release | TestFlight, optional | 12 testers × 14 days (new personal accounts) |
| Review | 1–2 days | A few days to a week |
| Realistic time to live | About 1 week | About 3 weeks |
