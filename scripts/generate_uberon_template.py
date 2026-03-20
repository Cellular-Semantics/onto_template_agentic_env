"""
Generate a ROBOT template TSV for Uberon skeleton landmark terms.

Input:  source_data/Uberon_skeleton_terms - Sheet1.csv
Output: outputs/uberon_skeleton_robot_template.tsv

Template columns:
  ID | LABEL | A IAO:0000115 | SC % | SC 'part of' some % | A oboInOwl:hasDbXref SPLIT=|
"""

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_CSV = ROOT / "source_data" / "Uberon_skeleton_terms - Sheet1.csv"
OUTPUT_TSV = ROOT / "outputs" / "uberon_skeleton_robot_template.tsv"
OUTPUT_TSV.parent.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Genus mapping: (label_keyword_test_fn, genus_label, genus_id)
# Evaluated in order; first match wins.
# ---------------------------------------------------------------------------

GENUS_RULES = [
    # --- Specific vertebral components ---
    (lambda l: "spinous process" in l,
     "neural spine", "UBERON:0001076"),
    (lambda l: "transverse process" in l,
     "transverse process of vertebra", "UBERON:0001077"),
    (lambda l: re.search(r"\barticular process\b", l),
     "process of vertebra", "UBERON:0006061"),
    (lambda l: "mammillary process" in l,
     "process of vertebra", "UBERON:0006061"),
    (lambda l: "anterior arch of" in l or "posterior arch of" in l,
     "arch of atlas", "UBERON:0005814"),
    (lambda l: "vertebral arch" in l,
     "neural arch", "UBERON:0003861"),
    (lambda l: "lamina of" in l and ("vertebra" in l or "vertebral" in l),
     "vertebra lamina", "UBERON:0004662"),
    (lambda l: "pedicle of vertebra" in l or re.search(r"pedicle of .+vertebra", l),
     "pedicle of vertebra", "UBERON:0001078"),
    (lambda l: "vertebral body" in l or re.search(r"body of .+(cervical|thoracic|lumbar|vertebra)", l),
     "bony vertebral centrum", "UBERON:0001075"),

    # --- Foramen / canal / meatus / hiatus / fissure / notch ---
    (lambda l: re.search(r"\b(foramen|foramina|canal|meatus|hiatus|fissure|notch)\b", l),
     "bone foramen", "UBERON:0005744"),

    # --- Condyle (zone of bone organ, not projection) ---
    (lambda l: re.search(r"\bcondyle\b", l),
     "condyle", "UBERON:0009979"),

    # --- Crest / crista (specific projection subclass) ---
    (lambda l: re.search(r"\b(crest|crista)\b", l),
     "crest", "UBERON:4200133"),

    # --- Fossa (specific class) — must precede projection keywords ---
    # e.g. "olecranon fossa" is a fossa, not a projection
    (lambda l: re.search(r"\bfossa\b", l),
     "bone fossa", "UBERON:0004704"),

    # --- Other projections ---
    (lambda l: re.search(r"\b(tubercle|tuberosity|malleolus|"
                         r"olecranon|protuberance|cornu|ramus|spine|"
                         r"eminence|epicondyle|trochanter|trochlea|"
                         r"styloid|hamulus|uncus|ala|alae|wing)\b", l),
     "skeletal element projection", "UBERON:4100000"),
    # 'process' catches acromial process, coronoid process, etc.
    (lambda l: re.search(r"\bprocess\b", l),
     "skeletal element projection", "UBERON:4100000"),

    # --- Groove / sulcus ---
    (lambda l: re.search(r"\b(groove|sulcus)\b", l),
     "surface groove", "UBERON:0006846"),

    # --- Fallback: zone of bone organ ---
    (lambda _: True,
     "zone of bone organ", "UBERON:0005913"),
]


def get_genus(label: str):
    l = label.lower()
    for test, genus_label, genus_id in GENUS_RULES:
        if test(l):
            return genus_label, genus_id
    return "zone of bone organ", "UBERON:0005913"


# ---------------------------------------------------------------------------
# Parent bone extraction: regex on label -> UBERON ID
# ---------------------------------------------------------------------------

