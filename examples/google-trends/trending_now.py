"""Print what people are searching for right now in one or more countries.

Usage:
    python trending_now.py US GB DE
"""
import os
import sys

from apify_client import ApifyClient

countries = sys.argv[1:] or ["US"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/google-trends-scraper").call(run_input={
    "searchTerms": [],
    "trendingNow": countries,
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("type") == "explore":
        continue
    print(f"{item['geo']}  #{item['rank']:<3} {item['query']:<35} {item.get('approxTraffic', '')}")
