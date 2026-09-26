# Why is it rising? Google Trends + Google News

A two-step recipe:

1. [Google Trends Scraper](https://apify.com/fguiraud/google-trends-scraper) finds the fastest rising searches around a topic.
2. [Google News Scraper](https://apify.com/fguiraud/google-news-scraper) pulls this week's articles for each one.

The result is `briefing.md`: every rising search, its growth and the news behind it.

```bash
python why_is_it_rising.py "heat pump" --geo US --top 3
```

Real `briefing.md` (September 2026, shortened):

```markdown
# Why searches around 'heat pump' are rising (US)

## google heat pump program bay area (+3,750%)
- [Should we get excited about California's latest virtual power plant?](https://www.canarymedia.com/...) (Canary Media)

## us heat pump sales trends (+2,400%)
- [Heat Pump Water Heaters Market Forecast to Accelerate Toward 2035](https://www.indexbox.io/...) (IndexBox)
- [Cold Climate Air Source Heat Pump Market to Accelerate Through 2035](https://www.indexbox.io/...) (IndexBox)

## mrcool diy monoblock heat pump (+650%)
- No recent news found.
```

Google's rising list sometimes includes queries unrelated to the topic, so by default the script keeps only rising searches that share a word with it. Use `--all` to keep everything.

## Ideas

- Pass `briefing.md` to an LLM and ask for a 5-bullet summary: a daily trend report in one script.
- Run it every morning for your industry keywords and post the result to Slack.

Typical cost: about $0.02 per briefing (one Trends term + up to 9 headlines).
