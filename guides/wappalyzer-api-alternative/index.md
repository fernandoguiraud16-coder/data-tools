---
title: "Wappalyzer API alternative: bulk tech detection without credits"
description: "Detect website technologies in bulk through an API, pay $0.004 per domain with no monthly credits that expire. Includes DNS, SSL, hosting and SEO checks."
---

# A Wappalyzer API alternative for bulk lookups

Wappalyzer's browser extension is free, but its API comes with paid plans (Pro was listed at $250/month for 5,000 lookups in October 2026) and monthly credits. For occasional or bursty jobs, a pay-per-domain API avoids paying for unused credits.

## What you get

- Technology detection from HTML, scripts, headers, cookies, meta tags and DNS.
- Results grouped by category, with versions and confidence.
- Extra checks in the same call: DNS, SSL, HTTP security headers, hosting, SEO.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/website-tech-dns-whois-ssl").call(run_input={
    "domains": [
        "wordpress.org",
        "apify.com"
    ],
    "checks": [
        "tech"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["domain"], item.get("technologyNames"))
```

No Python? Open the [Actor page](https://apify.com/fguiraud/website-tech-dns-whois-ssl), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-01 (long values shortened):

```json
{
  "domain": "wordpress.org",
  "status": "ok",
  "technologies": [
    {
      "name": "WordPress",
      "version": "7.2",
      "confidence": 100,
      "detectedVia": [
        "website"
      ],
      "categories": [
        "CMS",
        "Blogs"
      ],
      "website": "https://wordpress.org"
    },
    {
      "name": "MySQL",
      "version": null,
      "confidence": 100,
      "detectedVia": [
        "implied"
      ],
      "categories": [
        "Databases"
      ],
      "website": "https://mysql.com"
    },
    {
      "name": "Google Font API",
      "version": null,
      "confidence": 100,
      "detectedVia": [
        "website"
      ],
      "categories": [
        "Font scripts"
      ],
      "website": "https://fonts.google.com/"
    },
    "..."
  ],
  "technologyNames": [
    "WordPress",
    "MySQL",
    "Google Font API",
    "..."
  ]
}
```

## Pricing

$0.004 per domain, no subscription or expiring credits.

## FAQ

**Is the output similar?**

Yes: name, version, confidence and categories per technology.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/website-tech-dns-whois-ssl` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Detect the tech stack of competitor websites](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/detect-competitor-tech-stack)
- [Monitor SSL and domain expiration dates](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/monitor-ssl-and-domain-expiration)
- [Check DNS records of many domains](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/check-dns-records-bulk)
- [On-page SEO check for many websites](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/seo-audit-website-list)
- [Find who hosts a website](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/find-website-hosting-provider)

## Related guides

- [BuiltWith alternative](https://fernandoguiraud16-coder.github.io/data-tools/guides/builtwith-alternative/)
- [Tech stack lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tech-stack-lookup-api/)
