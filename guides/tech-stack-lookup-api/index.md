---
title: "Tech Stack Lookup API: what technology a website uses (bulk)"
description: "Detect the CMS, analytics, frameworks and 7,000+ technologies of a list of websites, plus hosting, DNS, SSL and SEO. BuiltWith and Wappalyzer alternative."
---

# Tech stack lookup API

Sales and research teams sort leads by the technology they use. Give a list of domains and get their technologies by category, with hosting, email provider and security grade.

## What you get

- Technologies with version and confidence, grouped by category (CMS, analytics, ecommerce...).
- Hosting provider, DNS, email provider, SSL, security headers grade, on-page SEO.
- `monitorChanges` to see when a competitor adds or drops a technology.

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
        "tech",
        "hosting",
        "dns"
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
  },
  "security": {
    "score": 78,
    "grade": "B",
    "checks": {
      "validCertificate": true,
      "modernTls": true,
      "tls13": true,
      "certificateNotExpiringSoon": true,
      "httpsRedirect": true,
      "hsts": true,
      "contentSecurityPolicy": false,
      "clickjackingProtection": true,
      "noSniff": false,
      "referrerPolicy": false,
      "spf": true,
      "dmarcEnforced": true,
      "caa": true,
      "dnssec": false
    }
  }
}
```

## Pricing

$0.004 per domain.

| Tool | Price |
|---|---|
| This tool | $0.004 per domain, tech + WHOIS + DNS + SSL + SEO |
| nexgendata/wappalyzer-replacement | $0.10 per detection |
| builtwith/builtwith-official | $0.002 per lookup |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**How is technology detected?**

From the home page HTML, headers, cookies, scripts and DNS records.

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
- [Monitor domain and SSL expiry](https://fernandoguiraud16-coder.github.io/data-tools/guides/domain-expiry-monitoring/)
