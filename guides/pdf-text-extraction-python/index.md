---
title: "Extract text from PDF in Python: per page, metadata and OCR"
description: "Extract the text of PDFs in bulk with Python: full text, text per page, title, author and page count, with OCR for scanned PDFs. $0.003 per document."
---

# Extract text from PDFs in Python

`pypdf` and `pdfminer` return nothing for scanned pages and need care with layout. This tool returns the text of each page, the metadata, and reads scans with OCR automatically.

## What you get

- Full text and text per page with page numbers.
- Title, author, language, page count.
- OCR for scanned pages in 7 languages (`ocr: "auto"`).
- PDF links, share links, or base64 uploads; many files per run.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/pdf-text-extractor").call(run_input={
    "sources": [
        {
            "url": "https://www.irs.gov/pub/irs-pdf/fw9.pdf"
        }
    ],
    "outputs": [
        "text",
        "pages"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    for page in item["pages"]:
        print(page["page"], page["text"][:100])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/pdf-text-extractor), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-04 (long values shortened):

```json
{
  "source": "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
  "status": "ok",
  "fileType": "pdf",
  "pageCount": 6,
  "title": "Form W-9 (Rev. March 2024)",
  "author": "SE:W:CAR:MP",
  "language": "en",
  "characters": 37694,
  "ocrPages": 0,
  "text": "W-9\nRequest for Taxpayer\nForm Give form to the\n(Rev. March 2024) Identification Number and Certification requester. …",
  "pages": [
    { "page": 1, "text": "W-9\nRequest for Taxpayer …", "ocr": false },
    { "page": 2, "text": "Form W-9 (Rev. 3-2024) Page 2\nmust obtain your correct taxpayer identification number (TIN) …", "ocr": false }
  ],
  "metadata": {
    "subject": "Request for Taxpayer Identification Number and Certification",
    "creator": "Designer 6.5",
    "created": "2024-03-06T08:18:13",
    "modified": "2024-03-06T08:18:13",
    "pageCount": 6
  }
}
```

## Pricing

$0.003 per document.

| Tool | Price |
|---|---|
| This tool | $0.003 per document, OCR included |
| automation-lab/pdf-text-extractor | $0.003 + $0.005 start, no OCR |
| memo23/pdf-text-extractor | $0.005 + $0.005 start |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**Password-protected PDFs?**

Pass the password in `pdfPassword`.

**Only some pages?**

Use `pageRange`, e.g. `"1-3, 7"`.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/pdf-text-extractor` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Extract text from a PDF](https://apify.com/fguiraud/pdf-text-extractor/examples/extract-text-from-pdf)
- [Scanned PDF to text (OCR)](https://apify.com/fguiraud/pdf-text-extractor/examples/scanned-pdf-to-text-ocr)
- [PDF pages to JSON](https://apify.com/fguiraud/pdf-text-extractor/examples/pdf-pages-to-json)

## Related guides

- [PDF to Markdown for RAG](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-to-markdown-for-rag/)
- [PDF tables to Excel and CSV](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-table-extraction-excel/)
