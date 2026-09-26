"""Convert PDFs, Word, Excel, PowerPoint files or scans to Markdown files.

Usage:
    python pdf_to_markdown.py https://example.com/report.pdf https://example.com/slides.pptx
"""
import os
import re
import sys
from pathlib import Path

from apify_client import ApifyClient

urls = sys.argv[1:]
if not urls:
    raise SystemExit("Pass one or more document URLs (Google Drive, Dropbox and OneDrive share links work).")

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/document-to-markdown-tables").call(run_input={
    "sources": [{"url": u} for u in urls],
    "outputs": ["markdown", "tables"],
    "ocr": "auto",  # OCR only the pages that have no text layer
})

out = Path("markdown")
out.mkdir(exist_ok=True)
for doc in client.dataset(run.default_dataset_id).iterate_items():
    if doc.get("status") != "ok":
        print(f"[failed] {doc['source']}: {doc.get('error')}")  # failed documents are not charged
        continue
    name = re.sub(r"[^A-Za-z0-9.-]+", "_", doc["source"].rsplit("/", 1)[-1])[:80] or "document"
    (out / f"{name}.md").write_text(doc["markdown"], encoding="utf-8")
    s = doc.get("stats", {})
    print(f"[ok] {name}: {s.get('pagesProcessed')} pages, {s.get('tables')} tables, {s.get('ocrPages')} OCR pages")
