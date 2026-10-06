---
name: apify-video-audio-transcripts
description: Transcribe video and audio to text with Apify Actors - YouTube videos, channels and playlists, TikTok videos and accounts, Instagram Reels and creators, podcasts by name or RSS feed, and any audio or video file (MP3, WAV, M4A, MP4...). Returns plain text, timestamped segments, SRT/VTT subtitles, Markdown or RAG chunks, with optional speaker labels and translation to English. Use when the user asks for a transcript, captions, subtitles, speech to text, "what does this video say", summarizing a video or podcast, or building a dataset of spoken content.
author: Fernando Guiraud
author_url: https://github.com/fernandoguiraud16-coder
metadata:
  category: data-extraction
  keywords: "transcript, transcription, speech-to-text, whisper, youtube, tiktok, instagram, reels, podcast, subtitles, srt, vtt, captions, audio, video"
---

# Video and Audio Transcripts

Turn spoken content into text by routing the request to the right Apify Actor, running it, and returning the transcript in the format the user needs.

Disclosure: the routed Actors are built and sold (pay per use) by the author of this skill.

## Example prompts

Prompts this skill handles:

- "Get the transcript of this YouTube video and summarize it"
- "Transcribe the last 5 TikToks of @nasa"
- "Make SRT subtitles for this MP4"
- "Transcribe the newest episode of the Lex Fridman Podcast with speaker labels"

Out of scope (the boundary):

- "Download this TikTok video" - this skill returns text, not media files.
- Private or login-only videos - only public content works.

## Prerequisites

- Apify account ([sign up](https://apify.com)) and the Apify CLI (`npm install -g apify-cli`)
- Authentication: `apify login`, or the `APIFY_TOKEN` environment variable

## Actor routing

| User need | Actor ID | Price | Main input |
|-----------|----------|-------|------------|
| YouTube video, channel or playlist | `fguiraud/youtube-transcript-scraper` | $0.003 per transcript | `videos` (links or IDs), `channels` (@handle or playlist link) |
| TikTok video or account | `fguiraud/tiktok-transcript-scraper` | $0.009 per video | `sources` (links) or `profiles` (@handle) |
| Instagram Reel or creator | `fguiraud/instagram-reels-transcript-scraper` | $0.009 per reel | `sources` (links) or `profiles` (@handle, newest 12 reels max) |
| Podcast | `fguiraud/podcast-transcript-scraper` | $0.006 per minute | `podcastFeeds` (name, Apple Podcasts link or RSS URL) |
| SRT/VTT subtitles for a file | `fguiraud/srt-subtitle-generator` | $0.006 per minute | `sources` (file links) |
| Any audio or video file, X or Facebook video | `fguiraud/audio-video-transcriber` | $0.006 per minute | `sources` (file links) |

`sources` takes objects like `[{"url": "https://..."}]`. Plain strings and the field names `url`, `urls` and `startUrls` are accepted too.

## Workflow

1. Pick the Actor from the table. Several platforms in one request: run one Actor per platform.
2. Build the input. Useful options:
   - `outputs`: any of `text`, `segments`, `markdown`, `srt`, `vtt`, `chunks` (default text and segments).
   - `language`: ISO code or `auto` (default). For YouTube use `languages: ["en"]`.
   - `task: "translate"` gives English text from any language (Whisper Actors).
   - `speakerLabels: true` labels Speaker 1, Speaker 2... (podcast and `fguiraud/video-to-text-transcriber`; adds $0.003 per minute).
   - YouTube without captions: `aiFallback: true` transcribes the audio with Whisper ($0.010 per minute).
   - Monitoring: `onlyNewVideos` / `onlyNewEpisodes: true` on a schedule returns only new items.
3. For long audio (over an hour) or many items, tell the user the estimated cost first.
4. Run and read the results:

```bash
apify actors call fguiraud/youtube-transcript-scraper \
  -i '{"videos": ["https://youtu.be/arj7oStGLkU"], "languages": ["en"], "outputs": ["text"]}' \
  --json --user-agent fguiraud-data-tools/apify-video-audio-transcripts 2>/dev/null

apify datasets get-items DATASET_ID --format json \
  --user-agent fguiraud-data-tools/apify-video-audio-transcripts 2>/dev/null
```

5. Deliver: each dataset row is one video or file. Use `text` for summaries, `segments` (start, end, text) for quotes with timestamps, `srt`/`vtt` for subtitle files. Check `status` and `error`/`note` on each row: a failed item explains why (private video, no audio...).

## Interfaces

- Apify CLI (above).
- MCP: `https://mcp.apify.com/?tools=fguiraud/youtube-transcript-scraper` (replace the Actor name), OAuth or `Authorization: Bearer <APIFY_TOKEN>`.

## Troubleshooting

- YouTube row with `status: "no-captions"`: rerun with `aiFallback: true`.
- Empty input runs a small sample and says so in `note`: always send your own links.
- Very long files: set `maxDurationMinutes` to cap cost.
