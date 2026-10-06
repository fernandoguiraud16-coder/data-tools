---
title: "Google Trends API for Python without 429 errors"
description: "Get Google Trends interest over time and by region, related and rising queries and trending searches in Python, with automatic retries instead of 429 errors."
---

# Google Trends API for Python

There is no official Google Trends API, and `pytrends` fails with "429 Too Many Requests" after a few calls. This tool retries with new IPs and sessions and returns clean JSON.

## What you get

- Interest over time, interest by region (country, state, city, US metro), related and rising queries and topics.
- Compare up to 5 terms on the same scale; paste a Trends URL to keep its filters.
- Web, YouTube, News, Images or Shopping search.
- Trending now by country, and alerts for new rising searches.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/google-trends-scraper").call(run_input={
    "searchTerms": [
        "chatgpt, gemini, claude"
    ],
    "geo": [
        "US"
    ],
    "timeframe": "today 3-m",
    "outputs": [
        "interestOverTime",
        "relatedQueries"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["type"], item.get("terms"), item.get("averages"))
```

No Python? Open the [Actor page](https://apify.com/fguiraud/google-trends-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-09-30 (long values shortened):

```json
{
  "type": "trending",
  "geo": "US",
  "rank": 1,
  "query": "strait of hormuz news",
  "approxTraffic": "2000+",
  "published": "2026-09-30T06:40:00-07:00",
  "news": [
    {
      "title": "Iran war live: US response to proposal under review after Qatar mediation",
      "url": "https://www.aljazeera.com/news/liveblog/2026/9/30/iran-war-live-trump-claims-war-will-end-very-soon-provides-no-details",
      "source": "Al Jazeera"
    },
    {
      "title": "Iran says it got a U.S. response to its peace proposal as its currency hits a new record low seven months into the war",
      "url": "https://fortune.com/2026/09/30/trump-iran-hormuz-strait-talks/",
      "source": "Fortune"
    },
    {
      "title": "Iran proposes a deal to reopen the Strait of Hormuz in 7 days if the US meets its conditions",
      "url": "https://apnews.com/article/iran-us-war-negotiations-strait-hormuz-d8b9749fee99a11dd77513d326b824b6",
      "source": "AP News"
    }
  ]
}
```

## Pricing

$0.002 per search term.

| Tool | Price |
|---|---|
| This tool | $0.002 per term, automatic retries |
| apify/google-trends-scraper | $0.001 per row + platform usage |
| data_xplorer/google-trends-fast-scraper | $0.001 per row + $0.02 start |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**Are values search volumes?**

No. Google Trends gives relative interest from 0 to 100.

**Why do my numbers differ from the website?**

Google samples its data; small differences between requests are normal.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/google-trends-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Compare search interest of competing products](https://apify.com/fguiraud/google-trends-scraper/examples/compare-search-interest-products)
- [Get today's trending searches by country](https://apify.com/fguiraud/google-trends-scraper/examples/trending-searches-today-by-country)
- [Rising related searches for keyword research](https://apify.com/fguiraud/google-trends-scraper/examples/rising-related-searches-keyword-research)
- [Google Trends interest by city](https://apify.com/fguiraud/google-trends-scraper/examples/google-trends-interest-by-city)
- [YouTube search trends](https://apify.com/fguiraud/google-trends-scraper/examples/youtube-search-trends)

## Related guides

- [Google News API with full article text](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-news-api-full-text/)
