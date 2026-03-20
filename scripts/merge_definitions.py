"""
Merge per-group definition JSON files back into the ROBOT template TSV.

Input:  outputs/definitions/*.json  (label -> definition mappings)
        outputs/uberon_skeleton_robot_template.tsv
Output: outputs/uberon_skeleton_robot_template.tsv  (updated in-place)
"""

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_TSV = ROOT / "outputs" / "uberon_skeleton_robot_template.tsv"
DEFS_DIR = ROOT / "outputs" / "definitions"

GENERIC_PATTERN = re.compile(
    r"^A \w[\w ]+ (that is part of|of) the ", re.IGNORECASE
)


def load_definitions() -> dict[str, str]:
    """Load all label->definition mappings from outputs/definitions/*.json (not input/)."""
    defs = {}
    for jf in sorted(DEFS_DIR.glob("*.json")):
        if jf.parent.name == "input":
            continue
        with open(jf, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            defs.update(data)
        else:
            print(f"  WARNING: {jf.name} is not a plain dict, skipping")
    return defs


def process():
    definitions = load_definitions()
    print(f"Loaded {len(definitions)} definitions from JSON files")

    rows = []
    updated = 0
    still_generic = 0

    with open(INPUT_TSV, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        header_row = next(reader)
        directive_row = next(reader)
        rows.append(header_row)
        rows.append(directive_row)

        for row in reader:
            if len(row) < 3:
                rows.append(row)
                continue
            label = row[1]
            if label in definitions:
                new_def = definitions[label].strip()
                if new_def:
                    row[2] = new_def
                    updated += 1
            # Check if still generic after update attempt
            if GENERIC_PATTERN.match(row[2]):
                still_generic += 1
            rows.append(row)

    with open(INPUT_TSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(rows)

    data_rows = len(rows) - 2
    print(f"Updated: {updated}/{data_rows} definitions")
    print(f"Still generic: {still_generic}")


if __name__ == "__main__":
    process()
