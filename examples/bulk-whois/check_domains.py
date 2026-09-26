"""Check a list of domains: which are available, which expire soon, and how old the rest are.

Usage:
    python check_domains.py domains.txt --expiring-days 60
"""
import argparse
import csv
import os
from pathlib import Path

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Text file with one domain per line")
parser.add_argument("--expiring-days", type=int, default=60)
args = parser.parse_args()

domains = [d.strip() for d in Path(args.file).read_text(encoding="utf-8").splitlines() if d.strip()]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/bulk-whois-domain-lookup").call(run_input={"domains": domains})
rows = list(client.dataset(run.default_dataset_id).iterate_items())

available = [r["domain"] for r in rows if r.get("registered") is False]
expiring = [r for r in rows if r.get("daysUntilExpiry") is not None and r["daysUntilExpiry"] <= args.expiring_days]

print(f"Checked {len(rows)} domains")
print(f"\nNot registered ({len(available)}):", *available, sep="\n  ")
print(f"\nExpiring within {args.expiring_days} days ({len(expiring)}):")
for r in sorted(expiring, key=lambda r: r["daysUntilExpiry"]):
    print(f"  {r['domain']:<30} {r['expiryDate'][:10]}  ({r['registrar']})")

with open("whois.csv", "w", newline="", encoding="utf-8") as f:
    cols = ["domain", "registered", "registrar", "createdDate", "expiryDate", "domainAgeYears", "daysUntilExpiry"]
    writer = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
print("\nFull results saved to whois.csv")
