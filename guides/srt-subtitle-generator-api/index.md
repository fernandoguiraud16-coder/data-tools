---
title: "SRT Subtitle Generator API: automatic subtitles for any video"
description: "Generate SRT and VTT subtitle files from any video or audio with Whisper, formatted to broadcast rules or short lines for Reels and TikTok. 99 languages."
---

# SRT subtitle generator API

Upload-ready subtitles without manual timing: give a video link and download SRT and VTT files.

## What you get

- Line length, lines per cue and cue duration are configurable (42 characters, 2 lines by default).
- Short one-line captions for vertical video (`subtitleMaxChars: 24`).
- Translate to English subtitles with `task: "translate"`.
- Files saved to download links (`saveFiles`).

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/srt-subtitle-generator").call(run_input={
    "sources": [
        {
            "url": "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"
        }
    ],
    "outputs": [
        "srt",
        "vtt"
    ],
    "saveFiles": True
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["srt"][:300])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/srt-subtitle-generator), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-01 (long values shortened):

```json
{
  "source": "https://upload.wikimedia.org/wikipedia/commons/e/e4/President_Ronald_Reagan%27s_Radio_Address_to_the_Nation_on_Free_and_Fair_Trade_from_Camp_David%2C_Maryland.webm",
  "status": "ok",
  "language": "en",
  "durationSeconds": 310.56,
  "srt": "1\n00:00:07,500 --> 00:00:12,020\nMy fellow Americans, Prime Minister\nNakasoni of Japan will be visiting me here\n\n2\n00:00:12,020 --> 00:00:13,160\nat the White House next week.\n\n3\n00:00:13,720 --> 00:00:17,580\nIt's an impor...",
  "files": {
    "srt": "https://api.apify.com/v2/key-value-stores/86aj5q2hceQtE1Lfk/records/001-President_Ronald_Reagan-27s_Radio_Address_to_the_Nation_on_Free_and_Fair_Trade_f.srt?signature=GWiKbxsTSdAnjPLfzzUS",
    "vtt": "https://api.apify.com/v2/key-value-stores/86aj5q2hceQtE1Lfk/records/001-President_Ronald_Reagan-27s_Radio_Address_to_the_Nation_on_Free_and_Fair_Trade_f.vtt?signature=17TpsrASuIHq59ux6YvHq"
  }
}
```

## Pricing

$0.006 per minute of audio.

## FAQ

**Can I edit the subtitles?**

SRT is plain text; any editor or YouTube Studio opens it.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/srt-subtitle-generator` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Generate SRT subtitles for YouTube uploads](https://apify.com/fguiraud/srt-subtitle-generator/examples/srt-subtitles-for-youtube-uploads)
- [Translate video subtitles to English](https://apify.com/fguiraud/srt-subtitle-generator/examples/translate-video-subtitles-to-english)
- [Generate WebVTT (.vtt) subtitles](https://apify.com/fguiraud/srt-subtitle-generator/examples/vtt-subtitles-generator)
- [Short captions for Reels, TikTok and Shorts](https://apify.com/fguiraud/srt-subtitle-generator/examples/short-captions-for-reels-and-tiktok)
- [Word-by-word subtitle timing](https://apify.com/fguiraud/srt-subtitle-generator/examples/word-by-word-subtitles)

## Related guides

- [Speech to text API with Whisper](https://fernandoguiraud16-coder.github.io/data-tools/guides/speech-to-text-api-whisper/)
- [Video to text API](https://fernandoguiraud16-coder.github.io/data-tools/guides/video-to-text-api/)
