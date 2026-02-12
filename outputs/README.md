# Outputs

This folder contains all generated outputs from the template population and validation process.

## Purpose

Store generated files including:
- **Populated templates**: Templates with all fields filled in
- **Report versions**: Template copies with ontology term labels adjacent to ID columns
- **Validation reports**: Detailed validation results for each term
- **Explanation reports**: Justifications for content with supporting references

## Required Output Types

For each template processing run, generate:

1. **Gene/Protein Map** (if source has marker/gene columns)
   - `gene_protein_map.csv` — mapping of all markers to HGNC, NCBI, UniProt, PRO IDs with synonyms
   - `gene_protein_map_report.md` — summary of lookup results

2. **Location Synonym Map** (if source has location/anatomy columns)
   - `location_synonym_map.csv` — ontology IDs with labels and all synonyms from OLS4

3. **Validation Report**
   - `<source_name>_validation_report.md` — per-term validation with text snippets and match status
   - `<source_name>_validation_report.csv` — same data in CSV format
   - `executive_summary.md` — OK/PARTIAL/NO_MATCH counts

4. **Populated Template**
   - Original template format with all missing fields completed
   - Name: `<template_name>_populated.<ext>`

5. **Report Version**
   - Same as populated template, but with additional columns showing term labels for all ontology IDs
   - Validates that IDs are correct using OLS4 MCP
   - Name: `<template_name>_report.<ext>`

4. **Explanation Report**
   - Entry for each term with:
     - Validation results
     - Explanation of added/modified content
     - Text excerpts from references supporting the content
   - Name: `<template_name>_explanation.md`

## Organization

For large projects, consider organizing outputs by date or template name:

```
outputs/
├── 2026-02-09_kidney_arteries/
│   ├── kidney_arteries_populated.tsv
│   ├── kidney_arteries_report.tsv
│   ├── kidney_arteries_validation.md
│   └── kidney_arteries_explanation.md
└── ...
```

## Note

Template extensions (modified DOSDP/ROBOT templates themselves) should go in `source_data/`, not here.
