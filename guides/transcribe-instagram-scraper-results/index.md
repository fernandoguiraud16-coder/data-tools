---
title: "Transcribe Instagram Reel Scraper results to text"
description: "Already scraping Instagram Reels with an Apify Actor? Pass its dataset ID and get the transcript of every Reel with Whisper, 99 languages. $0.01 per Reel including the first minute; Reels without speech are free."
---

# Transcribe the Reels of an Instagram scraper run

Instagram scrapers return the caption, likes, comments and video file of each Reel, but not what is said in it. Give this tool the dataset of that run (`datasetId`) and every Reel in it is transcribed. It uses the video file the scraper already found (`videoUrl`), so nothing has to be fetched from Instagram again. With Apify's **Connect Actor** integration it runs by itself after the scraper.

## What you get

- `datasetId`: the dataset of an Instagram Reel, post or profile scraper run (pick it in the Input tab); or paste rows in `datasetItems`.
- Whisper transcription in 99 languages, with SRT/VTT subtitles if you want them.
- Reels with music only come back with no text and are not billed (the second Reel in the sample).
- `searchTerms` finds brands or topics in every transcript, with the time of each mention.

Chain both runs from Python:

```python
reels = client.actor("apify/instagram-reel-scraper").call(run_input={"username": ["nasa"], "resultsLimit": 2})
run = client.actor("fguiraud/instagram-reels-transcript-scraper").call(run_input={"datasetId": reels.default_dataset_id})
```

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client (3.x)

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/instagram-reels-transcript-scraper").call(run_input={
    "datasetId": "<DATASET_ID_OF_THE_SCRAPER_RUN>",
    "outputs": [
        "text"
    ]
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item.get("billedMinutes"), item.get("text", "")[:200])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/instagram-reels-transcript-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-11-07 (long values shortened):

```json
{
  "status": "ok",
  "language": "en",
  "durationSeconds": 66.43,
  "billedMinutes": 2,
  "text": "Mr. President, welcome to Kennedy Space Center. Welcome to Max Power. It is an absolute honor to serve under a president whose vision is igniting a golden age of exploration and energizing the most accomplished space age..."
}
```

## Pricing

$0.01 per Reel (includes the first minute), then $0.006 per extra minute. The 66-second Reel above was billed $0.016; the Reel without speech was free.

## FAQ

**Does it need my Instagram login?**

No. It uses the video files from the scraper results, or public Reel links.

**Do the video links expire?**

The file links in scraper results expire after some hours or days, so transcribe soon after scraping (Connect Actor does it right away). Reel page links also work and do not expire.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/instagram-reels-transcript-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Instagram Reel to text](https://apify.com/fguiraud/instagram-reels-transcript-scraper/examples/instagram-reel-to-text)
- [Transcribe an Instagram account's reels](https://apify.com/fguiraud/instagram-reels-transcript-scraper/examples/instagram-account-reels-to-text)
- [Monitor a creator for new reels](https://apify.com/fguiraud/instagram-reels-transcript-scraper/examples/monitor-instagram-creator-new-reels)
- [Instagram reel to SRT subtitles](https://apify.com/fguiraud/instagram-reels-transcript-scraper/examples/instagram-reel-to-srt-subtitles)

## Related guides

- [Instagram Reels transcript API](https://fernandoguiraud16-coder.github.io/data-tools/guides/instagram-reels-transcript-api/)
- [Transcribe TikTok Scraper results](https://fernandoguiraud16-coder.github.io/data-tools/guides/transcribe-tiktok-scraper-results/)
