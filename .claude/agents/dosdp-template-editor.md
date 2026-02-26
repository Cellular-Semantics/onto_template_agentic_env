---
name: dosdp-template-editor
description: Reads DOSDP pattern files (YAML) and data tables (TSV), populates data rows with validated ontology term data, and validates var values against pattern constraints. Use this agent when the user provides a DOSDP pattern + data TSV that needs to be filled in.
model: sonnet
---

# DOSDP Data Table Editor Agent

This agent reads DOSDP pattern files (YAML) and their corresponding data tables (TSV) from `source_data/`, populates data rows with validated term data provided from upstream research (e.g. CL-curator-research output), and writes populated outputs with validation reports.

**MVP scope**: Fill existing data rows only. Pattern extension (modifying the YAML) is a post-MVP goal (see ROADMAP.md).

## Compulsory Reading

Before working on any template, fetch and read:

- [DOSDP schema](https://github.com/INCATools/dead_simple_owl_design_patterns/blob/master/src/schema/dosdp_schema.yaml) — YAML schema defining all valid pattern fields
- `docs/relations_guide.md` — which OWL relations to use and their correct ranges
- `docs/LLM_prompt_guidelines_for_CL_definitions.md` — definition structure and content standards

## Tools Available

- **ontology-term-lookup subagent**: Validate ontology IDs and find terms by label. Use this for every `var` value that is an ontology ID.
- **artl-mcp**: Retrieve literature if additional evidence is needed for a field.
- **fetch-wiki-info skill**: Retrieve Wikipedia/Wikidata references.

## Step 1: Parse the DOSDP Pattern File

Read the YAML pattern file from `source_data/`. Extract the following fields:

### Key YAML Fields to Parse

```yaml
pattern_name:       # name of the pattern
description:        # description of what the pattern represents

classes:            # named ontology classes used in the pattern (constants)
relations:          # named relations used in the pattern (constants)

vars:               # ontology ID variables — each has a range constraint
  <var_name>: "'<range_class>'"   # e.g. location: "'anatomical structure'"

data_vars:          # free-text variables (no ontology constraint)
  <var_name>: xsd:string

annotations:        # OWL annotations added to the defined class
  - annotationProperty: <property>
    text: "<template string with %s placeholders>"
    vars:
      - <var_name>

data_list_annotations:   # like annotations but use a list of values
  - annotationProperty: <property>
    value: <var_name>

logical_axioms:     # SubClassOf / EquivalentTo axioms
  - axiom_type: equivalentTo | subClassOf
    text: "<template string>"
    vars:
      - <var_name>
```

### Output of Parsing

Produce a structured summary:

```
Pattern: <pattern_name>
Vars (ontology IDs):
  - <var_name>: range = <range_class>
  - ...
Data vars (free text):
  - <var_name>: xsd:string
  - ...
Annotations:
  - <property>: "<template>"
Logical axioms:
  - <axiom_type>: "<template>"
```

## Step 2: Read the Data Table

The data TSV has one column per variable defined in the pattern, plus a `defined_class` column for the OBO ID of the new term being defined.

**Required columns:**
- `defined_class` — OBO ID for the term (e.g. `CL:0000001`)
- One column per `var` and `data_var` from the YAML

**Assess each row:**
- **Populated and valid**: has content — validate ontology ID vars against OLS4
- **Empty and required**: missing content in a required column
- **Empty and optional**: missing content in an optional column

Produce a brief assessment summary before filling:

```
Data table: <filename>
Terms: <N> rows
Columns requiring population: [list]
Vars needing OLS4 validation: [list]
```

## Step 3: Validate Existing Data

For every `var` column cell (ontology ID):

1. Use **ontology-term-lookup subagent** to verify:
   - The ID exists in OLS4
   - The term's label matches what is expected
   - The term falls within the range specified in the YAML `vars` section
2. Record validation results in the validation report.

For `data_var` columns (free text):

- Check definitions conform to `docs/LLM_prompt_guidelines_for_CL_definitions.md`
- Check that synonym text is appropriate

## Step 4: Fill Missing Cells

For each empty cell:

1. Use the term data provided by the user or from CL-curator-research output.
2. For `var` columns (ontology IDs): use **ontology-term-lookup** to find the correct ID within the specified range from the YAML.
3. For `data_var` columns (free text): use provided term data; follow `docs/LLM_prompt_guidelines_for_CL_definitions.md` for definitions.
4. For `defined_class`: populate with the OBO ID for the new term if available; otherwise flag as missing.

**Flag** any cell where:
- No data is available to fill it
- A term cannot be found in OLS4 within the specified range
- Multiple candidate IDs exist and the correct one is ambiguous

## Step 5: Generate Outputs

Write all outputs to `outputs/<project_name>/` where `<project_name>` is derived from the pattern name or `Instructions.md`.

### 1. Populated Data Table (`<name>_populated.tsv`)

The filled TSV with all populated cells. Preserve original column order exactly. Do not add or remove columns.

### 2. Report Version (`<name>_report.tsv`)

Same as the populated data table but with an additional label column inserted immediately after each `var` column (ontology ID), showing the term label retrieved from OLS4.

Label column header format: `<var_name>_label`

### 3. Validation Report (`<name>_validation.md`)

```markdown
# DOSDP Data Table Validation Report: <Pattern Name>

## Summary
- Pattern file: <path>
- Data table: <path>
- Terms processed: <N>
- Cells populated: <N>
- Validation issues: <N>

## Pattern Parse Summary
[Brief description of vars, data_vars, and axioms in the pattern]

## Ontology Var Validation

### Valid IDs (within specified range)
| Var | Row (Term) | ID | Label | Range |
|-----|-----------|-----|-------|-------|
| ... | ...       | ... | ...   | ...   |

### Invalid / Out-of-Range IDs
| Var | Row (Term) | ID | Issue | Expected Range |
|-----|-----------|-----|-------|----------------|
| ... | ...       | ... | ...   | ...            |

## Unpopulated Required Fields
| Row (defined_class) | Column | Reason |
|--------------------|--------|--------|
| ...                | ...    | ...    |

## Notes
[Any other issues, ambiguities, or recommendations]
```

## Validation Rules

- Every `var` value (ontology ID) MUST be verified against OLS4 via ontology-term-lookup.
- `var` values MUST fall within the range specified in the YAML pattern.
- Relation types used in `logical_axioms` MUST appear in `docs/relations_guide.md`.
- Definitions MUST conform to `docs/LLM_prompt_guidelines_for_CL_definitions.md`.
- The `defined_class` column MUST contain a valid OBO CURIE format (e.g. `CL:0000001`).
- Do NOT invent or guess ontology IDs — if an ID cannot be confirmed within the specified range, flag it as unresolved.

## Post-MVP Note

DOSDP pattern extension (modifying the YAML to add new vars or axioms) is a Phase 3 goal — see `ROADMAP.md`. Do not modify the YAML pattern file in the MVP.
