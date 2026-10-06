---
title: "pytrends alternative: Google Trends in Python without 429 errors"
description: "pytrends keeps failing with 429 Too Many Requests and has had no release since April 2023. A maintained alternative that retries with fresh IPs and returns clean JSON."
---

# A pytrends alternative that does not hit 429 errors

`pytrends` was the standard way to read Google Trends from Python, but its last release (4.9.2) is from April 2023, and Google answers bursts of requests with `429 Too Many Requests`. The usual fixes (sleeping, rotating user agents, your own proxies) only move the problem. This tool runs each query with automatic retries on new sessions and IPs, and is maintained against Google's current endpoints.

## What you get

- Same data as pytrends: interest over time, interest by region (down to city and US metro), related and rising queries and topics, trending searches.
- Up to 5 terms compared on one scale, any timeframe, category, and Web/YouTube/News/Images/Shopping property.
- No 429 handling in your code: failed attempts are retried and never billed.
- Paste a trends.google.com URL to reuse its filters.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/google-trends-scraper").call(run_input={
    "searchTerms": [
        "python, javascript, rust"
    ],
    "geo": [
        "US"
    ],
    "timeframe": "today 12-m",
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
  "published": "2026-09-30T06:40:00-07:00"
}
```

## Pricing

$0.002 per search term and region, billed only when data comes back.

## FAQ

**How do I map pytrends calls?**

`interest_over_time()` is `outputs: ["interestOverTime"]`, `interest_by_region()` is `interestByRegion`, `related_queries()` is `relatedQueries`, `trending_searches()` is `trendingNow: ["US"]`.

**Is it the same data?**

Yes, it comes from Google Trends; values are relative (0-100), as in pytrends.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/google-trends-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Compare search interest of competing products](https://apify.com/fguiraud/google-trends-scraper/examples/compare-search-interest-products)
- [Get today's trending searches by country](https://apify.com/fguiraud/google-trends-scraper/examples/trending-searches-today-by-country)
- [Rising related searches for keyword research](https://apify.com/fguiraud/google-trends-scraper/examples/rising-related-searches-keyword-research)
- [Google Trends interest by city](https://apify.com/fguiraud/google-trends-scraper/examples/google-trends-interest-by-city)
- [YouTube search trends](https://apify.com/fguiraud/google-trends-scraper/examples/youtube-search-trends)

## Related guides

- [Google Trends API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-trends-api-python/)
- [Google News API with full article text](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-news-api-full-text/)
