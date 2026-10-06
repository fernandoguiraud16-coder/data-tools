---
title: "OpenAI Whisper API alternative: no 25 MB limit, file links, SRT"
description: "OpenAI's speech-to-text API caps uploads at 25 MB. Transcribe long files from links, TikTok or Instagram, with SRT/VTT and speaker labels, using open-source Whisper. No OpenAI key."
---

# An OpenAI Whisper API alternative without the 25 MB limit

OpenAI's speech-to-text endpoint takes uploads of at most 25 MB, so an hour of audio has to be compressed or cut into chunks first, and you upload every file yourself. This tool takes links (any size), downloads and transcribes them with open-source Whisper, and returns text, timestamps and subtitles. The price per minute is in the same range as OpenAI's whisper-1; OpenAI's newer models are cheaper, so the reasons to switch are the workflow ones below, not price.

## What you get

- File links of any size (MP3, WAV, M4A, MP4...), no chunking.
- SRT/VTT subtitles, word timestamps, Markdown and RAG chunks.
- Speaker labels and podcast/TikTok/Instagram inputs in the sibling tools.
- No OpenAI account or key; pay per minute on Apify.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/audio-video-transcriber").call(run_input={
    "sources": [
        {
            "url": "https://archive.org/download/gettysburg_johng_librivox/gettysburg_address_64kb.mp3"
        }
    ],
    "model": "small",
    "outputs": [
        "text",
        "srt"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["language"], item["durationSeconds"])
    print(item["text"][:300])
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

$0.006 per audio minute, rounded up per file. Speaker labels (podcast and video tools) add $0.003 per minute.

## FAQ

**Is accuracy the same as OpenAI?**

It is the same open-source Whisper family (`tiny`, `base`, `small`); `small` is the most accurate option here. OpenAI's hosted models may do better on hard audio.

**When should I stay with OpenAI?**

For short files you already have locally, the cheapest OpenAI model costs less per minute.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/audio-video-transcriber` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Transcribe meeting recordings to text](https://apify.com/fguiraud/audio-video-transcriber/examples/transcribe-meeting-recording)
- [Generate SRT subtitles for a video](https://apify.com/fguiraud/audio-video-transcriber/examples/generate-srt-subtitles)
- [Transcribe an audio file with timestamps](https://apify.com/fguiraud/audio-video-transcriber/examples/audio-to-text-with-timestamps)
- [Convert MP3 to text](https://apify.com/fguiraud/audio-video-transcriber/examples/mp3-to-text)
- [Transcribe an interview to text](https://apify.com/fguiraud/audio-video-transcriber/examples/transcribe-interview-to-text)

## Related guides

- [Speech to text API with Whisper](https://fernandoguiraud16-coder.github.io/data-tools/guides/speech-to-text-api-whisper/)
- [Podcast transcript API](https://fernandoguiraud16-coder.github.io/data-tools/guides/podcast-transcript-api/)