# Named bones: order matters (longer/more-specific patterns first)
NAMED_BONE_MAP = [
    # Skull
    ("sphenoid",        "UBERON:0001677"),
    ("ethmoid",         "UBERON:0001679"),
    ("temporal bone",   "UBERON:0001678"),
    ("temporal",        "UBERON:0001678"),
    ("occipital",       "UBERON:0001676"),
    ("frontal bone",    "UBERON:0000209"),
    ("frontal",         "UBERON:0000209"),
    ("parietal bone",   "UBERON:0000210"),
    ("parietal",        "UBERON:0000210"),
    ("maxill",          "UBERON:0002397"),   # maxilla / maxillary
    ("palatine",        "UBERON:0001682"),
    ("vomer",           "UBERON:0002396"),
    ("mandible",        "UBERON:0001684"),
    ("mandibular",      "UBERON:0001684"),
    ("zygomatic",       "UBERON:0001683"),   # jugal/zygomatic bone
    ("lacrimal",        "UBERON:0001680"),
    ("hyoid",           "UBERON:0001685"),
    # Thorax
    ("sternum",         "UBERON:0000975"),
    ("sternal",         "UBERON:0000975"),
    ("clavicle",        "UBERON:0001105"),
    # Vertebral column
    ("sacrum",          "UBERON:0003690"),
    ("sacral",          "UBERON:0003690"),
    ("coccyx",          "UBERON:0001350"),
    ("coccygeal",       "UBERON:0001350"),
    # Upper limb
    ("scapula",         "UBERON:0006849"),
    ("scapular",        "UBERON:0006849"),
    ("humerus",         "UBERON:0000976"),
    ("humeral",         "UBERON:0000976"),
    ("ulna",            "UBERON:0001424"),
    ("ulnar",           "UBERON:0001424"),
    ("radius",          "UBERON:0001423"),
    ("radial",          "UBERON:0001423"),
    # Lower limb
    ("os coxa",         "UBERON:0001272"),
    ("innominate",      "UBERON:0001272"),
    ("ilium",           "UBERON:0001273"),
    ("iliac",           "UBERON:0001273"),
    ("ischium",         "UBERON:0001274"),
    ("ischial",         "UBERON:0001274"),
    ("pubis",           "UBERON:0001275"),
    ("pubic",           "UBERON:0001275"),
    ("femur",           "UBERON:0000981"),
    ("femoral",         "UBERON:0000981"),
    ("tibia",           "UBERON:0000979"),
    ("tibial",          "UBERON:0000979"),
    ("fibula",          "UBERON:0001446"),
    ("fibular",         "UBERON:0001446"),
    ("patella",         "UBERON:0007110"),
    ("patellar",        "UBERON:0007110"),
    ("calcaneus",       "UBERON:0001450"),
    ("calcaneal",       "UBERON:0001450"),
    ("talus",           "UBERON:0002395"),
    ("talar",           "UBERON:0002395"),
    ("cuboid",          "UBERON:0001455"),
    ("navicular",       "UBERON:0001451"),
]

# Numbered vertebrae (ordinal -> UBERON)
CERVICAL_MAP = {
    "first": "UBERON:0001092",   # atlas
    "second": "UBERON:0001093",  # axis
    "third": "UBERON:0004612",
    "fourth": "UBERON:0004613",
    "fifth": "UBERON:0004614",
    "sixth": "UBERON:0004615",
    "seventh": "UBERON:0004616",
}
THORACIC_MAP = {
    "first": "UBERON:0004626",
    "second": "UBERON:0004627",
    "third": "UBERON:0004628",
    "fourth": "UBERON:0004629",
    "fifth": "UBERON:0004630",
    "sixth": "UBERON:0004631",
    "seventh": "UBERON:0004632",
    "eighth": "UBERON:0011050",
    "ninth": "UBERON:0004633",
    "tenth": "UBERON:0004634",
    "eleventh": "UBERON:0004635",
    "twelfth": "UBERON:0004636",
}
LUMBAR_MAP = {
    "first": "UBERON:0004617",
    "second": "UBERON:0004618",
    "third": "UBERON:0004619",
    "fourth": "UBERON:0004620",
    "fifth": "UBERON:0004621",
}
RIB_MAP = {
    "first": "UBERON:0004601",
    "second": "UBERON:0004602",
    "third": "UBERON:0004603",
    "fourth": "UBERON:0004604",
    "fifth": "UBERON:0004605",
    "sixth": "UBERON:0004606",
    "seventh": "UBERON:0004607",
    "eighth": "UBERON:0010757",
    "ninth": "UBERON:0004608",
    "tenth": "UBERON:0004609",
    "eleventh": "UBERON:0004610",
    "twelfth": "UBERON:0004611",
}

ORDINALS = list(CERVICAL_MAP.keys()) + ["eighth", "ninth", "tenth", "eleventh", "twelfth"]


