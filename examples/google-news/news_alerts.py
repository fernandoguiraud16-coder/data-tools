"""News alerts: print only the articles that are new since the last run.

Run it on a schedule (cron, Task Scheduler, or an Apify schedule on the Actor itself).
The Actor remembers what it already returned, so you only pay for new stories.

Usage:
    python news_alerts.py "your company name" "your competitor"
"""
import os
import sys

from apify_client import ApifyClient

queries = sys.argv[1:] or ["apify"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/google-news-scraper").call(run_input={
    "queries": queries,
    "timeRange": "1d",
    "maxArticlesPerQuery": 50,
    "onlyNewArticles": True,  # skip articles returned by earlier runs
    "fullText": False,        # headlines only: faster and half the price
})

articles = list(client.dataset(run.default_dataset_id).iterate_items())
if not articles:
    print("No new articles since the last run.")
for a in articles:
    found_by = ", ".join(a.get("foundBy") or [])
    print(f"- [{found_by}] {a['title']} ({a.get('source')})\n  {a['url']}")

# Send `articles` to Slack, email or a webhook here.
