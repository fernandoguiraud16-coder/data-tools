# Google News with full article text in Python

Search Google News in any country and language, and get the **real article URL** (not the news.google.com redirect) and the **full article text as Markdown**, through the [Google News Scraper](https://apify.com/fguiraud/google-news-scraper) Actor.

## Save articles as Markdown files

```bash
python news_to_markdown.py "AI regulation" --days 7 --max 20
```

Real output (September 2026):

```text
[blocked ] The Wild West of A.I. Needs to End. Here's How.
[saved]   OpenAI, Anthropic CEOs call for global AI regulation at UN
[saved]   Trump rejects AI regulation, citing parallels with climate change, in U.N. address
[saved]   Bill Gates says AI companies self-regulating isn't enough and governments should ...

3 articles saved to ./articles/
```

Each file is clean Markdown you can feed to an LLM, a summarizer or a RAG index. In tests about 80% of articles come with full text. Sites that block bots or have a paywall still return title, source, date and URL, and the full-text fee is **not charged** for them.

## News alerts: only new stories

```bash
python news_alerts.py "your company" "your competitor"
```

Run it hourly or daily. The Actor remembers what it already returned, so each run gives only new articles and you pay only for those.

## Use cases

- **Brand and competitor monitoring** with Slack or email alerts.
- **Datasets for LLMs**: collect thousands of articles on a topic (date windows go beyond Google's 100-result limit).
- **Market and investment research**: daily news per company or sector.

Full field reference: [`sample-output.json`](sample-output.json) and the [Actor page](https://apify.com/fguiraud/google-news-scraper).