# Phalanges
PHALANX_MAP = {
    # manual (hand)
    ("distal", "manual", "first"):   "UBERON:0004337",
    ("distal", "manual", "second"):  "UBERON:0004311",
    ("distal", "manual", "third"):   "UBERON:0004312",
    ("distal", "manual", "fourth"):  "UBERON:0004313",
    ("distal", "manual", "fifth"):   "UBERON:0004314",
    ("proximal", "manual", "first"): "UBERON:0004338",
    ("middle", "manual", "second"):  "UBERON:0004320",
    ("middle", "manual", "third"):   "UBERON:0004321",
    # pedal (foot)
    ("distal", "pedal", "first"):    "UBERON:0004315",
    ("distal", "pedal", "second"):   "UBERON:0004316",
    ("proximal", "pedal", "first"):  "UBERON:0004332",
    ("middle", "pedal", "second"):   "UBERON:0004324",
}


def get_parent_bone(label: str):
    """Return (parent_label, parent_id) or (None, None) if not found."""
    l = label.lower()

    # --- Phalanges ---
    if "phalanx" in l or "phalang" in l:
        # e.g. "distal phalanx of second manual digit"
        #      "proximal phalanx of first pedal digit"
        #      "head of second distal phalanx of hand/foot"
        pos_m = re.search(r"(distal|proximal|middle)", l)
        pos_limb = re.search(r"(manual|pedal|hand|foot)", l)
        pos_digit = re.search(
            r"(first|second|third|fourth|fifth)", l)
        if pos_m and pos_limb and pos_digit:
            limb_word = pos_limb.group(1)
            limb = {"hand": "manual", "foot": "pedal"}.get(limb_word, limb_word)
            key = (pos_m.group(1), limb, pos_digit.group(1))
            if key in PHALANX_MAP:
                return f"{key[0]} phalanx {key[2]} {limb} digit", PHALANX_MAP[key]

    # --- Numbered ribs ---
    m = re.search(r"(" + "|".join(ORDINALS) + r") rib\b", l)
    if m:
        ordinal = m.group(1)
        if ordinal in RIB_MAP:
            return f"{ordinal} rib", RIB_MAP[ordinal]

    # --- Numbered vertebrae ---
    for ordinal in ORDINALS:
        if ordinal in l:
            if "cervical" in l:
                if ordinal in CERVICAL_MAP:
                    return f"{ordinal} cervical vertebra", CERVICAL_MAP[ordinal]
            elif "thoracic" in l:
                if ordinal in THORACIC_MAP:
                    return f"{ordinal} thoracic vertebra", THORACIC_MAP[ordinal]
            elif "lumbar" in l:
                if ordinal in LUMBAR_MAP:
                    return f"{ordinal} lumbar vertebra", LUMBAR_MAP[ordinal]

    # Atlas / axis by special name
    if "atlas" in l or "first cervical vertebra" in l:
        return "atlas", "UBERON:0001092"
    if "axis" in l and "vertebra" in l:
        return "axis", "UBERON:0001093"

    # --- Named bones ---
    # First pass: look for "of {bone}" at the rightmost position in the label.
    # This handles cases like "fibular trochlea of calcaneus" where the first
    # matching keyword ("fibular") would point to the wrong bone.
    best_pos = -1
    best_name = None
    best_uid = None
    for name, uid in NAMED_BONE_MAP:
        # Find last occurrence of "of {name}" in the label (word boundary safe)
        pattern = r"\bof\s+" + re.escape(name) + r"\b"
        m = re.search(pattern, l)
        if m and m.start() > best_pos:
            best_pos = m.start()
            best_name = name
            best_uid = uid
    if best_name:
        return best_name, best_uid

    # Second pass: scan forward with word-boundary matching.
    # Stems (entries that don't end in a word char boundary, e.g. "maxill")
    # only require a leading boundary; full words require both boundaries.
    STEM_ENTRIES = {"maxill"}  # entries that are prefix stems, not full words
    for name, uid in NAMED_BONE_MAP:
        if name in STEM_ENTRIES:
            pattern = r"\b" + re.escape(name)
        else:
            pattern = r"\b" + re.escape(name) + r"\b"
        if re.search(pattern, l):
            return name, uid

    return None, None


# ---------------------------------------------------------------------------
# Definition templates
# ---------------------------------------------------------------------------

