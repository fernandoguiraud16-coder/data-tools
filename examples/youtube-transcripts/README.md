# YouTube transcripts in Python

Get the transcript of any YouTube video or Short as Markdown with timestamps, SRT subtitles or plain text, through the [YouTube Transcript Scraper](https://apify.com/fguiraud/youtube-transcript-scraper) Actor. No YouTube API key, no blocked IPs to deal with.

## Save transcripts as Markdown files

```bash
python transcripts.py https://youtu.be/arj7oStGLkU dQw4w9WgXcQ https://youtube.com/shorts/U5-dE2nCzjM
```

Real output (September 2026):

```text
[no-captions] https://www.youtube.com/watch?v=U5-dE2nCzjM: This video has no captions (not billed)
[saved] Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster) (en, human captions, 487 words)
[saved] Inside the Mind of a Master Procrastinator | Tim Urban | TED (en, human captions, 2277 words)
```

Each file starts like this, with a timestamp per paragraph so an LLM can cite the exact moment:

```markdown
# Inside the Mind of a Master Procrastinator | Tim Urban | TED

**[00:00:12]** So in college, I was a government major, which means I had to write a lot of papers. ...
```

Videos without captions (many Shorts, music without speech) are reported and **not charged**.

## Subtitles and bulk lists

```bash
python transcripts.py videos.txt --format srt --lang es,en
```

`videos.txt` holds one link per line. `--lang es,en` returns Spanish captions when they exist and English otherwise.

## Use cases

- **Summaries and notes** of talks, lectures and tutorials with ChatGPT or Claude.
- **Content repurposing**: blog posts, newsletters and threads from your own videos.
- **Research**: what creators or experts in a niche say, across hundreds of videos.

Full field reference: [`sample-output.json`](sample-output.json) and the [Actor page](https://apify.com/fguiraud/youtube-transcript-scraper).
