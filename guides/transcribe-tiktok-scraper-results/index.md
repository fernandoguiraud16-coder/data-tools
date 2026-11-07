---
title: "Transcribe TikTok Scraper results to text for $0.009 per video"
description: "Already scraping TikTok with an Apify Actor? Pass its dataset ID and get the transcript of every video: TikTok captions when they exist, Whisper otherwise. $0.009 per video including the first minute."
---

# Transcribe the videos of a TikTok Scraper run

Scrapers such as TikTok Scraper return the link, caption, views and likes of each video, but not what is said in it. Give this tool the dataset of that run (`datasetId`) and it transcribes every video in it: it finds the video link in each row (`webVideoUrl`, `videoUrl`, `url`...) whatever the scraper calls it. With Apify's **Connect Actor** integration it runs by itself every time the scraper finishes.

## What you get

- `datasetId`: the dataset of any TikTok, Instagram or podcast scraper run (pick it in the Input tab); or paste rows in `datasetItems`.
- TikTok's own captions when the video has them (about a second per video), Whisper when it does not; `transcriptSource` says which.
- Videos with music only and no speech come back empty and are not billed.
- `searchTerms` finds brands or topics in every transcript, with the time of each mention.

Chain both runs from Python:

```python
scrape = client.actor("clockworks/tiktok-scraper").call(run_input={"profiles": ["nasa"], "resultsPerPage": 3})
run = client.actor("fguiraud/tiktok-transcript-scraper").call(run_input={"datasetId": scrape.default_dataset_id})
```

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client (3.x)

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/tiktok-transcript-scraper").call(run_input={
    "datasetId": "<DATASET_ID_OF_THE_SCRAPER_RUN>",
    "outputs": [
        "text"
    ]
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["source"], item.get("transcriptSource"), item.get("text", "")[:200])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/tiktok-transcript-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-11-07 (long values shortened):

```json
{
  "source": "https://www.tiktok.com/@nasa/video/7702504724049743117",
  "status": "ok",
  "transcriptSource": "tiktok-captions",
  "language": "en",
  "durationSeconds": 108,
  "billedMinutes": 2,
  "text": "big things are coming together at NASA and some exciting journeys are just getting started here's what's new in your NASA minute following last week's Artemis acceleration update preparations for Artemis III are moving f..."
}
```

## Pricing

$0.009 per video (includes the first minute), then $0.006 per extra minute. The 108-second video above cost $0.015. Videos without speech are free.

| Tool | Price |
|---|---|
| This tool | $0.009 per video + $0.006 per extra minute |
| clockworks/tiktok-scraper built-in transcription | $0.041 per started minute per video (Bronze) |

Competitor prices as listed in the Apify Store on 2026-11-07 (Bronze plan where tiers differ); they can change.

## FAQ

**Do I need the scraper to download the videos?**

No. The video links in its results are enough.

**Does it work with Instagram or podcast scrapers?**

Yes: Instagram Reels Transcript Scraper and Podcast Transcript Scraper take `datasetId` the same way.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/tiktok-transcript-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Transcripts of a TikTok account's newest videos](https://apify.com/fguiraud/tiktok-transcript-scraper/examples/tiktok-account-transcripts)
- [TikTok video to SRT subtitles](https://apify.com/fguiraud/tiktok-transcript-scraper/examples/tiktok-to-srt-subtitles)
- [Monitor a TikTok creator for new videos](https://apify.com/fguiraud/tiktok-transcript-scraper/examples/monitor-tiktok-creator-new-videos)

## Related guides

- [TikTok transcript API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tiktok-transcript-api/)
- [Instagram Reels transcript API](https://fernandoguiraud16-coder.github.io/data-tools/guides/instagram-reels-transcript-api/)