def make_definition(label: str, genus_label: str, parent_label: str) -> str:
    """Generate a rolling definition."""
    article = "an" if genus_label[0].lower() in "aeiou" else "a"
    if parent_label:
        return (f"A {genus_label} that is part of the {parent_label}."
                if "zone" not in genus_label and "surface" not in genus_label and "groove" not in genus_label
                else f"A {genus_label} of the {parent_label}.")
    else:
        return f"A {genus_label} associated with the skeleton."


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

HEADER = [
    "ID",
    "LABEL",
    "A IAO:0000115",
    "SC %",
    "SC 'part of' some %",
    "A oboInOwl:hasDbXref SPLIT=|",
    "AI oboInOwl:inSubset",
    "A oboInOwl:creation_date",
    "AI dcterms:contributor",
    "AI RO:0002175",
]
DIRECTIVES = HEADER  # ROBOT uses the first row as both header and template

XREFS_BASE = "https://fipat.library.dal.ca/ta2/|ISBN:9780323393225"

SUBSET_IRI = "http://purl.obolibrary.org/obo/uberon/core#added_by_HRA"
CREATION_DATE = "2026-03-19T00:00:00Z"
CONTRIBUTOR_IRI = "https://orcid.org/0000-0002-7073-9172"
TAXON_IRI = "http://purl.obolibrary.org/obo/NCBITaxon_9606"

# Map from UBERON parent-bone ID to a Wikipedia article title (used as xref).
# Format: "Wikipedia:Article_title" (OBO standard)
WIKIPEDIA_BY_PARENT = {
    # Skull
    "UBERON:0001677": "Wikipedia:Sphenoid_bone",
    "UBERON:0001679": "Wikipedia:Ethmoid_bone",
    "UBERON:0001678": "Wikipedia:Temporal_bone",
    "UBERON:0001676": "Wikipedia:Occipital_bone",
    "UBERON:0000209": "Wikipedia:Frontal_bone",
    "UBERON:0000210": "Wikipedia:Parietal_bone",
    "UBERON:0002397": "Wikipedia:Maxilla",
    "UBERON:0001682": "Wikipedia:Palatine_bone",
    "UBERON:0002396": "Wikipedia:Vomer",
    "UBERON:0001684": "Wikipedia:Mandible",
    "UBERON:0001683": "Wikipedia:Zygomatic_bone",
    "UBERON:0001680": "Wikipedia:Lacrimal_bone",
    "UBERON:0001685": "Wikipedia:Hyoid_bone",
    # Thorax
    "UBERON:0000975": "Wikipedia:Sternum",
    "UBERON:0001105": "Wikipedia:Clavicle",
    # Vertebral column
    "UBERON:0003690": "Wikipedia:Sacrum",
    "UBERON:0001350": "Wikipedia:Coccyx",
    # Atlas / Axis
    "UBERON:0001092": "Wikipedia:Atlas_(anatomy)",
    "UBERON:0001093": "Wikipedia:Axis_(anatomy)",
    # Cervical vertebrae C3-C7
    "UBERON:0004612": "Wikipedia:Cervical_vertebrae",
    "UBERON:0004613": "Wikipedia:Cervical_vertebrae",
    "UBERON:0004614": "Wikipedia:Cervical_vertebrae",
    "UBERON:0004615": "Wikipedia:Cervical_vertebrae",
    "UBERON:0004616": "Wikipedia:Cervical_vertebrae",
    # Thoracic vertebrae
    "UBERON:0004626": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004627": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004628": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004629": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004630": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004631": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004632": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0011050": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004633": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004634": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004635": "Wikipedia:Thoracic_vertebrae",
    "UBERON:0004636": "Wikipedia:Thoracic_vertebrae",
    # Lumbar vertebrae
    "UBERON:0004617": "Wikipedia:Lumbar_vertebrae",
    "UBERON:0004618": "Wikipedia:Lumbar_vertebrae",
    "UBERON:0004619": "Wikipedia:Lumbar_vertebrae",
    "UBERON:0004620": "Wikipedia:Lumbar_vertebrae",
    "UBERON:0004621": "Wikipedia:Lumbar_vertebrae",
    # Ribs
    "UBERON:0004601": "Wikipedia:Rib",
    "UBERON:0004602": "Wikipedia:Rib",
    "UBERON:0004603": "Wikipedia:Rib",
    "UBERON:0004604": "Wikipedia:Rib",
    "UBERON:0004605": "Wikipedia:Rib",
    "UBERON:0004606": "Wikipedia:Rib",
    "UBERON:0004607": "Wikipedia:Rib",
    "UBERON:0010757": "Wikipedia:Rib",
    "UBERON:0004608": "Wikipedia:Rib",
    "UBERON:0004609": "Wikipedia:Rib",
    "UBERON:0004610": "Wikipedia:Rib",
    "UBERON:0004611": "Wikipedia:Rib",
    # Upper limb
    "UBERON:0006849": "Wikipedia:Scapula",
    "UBERON:0000976": "Wikipedia:Humerus",
    "UBERON:0001424": "Wikipedia:Ulna",
    "UBERON:0001423": "Wikipedia:Radius_(bone)",
    # Lower limb – os coxa & parts
    "UBERON:0001272": "Wikipedia:Hip_bone",
    "UBERON:0001273": "Wikipedia:Ilium_(bone)",
    "UBERON:0001274": "Wikipedia:Ischium",
    "UBERON:0001275": "Wikipedia:Pubis_(bone)",
    "UBERON:0000981": "Wikipedia:Femur",
    "UBERON:0000979": "Wikipedia:Tibia",
    "UBERON:0001446": "Wikipedia:Fibula",
    "UBERON:0007110": "Wikipedia:Patella",
    # Foot
    "UBERON:0001450": "Wikipedia:Calcaneus",
    "UBERON:0002395": "Wikipedia:Talus_bone",
    "UBERON:0001455": "Wikipedia:Cuboid_bone",
    "UBERON:0001451": "Wikipedia:Navicular_bone",
    # Phalanges (hand)
    "UBERON:0004337": "Wikipedia:Phalanx_bone",
    "UBERON:0004311": "Wikipedia:Phalanx_bone",
    "UBERON:0004312": "Wikipedia:Phalanx_bone",
    "UBERON:0004313": "Wikipedia:Phalanx_bone",
    "UBERON:0004314": "Wikipedia:Phalanx_bone",
    "UBERON:0004338": "Wikipedia:Phalanx_bone",
    "UBERON:0004320": "Wikipedia:Phalanx_bone",
    "UBERON:0004321": "Wikipedia:Phalanx_bone",
    # Phalanges (foot)
    "UBERON:0004315": "Wikipedia:Phalanx_bone",
    "UBERON:0004316": "Wikipedia:Phalanx_bone",
    "UBERON:0004332": "Wikipedia:Phalanx_bone",
    "UBERON:0004324": "Wikipedia:Phalanx_bone",
}

