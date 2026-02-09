# Scripts

This folder contains Python scripts for automation and data processing.

## Purpose

Store all custom scripts used for:
- Template processing and transformation
- Data validation and cleanup
- Automated literature searches
- Report generation
- Integration with ontology tools

## Guidelines

- Use Python 3.10+ compatible code
- Manage dependencies with UV and `pyproject.toml`
- Include docstrings for all functions
- Add a brief header comment explaining the script's purpose
- Name scripts descriptively (e.g., `validate_template.py`, `fetch_references.py`)

## Running Scripts

Always run scripts from the project root with the virtual environment activated:

```bash
# Activate venv
source .venv/bin/activate

# Run script
python scripts/your_script.py
```

## Dependencies

Install dependencies using UV:

```bash
uv pip install <package-name>
```

Add them to `pyproject.toml` for version tracking.
