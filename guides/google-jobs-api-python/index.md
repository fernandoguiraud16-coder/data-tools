---
title: "Google Jobs API for Python: listings, salaries and apply links"
description: "Scrape Google Jobs in Python: postings from LinkedIn, Indeed, ZipRecruiter and company sites with salary ranges as numbers, highlights, full description and every apply link."
---

# Google Jobs API for Python

Google Jobs gathers postings from LinkedIn, Indeed, ZipRecruiter, Monster and company career sites in one search, but it renders only for real browsers and has no API. This tool returns each job as data, with the salary range split into numbers and the real URLs to apply.

## What you get

- Title, company, location, source (`via`), posting age in days.
- `salaryMin`, `salaryMax`, `salaryPeriod`, `salaryCurrency` parsed from the text.
- Employment type, Qualifications / Responsibilities / Benefits, full description.
- Every apply link with its source.
- Filters by age and type (filtered jobs are free) and daily alerts with only new jobs.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client (3.x)

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/google-jobs-scraper").call(run_input={
    "queries": [
        "python developer"
    ],
    "location": "New York",
    "maxJobsPerQuery": 30,
    "maxDaysOld": 7
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["title"], "|", item["company"], "|", item.get("salary"), "|", item["applyUrl"])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/google-jobs-scraper), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-23 (long values shortened):

```json
{
  "title": "Python Fastapi with React AI/Agentic AI developers",
  "company": "Logicplanet, Inc.",
  "location": "New York, NY",
  "via": "Dice",
  "postedAt": "2 days ago",
  "salary": null,
  "salaryMin": null,
  "salaryMax": null,
  "salaryPeriod": null,
  "employmentType": "Contractor",
  "applyUrl": "https://www.dice.com/job-detail/95a6c0de-dd14-4fbc-9b16-1fd72420ad04?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
  "highlights": {
    "Qualifications": [
      "We are looking for an experienced Full Stack Developer with strong expertise in Python backend development and React frontend development",
      "The ideal candidate will be responsible for designing, developing, testing, and maintaining scalable web applications and APIs",
      "Strong experience in Python and backend development",
      "..."
    ],
    "Responsibilities": [
      "Develop and maintain robust backend applications using Python",
      "Build scalable RESTful APIs and backend services",
      "Develop responsive and user-friendly web applications using React.js",
      "..."
    ]
  }
}
```

## Pricing

$0.003 per job. Failed searches, filtered jobs and jobs already delivered (only new jobs) are not charged.

| Tool | Price |
|---|---|
| This tool | $0.003 per job, salary as numbers, all apply links |
| johnvc/Google-Jobs-Scraper | $0.09 per page of results |
| gio21/google-jobs-scraper | $0.003 per job |
| automation-lab/google-jobs-scraper | $0.006 per job |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**How many jobs per search?**

Google shows 10 per search; related searches (contract type, seniority, remote) bring it to about 30-50 different jobs.

**Is the salary always there?**

Only when the employer or job board publishes it.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/google-jobs-scraper` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Jobs by title and city](https://apify.com/fguiraud/google-jobs-scraper/examples/jobs-by-title-and-city)
- [Daily job alerts (only new postings)](https://apify.com/fguiraud/google-jobs-scraper/examples/daily-job-alerts-only-new)
- [Remote jobs with salary ranges](https://apify.com/fguiraud/google-jobs-scraper/examples/remote-jobs-with-salary)
- [Jobs from LinkedIn, Indeed and company sites in one search](https://apify.com/fguiraud/google-jobs-scraper/examples/jobs-from-linkedin-and-indeed)

## Related guides

- [Google Hotels API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-hotels-api-python/)
- [LinkedIn and Indeed jobs in one search](https://fernandoguiraud16-coder.github.io/data-tools/guides/linkedin-indeed-jobs-api-python/)
