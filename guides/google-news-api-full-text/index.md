---
title: "Google News API with full article text in Markdown"
description: "Search Google News by keyword, section or country and get the real article URL plus the full article text in Markdown for LLMs and RAG. Only-new mode."
---

# Google News API with full article text

Google News RSS gives titles and redirect links, not articles. This tool resolves the real URL and, if you want, downloads the full text as Markdown.

## What you get

- Keyword search, sections (Top, Business, Technology...), any country and language edition.
- Real article URL, source, date, author and image.
- `fullText: true` for the article body in Markdown or plain text.
- `onlyNewArticles` for scheduled monitoring; date ranges for research.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/google-news-scraper").call(run_input={
    "queries": [
        "solar energy"
    ],
    "timeRange": "1d",
    "maxArticlesPerQuery": 20,
    "fullText": True
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["publishedAt"], item["source"], item["title"])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/google-news-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-01 (long values shortened):

```json
{
  "title": "California Officially Legalizes Balcony Solar, Opening the Market to the New Technology",
  "source": "KQED",
  "publishedAt": "2026-10-01T00:37:14Z",
  "url": "https://www.kqed.org/science/2002120/california-officially-legalizes-balcony-solar-opening-the-market-to-the-new-technology",
  "foundBy": [
    "search: solar energy"
  ],
  "status": "ok"
}
```

## Pricing

$0.002 per article, plus $0.002 when full text is requested.

| Tool | Price |
|---|---|
| This tool | $0.002 per article (+$0.002 full text) |
| data_xplorer/google-news-scraper-fast | $0.004 per article, no full text |
| easyapi/google-news-scraper | $0.005 + $0.09 start |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**Paywalled sites?**

The row reports when the full text could not be read (`fullTextStatus`).

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/google-news-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Monitor news about a topic daily](https://apify.com/fguiraud/google-news-scraper/examples/monitor-news-about-topic)
- [Get full article text for news on a keyword](https://apify.com/fguiraud/google-news-scraper/examples/news-full-article-text-keyword)
- [Monitor news about a company](https://apify.com/fguiraud/google-news-scraper/examples/company-news-monitoring)
- [Google News business headlines](https://apify.com/fguiraud/google-news-scraper/examples/google-news-business-headlines)
- [News in Spanish from Latin America](https://apify.com/fguiraud/google-news-scraper/examples/spanish-news-latin-america)

## Related guides

- [Google Trends API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-trends-api-python/)
