# Instructions.md

<!-- Project-specific instructions go here -->

## Persistent Rules For Gene/Protein Mapping

1. For `gene_protein_map.csv`, resolve `pro_id` and `pro_name` using OLS4 via MCP only.
2. Do not infer or construct Protein Ontology IDs from UniProt accessions.
3. For default template population, use gene-level Protein Ontology classes (`PR:000...`), not organism-specific entries (`PR:<UniProt>`).
4. Treat organism-specific PRO terms as optional and include them only if explicitly requested.
5. Every chosen `pro_id` must be auditable from OLS4 MCP output (matched `curie` and label).
6. When helpful, provide the PRO Consortium URL form for verification:
   - `https://proconsortium.org/cgi-bin/entry_pro?id=PR_########`

## Tool Priority — CRITICAL

**Do NOT write Python scripts with `urllib`, `requests`, or `httpx` for network calls — they will fail in sandboxed environments.**

Use **ols4-mcp** and **curl** (via terminal) to query REST APIs directly:

| Task | Use | NOT |
|------|-----|-----|
| Gene/marker synonyms & IDs | **curl** → HGNC REST API, UniProt REST API | ❌ Python urllib/requests |
| Location/anatomy synonyms | **ols4-mcp** → search UBERON/FMA | ❌ Python HTTP calls |
| Protein Ontology IDs | **ols4-mcp** → search PR ontology | ❌ Constructing IDs from UniProt |
| Literature retrieval | **artl-mcp** | ❌ Manual web scraping |
| Validate ontology IDs | **ols4-mcp** → get term by ID | ❌ Hardcoded ID-to-label maps |

## REST API Reference (via curl)

### HGNC — `https://rest.genenames.org/`

**Fetch by HGNC ID:**
```
curl -s 'https://rest.genenames.org/fetch/hgnc_id/HGNC:<id>' -H 'Accept: application/json'
```

**Search by gene symbol:**
```
curl -s 'https://rest.genenames.org/search/<symbol>' -H 'Accept: application/json'
```

**Response path:** `.response.docs[0]` → `hgnc_id`, `symbol`, `name`, `prev_symbol` (array), `alias_symbol` (array), `entrez_id`, `uniprot_ids` (array)

*Note: HGNC provides NCBI Gene ID (`entrez_id`) and UniProt ID (`uniprot_ids`), so a separate NCBI Gene query is usually unnecessary.*

### UniProt — `https://rest.uniprot.org/uniprotkb/search`

**By accession:**
```
curl -s 'https://rest.uniprot.org/uniprotkb/search?query=accession:<uniprot_id>&format=json'
```

**By gene symbol (human, reviewed):**
```
curl -s 'https://rest.uniprot.org/uniprotkb/search?query=gene:<symbol>+AND+organism_id:9606+AND+reviewed:true&format=json'
```

**Response path:** `.results[0]` → `primaryAccession`, `proteinDescription.recommendedName.fullName.value`, gene synonyms from `genes[0].synonyms`

## PRO ID Rules

When searching for Protein Ontology IDs via ols4-mcp:

1. Use `searchClasses` with `ontologyId: "pr"` and `query: "<symbol>"`
2. Find entries with **Category=gene** in description (species-independent, numeric IDs like `PR:000013041`)
3. Do **NOT** pick `Category=organism-gene` entries (UniProt-based IDs like `PR:Q01851`)
4. If symbol is ambiguous (e.g., NOS1 matching "nanos homolog 1"), retry with the HGNC full gene name
5. Always verify the PRO label is semantically related to the gene before accepting

## Output File Specifications

### `outputs/gene_protein_map.csv`

Columns:
- `source_symbol`, `source_id`, `source_symbol_column`, `source_id_column`, `id_type`
- `hgnc_id`, `hgnc_symbol`, `hgnc_name`, `ncbi_gene_id`
- `uniprot_id`, `uniprot_name`
- `pro_id`, `pro_name`
- `all_synonyms` — combined pipe-separated synonyms from ALL sources (HGNC aliases, UniProt names, PRO synonyms)
- `lookup_status`, `error_message`

**IMPORTANT:** The `all_synonyms` column is critical for downstream PDF text searching. Only use synonyms that were fetched from databases — do not guess synonyms from LLM knowledge.

### `outputs/location_synonym_map.csv`

Columns: `ontology_id`, `label`, `all_synonyms`, `lookup_status`

## PDF Validation Rules

When validating marker+location co-occurrence against PDFs:

1. **Use only database-derived synonyms** from `gene_protein_map.csv` and `location_synonym_map.csv`
2. **Match status definitions:**
   - **OK**: Marker AND location found in **same paragraph**
   - **PARTIAL**: Both found but in **different paragraphs**, or only partial location match
   - **NO_MATCH**: Marker or location not found in any PDF
3. Always extract evidence snippets and list matched files

---

## Typical Workflow

### Step 1: Discover Source Files

