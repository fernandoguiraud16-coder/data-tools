---
title: "python-whois alternative: bulk WHOIS that parses every TLD"
description: "Raw WHOIS text differs by registry and gets rate-limited. Bulk RDAP/WHOIS lookups with one clean schema for every TLD, from Python, $0.002 per domain."
---

# A python-whois alternative for bulk lookups

Libraries like `python-whois` query port 43 and parse free-text answers whose format changes from registry to registry, so fields come back empty for many country-code domains, and registries throttle repeated queries. This tool asks RDAP first (structured JSON published by the registries), falls back to WHOIS only when needed, and returns the same fields for every domain.

## What you get

- One schema for all TLDs: registrar, created/updated/expiry dates, age, days to expiry, status, nameservers, DNSSEC.
- `registered: false` for free domains.
- DNS, email provider, SPF/DMARC and optional SSL expiry in the same row.
- Thousands of domains per run.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/bulk-whois-domain-lookup").call(run_input={
    "domains": [
        "apify.com",
        "bbc.co.uk",
        "wordpress.org"
    ],
    "includeSsl": False
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["domain"], item.get("registered"), item.get("expiryDate"))
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
  "domainAgeDays": 6329,
  "whoisSource": "rdap"
}
```

## Pricing

$0.002 per domain.

## FAQ

**Does it return the raw WHOIS text?**

No, parsed fields only; `whoisSource` says whether RDAP or WHOIS answered.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/bulk-whois-domain-lookup` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Bulk WHOIS lookup for a list of domains](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/bulk-whois-lookup-domain-list)
- [Check domain expiration dates](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/check-domain-expiration-dates)
- [Check domain age in bulk](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/check-domain-age-bulk)
- [Check if domains are available](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/domain-availability-checker-bulk)
- [Find the registrar of many domains](https://apify.com/fguiraud/bulk-whois-domain-lookup/examples/find-domain-registrar-bulk)

## Related guides

- [Bulk WHOIS lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/bulk-whois-lookup-api/)
- [Monitor domain and SSL expiry](https://fernandoguiraud16-coder.github.io/data-tools/guides/domain-expiry-monitoring/)
