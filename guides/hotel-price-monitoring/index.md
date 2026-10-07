---
title: "Hotel price monitoring: daily price changes from Google Hotels"
description: "Track hotel prices every day for your dates: see which hotels got cheaper or more expensive since the last check, and get only the ones whose price moved."
---

# Daily hotel price monitoring

Revenue managers, travel agents and travelers watch competitor and destination prices every day. Schedule this tool daily: it remembers each hotel price for the same search and adds the change since the previous run.

## What you get

- `previousPricePerNight`, `priceChange`, `priceChangePercent` and `priceStatus` (down, up, unchanged, new).
- "Only hotels whose price changed" returns, and charges, only the hotels that moved.
- Same search = same location, dates, guests, currency and filters, so several monitors can run side by side.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/google-hotels-scraper").call(run_input={
    "locations": [
        "Madrid, Spain"
    ],
    "checkIn": "2026-12-20",
    "nights": 3,
    "currency": "EUR",
    "maxHotelsPerLocation": 40,
    "monitorPrices": True,
    "onlyPriceChanges": True
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["name"], item.get("previousPricePerNight"), "->", item["pricePerNight"], item.get("priceStatus"))
```

No Python? Open the [Actor page](https://apify.com/fguiraud/google-hotels-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-07 (long values shortened):

```json
{
  "name": "Hilton Panama",
  "pricePerNight": 201.97,
  "totalPrice": 664.16,
  "currency": "USD",
  "checkIn": "2026-12-20",
  "nights": 3,
  "rating": 4.6
}
```

## Pricing

$0.0015 per hotel returned; with "only changes", unchanged hotels are not charged.

## FAQ

**How do I get alerts?**

Schedule the task in Apify and connect the run to email, Slack or Google Sheets (Apify integrations, Make, Zapier or n8n).

**Why do some hotels show as new?**

Google rotates part of its list between searches, so a hotel can reappear after missing one run.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/google-hotels-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Hotel prices for a city and dates](https://apify.com/fguiraud/google-hotels-scraper/examples/hotel-prices-for-a-city)
- [Daily hotel price monitor](https://apify.com/fguiraud/google-hotels-scraper/examples/daily-hotel-price-monitor)
- [5-star hotels with ratings and review topics](https://apify.com/fguiraud/google-hotels-scraper/examples/five-star-hotels-with-reviews)
- [Hotels near a landmark or airport](https://apify.com/fguiraud/google-hotels-scraper/examples/hotels-near-a-landmark)
- [Hotel market research dataset](https://apify.com/fguiraud/google-hotels-scraper/examples/hotel-market-research-dataset)

## Related guides

- [Google Hotels API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-hotels-api-python/)
