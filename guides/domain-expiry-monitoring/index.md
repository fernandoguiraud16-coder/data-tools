---
title: "Monitor domain and SSL certificate expiry (scheduled alerts)"
description: "Track domain and SSL certificate expiry dates for a list of domains on a schedule and get alerts N days before. DNS and registrar changes included."
---

# Monitor domain and SSL expiry

An expired domain or certificate takes a site down. Schedule this check daily or weekly and the result lists what expires soon and what changed.

## What you get

- `alertDaysBeforeExpiry` flags domains and certificates expiring within N days.
- `monitorChanges: true` reports registrar, DNS, nameserver and certificate changes since the last run.
- One row per domain with WHOIS, DNS and SSL.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/website-tech-dns-whois-ssl").call(run_input={
    "domains": [
        "wordpress.org",
        "apify.com",
        "bbc.co.uk"
    ],
    "checks": [
        "whois",
        "ssl",
        "dns"
    ],
    "alertDaysBeforeExpiry": 30,
    "monitorChanges": True
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["domain"], item.get("alerts"))
```

No Python? Open the [Actor page](https://apify.com/fguiraud/website-tech-dns-whois-ssl), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-01 (long values shortened):

```json
{
  "domain": "wordpress.org",
  "status": "ok",
  "whois": {
    "registrar": "MarkMonitor Inc.",
    "registrarIanaId": "292",
    "created": "2003-03-28T01:07:35.665Z",
    "updated": "2026-08-12T03:29:29.463Z",
    "expires": "2035-03-28T01:07:35.665Z",
    "ageDays": 8588,
    "daysUntilExpiry": 3099,
    "status": [
      "client delete prohibited",
      "client transfer prohibited",
      "client update prohibited"
    ],
    "nameservers": [
      "ns1.wordpress.org",
      "ns2.wordpress.org",
      "ns3.wordpress.org",
      "..."
    ],
    "dnssec": false,
    "source": "rdap"
  },
  "ssl": {
    "valid": true,
    "error": null,
    "subject": "wordpress.org",
    "issuer": "Let's Encrypt",
    "validFrom": "2026-09-23T19:43:58+00:00",
    "validTo": "2026-12-22T19:43:57+00:00",
    "daysUntilExpiry": 82,
    "sans": [
      "*.wordpress.org",
      "wordpress.org"
    ],
    "sanCount": 2,
    "tlsVersion": "TLSv1.3",
    "cipher": "TLS_AES_128_GCM_SHA256"
  },
  "alerts": []
}
```

## Pricing

$0.004 per domain per run (only the checks you choose run).

## FAQ

**How do I get an email?**

Schedule the run in Apify and add a notification, or send the results to Slack or email with Make, n8n or Zapier.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/website-tech-dns-whois-ssl` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Detect the tech stack of competitor websites](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/detect-competitor-tech-stack)
- [Monitor SSL and domain expiration dates](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/monitor-ssl-and-domain-expiration)
- [Check DNS records of many domains](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/check-dns-records-bulk)
- [On-page SEO check for many websites](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/seo-audit-website-list)
- [Find who hosts a website](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/find-website-hosting-provider)

## Related guides

- [Bulk WHOIS lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/bulk-whois-lookup-api/)
- [Tech stack lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tech-stack-lookup-api/)
