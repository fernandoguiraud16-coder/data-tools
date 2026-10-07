---
title: "Google Hotels API for Python: hotel prices, ratings and reviews"
description: "Get Google Hotels data for any city and dates in Python: price per night, total with taxes, star class, rating, reviews, amenities and review topics. Up to 150 hotels per city."
---

# Google Hotels API for Python

Google Hotels compares prices from every booking site, but has no public API, and its result list shows about 20 hotels and loads the rest with JavaScript. This tool reads Google Hotels for your dates, guests and currency, and combines searches by hotel class and sort order to return up to about 150 different hotels per destination.

## What you get

- Price per night, total stay with taxes and fees, currency of your choice.
- Star class, Google rating, review count and the 1-5 star breakdown.
- Review topics (breakfast, cleanliness, service...) with positive and negative mentions.
- Amenities, coordinates, nearby places with travel time, photos and the hotel website.
- Filters: hotel class, minimum rating, sort order; applied to the results too.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/google-hotels-scraper").call(run_input={
    "locations": [
        "Panama City, Panama"
    ],
    "checkIn": "2026-12-20",
    "nights": 3,
    "adults": 2,
    "currency": "USD",
    "maxHotelsPerLocation": 20
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["name"], item["pricePerNight"], item["currency"], item["rating"])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/google-hotels-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-07 (long values shortened):

```json
{
  "name": "Hilton Panama",
  "hotelClass": 5,
  "rating": 4.6,
  "reviewCount": 4927,
  "pricePerNight": 201.97,
  "totalPrice": 664.16,
  "taxesAndFees": 58.25,
  "currency": "USD",
  "checkIn": "2026-12-20",
  "nights": 3,
  "amenities": [
    "Breakfast ($)",
    "Wi-Fi ($)",
    "Parking ($)",
    "..."
  ],
  "reviewHighlights": [
    {
      "aspect": "Service",
      "mentions": 321,
      "positive": 258,
      "negative": 50
    },
    {
      "aspect": "Property",
      "mentions": 342,
      "positive": 289,
      "negative": 34
    },
    {
      "aspect": "Fitness",
      "mentions": 114,
      "positive": 103,
      "negative": 6
    },
    "..."
  ],
  "website": "https://www.hilton.com/en/hotels/ptyhfhh-hilton-panama/?SEO_id=GMB-AMER-HH-PTYHFHH"
}
```

## Pricing

$0.0015 per hotel. Locations that fail are not charged.

| Tool | Price |
|---|---|
| This tool | $0.0015 per hotel, price monitor included |
| zerobreak/google-hotels-scraper | $0.005 per result |
| vittuhy/google-travel-hotel-prices | $0.001 per result |
| factden/google-hotels-scraper | $0.004 per hotel |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**How far ahead can I search?**

Up to about 11 months, stays of 1 to 30 nights.

**Why do some hotels have no price?**

Google shows none when the hotel is sold out or has no offers for those dates; the other fields are still returned.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/google-hotels-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Hotel prices for a city and dates](https://apify.com/fguiraud/google-hotels-scraper/examples/hotel-prices-for-a-city)
- [Daily hotel price monitor](https://apify.com/fguiraud/google-hotels-scraper/examples/daily-hotel-price-monitor)
- [5-star hotels with ratings and review topics](https://apify.com/fguiraud/google-hotels-scraper/examples/five-star-hotels-with-reviews)
- [Hotels near a landmark or airport](https://apify.com/fguiraud/google-hotels-scraper/examples/hotels-near-a-landmark)
- [Hotel market research dataset](https://apify.com/fguiraud/google-hotels-scraper/examples/hotel-market-research-dataset)

## Related guides

- [Daily hotel price monitoring](https://fernandoguiraud16-coder.github.io/data-tools/guides/hotel-price-monitoring/)
- [Google Jobs API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-jobs-api-python/)
