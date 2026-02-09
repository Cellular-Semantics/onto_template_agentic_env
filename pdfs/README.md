# PDFs

This folder contains downloaded scientific papers and their text conversions.

## Purpose

Store all referenced scientific literature:
- **PDF files**: Original papers in PDF format
- **Text conversions**: Extracted text from PDFs or retrieved from Europe PMC
- **Markdown conversions**: Papers converted to markdown for easier AI processing

## Important Guidelines

**ALWAYS download PDFs for papers you access**. This ensures:
- Reproducibility of research
- Offline access to references
- Compliance with documentation requirements
- Permanent local copies even if sources change

## File Naming

Use consistent naming conventions:
- PDFs: `PMID_<id>.pdf` or `DOI_<doi_with_underscores>.pdf`
- Text: `PMID_<id>.txt` or `DOI_<doi_with_underscores>.txt`
- Markdown: `PMID_<id>.md` or `DOI_<doi_with_underscores>.md`

Examples:
- `PMID_12345678.pdf`
- `DOI_10.1038_nature12345.pdf`
- `PMID_12345678_fulltext.txt`

## Organization

For large projects with many papers, consider organizing by topic:

```
pdfs/
├── kidney_arteries/
│   ├── PMID_12345678.pdf
│   ├── PMID_12345678.txt
│   └── ...
├── cell_types/
│   └── ...
└── README.md
```

## Sources

Papers are typically retrieved using:
- **ARTL MCP**: Europe PMC API for full text and PDFs
- **DOI resolution**: Direct PDF downloads from publishers
- **Manual downloads**: For papers not available via automated tools

## Text Extraction

Text can be extracted via:
- ARTL MCP's PDF-to-markdown conversion
- Europe PMC full text API
- OCR for scanned documents
