# Roadmap: CL/Uberon Template Agentic Framework

## MVP — Template Population + Validation

### ROBOT Template Editor Agent (`.claude/agents/robot-template-editor.md`)

- [ ] Read and parse ROBOT TSV column headers (row 1 + ROBOT syntax row 2)
- [ ] Detect populated vs. missing cells per row
- [ ] Fill rows from upstream term data (CL-curator-research output or user-provided)
- [ ] Validate ontology IDs via OLS4 (using ontology-term-lookup subagent)
- [ ] Validate ROBOT column header syntax (row 2)
- [ ] Flag unresolvable cells with clear reasons
- [ ] Output: populated TSV, report TSV (with labels), validation markdown

### DOSDP Data Table Editor Agent (`.claude/agents/dosdp-template-editor.md`)

- [ ] Parse DOSDP YAML pattern file (vars, ranges, annotations, logical axioms)
- [ ] Read data TSV and detect populated vs. missing cells per row
- [ ] Fill data rows from upstream term data
- [ ] Validate `var` values against OLS4 and pattern-specified ranges
- [ ] Flag unresolvable cells with clear reasons
- [ ] Output: populated TSV, report TSV (with labels), validation markdown

### Integration

- [ ] CLAUDE.md orchestrator delegates to robot-template-editor or dosdp-template-editor as appropriate
- [ ] Symlink strategy: canonical agents in `.claude/agents/`, linked from `.github/agents/` for Copilot
- [ ] CL-curator-research symlinked into `.claude/agents/` so Claude Code can call it as a subagent

---

## Phase 2 — ROBOT Template Extension (Post-MVP)

> Extending ROBOT templates is relatively straightforward as column header syntax is self-contained.

- [ ] Add new annotation columns to an existing ROBOT template
- [ ] Add new relationship columns (SubClassOf, EquivalentClass) to an existing template
- [ ] Generate a new ROBOT template from a term specification / column list
- [ ] Validate the extended template structure before populating

---

## Phase 3 — DOSDP Pattern Extension (Final Goal)

> Extending DOSDP patterns requires modifying the YAML and keeping data TSV columns in sync — more complex than ROBOT extension.

- [ ] Add new `var` (ontology ID) to an existing DOSDP YAML pattern
- [ ] Add new `data_var` (free text) to an existing pattern
- [ ] Add new annotation or logical axiom using the new var
- [ ] Update the data TSV columns to match the extended pattern
- [ ] Validate the modified pattern against the DOSDP schema
- [ ] Handle cases where new vars require new terms to be imported into dependent ontologies
