---
title: "Speech to Text API with Whisper, no OpenAI key (pay per minute)"
description: "Transcribe MP3, WAV, M4A and MP4 files to text, timestamps and subtitles with open-source Whisper. 99 languages, translation to English, $0.006 per minute."
---

# Speech to text API with Whisper

Running Whisper yourself needs a GPU or a lot of patience; the hosted API needs an OpenAI key and a 25 MB upload limit. This tool takes file links of any size, transcribes them with open-source Whisper and returns text, timestamps and subtitles.

## What you get

- Any audio or video file link (MP3, WAV, M4A, FLAC, MP4, MOV...), or base64 uploads.
- Text, segments, word timestamps, SRT/VTT, Markdown, RAG chunks.
- `task: "translate"` to English; custom `vocabulary` for names and jargon.
- Many files per run, one row per file.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/audio-video-transcriber").call(run_input={
    "sources": [
        {
            "url": "https://raw.githubusercontent.com/openai/whisper/main/tests/jfk.flac"
        }
    ],
    "model": "base",
    "outputs": [
        "text",
        "srt"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["language"], item["text"])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/audio-video-transcriber), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-09-30 (long values shortened):

```json
{
  "source": "https://github.com/openai/whisper/raw/main/tests/jfk.flac",
  "status": "ok",
  "model": "tiny",
  "language": "en",
  "durationSeconds": 11,
  "billedMinutes": 1,
  "text": "And so my fellow Americans ask not what your country can do for you ask what you can do for your country",
  "srt": "1\n00:00:00,000 --> 00:00:10,900\nAnd so my fellow Americans ask not what your country can do for you ask what you can do for your country\n"
}
```

## Pricing

$0.006 per audio minute, rounded up per file.

| Tool | Price |
|---|---|
| This tool | $0.006 per minute |
| kaz_kakyo/audio-transcriber | $0.01 per minute |
| amanatools/whisper-transcriber | $0.008 per minute + $0.005 per file |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**Which Whisper model?**

`tiny`, `base` (default) or `small`. `small` is more accurate on accents and noisy audio.

**Is there a file size limit?**

Set by `maxFileSizeMb`; long recordings are fine.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/audio-video-transcriber` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Transcribe meeting recordings to text](https://apify.com/fguiraud/audio-video-transcriber/examples/transcribe-meeting-recording)
- [Generate SRT subtitles for a video](https://apify.com/fguiraud/audio-video-transcriber/examples/generate-srt-subtitles)
- [Transcribe an audio file with timestamps](https://apify.com/fguiraud/audio-video-transcriber/examples/audio-to-text-with-timestamps)
- [Convert MP3 to text](https://apify.com/fguiraud/audio-video-transcriber/examples/mp3-to-text)
- [Transcribe an interview to text](https://apify.com/fguiraud/audio-video-transcriber/examples/transcribe-interview-to-text)

## Related guides

- [SRT subtitle generator API](https://fernandoguiraud16-coder.github.io/data-tools/guides/srt-subtitle-generator-api/)
- [Podcast transcript API](https://fernandoguiraud16-coder.github.io/data-tools/guides/podcast-transcript-api/)
