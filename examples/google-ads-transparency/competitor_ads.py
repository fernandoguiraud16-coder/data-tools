"""See every Google ad a competitor runs, longest-running first, and save them to CSV.

Long-running ads are usually the ones that work, so they are the best place to start.

Usage:
    export APIFY_TOKEN=your_token      # Windows PowerShell: $env:APIFY_TOKEN="your_token"
    python competitor_ads.py "Notion" "clickup.com" --region US --max 200
"""
import argparse
import csv
import os

from apify_client import ApifyClient

ACTOR = "fguiraud/google-ads-transparency-scraper"

parser = argparse.ArgumentParser()
parser.add_argument("targets", nargs="+", help="Advertiser names, IDs (AR...) or domains (example.com)")
parser.add_argument("--region", default="US", help="2-letter country code, or empty for anywhere")
parser.add_argument("--format", default="all", choices=["all", "text", "image", "video"])
parser.add_argument("--max", type=int, default=100, help="Max ads per advertiser or domain")
parser.add_argument("--out", default="competitor_ads.csv")
args = parser.parse_args()

domains = [t for t in args.targets if "." in t and " " not in t]
advertisers = [t for t in args.targets if t not in domains]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor(ACTOR).call(run_input={
    "advertisers": advertisers,
    "domains": domains,
    "region": args.region,
    "adFormat": args.format,
    "maxAdsPerSearch": args.max,
})

ads = [a for a in client.dataset(run.default_dataset_id).iterate_items() if a.get("status") == "ok"]
ads.sort(key=lambda a: a.get("daysRunning") or 0, reverse=True)

print(f"{len(ads)} ads. Longest running:")
for a in ads[:10]:
    print(f"  {a['daysRunning']:5} days  {a['format']:5}  {a['advertiserName'][:30]:30}  {a['adUrl']}")

fields = ["advertiserName", "format", "firstShown", "lastShown", "daysRunning", "imageUrl", "previewUrl", "adUrl", "searchedBy"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(ads)
print(f"\nSaved to {args.out}")
