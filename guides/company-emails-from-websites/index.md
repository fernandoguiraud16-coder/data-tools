---
title: "Find company emails, phones and social profiles from a list of websites"
description: "Turn a list of company websites into role emails (info@, sales@, support@), phone numbers, address, contact page and LinkedIn, Instagram and X profiles, one row per company. Business contacts only."
---

# Company emails and phones from websites

Prospecting lists usually start as a column of company domains. This tool reads each website (home page plus up to two contact, about or legal pages) and returns the business contact details the company publishes: role emails, phone numbers, postal address, contact page and official social profiles. Emails that name a person are never collected, so the output is company data, not a list of individuals.

## What you get

- Role emails only: info@, sales@, support@, hello@, press@ and similar; obfuscated "name [at] domain [dot] com" addresses are decoded.
- Phones from `tel:` links and schema.org data, digits only with `+` for international numbers.
- Company name and postal address from the site's structured data.
- LinkedIn company page, Facebook, Instagram, X, YouTube and TikTok profiles.
- Paste domains, URLs or a Google Sheet link; one row per company, ready for a CRM.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/website-contact-scraper").call(run_input={
    "domains": [
        "apify.com",
        "buffer.com",
        "hubspot.com"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["domain"], item["status"], item["emails"], item["phones"][:2], item.get("linkedin"))
```

No Python? Open the [Actor page](https://apify.com/fguiraud/website-contact-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-17 (long values shortened):

```json
{
  "domain": "apify.com",
  "status": "ok",
  "companyName": "Apify",
  "emails": [
    "support@apify.com",
    "hello@apify.com"
  ],
  "phones": [],
  "address": "Na Příkopě 959/27, 11000, Prague, CZ",
  "contactPageUrl": "https://apify.com/contact",
  "linkedin": "http://linkedin.com/company/apify",
  "x": "https://x.com/apify",
  "pagesChecked": [
    "https://apify.com/",
    "https://apify.com/contact",
    "https://apify.com/contact-sales"
  ]
}
```

## Pricing

$0.003 per website with contacts. Websites without contacts or that cannot be reached are not charged.

## FAQ

**Why are some websites empty?**

Sites that build their pages with JavaScript or block automated visitors show no contacts to a plain HTTP request; they return `no-contacts` and are not charged.

**Why no personal emails?**

An address that names a person is personal data under laws such as the GDPR; the tool keeps only role addresses a company publishes for contact.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/website-contact-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Company emails from a list of websites](https://apify.com/fguiraud/website-contact-scraper/examples/company-emails-from-a-list-of-websites)

## Related guides

- [Bulk WHOIS lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/bulk-whois-lookup-api/)
- [Tech stack lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tech-stack-lookup-api/)
