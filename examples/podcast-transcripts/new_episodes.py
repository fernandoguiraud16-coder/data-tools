"""Transcribe the newest episodes of your favourite podcasts. Run it weekly: only new episodes are processed.

Usage:
    python new_episodes.py "Lex Fridman Podcast" "https://podcasts.apple.com/us/podcast/the-daily/id1200361736"
"""
import os
import re
import sys
from pathlib import Path

from apify_client import ApifyClient

podcasts = sys.argv[1:]
if not podcasts:
    raise SystemExit("Pass podcast names, Apple Podcasts links or RSS feed URLs.")

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/podcast-transcript-scraper").call(run_input={
    "podcastFeeds": podcasts,
    "maxEpisodesPerFeed": 1,
    "onlyNewEpisodes": True,  # episodes transcribed in earlier runs are skipped (and not charged)
    "model": "base",
    "outputs": ["text"],
})

out = Path("podcasts")
out.mkdir(exist_ok=True)
episodes = list(client.dataset(run.default_dataset_id).iterate_items())
if not episodes:
    print("No new episodes since the last run.")
for ep in episodes:
    if ep.get("status") != "ok":
        print(f"[{ep.get('status')}] {ep.get('episodeTitle')}: {ep.get('error')}")
        continue
    name = re.sub(r"[^A-Za-z0-9]+", "-", f"{ep['podcast']} {ep['episodeTitle']}")[:90].strip("-")
    (out / f"{name}.md").write_text(f"# {ep['episodeTitle']}\n\n{ep['podcast']}, {ep['published'][:10]}\n\n{ep['text']}\n", encoding="utf-8")
    print(f"[ok] {ep['podcast']}: {ep['episodeTitle'][:70]}")
