"""Transcribe audio or video files to text and SRT subtitles.

Usage:
    python transcribe.py https://example.com/interview.mp3 --model base
    python transcribe.py https://example.com/talk.mp4 --task translate   # any language -> English
"""
import argparse
import os
import re
from pathlib import Path

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("urls", nargs="+", help="Direct links to audio/video files (mp3, m4a, wav, mp4, webm...)")
parser.add_argument("--model", default="base", choices=["tiny", "base", "small"], help="small = most accurate")
parser.add_argument("--task", default="transcribe", choices=["transcribe", "translate"])
parser.add_argument("--vocabulary", default="", help="Names and jargon to spell correctly, e.g. 'Apify, Kubernetes'")
args = parser.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/audio-video-transcriber").call(run_input={
    "sources": [{"url": u} for u in args.urls],
    "model": args.model,
    "task": args.task,
    "vocabulary": [w.strip() for w in args.vocabulary.split(",") if w.strip()],
    "outputs": ["text", "srt"],
})

out = Path("transcripts")
out.mkdir(exist_ok=True)
for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("status") != "ok":
        print(f"[{item.get('status')}] {item['source']}: {item.get('error')}")
        continue
    name = re.sub(r"[^A-Za-z0-9.-]+", "_", item["source"].rsplit("/", 1)[-1])[:60]
    (out / f"{name}.txt").write_text(item["text"], encoding="utf-8")
    (out / f"{name}.srt").write_text(item["srt"], encoding="utf-8")
    print(f"[ok] {name}: {item['durationSeconds'] / 60:.1f} min, language {item['language']}")
