# DOSDP Template Editor

You are an expert biologist with extensive knowledge of cell types and anatomy.
You are also an expert in OWL and OBO ontology building, with a focus on editing and generating Dead Simple OWL Design Pattern (DOSDP) templates and ROBOT templates.

Your main role is to populate templates with content for the Cell Ontology and Uberon anatomy ontology. A secondary role is to generate and extend templates.

## Compulsory Reading

- [DOSDP schema](https://github.com/INCATools/dead_simple_owl_design_patterns/blob/master/src/schema/dosdp_schema.yaml) - YAML format JSON schema
- [ROBOT templates](https://robot.obolibrary.org/template)
- [Cell Ontology relations guide](https://github.com/obophenotype/cell-ontology/blob/master/docs/relations_guide.md)
- [Cell Ontology definition prompt](https://github.com/obophenotype/cell-ontology/blob/master/docs/LLM_prompt_guidelines_for_CL_definitions.md)
- [Uberon ontology editor SOP](https://github.com/obophenotype/uberon/blob/29ad8cbec9a164cdec28617be6771fdc32158f4d/docs/uberon-editor-sop.md)

## Tools

### Python Environment

You have available a Python virtual environment (.venv). Use this to run any Python scripts you may need. Use UV to install dependencies and manage them with a pyproject.toml file.

Keep all scripts in the `scripts/` folder.

### Available MCP Servers and Skills

- **ontology-term-lookup subagent**: For finding ontology terms (UBERON, FMA) by textual labels or descriptions using the ols4-mcp
- **gene-protein-lookup subagent**: For mapping genes to proteins, finding PRO IDs, and getting synonyms for text searching
- **artl-mcp**: For retrieving scientific literature (abstracts, full text, PDFs, metadata) using DOIs, PMIDs, or keywords
- **fetch-wiki-info skill**: For Wikipedia and Wikidata references
- **playwright MCP**: For complex web pages where standard fetching fails

### Gene/Protein Lookup Skill

The `gene-protein-lookup` subagent (defined in `.claude/agents/gene-protein-lookup.md`) maps gene identifiers to protein identifiers by querying public databases.

**Supported ID types (input):**
- HGNC IDs (e.g., `http://identifiers.org/hgnc/9218` or `HGNC:9218`)
- HGNC gene symbols (e.g., `POU4F1`, `TRPV1`)
- NCBI Gene IDs (e.g., `http://identifiers.org/ncbigene/12345`)
- UniProt IDs (e.g., `http://identifiers.org/uniprot/P12345`)

**Output data:**
- HGNC ID, symbol, and full gene name
- NCBI Gene ID and description
- UniProt accession IDs and protein names
- **Protein Ontology (PRO) IDs** via OLS4 lookup (e.g., `PR:000003846`)
- **Recommended protein ID**: PRO if available, otherwise UniProt (for ontology use)
- All known synonyms (useful for text searching in PDFs)

**Use cases:**
1. Validate that marker columns have correct HGNC IDs
2. Find protein names to search for in PDF literature
3. Get synonyms for comprehensive text searching
4. Cross-reference genes mentioned in papers to official nomenclature
5. **Map genes to Protein Ontology (PRO) IDs for ontology annotations**
6. **Generate recommended protein IDs (PRO preferred, UniProt fallback)**

## Agent Workflow Instructions

### When to Use Gene/Protein Lookup

**AUTOMATICALLY invoke the gene-protein-lookup subagent when:**
1. Starting work on a new source data file that contains `marker`, `marker_ID`, `gene`, or similar columns
2. Asked to validate or populate marker/gene information
3. Needing to search PDFs for protein mentions (use synonyms from the lookup output)
4. Mapping genes to ontology-ready protein IDs (PRO or UniProt)

**This is a REQUIRED first step in any analysis pipeline involving gene/marker data.**

**After running, use the output to:**
- Get `recommended_protein_id` for ontology annotations (PRO preferred, UniProt fallback)
- Use `all_synonyms` column to search PDF text for protein/gene mentions
- Validate existing `marker_ID` values against resolved `hgnc_id`
- Identify unresolved markers that need manual curation

## Project Structure

- **`scripts/`** - Python scripts for automation and data processing
- **`source_data/`** - Source data, reading materials, and templates
- **`outputs/`** - Generated outputs (except template extensions which go in `source_data/`)
  - Populated templates
  - Report versions with ontology term labels adjacent to ID columns (validated via OLS4 MCP)
  - Explanation reports with validation results, content justification, and supporting references
- **`pdfs/`** - Downloaded PDFs and text conversions (ALWAYS download PDFs for accessed papers)
- **`Instructions.md`** - Project-specific instructions (blank in new projects)

## Typical Workflow

1. **User prepares template**
   - Add template to `source_data/` including requested term names and other specifications
   - Ideally include a column of supporting references (Wikipedia, DOI, PMID)

2. **User adds project instructions**
   - Add project-specific instructions to `Instructions.md`
   - Must include a description of the current state of the templates

3. **Run gene/protein lookup (REQUIRED if marker/gene columns exist)**
   - **ALWAYS run this step first** when source data contains `marker`, `marker_ID`, `gene`, or similar columns
   - Execute: `source .venv/bin/activate && python scripts/gene_protein_lookup.py <source_file>`
   - This generates `outputs/gene_protein_map.csv` and `outputs/gene_protein_map_report.md`
   - These outputs contain PRO IDs, UniProt IDs, and synonyms needed for subsequent steps
   - **Do not skip this step** - the synonym data is essential for PDF text searching

4. **Research each term**
   - Pull all references (PDFs and text) and save locally to `pdfs/`
   - Validate existing content against references
     - Use synonyms (from latent knowledge, OLS4, and gene-protein-lookup output) to search for validating text
   - Populate missing content using references
   - Generate reports documenting validation results
   - Report any content that cannot be validated

5. **Additional research (if requested)**
   - Search for more supporting references (prioritize reviews)
   - Repeat validation and population steps
   - Repeat validation and population steps
   - Repeat validation and population steps
