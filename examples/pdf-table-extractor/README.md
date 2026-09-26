# Extract PDF tables to Excel in Python

Get every table in a PDF as an **Excel workbook with one sheet per table**, plus CSV and JSON, through the [PDF Table Extractor](https://apify.com/fguiraud/pdf-table-extractor) Actor. Scanned PDFs are handled with OCR.

```bash
python tables_to_excel.py https://raw.githubusercontent.com/jsvine/pdfplumber/stable/examples/pdfs/background-checks.pdf
```

Real output (a 25-column FBI statistics table):

```text
https://raw.githubusercontent.com/jsvine/pdfplumber/stable/examples/pdfs/background-checks.pdf: 1 tables
  saved tables-1.xlsx
  page 1: 59 rows x 25 columns
```

## Good for

- Financial statements and annual reports.
- Government statistics and price lists.
- Scientific papers (tables with only horizontal lines).

Tips: numbers stay numbers in Excel (`1,234.5` → 1234.5), and multi-page tables with a repeated header come back as one table. For tables without any lines, set `"tableDetection": "text"`.

Full field reference: [`sample-output.json`](sample-output.json) and the [Actor page](https://apify.com/fguiraud/pdf-table-extractor).
