"""Download the app's fonts (Latin subset, woff2) so the app never calls Google Fonts.

Writes app/public/fonts/*.woff2 and app/public/fonts/fonts.css.
Run once from the repo root:  python3 scripts/fetch_fonts.py
All four families are under the SIL Open Font License 1.1 (see app/public/fonts/LICENSE.md).
"""
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "app/public/fonts"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
URL = ("https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Atkinson+Hyperlegible:wght@400;700"
       "&family=Grandstander:wght@600;800&family=Lexend:wght@400;600&display=swap")


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read()


css = get(URL).decode()
blocks = re.findall(r"/\* latin \*/\s*@font-face\s*{([^}]*)}", css)
out, seen = [], {}
for b in blocks:
    fam = re.search(r"font-family:\s*'([^']+)'", b).group(1)
    weight = re.search(r"font-weight:\s*(\d+)", b).group(1)
    src = re.search(r"url\(([^)]+\.woff2)\)", b).group(1)
    urange = re.search(r"unicode-range:\s*([^;]+);", b).group(1)
    if src not in seen:
        name = fam.lower().replace(" ", "-") + "-" + str(len([v for v in seen.values() if v.startswith(fam.lower().replace(" ", "-"))])) + ".woff2"
        (OUT / name).write_bytes(get(src))
        seen[src] = name
    out.append(f"@font-face {{ font-family: '{fam}'; font-style: normal; font-weight: {weight}; font-display: swap; "
               f"src: url(fonts/{seen[src]}) format('woff2'); unicode-range: {urange}; }}")
(OUT / "fonts.css").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"{len(out)} faces, {len(seen)} files:", ", ".join(sorted(seen.values())))
