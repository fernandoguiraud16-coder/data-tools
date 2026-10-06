---
title: "Instagram Reels Transcript API: reels and creators to text"
description: "Transcribe Instagram Reels by link, or a creator's newest reels by @username, to text and SRT with Whisper. No login or cookies."
---

# Instagram Reels transcript API

Instagram's official API has no transcripts. Paste reel links, or just a creator's username, and get the spoken text of each reel with views and dates.

## What you get

- Reel links (`sources`) or creators (`profiles`: up to the 12 newest reels Instagram shows without login).
- Text, segments, SRT/VTT, Markdown; 99 languages.
- `onlyNewVideos` to follow creators on a schedule.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/instagram-reels-transcript-scraper").call(run_input={
    "profiles": [
        "@zachking"
    ],
    "maxVideosPerProfile": 3,
    "outputs": [
        "text"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["source"], item.get("text", "")[:200])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/instagram-reels-transcript-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-03 (long values shortened):

```json
{
  "source": "https://www.instagram.com/reel/C0hQSaMpD97/",
  "status": "ok",
  "language": "en",
  "durationSeconds": 60.02,
  "text": "Hey Space Nerds, I got a special delivery for you. So picture this. You're on a military range in the middle of the Utah desert. It's flat, it's barren, and everyone's looking up to the sky, waiting to catch sight of a c...",
  "video": {
    "platform": "instagram",
    "url": "https://www.instagram.com/reel/C0hQSaMpD97/",
    "title": "Video by nasagoddard",
    "author": "NASA Goddard",
    "uploadDate": "2023-12-06",
    "views": null,
    "likes": 8391,
    "comments": 17
  }
}
```

## Pricing

$0.009 per reel (includes the first minute), then $0.006 per extra minute.

## FAQ

**Do I need to log in?**

No. Public reels and public accounts only.

**Why at most 12 reels per account?**

That is what Instagram shows to visitors who are not logged in.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/instagram-reels-transcript-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Instagram Reel to text](https://apify.com/fguiraud/instagram-reels-transcript-scraper/examples/instagram-reel-to-text)
- [Transcribe an Instagram account's reels](https://apify.com/fguiraud/instagram-reels-transcript-scraper/examples/instagram-account-reels-to-text)
- [Monitor a creator for new reels](https://apify.com/fguiraud/instagram-reels-transcript-scraper/examples/monitor-instagram-creator-new-reels)
- [Instagram reel to SRT subtitles](https://apify.com/fguiraud/instagram-reels-transcript-scraper/examples/instagram-reel-to-srt-subtitles)

## Related guides

- [TikTok transcript API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tiktok-transcript-api/)
- [Video to text API](https://fernandoguiraud16-coder.github.io/data-tools/guides/video-to-text-api/)
