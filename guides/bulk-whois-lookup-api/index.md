---
title: "Bulk WHOIS Lookup API: domain age, expiry and registrar"
description: "Look up thousands of domains at once: registrar, creation and expiry dates, domain age, availability, DNS, email provider and SSL expiry. $0.002 per domain."
---

# Bulk WHOIS lookup API

WHOIS websites throttle after a few dozen lookups and every registry formats WHOIS differently. This tool uses RDAP (structured JSON from the registries) with a WHOIS fallback and returns one clean row per domain.

## What you get

- Registrar, creation, update and expiry dates, age in days and years, days to expiry.
- Registered or not, status codes, nameservers, DNSSEC.
- MX records, email provider, SPF, DMARC; optional SSL expiry.
- Domain lists from a Google Sheet or CSV (`domainsFromUrl`).

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/bulk-whois-domain-lookup").call(run_input={
    "domains": [
        "apify.com",
        "wordpress.org",
        "bbc.co.uk"
    ],
    "includeSsl": True,
    "alertDaysBeforeExpiry": 60
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["domain"], item.get("registrar"), item.get("expiryDate"))
```

No Python? Open the [Actor page](https://apify.com/fguiraud/bulk-whois-domain-lookup), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-01 (long values shortened):

```json
{
  "domain": "apify.com",
  "status": "ok",
  "registered": true,
  "registrar": "Amazon Registrar, Inc.",
  "createdDate": "2009-06-02T17:14:10Z",
  "expiryDate": "2035-06-02T17:14:10Z",
  "domainAgeYears": 17.3,
  "daysUntilExpiry": 3166,
  "registrationStatus": [
    "client transfer prohibited"
  ],
  "nameservers": [
    "ns-1225.awsdns-25.org",
    "ns-1928.awsdns-49.co.uk",
    "ns-449.awsdns-56.com",
    "..."
  ],
  "emailProvider": "Google Workspace",
  "dmarcPolicy": "reject",
  "sslExpiryDate": "2027-01-16T23:59:59+00:00"
}
```

## Pricing

$0.002 per domain: 1,000 domains cost $2.

| Tool | Price |
|---|---|
| This tool | $0.002 per domain, with DNS, email and SSL |
| agenscrape/whois-domain-lookup | $0.0025 per domain |
| santamaria-automations/domain-whois-dns | $0.003 + $0.001 |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**How many domains per run?**

Thousands. Very large lists stop safely before the run timeout and mark the rest as skipped.

**Does it show the owner?**

Only when the registry publishes it; most redact personal data.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/bulk-whois-domain-lookup` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Bulk WHOIS lookup for a list of domains](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/bulk-whois-lookup-domain-list)
- [Check domain expiration dates](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/check-domain-expiration-dates)
- [Check domain age in bulk](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/check-domain-age-bulk)
- [Check if domains are available](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/domain-availability-checker-bulk)
- [Find the registrar of many domains](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/find-domain-registrar-bulk)

## Related guides

- [Monitor domain and SSL expiry](https://fernandoguiraud16-coder.github.io/data-tools/guides/domain-expiry-monitoring/)
- [Tech stack lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tech-stack-lookup-api/)
