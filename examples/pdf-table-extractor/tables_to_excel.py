"""Extract every table from PDFs and download one Excel workbook per document (one sheet per table).

Usage:
    python tables_to_excel.py https://example.com/annual-report.pdf
"""
import os
import sys
import urllib.request

from apify_client import ApifyClient

urls = sys.argv[1:]
if not urls:
    raise SystemExit("Pass one or more PDF / DOCX / XLSX / HTML URLs.")

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/pdf-table-extractor").call(run_input={
    "sources": [{"url": u} for u in urls],
    "saveFiles": True,          # adds download links for .xlsx and .csv files
    "tableDetection": "lines",  # use "text" for tables without any lines (experimental)
})

for i, doc in enumerate(client.dataset(run.default_dataset_id).iterate_items(), 1):
    print(f"{doc['source']}: {doc.get('tableCount', 0)} tables")
    xlsx = (doc.get("files") or {}).get("xlsx")
    if xlsx:
        name = f"tables-{i}.xlsx"
        urllib.request.urlretrieve(xlsx, name)
        print(f"  saved {name}")
    for t in doc.get("tables", [])[:3]:
        print(f"  page {t['page']}: {len(t['rows'])} rows x {len(t['header'])} columns")
