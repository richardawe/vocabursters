"""Record every spelling word and example sentence with Kokoro (open-source text-to-speech).

Output (committed, served with the app):
  app/public/audio/w/<id>.mp3      one clip per word
  app/public/audio/s/<id>.mp3      one clip per example sentence
  app/public/audio/manifest.json   { voice, model, w: {word: path}, s: {word: path} }

Kokoro-82M (https://huggingface.co/hexgrad/Kokoro-82M) is Apache-2.0 licensed. The model downloads
from Hugging Face on first run (~330 MB).

Setup (Kokoro needs Python 3.10-3.12, espeak-ng and ffmpeg):
  sudo apt-get install espeak-ng ffmpeg
  uv venv -p 3.12 .venv-voice
  VIRTUAL_ENV=.venv-voice uv pip install torch --index-url https://download.pytorch.org/whl/cpu
  VIRTUAL_ENV=.venv-voice uv pip install "kokoro>=0.9.4" soundfile pip
  export ESPEAK_DATA_PATH=/usr/lib/x86_64-linux-gnu/espeak-ng-data   # if Kokoro can't find espeak data
  .venv-voice/bin/python scripts/generate_voice.py            # only records clips that are missing
  .venv-voice/bin/python scripts/generate_voice.py --force    # re-record everything
"""
import concurrent.futures as cf
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

import numpy as np
import soundfile as sf
from kokoro import KPipeline

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "app/public/audio"
VOICE = "bf_emma"      # British English, female
SPEED = 0.9            # a little slower than conversational, for children

# Words spelt the same but said differently: say them the way the word list means them.
# Phonemes use Kokoro's (misaki) British notation.
OVERRIDES = {
    "lead": "[lead](/lˈɛd/)",   # the metal, paired with "led" in the Y3 homophone week
}


def spoken(text):
    """Text as Kokoro should read it."""
    for word, markup in OVERRIDES.items():
        text = __import__("re").sub(rf"(?<![\w']){word}(?![\w'])", markup, text)
    # plural possessives (girls') are read like the plain plural
    return __import__("re").sub(r"s'(?=\W|$)", "s", text)


def clip_id(word):
    return hashlib.sha1(word.encode("utf-8")).hexdigest()[:12]


def encode(wav_path, mp3_path):
    # trim silence at both ends, add a short pad, then a small mono MP3 that plays everywhere
    af = ("silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
          "silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
          "adelay=60,apad=pad_dur=0.12")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav_path), "-af", af,
                    "-ac", "1", "-ar", "24000", "-c:a", "libmp3lame", "-b:a", "40k", str(mp3_path)], check=True)


def main():
    force = "--force" in sys.argv
    words = json.loads((ROOT / "data/words.json").read_text(encoding="utf-8"))
    sentences = {k: v for k, v in json.loads((ROOT / "data/sentences.json").read_text(encoding="utf-8")).items() if not k.startswith("_")}
    all_words = sorted({w for y in words["years"] for wk in y["weeks"] for w in wk["words"]})

    jobs = [("w", w, w + ".") for w in all_words] + [("s", w, t) for w, t in sorted(sentences.items())]
    for kind in "ws":
        (OUT / kind).mkdir(parents=True, exist_ok=True)
    manifest = {"voice": VOICE, "model": "hexgrad/Kokoro-82M", "speed": SPEED, "w": {}, "s": {}}
    todo = []
    for kind, key, text in jobs:
        rel = f"audio/{kind}/{clip_id(key)}.mp3"
        manifest[kind][key] = rel
        if force or not (ROOT / "app/public" / rel).exists():
            todo.append((kind, key, text, ROOT / "app/public" / rel))
    print(f"{len(jobs)} clips in total, {len(todo)} to record")

    pipe = KPipeline(lang_code="b", repo_id="hexgrad/Kokoro-82M")
    tmp = pathlib.Path(tempfile.mkdtemp())
    with cf.ThreadPoolExecutor(4) as pool:
        futures = []
        for i, (kind, key, text, dest) in enumerate(todo, 1):
            audio = [r.audio.numpy() if hasattr(r.audio, "numpy") else np.asarray(r.audio)
                     for r in pipe(spoken(text), voice=VOICE, speed=SPEED) if r.audio is not None]
            if not audio:
                print("NO AUDIO:", kind, key); continue
            wav = tmp / f"{kind}-{dest.stem}.wav"
            sf.write(wav, np.concatenate(audio), 24000)
            futures.append(pool.submit(encode, wav, dest))
            if i % 100 == 0:
                print(f"  {i}/{len(todo)}")
        for f in futures:
            f.result()
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    size = sum(p.stat().st_size for p in OUT.rglob("*.mp3"))
    print(f"done: {len(manifest['w'])} words, {len(manifest['s'])} sentences, {size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
