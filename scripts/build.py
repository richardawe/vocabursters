"""Build Vocabursters into dist/ (what GitHub Pages serves).

  dist/index.html          the installable app: self-hosted fonts, manifest, offline service worker
  dist/preview.html        page body for the hosted claude.ai preview (Google-hosted fonts, no voice files)
  dist/sw.js               service worker, stamped with a content hash so updates reach devices
  dist/...                 everything from app/public (icons, fonts, recorded voice)
  dist/privacy.html, dist/support.html   from app/site (linked from the store listings)

  python3 scripts/build.py --native
  native-www/              what the App Store and Google Play apps bundle (Capacitor's webDir):
                           the same app plus capacitor.js, every voice clip, no service worker

Run from the repo root:  python3 scripts/build.py [--native]
"""
import hashlib
import json
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, PUBLIC, DIST = ROOT / "app/src/app.html", ROOT / "app/public", ROOT / "dist"
SITE = ROOT / "app/site"  # web-only pages: privacy policy and support (the store listings link to them)
NATIVE = ROOT / "native-www"

GOOGLE_FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Atkinson+Hyperlegible:wght@400;700&family=Grandstander:wght@600;800&family=Lexend:wght@400;600&display=swap">"""

HEAD = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Vocabursters">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style>
</head>
<body>
"""
TAIL = """
<script>
if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost")) {
  window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}
</script>
</body>
</html>
"""


def app_body():
    src = SRC.read_text(encoding="utf-8")
    words = json.loads((ROOT / "data/words.json").read_text(encoding="utf-8"))
    sentences = json.loads((ROOT / "data/sentences.json").read_text(encoding="utf-8"))
    compact = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    body = src.replace("__WORDS__", compact(words)).replace("__SENTENCES__", compact(sentences))
    assert "__WORDS__" not in body and "__SENTENCES__" not in body and "<!--FONTS-->" in body
    return body


def native():
    """The bundle inside the iOS and Android apps: works fully offline, no service worker or install prompts."""
    body = app_body()
    if NATIVE.exists():
        shutil.rmtree(NATIVE)
    shutil.copytree(PUBLIC, NATIVE, ignore=shutil.ignore_patterns("sw.js", "manifest.webmanifest"))
    core = ROOT / "node_modules/@capacitor/core/dist/capacitor.js"
    if not core.exists():
        sys.exit("Run npm install first (needs node_modules/@capacitor/core).")
    shutil.copy(core, NATIVE / "capacitor.js")
    fonts_css = (PUBLIC / "fonts/fonts.css").read_text(encoding="utf-8")
    head = (HEAD.replace('<link rel="manifest" href="manifest.webmanifest">\n', "")
            .replace('<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
                     '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<script src="capacitor.js"></script>'))
    assert "capacitor.js" in head
    (NATIVE / "index.html").write_text(head + body.replace("<!--FONTS-->", f"<style>\n{fonts_css}</style>") + "\n</body>\n</html>\n", encoding="utf-8")
    n_audio = len(list((NATIVE / "audio").rglob("*.mp3"))) if (NATIVE / "audio").exists() else 0
    size = sum(p.stat().st_size for p in NATIVE.rglob("*") if p.is_file())
    print(f"built native-www/: {n_audio} voice clips, {size / 1e6:.1f} MB in total")


def main():
    body = app_body()

    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(PUBLIC, DIST)
    shutil.copytree(SITE, DIST, dirs_exist_ok=True)
    fonts_css = (PUBLIC / "fonts/fonts.css").read_text(encoding="utf-8")  # urls are relative to index.html
    (DIST / "index.html").write_text(HEAD + body.replace("<!--FONTS-->", f"<style>\n{fonts_css}</style>") + TAIL, encoding="utf-8")
    (DIST / "preview.html").write_text(body.replace("<!--FONTS-->", GOOGLE_FONTS), encoding="utf-8")
    (DIST / ".nojekyll").write_text("", encoding="utf-8")

    shell = ["./", "index.html", "manifest.webmanifest", "icon.svg", "icon-192.png", "icon-512.png", "icon-maskable-512.png"]
    shell += sorted("fonts/" + p.name for p in (DIST / "fonts").glob("*.woff2"))
    if (DIST / "audio/manifest.json").exists():
        shell.append("audio/manifest.json")
    digest = hashlib.sha256()
    for p in sorted(DIST.rglob("*")):
        if p.is_file() and ("audio" not in p.parts or p.name == "manifest.json"):
            digest.update(p.name.encode()); digest.update(p.read_bytes())
    version = digest.hexdigest()[:10]
    sw = (PUBLIC / "sw.js").read_text(encoding="utf-8")
    sw = sw.replace("__VERSION__", version).replace("__SHELL__", json.dumps(shell))
    (DIST / "sw.js").write_text(sw, encoding="utf-8")

    n_audio = len(list((DIST / "audio").rglob("*.mp3"))) if (DIST / "audio").exists() else 0
    size = sum(p.stat().st_size for p in DIST.rglob("*") if p.is_file())
    print(f"built dist/ (version {version}): index.html {len((DIST / 'index.html').read_bytes()) // 1024} KB, "
          f"{n_audio} voice clips, {size / 1e6:.1f} MB in total")


if __name__ == "__main__":
    native() if "--native" in sys.argv else main()
