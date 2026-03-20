# Workflow: Enriching Uberon Bone Landmark Definitions

## Purpose

This document describes the workflow used to generate anatomically specific definitions for the 390 new Uberon skeletal landmark terms derived from the ASCTB project. It serves as a reusable example for similar batched definition-writing tasks.

---

## Background

The initial ROBOT template generation script (`scripts/generate_uberon_template.py`) produces generic placeholder definitions of the form:

> "A bone fossa that is part of the os coxa."

These are insufficient for ontology use. Definitions must describe *what* the structure is — its shape, position, articular relationships, attachments, or function — not merely its ontological type and parent bone.

---

## Workflow Overview

```
TSV template (390 rows)
        |
        v
[1. Group script]  → outputs/definitions/input/{group}.json  (~24 groups)
        |
        v
[2. Subagents]     → outputs/definitions/{group}.json        (one per group)
  (up to 8 in parallel)
        |
        v
[3. Merge script]  → updated outputs/uberon_skeleton_robot_template.tsv
```

---

## Stage 1: Group Terms by Parent Bone

**Script:** `scripts/group_terms_by_bone.py`

Reads the ROBOT template TSV and outputs one JSON file per anatomical group into `outputs/definitions/input/`. Each file contains a list of term objects:

```json
[
  {
    "label": "acetabular fossa of os coxa",
    "genus_label": "bone fossa",
    "genus_id": "UBERON:0004704",
    "parent_bone": "os coxa",
    "parent_id": "UBERON:0001272"
  },
  ...
]
```

### Grouping table

| Group file | Parent bone(s) | Primary Wikipedia article |
|---|---|---|
| `os_coxa` | os coxa / ilium / ischium / pubis | Acetabulum, Hip bone |
| `femur` | femur | Femur |
| `tibia` | tibia | Tibia |
| `fibula_patella` | fibula, patella | Fibula, Patella |
| `calcaneus` | calcaneus | Calcaneus |
| `talus_foot` | talus, cuboid, navicular | Talus, Cuboid bone |
| `foot_phalanges` | pedal phalanges | Phalanx (foot) |
| `humerus` | humerus | Humerus |
| `ulna_radius` | ulna, radius | Ulna, Radius |
| `hand_phalanges` | manual phalanges | Phalanx (hand) |
| `scapula_clavicle` | scapula, clavicle | Scapula, Clavicle |
| `mandible` | mandible | Mandible |
| `maxilla_palatine` | maxilla, palatine, vomer | Maxilla, Palatine bone |
| `temporal` | temporal bone | Temporal bone |
| `sphenoid` | sphenoid bone | Sphenoid bone |
| `ethmoid` | ethmoid bone | Ethmoid bone |
| `skull_vault` | occipital, frontal, parietal | Occipital bone |
| `sternum` | sternum | Sternum |
| `ribs` | ribs 1–12 | Rib (anatomy) |
| `sacrum_coccyx` | sacrum, coccyx | Sacrum, Coccyx |
| `hyoid_misc` | hyoid and miscellaneous | Hyoid bone |
| `cervical_vertebrae` | C1–C7 | Cervical vertebrae |
| `thoracic_vertebrae` | T1–T12 | Thoracic vertebrae |
| `lumbar_vertebrae` | L1–L5 | Lumbar vertebrae |

---

## Stage 2: Subagent Definition Writing

### Parallelism
Up to 8 subagents are launched in parallel. Each handles one group. More than 8 risks saturating Playwright/Wikipedia.

### Search strategy (applied within each subagent, in order)

1. **Latent knowledge — first draft**
   Write a working definition for every term using anatomical knowledge. This avoids unnecessary web fetches for well-known structures.

2. **Wikipedia — specific article**
   For structures that have their own Wikipedia page (e.g., *Acetabular fossa*, *Linea aspera*, *Olecranon*), fetch it via Playwright and refine the definition.

3. **Wikipedia — parent bone article**
   Fetch the main Wikipedia article for the parent bone (e.g., *Femur*, *Temporal bone*). These articles typically describe all major sub-structures. Extract the relevant passage for each term.

4. **WebSearch fallback**
   If Wikipedia yields nothing useful for a term, run a web search for `"{term label}" anatomy`.

### Definition quality criteria

| Criterion | Detail |
|---|---|
| Form | Aristotelian: starts with `A {genus_label} ...` |
| Content | Describes position, shape, function, articular relationships, or attachments |
| Length | 20–50 words; one sentence preferred, two maximum |
| Negative | Must NOT be merely `"A {genus} that is part of bone X"` |
| Parent bone | Must be referenced naturally somewhere in the definition |

### Good definition example

**Term:** *acetabular fossa of os coxa*
**Generic (bad):** "A bone fossa that is part of the os coxa."
**Specific (good):** "A bone fossa forming the non-articular floor of the acetabulum of the os coxa, occupied by fatty tissue covered by synovial membrane and providing attachment for the ligament of the femoral head."

### Subagent prompt template

```
You are an expert anatomist writing definitions for anatomical ontology terms.

## Group: {GROUP_NAME}
Parent bone(s): {PARENT_BONE_NAMES}
Wikipedia target(s): {WIKIPEDIA_URLS}

## Terms to define

| Label | Structural type (genus) |
|-------|------------------------|
| {label} | {genus_label} |
...

## Task
Write specific, informative definitions in Aristotelian form ("A {genus} that/which...").
Definitions must describe what the structure IS — shape, position, articular relationships,
attachments, or function — not merely that it is "part of bone X".

## Search strategy
1. Draft all definitions from anatomical knowledge first.
2. Use Playwright (mcp__playwright__browser_navigate + mcp__playwright__browser_snapshot)
   to fetch the Wikipedia article for the parent bone. Extract descriptions for each term.
3. For terms with their own Wikipedia page, fetch those too.
4. Use WebSearch as a fallback for any terms not covered.

## Output
Write a JSON object mapping each label to its definition, and save it to:
outputs/definitions/{GROUP_NAME}.json

Example:
{
  "acetabular fossa of os coxa": "A bone fossa forming the non-articular floor...",
  "acetabular notch of os coxa": "A bone foramen interrupting the inferior margin..."
}
```

### Subagent output format

```json
{
  "term label": "definition string",
  ...
}
```
Saved to: `outputs/definitions/{group_name}.json`

---

## Stage 3: Merge Definitions into TSV

**Script:** `scripts/merge_definitions.py`

- Loads all `outputs/definitions/*.json` files (excluding the `input/` subdirectory)
- Reads the ROBOT template TSV
- Replaces column 3 (IAO:0000115 definition) for each matching label
- Writes the updated TSV back to `outputs/uberon_skeleton_robot_template.tsv`
- Reports: count updated, count remaining generic

---

## Verification

1. Spot-check 5–10 definitions across different bone groups for anatomical accuracy.
2. Confirm no row still contains the generic pattern `"A {genus} that is part of the"`.
3. Confirm row count is still 390 (plus 2 header rows).
4. If ROBOT is available: `robot validate --input outputs/uberon_skeleton_robot_template.tsv`.

---

## Reuse notes

This workflow (group → subagent → merge) is applicable to any large ROBOT or DOSDP template task where:
- Terms cluster naturally into ~20–30 thematic groups
- Per-group context fits within one subagent's working memory
- Web lookups are useful but must be bounded per agent
