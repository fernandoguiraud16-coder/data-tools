"""Find the fastest rising searches around a topic, then pull the news that explains each one.

Step 1: Google Trends Scraper returns rising related searches (+growth %).
Step 2: Google News Scraper fetches recent articles for the top rising searches.
The result is a short Markdown briefing you can read, or pass to an LLM to summarize.

Usage:
    python why_is_it_rising.py "electric cars" --geo US --top 3
"""
import argparse
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("topic")
parser.add_argument("--geo", default="US")
parser.add_argument("--top", type=int, default=3, help="How many rising searches to explain")
parser.add_argument("--timeframe", default="today 3-m", help='e.g. "today 1-m", "today 12-m"')
parser.add_argument("--all", action="store_true",
                    help="Keep every rising search. By default only searches sharing a word with the topic are kept, "
                         "because Google's rising list sometimes includes unrelated queries.")
args = parser.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])

trends_run = client.actor("fguiraud/google-trends-scraper").call(run_input={
    "searchTerms": [args.topic],
    "geo": [args.geo],
    "timeframe": args.timeframe,
    "outputs": ["relatedQueries"],
})
rising = []
for item in client.dataset(trends_run.default_dataset_id).iterate_items():
    for related in (item.get("relatedQueries") or {}).values():
        rising += related.get("rising", [])

topic_words = {w for w in args.topic.lower().split() if len(w) > 2}
if not args.all:
    rising = [q for q in rising if topic_words & set(q["query"].lower().split())]
rising = rising[: args.top]
if not rising:
    raise SystemExit("Google reports no rising searches for this topic and period.")

news_run = client.actor("fguiraud/google-news-scraper").call(run_input={
    "queries": [q["query"] for q in rising],
    "timeRange": "7d",
    "maxArticlesPerQuery": 3,
    "country": args.geo,
    "fullText": False,
})
by_query = {}
for a in client.dataset(news_run.default_dataset_id).iterate_items():
    for found in a.get("foundBy") or []:
        by_query.setdefault(found.removeprefix("search: "), []).append(a)

lines = [f"# Why searches around '{args.topic}' are rising ({args.geo})", ""]
for q in rising:
    lines.append(f"## {q['query']} ({q['label']})")
    for a in by_query.get(q["query"], []) or [None]:
        lines.append(f"- [{a['title']}]({a['url']}) ({a.get('source')})" if a else "- No recent news found.")
    lines.append("")

briefing = "\n".join(lines)
print(briefing)
with open("briefing.md", "w", encoding="utf-8") as f:
    f.write(briefing)
