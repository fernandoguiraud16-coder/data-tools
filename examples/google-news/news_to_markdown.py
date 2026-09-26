"""Search Google News and save every article as a Markdown file, ready for an LLM or a RAG index.

Usage:
    python news_to_markdown.py "AI regulation" --days 7 --max 20
"""
import argparse
import os
import re
from pathlib import Path

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("query", help='Google News search, operators allowed: "exact phrase", site:bbc.co.uk, -sports')
parser.add_argument("--days", type=int, default=7, choices=[1, 7, 30, 365])
parser.add_argument("--max", type=int, default=20, help="Max articles")
parser.add_argument("--country", default="US")
parser.add_argument("--language", default="en")
parser.add_argument("--out", default="articles")
args = parser.parse_args()

time_range = {1: "1d", 7: "7d", 30: "30d", 365: "1y"}[args.days]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/google-news-scraper").call(run_input={
    "queries": [args.query],
    "timeRange": time_range,
    "maxArticlesPerQuery": args.max,
    "fullText": True,
    "textFormat": "markdown",
    "country": args.country,
    "language": args.language,
})

out = Path(args.out)
out.mkdir(exist_ok=True)
saved = 0
for a in client.dataset(run.default_dataset_id).iterate_items():
    header = f"Source: {a.get('source')} | Published: {a.get('publishedAt', '')[:10]} | {a.get('url')}"
    if a.get("fullTextStatus") == "ok" and a.get("text"):
        slug = re.sub(r"[^a-z0-9]+", "-", a["title"].lower()).strip("-")[:60]
        (out / f"{slug}.md").write_text(f"<!-- {header} -->\n\n{a['text']}\n", encoding="utf-8")
        saved += 1
        print(f"[saved]   {a['title'][:80]}")
    else:
        # Paywalled or bot-protected sites: you still get title, source, date and the real URL.
        print(f"[{a.get('fullTextStatus', 'no text'):<8}] {a['title'][:80]}")

print(f"\n{saved} articles saved to ./{out}/")