- Scan `source_data/` for CSV/TSV files
- Read `Instructions.md` for project-specific guidance
- Identify columns: look for `marker`, `marker_ID`, `gene`, `soma_location`, `soma_location_ID`, `references`, etc.

### Step 2: Run Gene/Protein Lookup (if marker/gene columns exist)

- **REQUIRED** when source data contains gene/marker/protein columns
- **Auto-detect** which columns contain gene/marker symbols and IDs from the headers
- For each unique gene/marker, query databases using MCP tools (see REST API Reference above)
- Output: `outputs/gene_protein_map.csv`

### Step 3: Generate Location Synonyms (if location/anatomy columns exist)

- **REQUIRED** when source data contains `soma_location_ID`, `location_ID`, or similar UBERON/FMA columns
- Extract unique ontology IDs from the source file
- For each ID, use **ols4-mcp** to:
  - Get the official label
  - Get all synonyms (exact, related, broad, narrow)
- Output: `outputs/location_synonym_map.csv`

### Step 4: Download References

- Extract DOIs, PMIDs, and URLs from the `references` column
- Use `artl-mcp` to retrieve full text and PDFs
- Save all papers to `pdfs/` folder as `.txt` files
- If PDFs need conversion, use `scripts/extract_pdfs_to_txt.py`

### Step 5: Validate Content Against PDFs (REQUIRED - MAIN DELIVERABLE)

**This is the core validation step. Do NOT skip this.**

Read all `.txt` files in `pdfs/` folder and search for marker+location co-occurrence.

For each term/row in the source data:

1. **Search for marker mentions** in PDF text files in `pdfs/`
   - Use synonyms from `gene_protein_map.csv` (`all_synonyms` column)
   - Only use synonyms that were fetched from databases — do not guess synonyms from memory

2. **Search for location mentions** in PDF text files
   - Use synonyms from `location_synonym_map.csv`
   - Include partial matches (e.g., "DRG" for "dorsal root ganglion")

3. **Determine match status** (see PDF Validation Rules above)

4. **Extract evidence:**
   - `marker_snippet` - text showing marker mention
   - `location_snippet` - text showing location mention
   - `matched_files` - which PDF files contained matches

5. **Generate validation outputs:**
   - `<source_name>_validation_report.md` - per-term details with snippets, match status, matched files
   - `<source_name>_validation_report.csv` - same data in CSV format
   - `executive_summary.md` - summary with OK/PARTIAL/NO_MATCH counts and term lists

**WARNING:** Do not confuse this with "location ID validation" (checking IDs resolve in OLS4). This step requires **searching PDF text content** for marker and location mentions.

### Step 6: Populate Missing Content

- For terms with NO_MATCH or incomplete data, research additional sources
- Use `artl-mcp` to find more references (prioritize reviews)
- Update source data with validated content
- Re-run validation as needed

### Step 7: Additional Research (if requested)

- Search for more supporting references
- Repeat validation steps for new references

---

## Tool Reference

### ols4-mcp (Ontology Lookup)

**Key operations:**
- `searchClasses({ontologyId: "pr", query: "<symbol>", pageSize: 10})` — search Protein Ontology
- `searchClasses({ontologyId: "uberon", query: "<term>", pageSize: 10})` — search anatomy
- `getClass({ontologyId: "uberon", classId: "UBERON:0002834"})` — get term details + synonyms

**Supported ontologies:** UBERON, FMA, CL, GO, PR

### artl-mcp (Literature)

Search Europe PMC, retrieve abstracts, full text, and PDFs by DOI or PMID.

### playwright MCP (optional fallback)

Only needed if REST APIs are insufficient (e.g., NCBI Gene pages with no REST equivalent).
- `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`
- Note: browser binary may need installation (`npx playwright install chromium`) in some environments

**Database URLs (if using playwright instead of curl):**

1. **HGNC** — `https://www.genenames.org/tools/search/#!/?query=<symbol>`
   - Navigate → click gene row → extract from report page: HGNC ID, symbol, name, aliases, NCBI Gene ID, UniProt ID

2. **NCBI Gene** — `https://www.ncbi.nlm.nih.gov/gene/?term=<symbol>+AND+human[orgn]`
   - Navigate → click top human result → extract: Gene ID, full name, "Also known as"

3. **UniProt** — `https://www.uniprot.org/uniprotkb?query=gene:<symbol>+AND+organism_id:9606`
   - Navigate → click top reviewed result → extract: accession, protein names, gene name synonyms

### Optional: Subagents (Claude Code only)

If running in Claude Code, subagents at `.claude/agents/` wrap the above tools:
- `gene-protein-lookup.md` — wraps curl + ols4-mcp for gene→protein mapping
- `ontology-term-lookup.md` — wraps ols4-mcp for ontology term lookups

---

## Current Project

<!-- Describe the template(s) you are working with -->

## Template State

<!-- Describe what fields are populated vs. need to be filled -->

## Special Requirements

<!-- Any constraints, preferences, or notes for the agent -->
