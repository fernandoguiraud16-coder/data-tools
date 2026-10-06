---
title: "Download transcripts of a whole YouTube channel or playlist"
description: "Bulk-download the transcripts of every video of a YouTube channel or playlist as text, SRT or Markdown, and get only new uploads on a schedule."
---

# Transcripts of a whole YouTube channel or playlist

Researching a creator, building a dataset or feeding a channel into an LLM means hundreds of transcripts. Give the channel handle or a playlist link and get one row per video, newest first.

## What you get

- `channels`: `@handle`, channel URL or playlist link; `maxVideosPerChannel` sets how many.
- `onlyNewVideos: true` remembers what was delivered, so a daily schedule returns only new uploads.
- Same outputs as single videos: text, segments, SRT, VTT, Markdown, chunks.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/youtube-transcript-scraper").call(run_input={
    "channels": [
        "@TED"
    ],
    "maxVideosPerChannel": 20,
    "languages": [
        "en"
    ],
    "outputs": [
        "text"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["title"], "-", item.get("wordCount"), "words")
```

No Python? Open the [Actor page](https://apify.com/fguiraud/youtube-transcript-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-09-26 (long values shortened):

```json
{
  "videoId": "QT3e6x5CZC8",
  "status": "ok",
  "title": "What if AI wasn’t a shortcut, but a learning partner? #TEDTalks",
  "channel": "TED",
  "language": "en",
  "wordCount": 185,
  "text": "A lot of the narrative, we saw that in the headlines, has been it's going to do the writing for kids, kids are not going to learn to write. But we are showing that there's ways that the AI doesn't write for you, it write..."
}
```

## Pricing

$0.003 per transcript. 100 videos cost $0.30.

## FAQ

**How many videos can I get?**

As many as the channel lists; set `maxVideosPerChannel`.

**Does it include Shorts and live streams?**

Shorts with captions, yes. Live streams have no transcript until they end.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/youtube-transcript-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Get YouTube transcripts for LLMs and RAG](https://apify.com/fguiraud/youtube-transcript-scraper/examples/youtube-transcripts-for-llm)
- [Download YouTube subtitles as SRT](https://apify.com/fguiraud/youtube-transcript-scraper/examples/download-youtube-subtitles-srt)
- [Transcripts of every new video of a YouTube channel](https://apify.com/fguiraud/youtube-transcript-scraper/examples/youtube-channel-transcripts)
- [Transcripts of a whole YouTube playlist](https://apify.com/fguiraud/youtube-transcript-scraper/examples/youtube-playlist-transcripts)
- [Transcribe YouTube videos without captions](https://apify.com/fguiraud/youtube-transcript-scraper/examples/youtube-video-without-captions-ai-transcript)

## Related guides

- [YouTube transcript API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/youtube-transcript-api-python/)
- [Transcripts as chunks for RAG](https://fernandoguiraud16-coder.github.io/data-tools/guides/transcript-chunks-for-rag/)
