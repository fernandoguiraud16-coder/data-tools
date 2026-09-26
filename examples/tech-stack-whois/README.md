# Enrich company domains: tech stack, email provider, WHOIS and security

Turn a list of domains into a lead-enrichment CSV with the [Tech Stack Detector & WHOIS, SSL Checker](https://apify.com/fguiraud/website-tech-dns-whois-ssl) Actor: 7,000+ technologies, WHOIS/RDAP, DNS, email provider, hosting, SSL and a security grade. A BuiltWith / Wappalyzer alternative, priced per domain.

```bash
python enrich_leads.py domains.txt
```

Real `enriched.csv` (shortened):

| domain | cms | analytics | email_provider | hosting | domain_age_years | ssl_days_left | security_grade |
|---|---|---|---|---|---|---|---|
| wordpress.org | WordPress | | Self-hosted / other | WordPress.org | 23.5 | 88 | B |
| apify.com | | Leadfeeder, Mixpanel | Google Workspace | Amazon.com, Inc. | 17.3 | 113 | A |

## Use cases

- **Sales prospecting**: find companies on Shopify, HubSpot or a competitor's product.
- **Security and IT audits**: expiring SSL certificates, missing DMARC, weak security headers.
- **SEO audits**: add `"seo"` and `"performance"` to `checks` for titles, meta tags, robots.txt, sitemap and TTFB.

Full field reference: [`sample-output.json`](sample-output.json) and the [Actor page](https://apify.com/fguiraud/website-tech-dns-whois-ssl).
