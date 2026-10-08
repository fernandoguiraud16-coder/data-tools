---
title: "Search YouTube by keyword and get the transcripts of the results"
description: "Search YouTube for any topic and download the transcripts of the top videos as text, Markdown or RAG chunks, with filters by upload date, length and sort order, and daily alerts with only new videos."
---

# YouTube search results as transcripts

Researching a topic on YouTube usually means opening video after video. Give a search instead, such as "how to use claude code" or "nvidia earnings", and get one row per result with the full transcript, in the order YouTube shows them (`searchRank`), with title, channel, duration and views.

## What you get

- `searchQueries`: any keyword or phrase; `maxVideosPerSearch` up to 500 (20 results per page).
- Filters: `sortBy` (relevance, date, views, rating), `uploadDate` (hour to year), `videoDuration` (under 4, 4-20 or over 20 minutes).
- Only regular videos: channels, playlists, Shorts shelves and ads are left out.
- `onlyNewVideos: true` on a schedule turns a search into an alert: each run returns only videos not delivered before.
- Same outputs as single videos: text, segments, SRT, VTT, Markdown, chunks; optional AI transcription for videos without captions.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/youtube-transcript-scraper").call(run_input={
    "searchQueries": [
        "how to use claude code"
    ],
    "maxVideosPerSearch": 10,
    "outputs": [
        "text"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("searchRank"), item["title"], "-", item.get("wordCount"), "words")
```

No Python? Open the [Actor page](https://apify.com/fguiraud/youtube-transcript-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-08 (long values shortened):

```json
{
  "videoId": "3aKVArutiIU",
  "status": "ok",
  "searchQuery": "how to use claude code",
  "searchRank": 2,
  "title": "Learn 80% of Claude Code in 10 Minutes (2026 Tutorial)",
  "channel": "Sajjaad Khader",
  "durationSeconds": 596,
  "viewCount": 341374,
  "wordCount": 2056,
  "text": "I have been obsessed with Claude Code for the last eight months because this is the tool that will actually make you a top 1% software engineer even if you have no prior experience. With Claude Code, you can code, plan,..."
}
```

## Pricing

$0.003 per transcript. Searching is free; videos without captions are not charged.

## FAQ

**Are the results the same as in my browser?**

They follow YouTube's order for a signed-out visitor in the US, so they can differ slightly from a signed-in search.

**Can I get only new videos about a topic?**

Yes: sort by date, turn on `onlyNewVideos` and schedule the run; each run returns only videos earlier runs did not deliver.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/youtube-transcript-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Get YouTube transcripts for LLMs and RAG](https://apify.com/fguiraud/youtube-transcript-scraper/examples/youtube-transcripts-for-llm)
- [Download YouTube subtitles as SRT](https://apify.com/fguiraud/youtube-transcript-scraper/examples/download-youtube-subtitles-srt)
- [Transcripts of every new video of a YouTube channel](https://apify.com/fguiraud/youtube-transcript-scraper/examples/youtube-channel-transcripts)
- [Transcripts of a whole YouTube playlist](https://apify.com/fguiraud/youtube-transcript-scraper/examples/youtube-playlist-transcripts)
- [Transcribe YouTube videos without captions](https://apify.com/fguiraud/youtube-transcript-scraper/examples/youtube-video-without-captions-ai-transcript)

## Related guides

- [Transcripts of a whole YouTube channel](https://fernandoguiraud16-coder.github.io/data-tools/guides/youtube-channel-transcripts/)
- [YouTube transcript API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/youtube-transcript-api-python/)
