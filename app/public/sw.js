// Vocabursters service worker: makes the app work offline and install as an app.
// __VERSION__ and __SHELL__ are filled in by scripts/build.py.
const VERSION = "__VERSION__";
const APP_CACHE = "vocabursters-app-" + VERSION;
const AUDIO_CACHE = "vocabursters-audio-v1";   // the recorded voice, kept across app updates
const SHELL = __SHELL__;

self.addEventListener("install", e => {
  e.waitUntil(caches.open(APP_CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k.startsWith("vocabursters-app-") && k !== APP_CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Safari asks for audio in byte ranges; answer from the cached file with a 206.
async function withRange(request, response) {
  const range = request.headers.get("range");
  if (!range || !response || response.status !== 200) return response;
  const buf = await response.arrayBuffer(), size = buf.byteLength;
  const m = /bytes=(\d*)-(\d*)/.exec(range) || [];
  let start = m[1] ? +m[1] : 0, end = m[2] ? Math.min(+m[2], size - 1) : size - 1;
  if (!m[1] && m[2]) { start = Math.max(0, size - +m[2]); end = size - 1; }
  return new Response(buf.slice(start, end + 1), {
    status: 206,
    headers: { "Content-Type": "audio/mpeg", "Content-Range": `bytes ${start}-${end}/${size}`, "Content-Length": String(end - start + 1), "Accept-Ranges": "bytes" }
  });
}

async function audio(request) {
  const url = request.url.split("#")[0];
  const cache = await caches.open(AUDIO_CACHE);
  let res = await cache.match(url);
  if (!res) {
    res = await fetch(url);                 // full file, no range, so it can be cached
    if (res.ok) await cache.put(url, res.clone());
  }
  return withRange(request, res);
}

async function networkFirst(request, fallbackKey) {
  const cache = await caches.open(APP_CACHE);
  try {
    const res = await fetch(request);
    if (res.ok) cache.put(fallbackKey || request, res.clone());
    return res;
  } catch (e) {
    return (await cache.match(fallbackKey || request)) || (await caches.match("index.html")) || Response.error();
  }
}

async function cacheFirst(request) {
  const hit = await caches.match(request);
  if (hit) return hit;
  const res = await fetch(request);
  if (res.ok) (await caches.open(APP_CACHE)).put(request, res.clone());
  return res;
}

self.addEventListener("fetch", e => {
  const { request } = e;
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  if (url.origin !== location.origin) return;
  if (request.mode === "navigate") return e.respondWith(networkFirst(request, "index.html"));
  if (url.pathname.endsWith("/audio/manifest.json")) return e.respondWith(networkFirst(request));
  if (url.pathname.includes("/audio/") && url.pathname.endsWith(".mp3")) return e.respondWith(audio(request));
  e.respondWith(cacheFirst(request));
});
