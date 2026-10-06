---
title: "Audio and video transcripts as chunks for RAG"
description: "Turn audio, video, podcasts and YouTube into timestamped text chunks ready for embeddings, vector databases and LLM apps."
---

# Transcripts as chunks for RAG

For retrieval you need overlapping text chunks with a pointer back to the source and time. Every transcription tool here can return `chunks` directly.

## What you get

- `outputs: ["chunks"]` with `chunkSize` in characters.
- Each chunk keeps its start and end time, so answers can cite the exact moment.
- Works the same for files, podcasts, TikTok, Instagram and YouTube.

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
    "outputs": [
        "chunks"
    ],
    "chunkSize": 1000
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    for chunk in item.get("chunks", []):
        print(chunk)
```

No Python? Open the [Actor page](https://apify.com/fguiraud/audio-video-transcriber), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-09-30 (long values shortened):

```json
{
  "source": "https://github.com/openai/whisper/raw/main/tests/jfk.flac",
  "status": "ok",
  "language": "en",
  "durationSeconds": 11,
  "text": "And so my fellow Americans ask not what your country can do for you ask what you can do for your country"
}
```

## Pricing

Same as the transcription itself: $0.006 per minute (files), $0.003 per YouTube transcript.

## FAQ

**Which vector database?**

Any: the output is plain JSON you embed with your own model.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/audio-video-transcriber` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Transcribe meeting recordings to text](https://apify.com/fguiraud/audio-video-transcriber/examples/transcribe-meeting-recording)
- [Generate SRT subtitles for a video](https://apify.com/fguiraud/audio-video-transcriber/examples/generate-srt-subtitles)
- [Transcribe an audio file with timestamps](https://apify.com/fguiraud/audio-video-transcriber/examples/audio-to-text-with-timestamps)
- [Convert MP3 to text](https://apify.com/fguiraud/audio-video-transcriber/examples/mp3-to-text)
- [Transcribe an interview to text](https://apify.com/fguiraud/audio-video-transcriber/examples/transcribe-interview-to-text)

## Related guides

- [PDF to Markdown for RAG](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-to-markdown-for-rag/)
- [YouTube transcript API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/youtube-transcript-api-python/)
