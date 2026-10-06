---
name: apify-google-trends-news
description: Research search demand and news with Apify Actors - Google Trends interest over time and by region (country, state, city), related and rising queries, comparisons of up to 5 terms, today's trending searches, plus Google News articles for any query, section or country with the full article text in Markdown. Use when the user asks what is trending, how popular a topic or product is, seasonality, keyword research, rising searches, why something is trending, or recent news coverage of a company or topic.
author: Fernando Guiraud
author_url: https://github.com/fernandoguiraud16-coder
metadata:
  category: data-extraction
  keywords: "google-trends, trending, search-interest, keyword-research, seasonality, google-news, news, news-monitoring, articles, full-text, rag"
---

# Google Trends and Google News Research

Answer questions about search demand and news coverage with real data.

Disclosure: the routed Actors are built and sold (pay per use) by the author of this skill.

## Example prompts

Prompts this skill handles:

- "Compare interest in ChatGPT, Gemini and Claude in the US over the last 3 months"
- "What is trending in Mexico today, and what news explains it?"
- "Give me the full text of this week's news about Tesla"

Out of scope (the boundary):

- Absolute search volumes: Google Trends gives relative interest (0-100), not counts.
- Paywalled article text: the row reports when full text could not be read.

## Prerequisites

- Apify account ([sign up](https://apify.com)) and the Apify CLI (`npm install -g apify-cli`)
- Authentication: `apify login`, or the `APIFY_TOKEN` environment variable

## Actor routing

| User need | Actor ID | Price |
|-----------|----------|-------|
| Search interest, related/rising queries, trending now | `fguiraud/google-trends-scraper` | $0.002 per term |
| News articles, optional full text | `fguiraud/google-news-scraper` | $0.002 per article, +$0.002 with full text |

## Workflow

1. Trends input: `searchTerms` (one query per line; up to 5 comma-separated terms on one line are compared on the same scale), `geo` (`US`, `US-CA`, `worldwide`...), `timeframe` (`now 7-d`, `today 3-m`, `today 12-m`, `today 5-y`...), `outputs` (`interestOverTime`, `interestByRegion`, `relatedQueries`, `relatedTopics`). Trending searches: `trendingNow: ["US"]`.
2. News input: `queries` or `topics` (`TOP`, `BUSINESS`, `TECHNOLOGY`...), `country`, `language`, `timeRange` (`1h`, `1d`, `7d`, `30d`...) or `dateFrom`/`dateTo`, `maxArticlesPerQuery`, `fullText: true` for the article body.
3. Run and fetch:

```bash
apify actors call fguiraud/google-trends-scraper \
  -i '{"searchTerms": ["chatgpt, gemini, claude"], "geo": ["US"], "timeframe": "today 3-m", "outputs": ["interestOverTime", "relatedQueries"]}' \
  --json --user-agent fguiraud-data-tools/apify-google-trends-news 2>/dev/null

apify datasets get-items DATASET_ID --format json \
  --user-agent fguiraud-data-tools/apify-google-trends-news 2>/dev/null
```

4. Deliver a direct answer (which term leads, the peak, what is rising), not a data dump. For "why is X trending", run Trends first, then News on the rising queries.

## Interfaces

- Apify CLI (above).
- MCP: `https://mcp.apify.com/?tools=fguiraud/google-trends-scraper`, OAuth or `Authorization: Bearer <APIFY_TOKEN>`.

## Troubleshooting

- Google rate limits are retried automatically with new IPs; a row with `status: "error"` explains what failed.
- Low-volume terms can return empty regions; widen `geo` or `timeframe`.
