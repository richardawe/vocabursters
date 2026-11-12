// Takes the App Store and Google Play screenshots from the app bundle (native-www/), plus the
// Google Play feature graphic and 512px icon. Run from the repo root after `npm run build:native`:
//   node scripts/store_screenshots.js        → store/screenshots/<device>/NN-name.png
const { chromium } = require("playwright");
const http = require("http"), fs = require("fs"), path = require("path");
const ROOT = path.resolve(__dirname, ".."), WWW = path.join(ROOT, "native-www"), OUT = path.join(ROOT, "store");
const TYPES = { ".html": "text/html", ".js": "text/javascript", ".json": "application/json", ".css": "text/css", ".svg": "image/svg+xml", ".png": "image/png", ".woff2": "font/woff2", ".mp3": "audio/mpeg" };

// [folder, CSS viewport width, height, scale] → pixel sizes the stores accept
const DEVICES = [
  ["ios-iphone-6.9in", 440, 956, 3],      // 1320 × 2868  (App Store: required iPhone size)
  ["ios-ipad-13in", 1032, 1376, 2],       // 2064 × 2752  (App Store: required iPad size)
  ["android-phone", 360, 720, 3],         // 1080 × 2160
  ["android-tablet-7in", 600, 960, 2],    // 1200 × 1920
  ["android-tablet-10in", 800, 1280, 2],  // 1600 × 2560
];

// A stand-in for the native bridge, so the bundle renders exactly as it does inside the apps.
const FAKE_NATIVE = () => {
  window.androidBridge = { postMessage() { } };
  const m = n => n.map(name => ({ name, rtype: "promise" }));
  window.Capacitor = {
    PluginHeaders: [{ name: "SplashScreen", methods: m(["hide"]) }, { name: "Haptics", methods: m(["impact", "notification"]) }, { name: "TextToSpeech", methods: m(["speak", "stop"]) }],
    nativePromise: () => Promise.resolve({}), nativeCallback: () => "0",
  };
};

const SHOTS = [
  ["01-home", async p => { await p.evaluate(() => go("map")); }],
  ["02-learn", async p => { await p.evaluate(() => startRound("learn")); }],
  ["03-spot", async p => { await p.evaluate(() => startRound("spot")); }],
  ["04-battle", async p => { await p.evaluate(() => go("battle")); }],
  ["05-wordmap", async p => { await p.evaluate(() => go("wordmap")); }],
  ["06-pet", async p => { await p.evaluate(() => go("pet")); }],
  ["07-grownups", async p => { await p.evaluate(() => go("parent", { tab: "progress" })); }],
];

(async () => {
  if (!fs.existsSync(path.join(WWW, "index.html"))) throw new Error("Run npm run build:native first");
  const server = http.createServer((q, r) => {
    const f = path.join(WWW, decodeURIComponent(q.url.split("?")[0]).replace(/\/$/, "/index.html"));
    fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { "content-type": TYPES[path.extname(f)] || "application/octet-stream" }); r.end(d); });
  }).listen(8766);
  const browser = await chromium.launch();
  for (const [name, w, h, scale] of DEVICES) {
    const dir = path.join(OUT, "screenshots", name); fs.mkdirSync(dir, { recursive: true });
    const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: scale, isMobile: true, hasTouch: true });
    await ctx.addInitScript(FAKE_NATIVE);
    const page = await ctx.newPage();
    await page.goto("http://localhost:8766/index.html");
    await page.click("#demo");                       // example players with made-up progress
    await page.waitForTimeout(300);
    await page.locator("[data-pick]").first().click();
    await page.waitForTimeout(300);
    for (const [shot, act] of SHOTS) {
      await act(page);
      await page.evaluate(() => { document.querySelectorAll(".toast").forEach(t => t.remove()); window.scrollTo(0, 0); });
      await page.waitForTimeout(400);
      await page.screenshot({ path: path.join(dir, shot + ".png") });
    }
    await ctx.close();
    console.log(`store/screenshots/${name}: ${SHOTS.length} at ${w * scale}×${h * scale}`);
  }
  // Google Play: 1024 × 500 feature graphic and 512 × 512 icon
  const icon = fs.readFileSync(path.join(ROOT, "assets/icon-only.png")).toString("base64");
  const page = await browser.newPage({ viewport: { width: 1024, height: 500 } });
  await page.goto("http://localhost:8766/index.html");   // same origin, so the bundled fonts load
  const fonts = fs.readFileSync(path.join(WWW, "fonts/fonts.css"), "utf8");
  await page.setContent(`<html><head><style>${fonts}
    body{margin:0;width:1024px;height:500px;background:#fff;display:flex;align-items:center;gap:48px;padding:0 64px;box-sizing:border-box;font-family:Grandstander,sans-serif;color:#17304A}
    img{width:300px;height:300px;border-radius:66px;flex:none}
    h1{font-size:84px;font-weight:800;margin:0;line-height:1}h1 span{color:#D9472A}p{font-family:Andika,sans-serif;font-size:34px;margin:18px 0 0;line-height:1.3}
  </style></head><body><img src="data:image/png;base64,${icon}"><div><h1>Vocab<span>ursters</span></h1><p>Weekly spelling games<br>for Year 1 to Year 6</p></div></body></html>`);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  fs.mkdirSync(path.join(OUT, "google-play"), { recursive: true });
  await page.screenshot({ path: path.join(OUT, "google-play/feature-graphic-1024x500.png") });
  await page.setViewportSize({ width: 512, height: 512 });
  await page.setContent(`<body style="margin:0"><img style="width:512px;height:512px;display:block" src="data:image/png;base64,${icon}"></body>`);
  await page.screenshot({ path: path.join(OUT, "google-play/icon-512.png") });
  fs.copyFileSync(path.join(ROOT, "assets/icon-only.png"), path.join(OUT, "app-store-icon-1024.png"));
  console.log("store/google-play: feature graphic and icon");
  await browser.close(); server.close();
})();
