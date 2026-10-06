---
name: apify-domain-whois-intel
description: Look up domains and websites in bulk with Apify Actors - WHOIS/RDAP (registrar, creation and expiry dates, domain age, availability), DNS records (MX, SPF, DMARC, NS), SSL certificate expiry, hosting provider, technology stack (CMS, analytics, frameworks) and on-page SEO. Use when the user asks who owns or hosts a domain, when a domain expires, if a domain is available, how old a domain is, what technology a website uses, or to enrich a list of company domains.
author: Fernando Guiraud
author_url: https://github.com/fernandoguiraud16-coder
metadata:
  category: data-extraction
  keywords: "whois, rdap, domain, domain-age, domain-expiry, dns, ssl, tech-stack, builtwith, wappalyzer, hosting, seo, lead-enrichment"
---

# Domain and Website Intelligence

Check one or thousands of domains and return one row per domain.

Disclosure: the routed Actors are built and sold (pay per use) by the author of this skill.

## Example prompts

Prompts this skill handles:

- "When do these 300 domains expire, and which are already free?"
- "What CMS and analytics do these competitor websites use?"
- "Check SPF and DMARC for our client domains"

Out of scope (the boundary):

- Registering or buying domains.
- Personal data of domain owners (most registries redact it).

## Prerequisites

- Apify account ([sign up](https://apify.com)) and the Apify CLI (`npm install -g apify-cli`)
- Authentication: `apify login`, or the `APIFY_TOKEN` environment variable

## Actor routing

| User need | Actor ID | Price |
|-----------|----------|-------|
| WHOIS only: registrar, age, expiry, availability (optional SSL) | `fguiraud/bulk-whois-domain-lookup` | $0.002 per domain |
| Tech stack, DNS, SSL, hosting, HTTP, SEO, WHOIS | `fguiraud/website-tech-dns-whois-ssl` | $0.004 per domain |

Input: `domains` (list of domains or URLs). A link to a public Google Sheet or CSV works through `domainsFromUrl`.

## Workflow

1. Pick the Actor. WHOIS-only questions go to the cheaper one.
2. Build the input. Useful options:
   - `checks` (tech stack Actor): any of `tech`, `whois`, `dns`, `ssl`, `http`, `seo`, `performance`, `hosting`. Ask only for what is needed.
   - `alertDaysBeforeExpiry`: flags domains or certificates expiring within N days.
   - `monitorChanges: true` on a schedule reports what changed since the previous run.
   - `includeSsl: true` (WHOIS Actor) adds certificate expiry.
3. Run and fetch:

```bash
apify actors call fguiraud/bulk-whois-domain-lookup \
  -i '{"domains": ["wordpress.org", "apify.com"], "alertDaysBeforeExpiry": 60}' \
  --json --user-agent fguiraud-data-tools/apify-domain-whois-intel 2>/dev/null

apify datasets get-items DATASET_ID --format json \
  --user-agent fguiraud-data-tools/apify-domain-whois-intel 2>/dev/null
```

4. Deliver: one row per domain (`whois`, `dns`, `ssl`, `technologies`, `hosting`, `seo`, `alerts`). Domains that are not registered say so in their row. Summarize: expiring soon, available, by technology.

## Interfaces

- Apify CLI (above).
- MCP: `https://mcp.apify.com/?tools=fguiraud/bulk-whois-domain-lookup`, OAuth or `Authorization: Bearer <APIFY_TOKEN>`.

## Troubleshooting

- Some country-code registries give partial data: the row lists what was found and why the rest is missing (`errors`).
- Very large lists finish safely before the run timeout; skipped domains are marked and can be rerun.
