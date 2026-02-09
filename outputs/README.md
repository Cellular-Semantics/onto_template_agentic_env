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

1. **Populated Template**
   - Original template format with all missing fields completed
   - Name: `<template_name>_populated.<ext>`

2. **Report Version**
   - Same as populated template, but with additional columns showing term labels for all ontology IDs
   - Validates that IDs are correct using OLS4 MCP
   - Name: `<template_name>_report.<ext>`

3. **Validation Report**
   - Markdown or text file documenting validation results
   - Lists any content that could not be validated
   - Name: `<template_name>_validation.md`

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
