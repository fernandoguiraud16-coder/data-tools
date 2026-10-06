---
title: "BuiltWith alternative: pay per domain instead of a monthly plan"
description: "Check the technology stack of your own list of domains for $0.004 each, with hosting, DNS, SSL and WHOIS, instead of a BuiltWith subscription."
---

# A pay-per-domain BuiltWith alternative

BuiltWith is the reference for technology lookups, and its paid plans start at a few hundred dollars a month (Basic was listed at $295/month in October 2026). That fits teams that need its database of sites by technology. If you already have a list of domains and need to know what they run, paying per domain costs far less.

## What you get

- 7,000+ technology fingerprints with version and category.
- Hosting provider, DNS, email provider, SSL, security grade, on-page SEO and WHOIS in the same row.
- Lists from a Google Sheet or CSV link; `monitorChanges` for recurring checks.

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
        "tech",
        "hosting",
        "whois"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["domain"], item.get("technologiesByCategory"))
```

No Python? Open the [Actor page](https://apify.com/fguiraud/website-tech-dns-whois-ssl), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-01 (long values shortened):

```json
{
  "domain": "wordpress.org",
  "status": "ok",
  "technologyNames": [
    "WordPress",
    "MySQL",
    "Google Font API",
    "..."
  ],
  "technologiesByCategory": {
    "Blogs": [
      "WordPress"
    ],
    "CMS": [
      "WordPress"
    ],
    "Databases": [
      "MySQL"
    ],
    "Editors": [
      "Gutenberg"
    ],
    "Font scripts": [
      "Google Font API"
    ],
    "Miscellaneous": [
      "Open Graph",
      "RSS"
    ],
    "Page builders": [
      "WordPress Block Editor",
      "WordPress Site Editor"
    ],
    "Performance": [
      "Priority Hints"
    ],
    "Programming languages": [
      "PHP"
    ],
    "Reverse proxies": [
      "Nginx"
    ],
    "Security": [
      "HSTS"
    ],
    "Tag managers": [
      "Google Tag Manager"
    ],
    "Web servers": [
      "Nginx"
    ],
    "WordPress plugins": [
      "Gutenberg"
    ]
  },
  "hosting": {
    "ip": "66.6.42.252",
    "provider": "WordPress.org",
    "network": "WORDPRESS-ORG",
    "country": null,
    "cidr": "66.6.42.0/24"
  }
}
```

## Pricing

$0.004 per domain: 1,000 domains cost $4.

## FAQ

**Can it find all sites that use a technology?**

No. It checks the domains you give it; BuiltWith-style "all sites using X" lists need their database.

**How fresh is the data?**

Live: each run fetches the site at that moment.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/website-tech-dns-whois-ssl` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Detect the tech stack of competitor websites](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/detect-competitor-tech-stack)
- [Monitor SSL and domain expiration dates](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/monitor-ssl-and-domain-expiration)
- [Check DNS records of many domains](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/check-dns-records-bulk)
- [On-page SEO check for many websites](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/seo-audit-website-list)
- [Find who hosts a website](https://apify.com/fguiraud/website-tech-dns-whois-ssl/examples/find-website-hosting-provider)

## Related guides

- [Tech stack lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tech-stack-lookup-api/)
- [Wappalyzer API alternative](https://fernandoguiraud16-coder.github.io/data-tools/guides/wappalyzer-api-alternative/)
