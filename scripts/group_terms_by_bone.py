"""
Group ROBOT template rows by parent bone and write per-group JSON input files
for definition-writing subagents.

Input:  outputs/uberon_skeleton_robot_template.tsv
Output: outputs/definitions/input/{group_name}.json  (one per group)
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_TSV = ROOT / "outputs" / "uberon_skeleton_robot_template.tsv"
OUTPUT_DIR = ROOT / "outputs" / "definitions" / "input"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Map parent UBERON ID -> (group_name, parent_bone_label, wikipedia_urls)
PARENT_ID_TO_GROUP = {
    # Os coxa
    "UBERON:0001272": ("os_coxa", "os coxa (innominate bone)",
                       ["https://en.wikipedia.org/wiki/Hip_bone",
                        "https://en.wikipedia.org/wiki/Acetabulum",
                        "https://en.wikipedia.org/wiki/Ilium_(bone)",
                        "https://en.wikipedia.org/wiki/Ischium",
                        "https://en.wikipedia.org/wiki/Pubis_(bone)"]),
    "UBERON:0001273": ("os_coxa", "ilium",
                       ["https://en.wikipedia.org/wiki/Ilium_(bone)"]),
    "UBERON:0001274": ("os_coxa", "ischium",
                       ["https://en.wikipedia.org/wiki/Ischium"]),
    "UBERON:0001275": ("os_coxa", "pubis",
                       ["https://en.wikipedia.org/wiki/Pubis_(bone)"]),
    # Femur
    "UBERON:0000981": ("femur", "femur",
                       ["https://en.wikipedia.org/wiki/Femur"]),
    # Tibia
    "UBERON:0000979": ("tibia", "tibia",
                       ["https://en.wikipedia.org/wiki/Tibia"]),
    # Fibula + patella
    "UBERON:0001446": ("fibula_patella", "fibula",
                       ["https://en.wikipedia.org/wiki/Fibula"]),
    "UBERON:0007110": ("fibula_patella", "patella",
                       ["https://en.wikipedia.org/wiki/Patella"]),
    # Calcaneus
    "UBERON:0001450": ("calcaneus", "calcaneus",
                       ["https://en.wikipedia.org/wiki/Calcaneus"]),
    # Talus + foot bones
    "UBERON:0002395": ("talus_foot", "talus",
                       ["https://en.wikipedia.org/wiki/Talus_bone"]),
    "UBERON:0001455": ("talus_foot", "cuboid bone",
                       ["https://en.wikipedia.org/wiki/Cuboid_bone"]),
    "UBERON:0001451": ("talus_foot", "navicular bone",
                       ["https://en.wikipedia.org/wiki/Navicular_bone"]),
    # Pedal phalanges
    "UBERON:0004315": ("foot_phalanges", "distal phalanx pedal digit 1",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004316": ("foot_phalanges", "distal phalanx pedal digit 2",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004332": ("foot_phalanges", "proximal phalanx pedal digit 1",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004324": ("foot_phalanges", "middle phalanx pedal digit 2",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    # Humerus
    "UBERON:0000976": ("humerus", "humerus",
                       ["https://en.wikipedia.org/wiki/Humerus"]),
    # Ulna + radius
    "UBERON:0001424": ("ulna_radius", "ulna",
                       ["https://en.wikipedia.org/wiki/Ulna"]),
    "UBERON:0001423": ("ulna_radius", "radius",
                       ["https://en.wikipedia.org/wiki/Radius_(bone)"]),
    # Manual phalanges
    "UBERON:0004337": ("hand_phalanges", "distal phalanx manual digit 1",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004311": ("hand_phalanges", "distal phalanx manual digit 2",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004312": ("hand_phalanges", "distal phalanx manual digit 3",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004313": ("hand_phalanges", "distal phalanx manual digit 4",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004314": ("hand_phalanges", "distal phalanx manual digit 5",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004338": ("hand_phalanges", "proximal phalanx manual digit 1",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004320": ("hand_phalanges", "middle phalanx manual digit 2",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    "UBERON:0004321": ("hand_phalanges", "middle phalanx manual digit 3",
                       ["https://en.wikipedia.org/wiki/Phalanx_bone"]),
    # Scapula + clavicle
    "UBERON:0006849": ("scapula_clavicle", "scapula",
                       ["https://en.wikipedia.org/wiki/Scapula"]),
    "UBERON:0001105": ("scapula_clavicle", "clavicle",
                       ["https://en.wikipedia.org/wiki/Clavicle"]),
    # Mandible
    "UBERON:0001684": ("mandible", "mandible",
                       ["https://en.wikipedia.org/wiki/Mandible"]),
    # Maxilla group
    "UBERON:0002397": ("maxilla_palatine", "maxilla",
                       ["https://en.wikipedia.org/wiki/Maxilla"]),
    "UBERON:0001682": ("maxilla_palatine", "palatine bone",
                       ["https://en.wikipedia.org/wiki/Palatine_bone"]),
    "UBERON:0002396": ("maxilla_palatine", "vomer",
                       ["https://en.wikipedia.org/wiki/Vomer"]),
    # Temporal
    "UBERON:0001678": ("temporal", "temporal bone",
                       ["https://en.wikipedia.org/wiki/Temporal_bone"]),
    # Sphenoid
    "UBERON:0001677": ("sphenoid", "sphenoid bone",
                       ["https://en.wikipedia.org/wiki/Sphenoid_bone"]),
    # Ethmoid
    "UBERON:0001679": ("ethmoid", "ethmoid bone",
                       ["https://en.wikipedia.org/wiki/Ethmoid_bone"]),
    # Skull vault
    "UBERON:0001676": ("skull_vault", "occipital bone",
                       ["https://en.wikipedia.org/wiki/Occipital_bone"]),
    "UBERON:0000209": ("skull_vault", "frontal bone",
                       ["https://en.wikipedia.org/wiki/Frontal_bone"]),
    "UBERON:0000210": ("skull_vault", "parietal bone",
                       ["https://en.wikipedia.org/wiki/Parietal_bone"]),
    # Sternum
    "UBERON:0000975": ("sternum", "sternum",
                       ["https://en.wikipedia.org/wiki/Sternum"]),
    # Ribs
    "UBERON:0004601": ("ribs", "first rib",   ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004602": ("ribs", "second rib",  ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004603": ("ribs", "third rib",   ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004604": ("ribs", "fourth rib",  ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004605": ("ribs", "fifth rib",   ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004606": ("ribs", "sixth rib",   ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004607": ("ribs", "seventh rib", ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0010757": ("ribs", "eighth rib",  ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004608": ("ribs", "ninth rib",   ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004609": ("ribs", "tenth rib",   ["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004610": ("ribs", "eleventh rib",["https://en.wikipedia.org/wiki/Rib"]),
    "UBERON:0004611": ("ribs", "twelfth rib", ["https://en.wikipedia.org/wiki/Rib"]),
    # Sacrum + coccyx
    "UBERON:0003690": ("sacrum_coccyx", "sacrum",
                       ["https://en.wikipedia.org/wiki/Sacrum"]),
    "UBERON:0001350": ("sacrum_coccyx", "coccyx",
                       ["https://en.wikipedia.org/wiki/Coccyx"]),
    # Hyoid + misc
    "UBERON:0001685": ("hyoid_misc", "hyoid bone",
                       ["https://en.wikipedia.org/wiki/Hyoid_bone"]),
    # Cervical vertebrae
    "UBERON:0001092": ("cervical_vertebrae", "atlas (C1)",
                       ["https://en.wikipedia.org/wiki/Atlas_(anatomy)",
                        "https://en.wikipedia.org/wiki/Cervical_vertebrae"]),
    "UBERON:0001093": ("cervical_vertebrae", "axis (C2)",
                       ["https://en.wikipedia.org/wiki/Axis_(anatomy)",
                        "https://en.wikipedia.org/wiki/Cervical_vertebrae"]),
    "UBERON:0004612": ("cervical_vertebrae", "C3",
                       ["https://en.wikipedia.org/wiki/Cervical_vertebrae"]),
    "UBERON:0004613": ("cervical_vertebrae", "C4",
                       ["https://en.wikipedia.org/wiki/Cervical_vertebrae"]),
    "UBERON:0004614": ("cervical_vertebrae", "C5",
                       ["https://en.wikipedia.org/wiki/Cervical_vertebrae"]),
    "UBERON:0004615": ("cervical_vertebrae", "C6",
                       ["https://en.wikipedia.org/wiki/Cervical_vertebrae"]),
    "UBERON:0004616": ("cervical_vertebrae", "C7",
                       ["https://en.wikipedia.org/wiki/Cervical_vertebrae"]),
    # Thoracic vertebrae
    "UBERON:0004626": ("thoracic_vertebrae", "T1",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004627": ("thoracic_vertebrae", "T2",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004628": ("thoracic_vertebrae", "T3",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004629": ("thoracic_vertebrae", "T4",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004630": ("thoracic_vertebrae", "T5",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004631": ("thoracic_vertebrae", "T6",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004632": ("thoracic_vertebrae", "T7",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0011050": ("thoracic_vertebrae", "T8",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004633": ("thoracic_vertebrae", "T9",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004634": ("thoracic_vertebrae", "T10",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004635": ("thoracic_vertebrae", "T11",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    "UBERON:0004636": ("thoracic_vertebrae", "T12",
                       ["https://en.wikipedia.org/wiki/Thoracic_vertebrae"]),
    # Lumbar vertebrae
    "UBERON:0004617": ("lumbar_vertebrae", "L1",
                       ["https://en.wikipedia.org/wiki/Lumbar_vertebrae"]),
    "UBERON:0004618": ("lumbar_vertebrae", "L2",
                       ["https://en.wikipedia.org/wiki/Lumbar_vertebrae"]),
    "UBERON:0004619": ("lumbar_vertebrae", "L3",
                       ["https://en.wikipedia.org/wiki/Lumbar_vertebrae"]),
    "UBERON:0004620": ("lumbar_vertebrae", "L4",
                       ["https://en.wikipedia.org/wiki/Lumbar_vertebrae"]),
    "UBERON:0004621": ("lumbar_vertebrae", "L5",
                       ["https://en.wikipedia.org/wiki/Lumbar_vertebrae"]),
}

# Genus ID -> label lookup
GENUS_LABELS = {
    "UBERON:0001076": "neural spine",
    "UBERON:0001077": "transverse process of vertebra",
    "UBERON:0006061": "process of vertebra",
    "UBERON:0005814": "arch of atlas",
    "UBERON:0003861": "neural arch",
    "UBERON:0004662": "vertebra lamina",
    "UBERON:0001078": "pedicle of vertebra",
    "UBERON:0001075": "bony vertebral centrum",
    "UBERON:0005744": "bone foramen",
    "UBERON:0009979": "condyle",
    "UBERON:4200133": "crest",
    "UBERON:4100000": "skeletal element projection",
    "UBERON:0004704": "bone fossa",
    "UBERON:0006846": "surface groove",
    "UBERON:0005913": "zone of bone organ",
}


def process():
    groups: dict[str, dict] = {}  # group_name -> {terms, parent_bones, wikipedia_urls}

    with open(INPUT_TSV, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        headers = next(reader)  # column names
        next(reader)            # directives row

        for row in reader:
            if len(row) < 5:
                continue
            iri, label, definition, genus_id, parent_id, *_ = row

            mapping = PARENT_ID_TO_GROUP.get(parent_id)
            if mapping is None:
                # fallback group
                group_name = "misc_unmatched"
                parent_bone = parent_id
                wikipedia_urls = []
            else:
                group_name, parent_bone, wikipedia_urls = mapping

            if group_name not in groups:
                groups[group_name] = {
                    "terms": [],
                    "parent_bones": set(),
                    "wikipedia_urls": [],
                }
            groups[group_name]["terms"].append({
                "label": label,
                "genus_id": genus_id,
                "genus_label": GENUS_LABELS.get(genus_id, genus_id),
                "parent_id": parent_id,
                "parent_bone": parent_bone,
            })
            groups[group_name]["parent_bones"].add(parent_bone)
            for url in wikipedia_urls:
                if url not in groups[group_name]["wikipedia_urls"]:
                    groups[group_name]["wikipedia_urls"].append(url)

    for group_name, data in sorted(groups.items()):
        out = {
            "group_name": group_name,
            "parent_bones": sorted(data["parent_bones"]),
            "wikipedia_urls": data["wikipedia_urls"],
            "terms": data["terms"],
        }
        out_path = OUTPUT_DIR / f"{group_name}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
        print(f"  {group_name:30s} {len(data['terms']):3d} terms → {out_path.name}")

    print(f"\nTotal groups: {len(groups)}")
    total = sum(len(d['terms']) for d in groups.values())
    print(f"Total terms:  {total}")


if __name__ == "__main__":
    process()
