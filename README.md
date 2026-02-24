# CL/Uberon Template Agentic Framework

An AI-assisted framework for populating and validating DOSDP (Dead Simple OWL Design Pattern) and ROBOT templates for the Cell Ontology (CL) and Uberon anatomy ontology.

## Overview

This framework provides an automated workflow for:
- Researching ontology terms from scientific literature
- Validating existing template content
- Populating missing template fields
- Generating detailed validation reports
- Managing supporting references (PDFs, articles, Wikipedia)

## Setup

### Prerequisites

- Python 3.10 or higher
- [UV](https://github.com/astral-sh/uv) - Python package manager
- Git
- Claude Code CLI with MCP server support

### Installation

1. **Clone this repository** (or create a new branch for your project - see [Usage](#usage) below)

```bash
git clone <repository-url>
cd CL_Uberon_template_agentic_framework
```

2. **Set up Python virtual environment**

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

3. **Install UV** (if not already installed)

```bash
# On macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

4. **Configure MCP servers**

The framework uses the following MCP servers (configured in `.mcp.json`):
- **ols4-mcp**: For ontology term lookups (UBERON, FMA)
- **artl-mcp**: For scientific literature retrieval
- **playwright**: For web page interaction

Ensure these are properly configured in your Claude Code environment.

## Usage

### For Specific Projects

**Recommended approach**: Create a new branch for each specific project to keep work isolated:

```bash
# Create and switch to a new branch for your project
git checkout -b project-kidney-arteries

# Work on your project...
# All changes stay in this branch

# When done, you can merge or create a PR
git add .
git commit -m "Complete kidney arteries template"
git push -u origin project-kidney-arteries
```

**Alternative approach**: Fork or copy this repository for each project (less recommended as it duplicates the framework).

### Workflow

1. **Prepare your template**
   - Add your DOSDP or ROBOT template to `source_data/`
   - Include term names and any existing content
   - Ideally include a column with supporting references (Wikipedia URLs, DOIs, PMIDs)

2. **Add project instructions**
   - Edit `Instructions.md` with project-specific details
   - Describe the template structure and current state
   - Specify any special requirements or constraints

3. **Run the AI assistant**
   - Use Claude Code CLI to work with the framework
   - The assistant will automatically:
     - Pull and save all references to `pdfs/`
     - Validate existing content
     - Populate missing fields
     - Generate reports in `outputs/`

4. **Review outputs**
   - Check `outputs/` for:
     - Populated template
     - Report version with term labels
     - Validation and explanation reports

## Project Structure

```
.
├── .claude/
│   ├── agents/       # Subagent definitions
│   │   ├── gene-protein-lookup.md
│   │   └── ontology-term-lookup.md
│   └── skills/       # Skill definitions
│       └── fetch-wiki-info/
├── scripts/          # Python automation scripts
├── source_data/      # Input templates and source materials
├── outputs/          # Generated outputs and reports
├── pdfs/             # Downloaded papers and conversions
├── Instructions.md   # Project-specific instructions
├── AGENTS.md         # AI assistant instructions (do not edit)
├── CLAUDE.md         # AI assistant instructions (do not edit)
└── README.md         # This file
```

See individual folder README files for more details.

## Available Tools

The framework uses:
- **gene-protein-lookup subagent**: Maps gene/marker identifiers to HGNC, NCBI Gene, UniProt, and PRO IDs via playwright
- **ontology-term-lookup subagent**: Finds ontology terms and synonyms via OLS4 MCP
- **OLS4 MCP**: Ontology term lookup and validation
- **ARTL MCP**: Europe PMC literature search and retrieval
- **Playwright MCP**: Web database queries (HGNC, NCBI, UniProt)
- **fetch-wiki-info skill**: Wikipedia and Wikidata lookups

## Resources

- [DOSDP Schema](https://github.com/INCATools/dead_simple_owl_design_patterns/blob/master/src/schema/dosdp_schema.yaml)
- [ROBOT Templates](https://robot.obolibrary.org/template)
- [Cell Ontology Relations Guide](https://github.com/obophenotype/cell-ontology/blob/master/docs/relations_guide.md)
- [Uberon Editor SOP](https://github.com/obophenotype/uberon/blob/29ad8cbec9a164cdec28617be6771fdc32158f4d/docs/uberon-editor-sop.md)

## Contributing

When working on improvements to the framework itself (not project-specific work):
1. Create a feature branch from `main`
2. Make your changes
3. Test with a sample project
4. Submit a pull request

For project-specific work, use project branches as described in [Usage](#usage).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Cellular Semantics
