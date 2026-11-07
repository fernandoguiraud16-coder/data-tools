---
title: "Domain age, hosting and email provider for Google Maps leads"
description: "Enrich Google Maps Scraper results with WHOIS: domain age, registrar, expiry date, hosting, email provider and Wayback Machine history of every business website. $0.002 per domain."
---

# Enrich Google Maps leads with domain data

A Google Maps scrape gives you businesses and their websites. Pass the run's dataset to Bulk WHOIS (`datasetId`) and every website gets its domain age, registrar, expiry date, hosting provider, email provider and the first capture of the site in the Wayback Machine. Old, well-kept domains point to established businesses; a domain that expires next month or a site that does not answer is a lead to treat differently.

## What you get

- `datasetId`: any dataset with a `website`, `domain` or `url` field (Google Maps, lead lists, CRM exports); links to the place on Google Maps or to social profiles are skipped.
- Domain age (`domainAgeYears`) and real age of the website (`waybackAgeYears`): in the sample, a café's domain was registered 3.3 years ago but its website has existed for 13.3 years.
- `includeHosting`, `includeHttpStatus`, `includeWayback`, `includeDkim`: same price.
- A SUMMARY record with the domains expiring soon and the top registrars.

Chain both runs from Python:

```python
places = client.actor("compass/crawler-google-places").call(run_input={"searchStringsArray": ["coffee shop"], "locationQuery": "Austin, Texas, USA", "maxCrawledPlacesPerSearch": 5})
run = client.actor("fguiraud/bulk-whois-domain-lookup").call(run_input={"datasetId": places.default_dataset_id, "includeHosting": True, "includeWayback": True})
```

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client (3.x)

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/bulk-whois-domain-lookup").call(run_input={
    "datasetId": "<DATASET_ID_OF_THE_GOOGLE_MAPS_RUN>",
    "includeHosting": True,
    "includeHttpStatus": True,
    "includeWayback": True
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["domain"], item.get("domainAgeYears"), item.get("hostingProvider"), item.get("emailProvider"))
```

No Python? Open the [Actor page](https://apify.com/fguiraud/bulk-whois-domain-lookup), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-11-07 (long values shortened):

```json
{
  "domain": "godsentcoffee.com",
  "input": "https://www.godsentcoffee.com/",
  "status": "ok",
  "registrar": "Squarespace Domains II LLC",
  "createdDate": "2023-07-23T06:26:50Z",
  "domainAgeYears": 3.3,
  "expiryDate": "2027-07-23T06:26:50Z",
  "hostingProvider": "Squarespace, Inc.",
  "emailProvider": null,
  "websiteStatus": 200,
  "waybackFirstCapture": "2013-07-18T10:01:46+00:00",
  "waybackAgeYears": 13.3
}
```

## Pricing

$0.002 per domain, with every option. Rows without a website are skipped and not billed.

## FAQ

**Does it return the owner of the domain?**

No. Since the GDPR, registries hide personal contact data; the registrar and dates are public.

**Can I use a CSV of websites instead?**

Yes: paste a link to the file or a Google Sheet in `domainsFromUrl`, or paste the rows in `datasetItems`.

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
- [Company emails from websites](https://fernandoguiraud16-coder.github.io/data-tools/guides/company-emails-from-websites/)
