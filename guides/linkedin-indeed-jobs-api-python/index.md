---
title: "LinkedIn and Indeed jobs in one search with Python"
description: "Get job postings listed on LinkedIn, Indeed, Monster and company career sites in one search, with salary ranges as numbers and every apply link, through Google Jobs. No login."
---

# LinkedIn and Indeed jobs in one search

Checking LinkedIn, Indeed and company career pages one by one is slow, and scraping LinkedIn directly needs a login. Google Jobs already collects postings from those sites; this tool returns them as data, and when the same job is listed on several sites you get every link to apply.

## What you get

- One row per job: title, company, location, source (`via`), posting age.
- `applyOptions`: every site where the job is listed (LinkedIn, Indeed...) with its URL.
- Salary range as numbers when published, employment type, highlights and full description.
- Filters by age, type and remote; daily alerts with only new jobs.
- Not a LinkedIn scraper: no applicant counts or recruiter profiles, only what Google Jobs shows.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/job-postings-aggregator").call(run_input={
    "queries": [
        "data analyst"
    ],
    "location": "Chicago",
    "maxJobsPerQuery": 20,
    "maxDaysOld": 7
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["title"], "|", item["company"], "|", [o["source"] for o in item.get("applyOptions") or []])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/job-postings-aggregator), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-24 (long values shortened):

```json
{
  "title": "Data Analyst at Chicago Housing Authority - Chicago, Illinois",
  "company": "Chicago Housing Authority",
  "location": "Chicago, IL (+1 other)",
  "via": "Talent.com",
  "postedAt": "2 days ago",
  "salary": null,
  "salaryMin": null,
  "salaryMax": null,
  "employmentType": "Full-time",
  "applyOptions": [
    {
      "source": "Talent.com",
      "url": "https://www.talent.com/view?id=642864359091735843&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic"
    },
    {
      "source": "Thrife",
      "url": "https://thrife.com/jobs/job/marketing-project-manager-remote-at-lead-with-integrity-chicago-il-YUdmb0NPUzJYeEdZMEljY095ZkxVdDNCSHc9PQ==?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic"
    }
  ]
}
```

## Pricing

$0.003 per job (plus a run start of $0.001 per GB of memory). Failed searches, filtered jobs and jobs already delivered are not charged.

## FAQ

**Does it log in to LinkedIn?**

No. It reads public postings shown on Google Jobs and links to the original listings.

**Which sites appear?**

Whatever Google Jobs indexes for the search: in a Chicago data analyst run, LinkedIn, Indeed, Monster, CareerBuilder, Built In Chicago and company career sites.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/job-postings-aggregator` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [LinkedIn and Indeed jobs in one search](https://apify.com/fguiraud/job-postings-aggregator/examples/linkedin-and-indeed-jobs-in-one-search)

## Related guides

- [Google Jobs API for Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/google-jobs-api-python/)
