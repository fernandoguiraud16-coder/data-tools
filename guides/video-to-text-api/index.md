---
title: "Video to Text API: TikTok, Instagram, X, Facebook and MP4"
description: "Transcribe videos from TikTok, Instagram Reels, X, Facebook or MP4 links to text and subtitles, with optional speaker labels. Whisper, $0.006 per minute."
---

# Video to text API

One tool for videos from social platforms and plain video files: paste links, get the spoken text with timestamps.

## What you get

- TikTok, Instagram Reels, X and Facebook links, or direct video files.
- `speakerLabels: true` for interviews and panels.
- Text, segments, SRT/VTT, Markdown; 99 languages.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/video-to-text-transcriber").call(run_input={
    "sources": [
        {
            "url": "https://www.tiktok.com/@tiktok/video/7689568478570843422"
        }
    ],
    "outputs": [
        "text",
        "segments"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["source"], item.get("text", "")[:200])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/video-to-text-transcriber), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-09-30 (long values shortened):

```json
{
  "source": "https://www.tiktok.com/@tiktok/video/7689568478570843422",
  "status": "ok",
  "language": "en",
  "durationSeconds": 52.72,
  "billedMinutes": 1,
  "text": "You three look so good. I'm getting serious 2000 flashbacks. Thanks. I have this disposable camera. If I were to give it to you, would you be able to show me with that 2000's revival kind of looks like? Sure, why not? Ye...",
  "video": {
    "platform": "tiktok",
    "url": "https://www.tiktok.com/@tiktok/video/7689568478570843422",
    "title": "the throwback sounds we didn’t know we were missing, given new life o...",
    "author": "tiktok",
    "uploadDate": "2026-09-25",
    "views": 327000,
    "likes": 4477,
    "comments": 1576
  }
}
```

## Pricing

$0.006 per minute; speaker labels add $0.003 per minute.

## FAQ

**YouTube links?**

Use the [YouTube transcript tool](https://apify.com/fguiraud/youtube-transcript-scraper): it reads captions first and is cheaper.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/video-to-text-transcriber` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Convert a video to text](https://apify.com/fguiraud/video-to-text-transcriber/examples/convert-video-to-text)
- [Create subtitles from a video file](https://apify.com/fguiraud/video-to-text-transcriber/examples/create-subtitles-from-video)
- [Transcribe TikTok videos to text](https://apify.com/fguiraud/video-to-text-transcriber/examples/tiktok-video-to-text)
- [Transcribe Instagram Reels to text](https://apify.com/fguiraud/video-to-text-transcriber/examples/instagram-reels-to-text)
- [Transcribe the latest videos of a TikTok account](https://apify.com/fguiraud/video-to-text-transcriber/examples/transcribe-tiktok-account)

## Related guides

- [TikTok transcript API](https://fernandoguiraud16-coder.github.io/data-tools/guides/tiktok-transcript-api/)
- [Speech to text API with Whisper](https://fernandoguiraud16-coder.github.io/data-tools/guides/speech-to-text-api-whisper/)
