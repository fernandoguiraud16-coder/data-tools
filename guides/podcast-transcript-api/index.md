---
title: "Podcast Transcript API: any podcast by name to text"
description: "Transcribe podcast episodes by podcast name, Apple Podcasts link or RSS feed, with speaker labels and only-new-episodes mode. Whisper, 99 languages."
---

# Podcast transcript API

Type a podcast name and get its newest episodes as text, with timestamps and optional speaker labels. Schedule it to receive only new episodes.

## What you get

- `podcastFeeds`: names, Apple Podcasts links or RSS URLs.
- Episode title, date and audio URL on every row.
- `speakerLabels: true` marks Speaker 1, Speaker 2...
- `maxDurationMinutes` caps cost on long shows.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/podcast-transcript-scraper").call(run_input={
    "podcastFeeds": [
        "NPR News Now"
    ],
    "maxEpisodesPerFeed": 2,
    "outputs": [
        "text"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["podcast"], "-", item["episodeTitle"])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/podcast-transcript-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-09-24 (long values shortened):

```json
{
  "podcast": "NPR News Now",
  "episodeTitle": "NPR News: 09-24-2026 1AM EDT",
  "published": "2026-09-24T05:10:11+00:00",
  "status": "ok",
  "language": "en",
  "durationSeconds": 280.06,
  "billedMinutes": 3,
  "text": "Live from NPR News on July, Snyder. Australia's Prime Minister says an AI agent created by OpenAI infiltrated a government website. The government says the incident occurred in June, but Christina Cuculio reports that Op..."
}
```

## Pricing

$0.006 per audio minute; speaker labels add $0.003 per minute. A 60-minute episode costs $0.36.

## FAQ

**Is silence billed?**

Billing is per transcribed minute, rounded up per episode.

**Can I transcribe a whole back catalog?**

Yes, raise `maxEpisodesPerFeed`; check the cost estimate first.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/podcast-transcript-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Transcribe the latest episodes of a podcast](https://apify.com/fguiraud/podcast-transcript-scraper/examples/transcribe-latest-podcast-episodes)
- [Monitor a podcast for new episode transcripts](https://apify.com/fguiraud/podcast-transcript-scraper/examples/monitor-podcast-new-episodes)
- [Podcast transcripts with speaker labels](https://apify.com/fguiraud/podcast-transcript-scraper/examples/podcast-transcript-with-speaker-labels)
- [Podcast episode to Markdown (show notes, blog)](https://apify.com/fguiraud/podcast-transcript-scraper/examples/podcast-episode-to-markdown)
- [Podcast transcripts as chunks for RAG](https://apify.com/fguiraud/podcast-transcript-scraper/examples/podcast-transcripts-for-rag)

## Related guides

- [Speech to text API with Whisper](https://fernandoguiraud16-coder.github.io/data-tools/guides/speech-to-text-api-whisper/)
- [Transcripts as chunks for RAG](https://fernandoguiraud16-coder.github.io/data-tools/guides/transcript-chunks-for-rag/)
