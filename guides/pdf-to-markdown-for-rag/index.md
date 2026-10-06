---
title: "PDF to Markdown for RAG and LLMs (tables, OCR, Word, Excel)"
description: "Convert PDF, Word, Excel, PowerPoint and scanned documents to clean Markdown, tables and RAG chunks with page numbers. OCR included, $0.003 per document."
---

# PDF to Markdown for RAG and LLMs

LLMs read Markdown far better than raw PDF text: headings, lists and tables survive. This tool converts documents in bulk and can split them into chunks with page numbers.

## What you get

- PDF (native or scanned), DOCX, XLSX, PPTX, HTML, CSV, images.
- Google Drive, Dropbox and OneDrive share links.
- Markdown, tables as rows, text per page, RAG chunks.
- OCR in 7 languages; headers and footers removed.

## Python example

```python
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fguiraud/document-to-markdown-tables").call(run_input={
    "sources": [
        {
            "url": "https://arxiv.org/pdf/1706.03762"
        }
    ],
    "outputs": [
        "markdown",
        "chunks"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["source"], item["stats"])
    print(item["markdown"][:500])
```

No Python? Open the [Actor page](https://apify.com/fguiraud/document-to-markdown-tables), paste your input in the form and press Start; results export to JSON, CSV or Excel.

## Real output

Fields from a real run on 2026-09-29 (long values shortened):

```json
{
  "source": "https://raw.githubusercontent.com/jsvine/pdfplumber/stable/examples/pdfs/background-checks.pdf",
  "status": "ok",
  "fileType": "pdf",
  "stats": {
    "pagesProcessed": 1,
    "ocrPages": 0,
    "tables": 1,
    "characters": 5650
  },
  "markdown": "| NICS Firearm Background Checks November - 2015 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |...",
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
  ]
}
```

## Pricing

$0.003 per document + $0.001 per run. OCR pages $0.01 each.

| Tool | Price |
|---|---|
| This tool | $0.003 per document, Markdown + tables + Office files |
| memo23/pdf-text-extractor | $0.005 + $0.005 start |
| gochujang/pdf-text-extractor | $0.02 + $0.001 per page |

Competitor prices as listed in the Apify Store on 2026-10-03 (Bronze plan where tiers differ); they can change.

## FAQ

**Scanned PDFs?**

OCR runs automatically on pages without a text layer (`ocr: "auto"`).

**Can it extract specific fields like invoice totals?**

Yes, with `extractionFields` and your own Anthropic API key.

**Can an AI agent use it?**

Yes. It is an MCP server at `https://mcp.apify.com/?tools=fguiraud/document-to-markdown-tables` (listed in the official MCP registry), and there is an [agent skill](https://github.com/fernandoguiraud16-coder/data-tools/tree/main/skills) for Claude Code, Codex and Cursor. Field-name guesses such as `url` or `urls` are accepted.

## Ready-made examples

- [Convert PDF to Markdown for RAG and LLMs](https://apify.com/fguiraud/document-to-markdown-tables/examples/pdf-to-markdown-for-rag)
- [Extract text from scanned PDFs with OCR](https://apify.com/fguiraud/document-to-markdown-tables/examples/extract-text-from-scanned-pdf-ocr)
- [PDF to chunks for RAG](https://apify.com/fguiraud/document-to-markdown-tables/examples/pdf-to-chunks-for-rag)

## Related guides

- [PDF tables to Excel and CSV](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-table-extraction-excel/)
- [Extract text from PDFs in Python](https://fernandoguiraud16-coder.github.io/data-tools/guides/pdf-text-extraction-python/)
