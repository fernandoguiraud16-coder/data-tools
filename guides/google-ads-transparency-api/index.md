---
title: "Google Ads Transparency Center API: all ads of a competitor"
description: "Get every Google ad of any advertiser or website domain from the Ads Transparency Center: text, image and YouTube ads with dates and regions. $0.0015 per ad."
---

# Google Ads Transparency Center API

The Ads Transparency Center shows every ad a company runs on Google, but only one at a time in a browser. This tool returns them as data: format, first and last shown, days running and preview links.

## What you get

- Search by advertiser name or by website domain.
- Filter by country, format (text, image, video) and platform (Search, YouTube, Play, Maps, Shopping).
- `onlyNewAds` for alerts when a competitor launches ads.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/google-ads-transparency-scraper").call(run_input={
    "advertisers": [
        "Nike"
    ],
    "region": "US",
    "maxAdsPerSearch": 100
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["advertiserName"], item["format"], item["firstShown"], item["daysRunning"])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/google-ads-transparency-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-01 (long values shortened):

```json
{
  "advertiserName": "Nike, Inc.",
  "creativeId": "CR16187970263927750657",
  "format": "text",
  "firstShown": "2022-11-30T16:32:33Z",
  "lastShown": "2026-10-01T02:09:50Z",
  "daysRunning": 1401,
  "adUrl": "https://adstransparency.google.com/advertiser/AR16735076323512287233/creative/CR16187970263927750657?region=US",
  "region": "US"
}
```

## Pricing

$0.0015 per ad; ad details $0.001 more.

| Tool | Price |
|---|---|
| This tool | $0.0015 per ad |
| scrapesage/google-ads-transparency-scraper | $0.002 + $0.003 details |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**Does it show ad spend?**

No; Google publishes spend only for political ads.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/google-ads-transparency-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [See all Google ads of a competitor](https://apify.com/fguiraud/google-ads-transparency-scraper/examples/see-all-google-ads-of-competitor)
- [Track new ads launched by competitors](https://apify.com/fguiraud/google-ads-transparency-scraper/examples/track-new-competitor-ads)
- [See a competitor's YouTube ads](https://apify.com/fguiraud/google-ads-transparency-scraper/examples/competitor-youtube-ads)
- [Google ads of a website (by domain)](https://apify.com/fguiraud/google-ads-transparency-scraper/examples/google-ads-by-website-domain)
- [Competitor display (image) ads](https://apify.com/fguiraud/google-ads-transparency-scraper/examples/competitor-image-display-ads)

## Related guides

- [Tech stack lookup API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tech-stack-lookup-api/)
- [Google Trends API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-trends-api-python/)
