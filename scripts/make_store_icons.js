// Renders the source images that `npm run assets` turns into every iOS and Android icon and splash size.
// Run from the repo root:  node scripts/make_store_icons.js   (needs Playwright + Chromium)
const { chromium } = require("playwright");
const fs = require("fs");
const FACE = `
  <circle cx="256" cy="268" r="168" fill="#FFC53D" stroke="#17304A" stroke-width="20"/>
  <circle cx="200" cy="236" r="30" fill="#fff" stroke="#17304A" stroke-width="10"/>
  <circle cx="312" cy="236" r="30" fill="#fff" stroke="#17304A" stroke-width="10"/>
  <circle cx="206" cy="242" r="13" fill="#17304A"/>
  <circle cx="318" cy="242" r="13" fill="#17304A"/>
  <path d="M210 312q46 40 92 0" fill="none" stroke="#17304A" stroke-width="14" stroke-linecap="round"/>`;
const BUBBLE = `<circle cx="404" cy="104" r="40" fill="#CDEBFF" stroke="#17304A" stroke-width="10"/>
  <text x="404" y="120" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="46" fill="#17304A">a</text>`;
const svg = (body, bg) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">${bg ? `<rect width="512" height="512" fill="${bg}"/>` : ""}${body}</svg>`;
const out = {
  // iOS app icon and store icon: full square, no transparency (Apple rounds the corners)
  "icon-only.png": [1024, svg(`<g transform="translate(256 256) scale(0.92) translate(-256 -256)">${FACE}${BUBBLE}</g>`, "#E6F3EF")],
  // Android adaptive icon layers: the face sits inside the 66% safe zone
  "icon-foreground.png": [1024, svg(`<g transform="translate(256 262) scale(0.6) translate(-256 -268)">${FACE}</g>`)],
  "icon-background.png": [1024, svg("", "#E6F3EF")],
  // splash screens: a small face centred on the app background
  "splash.png": [2732, svg(`<g transform="translate(256 256) scale(0.22) translate(-256 -268)">${FACE}</g>`, "#E6F3EF")],
  "splash-dark.png": [2732, svg(`<g transform="translate(256 256) scale(0.22) translate(-256 -268)">${FACE}</g>`, "#0D1C22")],
};
(async () => {
  const browser = await chromium.launch();
  for (const [name, [size, markup]] of Object.entries(out)) {
    const page = await browser.newPage({ viewport: { width: size, height: size } });
    await page.setContent(`<html><body style="margin:0;background:transparent">${markup}</body></html>`);
    await page.screenshot({ path: `assets/${name}`, omitBackground: !markup.includes("<rect") });
    await page.close();
    console.log("assets/" + name);
  }
  await browser.close();
})();
