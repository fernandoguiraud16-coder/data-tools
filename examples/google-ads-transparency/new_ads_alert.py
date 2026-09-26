"""Competitor ad alerts: print only the Google ads launched since the last run.

Run it weekly (cron, Task Scheduler, or an Apify schedule on the Actor itself).
The Actor remembers which ads it already returned, so you only pay for new ones.

Usage:
    python new_ads_alert.py "competitor one" competitor-two.com --region US
"""
import argparse
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("targets", nargs="+", help="Advertiser names, IDs (AR...) or domains")
parser.add_argument("--region", default="US")
args = parser.parse_args()

domains = [t for t in args.targets if "." in t and " " not in t]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/google-ads-transparency-scraper").call(run_input={
    "advertisers": [t for t in args.targets if t not in domains],
    "domains": domains,
    "region": args.region,
    "maxAdsPerSearch": 500,
    "onlyNewAds": True,  # skip ads returned by earlier runs
})

new_ads = [a for a in client.dataset(run.default_dataset_id).iterate_items() if a.get("status") == "ok"]
if not new_ads:
    print("No new ads since the last run.")
for a in new_ads:
    print(f"- {a['advertiserName']}: new {a['format']} ad, first shown {a['firstShown'][:10]}\n  {a['adUrl']}")

# Send `new_ads` to Slack, email or a webhook here.
