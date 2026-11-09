---
title: "Google Autocomplete and People Also Ask keyword research API"
description: "Get hundreds of keyword ideas for any topic from Google Autocomplete, People also ask questions and related searches, with search intent and question labels, for any country. $0.0006 per idea."
---

# Keyword research from Google Autocomplete and People Also Ask

Paid keyword tools start at tens of dollars a month. Google itself already shows what people search: the autocomplete suggestions, the "People also ask" box and "People also search for". This tool collects all three for any keyword, expands autocomplete with question words and the alphabet, removes duplicates and labels each idea with its source, intent and whether it is a question.

## What you get

- `expand`: the keyword alone, with question words (how, what, why, can, vs, for, near me...), with a-z, or both (about 250 ideas per keyword).
- `onlyQuestions` for FAQ pages and content briefs.
- `intent`: question, informational, commercial, transactional or local.
- Any market with `country` and `language`; up to 200 keywords per run, with optional de-duplication across keywords.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client (3.x)

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/google-keyword-research").call(run_input={
    "keywords": [
        "best crm for small business"
    ],
    "expand": "questions"
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["source"], item["intent"], item["keyword"])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/google-keyword-research), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-11-07 (long values shortened):

```json
{
  "seed": "best crm for small business",
  "keyword": "best crm for small business free",
  "source": "autocomplete",
  "position": 2,
  "isQuestion": false,
  "intent": "commercial",
  "wordCount": 6
}
```

## Pricing

$0.0006 per keyword idea (about $0.60 per 1,000). A run with 2 keywords returned 190 ideas for $0.115. Keywords without results are free.

| Tool | Price |
|---|---|
| This tool | $0.0006 per idea; autocomplete + People also ask + related searches |
| automation-lab/google-autocomplete-scraper | $0.0009 per keyword expanded (autocomplete only) |
| memo23/google-suggest-scraper | $0.0005 per item (autocomplete only) |

Competitor prices as listed in the Apify Store on 2026-11-07 (Bronze plan where tiers differ); they can change.

## FAQ

**Does it include search volume?**

No. Volumes are only published inside Google Ads; combine the ideas with Google Trends Scraper to compare interest over time.

**Which countries?**

Any country and language Google supports, with `country` (gl) and `language` (hl).

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/google-keyword-research` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples



## Related guides

- [Google Trends API in Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-trends-api-python/)
- [pytrends alternative](https://fernandoguiraud16-coder.github.io/data-tools/guides/pytrends-alternative/)
