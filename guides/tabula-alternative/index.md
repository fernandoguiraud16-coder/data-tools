---
title: "Tabula alternative: PDF tables to Excel without Java, with OCR"
description: "tabula-py needs Java and cannot read scanned PDFs. Extract PDF tables to Excel, CSV and JSON through an API, with OCR for scans, $0.003 per document."
---

# A Tabula alternative for PDF tables

`tabula-py` wraps the Java tool Tabula, so it needs a Java runtime, and it only reads PDFs that have a text layer: scanned tables come back empty. This tool runs in the cloud, reads scans with OCR, and returns every table with its page number plus an Excel workbook.

## What you get

- Ruled and borderless tables (`tableDetection`: `lines` or `text`).
- OCR for scanned pages (7 languages).
- Excel workbook (one sheet per table), CSV files and JSON rows.
- Many PDFs per run; no Java or local install.

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
        print(table["page"], len(table.get("rows", [])), "rows")
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

**Can I choose pages?**

Yes, with `pageRange`, e.g. `"2-4"`.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/pdf-table-extractor` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Extract tables from PDF to CSV and JSON](https://apify.com/fguiraud/pdf-table-extractor/examples/extract-tables-from-pdf-to-csv)
- [Extract tables from scanned PDFs](https://apify.com/fguiraud/pdf-table-extractor/examples/extract-tables-from-scanned-pdf)
- [PDF tables to Excel](https://apify.com/fguiraud/pdf-table-extractor/examples/pdf-tables-to-excel)
- [Extract tables from many PDFs](https://apify.com/fguiraud/pdf-table-extractor/examples/bulk-pdf-table-extraction)

## Related guides

- [PDF tables to Excel and CSV](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-table-extraction-excel/)
- [PDF to Markdown for RAG](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-to-markdown-for-rag/)