# Flags for terms that need manual review
TODO_NOTES = []


def process():
    rows = []
    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            iri = row["as"].strip()
            label = row["as_label"].strip()
            parents_as = row["parents_as"].strip()
            parents_as_label = row["parents_as_label"].strip()

            # Skip rows with no IRI or label
            if not iri or not label:
                continue

            genus_label, genus_id = get_genus(label)

            # Try to extract parent from label
            parent_label, parent_id = get_parent_bone(label)

            # If label-based extraction failed, fall back to parents_as
            # but only if the parents_as looks like a bone (UBERON:00014xx range typical for bones)
            if parent_id is None and parents_as.startswith("UBERON:"):
                # Trust it as a fallback
                parent_id = parents_as
                parent_label = parents_as_label

            if parent_id is None:
                TODO_NOTES.append(f"TODO - no parent bone: {label}")
                parent_id = "TODO"
                parent_label = "unknown"

            definition = make_definition(label, genus_label, parent_label)

            wiki_xref = WIKIPEDIA_BY_PARENT.get(parent_id, "")
            xrefs = XREFS_BASE + (f"|{wiki_xref}" if wiki_xref else "")

            rows.append({
                "ID": iri,
                "LABEL": label,
                "definition": definition,
                "genus_id": genus_id,
                "parent_id": parent_id,
                "xrefs": xrefs,
            })

    with open(OUTPUT_TSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(HEADER)
        writer.writerow(DIRECTIVES)
        for r in rows:
            writer.writerow([
                r["ID"],
                r["LABEL"],
                r["definition"],
                r["genus_id"],
                r["parent_id"],
                r["xrefs"],
                SUBSET_IRI,
                CREATION_DATE,
                CONTRIBUTOR_IRI,
                TAXON_IRI,
            ])

    print(f"Written {len(rows)} rows to {OUTPUT_TSV}")
    if TODO_NOTES:
        print(f"\n{len(TODO_NOTES)} terms need manual review:")
        for note in TODO_NOTES:
            print(f"  {note}")


if __name__ == "__main__":
    process()
