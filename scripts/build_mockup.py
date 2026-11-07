"""Build the Vocabursters mockup.

Inlines data/words.json and data/sentences.json into mockup/src/app.html and writes:
  mockup/vocabursters.html  page body only (used for the hosted preview)
  mockup/index.html         full standalone page with PWA manifest + offline service worker

Run from the repo root:  python3 scripts/build_mockup.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "mockup/src/app.html").read_text(encoding="utf-8")
words = json.loads((ROOT / "data/words.json").read_text(encoding="utf-8"))
sentences = json.loads((ROOT / "data/sentences.json").read_text(encoding="utf-8"))

compact = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
body = src.replace("__WORDS__", compact(words)).replace("__SENTENCES__", compact(sentences))
assert "__WORDS__" not in body and "__SENTENCES__" not in body

(ROOT / "mockup/vocabursters.html").write_text(body, encoding="utf-8")

head = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Vocabursters">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style>
</head>
<body>
"""
tail = """
<script>
if ("serviceWorker" in navigator && location.protocol !== "file:") {
  window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}
</script>
</body>
</html>
"""
(ROOT / "mockup/index.html").write_text(head + body + tail, encoding="utf-8")
print("built mockup/vocabursters.html and mockup/index.html",
      f"({len(body.encode()) // 1024} KB)")
