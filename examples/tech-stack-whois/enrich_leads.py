"""Enrich a list of company domains: CMS and tech stack, email provider, domain age, SSL and security grade.

Usage:
    python enrich_leads.py domains.txt          # one domain per line
    python enrich_leads.py stripe.com shopify.com
"""
import csv
import os
import sys
from pathlib import Path

from apify_client import ApifyClient

args = sys.argv[1:]
if len(args) == 1 and Path(args[0]).is_file():
    domains = [d.strip() for d in Path(args[0]).read_text(encoding="utf-8").splitlines() if d.strip()]
else:
    domains = args
if not domains:
    raise SystemExit("Pass domains or a text file with one domain per line.")

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/website-tech-dns-whois-ssl").call(run_input={
    "domains": domains,
    "checks": ["tech", "whois", "dns", "ssl", "hosting"],  # add "seo" and "performance" for audits
})

fields = ["domain", "cms", "ecommerce", "analytics", "email_provider", "hosting", "domain_age_years", "ssl_days_left", "security_grade", "technologies"]
with open("enriched.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for d in client.dataset(run.default_dataset_id).iterate_items():
        cats = d.get("technologiesByCategory") or {}
        whois = d.get("whois") or {}
        writer.writerow({
            "domain": d["domain"],
            "cms": ", ".join(cats.get("CMS", [])),
            "ecommerce": ", ".join(cats.get("Ecommerce", [])),
            "analytics": ", ".join(cats.get("Analytics", [])),
            "email_provider": (d.get("dns") or {}).get("emailProvider"),
            "hosting": (d.get("hosting") or {}).get("provider"),
            "domain_age_years": round(whois["ageDays"] / 365.25, 1) if whois.get("ageDays") else None,
            "ssl_days_left": (d.get("ssl") or {}).get("daysUntilExpiry"),
            "security_grade": (d.get("security") or {}).get("grade"),
            "technologies": ", ".join(d.get("technologyNames") or []),
        })
print("Saved enriched.csv")
