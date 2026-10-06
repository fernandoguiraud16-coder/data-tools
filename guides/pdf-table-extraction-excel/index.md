---
title: "Extract tables from PDF to Excel, CSV and JSON (with OCR)"
description: "Extract every table from PDFs and scans into Excel (one sheet per table), CSV and JSON. Multi-page tables merged, OCR for scans, $0.003 per document."
---

# Extract tables from PDF to Excel and CSV

Copying tables out of PDFs breaks columns. This tool detects each table, keeps rows and columns, and saves an Excel workbook you can download.

## What you get

- Every table as header + rows, with its page number.
- Excel workbook (one sheet per table) and CSV files with `saveFiles`.
- Ruled and borderless tables (`tableDetection`), scanned pages with OCR.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/pdf-table-extractor").call(run_input={
    "sources": [
        {
            "url": "https://raw.githubusercontent.com/jsvine/pdfplumber/stable/examples/pdfs/background-checks.pdf"
        }
    ],
    "saveFiles": True
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    for table in item["tables"]:
        print(table["page"], table["header"])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/pdf-table-extractor), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-10-01 (long values shortened):

```json
{
  "source": "https://raw.githubusercontent.com/jsvine/pdfplumber/stable/examples/pdfs/background-checks.pdf",
  "status": "ok",
  "tableCount": 1,
  "pagesProcessed": 1,
  "tables": [
    {
      "index": 0,
      "page": 1,
      "header": [
        "NICS Firearm Background Checks November - 2015",
        "",
        "",
        "..."
      ],
      "rows": [
        [
          "State / Territory",
          "Permit Handgun Long Gun *Other **Multiple Admin",
          "",
          "..."
        ],
        [
          "",
          "",
          "",
          "..."
        ],
        [
          "Alabama",
          "18,870",
          "23,022",
          "..."
        ],
        "..."
      ],
      "csv": "NICS Firearm Background Checks November - 2015,,,,,,,,,,,,,,,,,,,,,,,,\nState / Territory,Permit Handgun Long Gun *Other **Multiple Admin,,,,,,Pre-Pawn,,,Redemption,,,Returned/Disposition,,,Rentals,,Private Sale,,,Return..."
    }
  ],
  "files": {
    "tables": [
      "https://api.apify.com/v2/key-value-stores/yBL90wQZMyIloRpUY/records/001-background-checks-table-1.csv?signature=1lTVlAs5h5Hph1kfJpvAp"
    ],
    "xlsx": "https://api.apify.com/v2/key-value-stores/yBL90wQZMyIloRpUY/records/001-background-checks-tables.xlsx?signature=3uLdDUE8rTuwRNVLcbQm"
  }
}
```

## Pricing

$0.003 per document.

## FAQ

**Bank statements and invoices?**

Yes if the table is visible in the PDF; scans go through OCR.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/pdf-table-extractor` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Extract tables from PDF to CSV and JSON](https://apify.com/fguiraud/pdf-table-extractor/examples/extract-tables-from-pdf-to-csv)
- [Extract tables from scanned PDFs](https://apify.com/fguiraud/pdf-table-extractor/examples/extract-tables-from-scanned-pdf)
- [PDF tables to Excel](https://apify.com/fguiraud/pdf-table-extractor/examples/pdf-tables-to-excel)
- [Extract tables from many PDFs](https://apify.com/fguiraud/pdf-table-extractor/examples/bulk-pdf-table-extraction)

## Related guides

- [PDF to Markdown for RAG](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-to-markdown-for-rag/)
- [Extract text from PDFs in Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-text-extraction-python/)
