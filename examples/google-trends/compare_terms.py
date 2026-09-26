"""Compare search interest for several terms and save the weekly series to CSV.

Usage:
    export APIFY_TOKEN=your_token      # Windows PowerShell: $env:APIFY_TOKEN="your_token"
    python compare_terms.py "chatgpt, gemini, claude" --geo US --timeframe "today 12-m"
"""
import argparse
import csv
import os

from apify_client import ApifyClient

ACTOR = "fguiraud/google-trends-scraper"

parser = argparse.ArgumentParser()
parser.add_argument("terms", help='Up to 5 terms separated by commas, e.g. "chatgpt, gemini"')
parser.add_argument("--geo", default="US", help="Country code, or empty for worldwide")
parser.add_argument("--timeframe", default="today 12-m", help='e.g. "today 3-m", "today 5-y"')
parser.add_argument("--out", default="interest_over_time.csv")
args = parser.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor(ACTOR).call(run_input={
    "searchTerms": [args.terms],  # one comparison: all terms on the same 0-100 scale
    "geo": [args.geo],
    "timeframe": args.timeframe,
    "outputs": ["interestOverTime", "relatedQueries"],
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("type") != "explore":
        continue
    if item.get("status") != "ok":
        print(f"No data: {item.get('note') or item.get('error')}")
        continue

    print(f"\nTrend summary ({item['geo'] or 'worldwide'}, {item['timeframe']}):")
    for term, s in item["summary"].items():
        print(f"  {term:<12} {s['trend']:<8} change {s['changePercent']:+.0f}%  peak {s['peakDate'][:10]}")

    print("\nFastest rising related searches:")
    for term, related in item["relatedQueries"].items():
        for q in related.get("rising", [])[:3]:
            print(f"  [{term}] {q['query']} ({q['label']})")

    terms = item["terms"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", *terms])
        for point in item["interestOverTime"]:
            writer.writerow([point["date"][:10], *(point["values"].get(t) for t in terms)])
    print(f"\nSaved {len(item['interestOverTime'])} rows to {args.out}")
