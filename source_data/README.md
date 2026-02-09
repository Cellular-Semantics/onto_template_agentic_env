# Source Data

This folder contains source data, reading materials, and templates for ontology term population.

## Purpose

Store:
- **DOSDP templates**: Dead Simple OWL Design Pattern templates (YAML or TSV format)
- **ROBOT templates**: ROBOT tool templates for ontology term generation
- **Source materials**: Reference documents, existing term lists, CSV files with term data
- **Template extensions**: Modified or extended versions of templates (generated outputs of templates should go in `outputs/`)

## Template Format

Templates typically include:
- Term names or IDs
- Pattern specifications
- Supporting references (Wikipedia, DOI, PMID)
- Existing content to validate
- Fields to populate

## Best Practices

- Name templates descriptively (e.g., `kidney_arteries_dosdp.yaml`, `cell_types_robot.tsv`)
- Include a column for supporting references when possible
- Document the template structure in `Instructions.md`
- Keep original templates separate from populated versions (populated versions go in `outputs/`)

## File Types

Common file types in this folder:
- `.yaml` - DOSDP pattern templates
- `.tsv` / `.csv` - ROBOT templates or data tables
- `.txt` / `.md` - Reference materials and notes
- `.json` - Structured data files
