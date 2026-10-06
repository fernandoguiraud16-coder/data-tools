---
title: "TikTok Transcript API: videos and whole accounts to text"
description: "Transcribe TikTok videos or the newest videos of any account to text and SRT with Whisper. Works without captions, no login or TikTok API key."
---

# TikTok transcript API

Most TikTok videos have no captions, and the ones that do are often wrong. This tool downloads the audio and transcribes it with Whisper, for single links or for the newest videos of whole accounts.

## What you get

- Links (`sources`) or accounts (`profiles`: `@handle`).
- Text, timestamped segments, SRT/VTT, Markdown.
- Views, likes, upload date and caption of each video.
- `onlyNewVideos` for daily monitoring of creators.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/tiktok-transcript-scraper").call(run_input={
    "profiles": [
        "@nasa"
    ],
    "maxVideosPerProfile": 5,
    "outputs": [
        "text"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["source"], item.get("text", "")[:200])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/tiktok-transcript-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-02 (long values shortened):

```json
{
  "source": "https://www.tiktok.com/@nasa/video/7689547576265149710",
  "status": "ok",
  "language": "en",
  "durationSeconds": 121.65,
  "text": "This week NASA inspired future explorers, prepared the next crew for launch, studied life at the extremes, and looked ahead to the future of flight. Here's what's new, and you're NASA Minute. From aerospace workers to ai...",
  "video": {
    "platform": "tiktok",
    "url": "https://www.tiktok.com/@nasa/video/7689547576265149710",
    "title": "There's plenty happening across NASA as September comes to a close!  ...",
    "author": "nasa",
    "uploadDate": "2026-09-25",
    "views": 137300,
    "likes": 5194,
    "comments": 242
  }
}
```

## Pricing

$0.009 per video (includes the first minute), then $0.006 per extra minute.

| Tool | Price |
|---|---|
| This tool | $0.009 per video, accounts and only-new mode |
| clockworks/tiktok-transcript-extractor | $0.003 + $0.041 per AI minute |
| sian.agency/best-tiktok-ai-transcript-extractor | $0.012 + $0.005 start |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**Do I need a TikTok account or cookies?**

No. Public videos only.

**What languages?**

99, detected automatically; `task: "translate"` gives English.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/tiktok-transcript-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Transcripts of a TikTok account's newest videos](https://apify.com/fguiraud/tiktok-transcript-scraper/examples/tiktok-account-transcripts)
- [TikTok video to SRT subtitles](https://apify.com/fguiraud/tiktok-transcript-scraper/examples/tiktok-to-srt-subtitles)
- [Monitor a TikTok creator for new videos](https://apify.com/fguiraud/tiktok-transcript-scraper/examples/monitor-tiktok-creator-new-videos)

## Related guides

- [Instagram Reels transcript API](https://fernandoguiraud16-coder.github.io/data-tools/guides/instagram-reels-transcript-api/)
- [SRT subtitle generator API](https://fernandoguiraud16-coder.github.io/data-tools/guides/srt-subtitle-generator-api/)
