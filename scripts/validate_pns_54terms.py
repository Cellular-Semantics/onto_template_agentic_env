import csv
import re
from pathlib import Path
from collections import defaultdict, Counter

def extract_doi(ref: str):
    m = re.search(r'(10\.[^\s/]+/[^\s]+)', ref, re.I)
    if m:
        return m.group(1).rstrip(').,')
    return None

def normalize_text(s: str):
    return re.sub(r'\s+', ' ', s).strip().lower()

def make_location_variants(loc: str):
    loc = loc.strip()
    variants = set()
    if not loc:
        return variants
    variants.add(loc)
    # remove directional adjectives to allow partial matches
    # e.g., cervical dorsal root ganglion -> dorsal root ganglion
    tokens = loc.split()
    directional = {'cervical','thoracic','lumbar','sacral','cranial','caudal','upper','lower','middle','medial','lateral','rostral','caudal'}
    filtered = [t for t in tokens if t.lower() not in directional]
    if filtered and ' '.join(filtered) != loc:
        variants.add(' '.join(filtered))
    # remove region adjectives like "superior" or "inferior" if present
    regionals = {'superior','inferior','anterior','posterior','dorsal','ventral'}
    filtered2 = [t for t in tokens if t.lower() not in regionals]
    if filtered2 and ' '.join(filtered2) != loc:
        variants.add(' '.join(filtered2))
    # add common anatomical abbreviations / synonyms
    low = loc.lower()
    if 'dorsal root ganglion' in low:
        variants.add('dorsal root ganglion')
        variants.add('drg')
        variants.add('dorsal root ganglia')
        variants.add('drgs')
        if 'cervical' in low:
            variants.add('cervical drg')
        if 'thoracic' in low:
            variants.add('thoracic drg')
        if 'lumbar' in low:
            variants.add('lumbar drg')
        if 'sacral' in low:
            variants.add('sacral drg')
    if 'myenteric' in low:
        variants.update({
            'myenteric plexus',
            'myenteric ganglion',
            'myenteric plexus of small intestine',
            'small intestine myenteric plexus',
            'myenteric plexus of the small intestine',
        })
    if 'ciliary ganglion' in low:
        variants.update({'ciliary ganglion', 'main ciliary ganglion'})
    if 'cardiac ganglion' in low:
        variants.update({
            'cardiac ganglion',
            'cardiac ganglia',
            'intracardiac ganglion',
            'intracardiac ganglia',
            'intrinsic cardiac ganglion',
            'intrinsic cardiac ganglia',
        })
    return variants

def make_marker_variants(marker: str):
    m = marker.strip()
    if not m:
        return set()
    variants = {m}
    ml = m.lower()
    synonyms = {
        'pou4f1': ['brn3a', 'brn-3a', 'pou4f1'],
        'cgrp': ['cgrp', 'calcitonin gene-related peptide'],
        'edn1': ['edn1', 'endothelin 1', 'endothelin-1'],
        'scn9a': ['scn9a', 'nav1.7', 'na(v)1.7'],
        'scn11a': ['scn11a', 'nav1.9', 'na(v)1.9'],
        'neurofilament 200 (nf200)': ['nf200', 'nf-200', 'neurofilament 200', 'neurofilament-200'],
        'prph': ['prph', 'peripherin'],
        'piezo2': ['piezo2'],
        'receptor tyrosine kinase ret': ['ret', 'receptor tyrosine kinase ret'],
        'substance p (sp)': ['substance p', 'sp'],
        'trpv1': ['trpv1'],
        'vip': ['vip', 'vasoactive intestinal peptide'],
        'chat': ['chat', 'choline acetyltransferase', 'choline acetyl-transferase'],
        'calr': ['calr', 'calretinin'],
        'som': ['som', 'somatostatin', 'sst'],
        'nos1': ['nos1', 'nnos', 'neuronal nitric oxide synthase', 'nitric oxide synthase 1'],
        'gal': ['gal', 'galanin'],
        'th': ['th', 'tyrosine hydroxylase'],
        'nf200': ['nf200', 'nf-200', 'neurofilament 200'],
    }
    for key, vals in synonyms.items():
        if key in ml:
            variants.update(vals)
    variants.update({v.upper() for v in variants})
    variants.update({v.lower() for v in variants})
    return {v for v in variants if v}

def find_snippets(text: str, needle: str, max_snippets=2, window=120):
    # return short snippets around needle
    snippets = []
    if not needle:
        return snippets
    pattern = re.compile(re.escape(needle), re.I)
    for m in pattern.finditer(text):
        start = max(0, m.start() - window)
        end = min(len(text), m.end() + window)
        snippet = text[start:end].replace('\n', ' ')
        snippet = re.sub(r'\s+', ' ', snippet).strip()
        snippets.append(snippet)
        if len(snippets) >= max_snippets:
            break
    return snippets

def split_paragraphs(text: str):
    parts = re.split(r'\n\s*\n', text)
    return [p.strip() for p in parts if p.strip()]

def marker_location_in_same_paragraph(text: str, marker_variants, loc_variants):
    """Check if marker and any location variant appear in the same paragraph."""
    for para in split_paragraphs(text):
        para_l = para.lower()
        has_marker = any(mv.lower() in para_l for mv in marker_variants)
        if not has_marker:
            continue
        has_loc = any(lv.lower() in para_l for lv in loc_variants)
        if has_loc:
            snippet = re.sub(r'\s+', ' ', para.strip())
            return True, snippet[:300]
    return False, ''


def make_full_location_variants(loc: str):
    """Generate variants of the FULL location (with segment qualifiers preserved).
    
    Unlike make_location_variants, this does NOT strip directional/segment qualifiers.
    Used for strict full-location matching.
    """
    loc = loc.strip()
    variants = set()
    if not loc:
        return variants
    variants.add(loc.lower())
    
    # Add common abbreviation forms but preserve the segment qualifier
    low = loc.lower()
    if 'dorsal root ganglion' in low:
        if 'cervical' in low:
            variants.update({'cervical drg', 'cervical dorsal root ganglion', 'cervical dorsal root ganglia', 'cervical drgs'})
        elif 'thoracic' in low:
            variants.update({'thoracic drg', 'thoracic dorsal root ganglion', 'thoracic dorsal root ganglia', 'thoracic drgs'})
        elif 'lumbar' in low:
            variants.update({'lumbar drg', 'lumbar dorsal root ganglion', 'lumbar dorsal root ganglia', 'lumbar drgs'})
        elif 'sacral' in low:
            variants.update({'sacral drg', 'sacral dorsal root ganglion', 'sacral dorsal root ganglia', 'sacral drgs'})
        else:
            # No segment qualifier - the full location IS the base form
            variants.update({'dorsal root ganglion', 'dorsal root ganglia', 'drg', 'drgs'})
    
    # Other ganglia types - keep full name
    if 'myenteric' in low:
        variants.update({
            'myenteric plexus',
            'myenteric ganglion',
            'myenteric ganglia',
            'myenteric nerve plexus',
            'myenteric plexus of small intestine',
            'small intestine myenteric plexus',
        })
    if 'ciliary ganglion' in low:
        variants.update({'ciliary ganglion', 'main ciliary ganglion', 'ciliary ganglia'})
    if 'cardiac ganglion' in low:
        variants.update({
            'cardiac ganglion',
            'cardiac ganglia',
            'intracardiac ganglion',
            'intracardiac ganglia',
            'intrinsic cardiac ganglion',
            'intrinsic cardiac ganglia',
        })
    
    return variants


def marker_and_full_location_in_same_paragraph(text: str, marker_variants, location: str):
    """Check if marker and FULL location (with segment qualifier) appear in same paragraph."""
    full_loc_variants = make_full_location_variants(location)
    for para in split_paragraphs(text):
        para_l = para.lower()
        has_marker = any(mv.lower() in para_l for mv in marker_variants)
        if not has_marker:
            continue
        has_full_loc = any(lv in para_l for lv in full_loc_variants)
        if has_full_loc:
            snippet = re.sub(r'\s+', ' ', para.strip())
            return True, snippet[:300]
    return False, ''

def explicit_segment_variants(loc: str):
    low = loc.lower()
    variants = {loc.lower()}
    if 'dorsal root ganglion' in low:
        if 'cervical' in low:
            variants.update({'cervical drg', 'cervical dorsal root ganglion', 'cervical dorsal root ganglia'})
        if 'thoracic' in low:
            variants.update({'thoracic drg', 'thoracic dorsal root ganglion', 'thoracic dorsal root ganglia'})
        if 'lumbar' in low:
            variants.update({'lumbar drg', 'lumbar dorsal root ganglion', 'lumbar dorsal root ganglia'})
        if 'sacral' in low:
            variants.update({'sacral drg', 'sacral dorsal root ganglion', 'sacral dorsal root ganglia'})
    return variants

def explicit_segment_in_paragraph(text: str, marker_variants, location: str):
    low_loc = location.lower()
    if 'dorsal root ganglion' not in low_loc:
        return False, ''
    segments = [s for s in ['cervical', 'thoracic', 'lumbar', 'sacral'] if s in low_loc]
    if not segments:
        return False, ''
    base_locs = {'dorsal root ganglion', 'dorsal root ganglia', 'drg', 'drgs'}
    for para in split_paragraphs(text):
        para_l = para.lower()
        if not any(mv.lower() in para_l for mv in marker_variants):
            continue
        if not any(bl in para_l for bl in base_locs):
            continue
        if any(seg in para_l for seg in segments):
            snippet = re.sub(r'\s+', ' ', para.strip())
            return True, snippet[:300]
    return False, ''

# load source data
source_path = Path('source_data/PNS_54terms.csv')
rows = []
with source_path.open(newline='') as f:
    r = csv.DictReader(f)
    rows = list(r)

# index available text files
pdf_dir = Path('pdfs')
text_files = [p for p in pdf_dir.iterdir() if p.suffix == '.txt']
text_content = {}
for p in text_files:
    try:
        text_content[p.name] = p.read_text(errors='ignore')
    except Exception:
        text_content[p.name] = ''

# build DOI->files mapping by searching content and filename
all_refs = set()
for row in rows:
    for ref in row['references'].split('|'):
        if ref.strip():
            all_refs.add(ref.strip())

doi_refs = {}
for ref in all_refs:
    doi = extract_doi(ref)
    if doi:
        doi_refs[ref] = doi

ref_to_files = defaultdict(list)
for ref, doi in doi_refs.items():
    doi_l = doi.lower()
    doi_file_hint = doi.replace('/', '_').lower()
    doi_suffix = doi.split('/')[-1].lower()
    for fname, txt in text_content.items():
        f_low = fname.lower()
        if doi_l in txt.lower() or doi_file_hint in f_low or doi_suffix in f_low:
            ref_to_files[ref].append(fname)

# supplemental references from autonomic ganglia report (by location)
supplemental_by_location = {
    'main ciliary ganglion': ['PMC8788436.txt', 'PMC6576920.txt', 'PMC6569016.txt'],
    'cardiac ganglion': ['PMC8324809.txt', 'PMC7712215.txt', 'PMC11594459.txt'],
    'myenteric nerve plexus of small intestine': [
        'PMC7610403.txt', 'PMC8099699.txt', 'PMC11119846.txt', 's00441-020-03279-6.txt'
    ],
    'cervical dorsal root ganglion': ['PMC11723807.txt', 'PMC8929296.txt', '10.1186_1744-8069-3-42.txt', 'PMC6564303.txt'],
    'thoracic dorsal root ganglion': ['PMC11723807.txt', 'PMC8929296.txt', '10.1186_1744-8069-3-42.txt', 'PMC6564303.txt'],
    'lumbar dorsal root ganglion': ['PMC11723807.txt', 'PMC8929296.txt', '10.1186_1744-8069-3-42.txt', 'PMC6564303.txt'],
    'sacral dorsal root ganglion': ['PMC11723807.txt', 'PMC8929296.txt', '10.1186_1744-8069-3-42.txt', 'PMC6564303.txt'],
}

# create report
out_md = Path('outputs/pns_54terms_validation_report.md')
out_csv = Path('outputs/pns_54terms_validation_report.csv')
out_summary = Path('outputs/executive_summary.md')

status_counts = Counter()
status_rows = {'OK': [], 'PARTIAL': [], 'NO_MATCH': []}

with out_md.open('w') as md, out_csv.open('w', newline='') as csv_out:
    fieldnames = [
        'ID','label','soma_location','soma_location_ID','marker','marker_ID',
        'references','matched_files','marker_found','location_found','location_partial_found',
        'marker_snippet','location_snippet',
        'marker_and_partial_location_same_paragraph','partial_location_snippet',
        'marker_and_full_location_same_paragraph','full_location_snippet',
        'match_status'
    ]
    w = csv.DictWriter(csv_out, fieldnames=fieldnames)
    w.writeheader()

    md.write('# PNS 54 Terms Validation Report (Local Text Scan)\n\n')
    md.write('This report scans local text files in `pdfs/` for marker and location mentions.\n\n')
    md.write('## Match Status Definitions\n')
    md.write('- **OK**: Marker AND full location (with segment qualifier like "cervical DRG") found in same paragraph\n')
    md.write('- **PARTIAL**: Marker found AND location found somewhere in text, but NOT both in same paragraph with full qualifier\n')
    md.write('- **NO_MATCH**: Marker or location not found in any reference text\n\n')

    for row in rows:
        label = row['label']
        marker = row['marker']
        location = row['soma_location']
        refs = [r.strip() for r in row['references'].split('|') if r.strip()]
        matched_files = []
        marker_found = False
        location_found = False
        location_partial_found = False
        marker_snippet = ''
        location_snippet = ''

        # aggregate over all references
        for ref in refs:
            for fname in ref_to_files.get(ref, []):
                if fname not in matched_files:
                    matched_files.append(fname)

        # include supplemental references by location
        for fname in supplemental_by_location.get(location, []):
            if fname in text_content and fname not in matched_files:
                matched_files.append(fname)

        marker_variants = make_marker_variants(marker)
        marker_variants = make_marker_variants(marker)
        loc_variants = make_location_variants(location)
        # scan matched files
        for fname in matched_files:
            text = text_content.get(fname, '')
            if not text:
                continue
            if not marker_found:
                for mv in marker_variants:
                    snippets = find_snippets(text, mv)
                    if snippets:
                        marker_found = True
                        marker_snippet = snippets[0]
                        break
            if not location_found:
                for loc_variant in make_location_variants(location):
                    snippets = find_snippets(text, loc_variant)
                    if snippets:
                        if loc_variant.lower() == location.lower():
                            location_found = True
                            location_snippet = snippets[0]
                        else:
                            location_partial_found = True
                            if not location_snippet:
                                location_snippet = snippets[0]
                        break

        # strict support: marker and PARTIAL location in same paragraph (e.g., just "DRG")
        partial_loc_supported = False
        partial_loc_snippet = ''
        for fname in matched_files:
            text = text_content.get(fname, '')
            if not text:
                continue
            ok, snippet = marker_location_in_same_paragraph(text, marker_variants, loc_variants)
            if ok:
                partial_loc_supported = True
                partial_loc_snippet = snippet
                break

        # full location match: marker and FULL location (with segment) in same paragraph
        full_loc_supported = False
        full_loc_snippet = ''
        for fname in matched_files:
            text = text_content.get(fname, '')
            if not text:
                continue
            ok, snippet = marker_and_full_location_in_same_paragraph(text, marker_variants, location)
            if ok:
                full_loc_supported = True
                full_loc_snippet = snippet
                break

        # match status per requested rules:
        # OK = marker + full location (with segment qualifier) in same paragraph
        # PARTIAL = marker found AND location found in text (anywhere), but not full co-occurrence
        # NO_MATCH = marker or location not found
        if full_loc_supported:
            match_status = 'OK'
        elif marker_found and (location_found or location_partial_found):
            match_status = 'PARTIAL'
        else:
            match_status = 'NO_MATCH'

        status_counts[match_status] += 1
        status_rows[match_status].append(f"{row['ID']} {label}")

        w.writerow({
            'ID': row['ID'],
            'label': label,
            'soma_location': location,
            'soma_location_ID': row['soma_location_ID'],
            'marker': marker,
            'marker_ID': row['marker_ID'],
            'references': '|'.join(refs),
            'matched_files': '|'.join(matched_files),
            'marker_found': marker_found,
            'location_found': location_found,
            'location_partial_found': location_partial_found,
            'marker_snippet': marker_snippet,
            'location_snippet': location_snippet,
            'marker_and_partial_location_same_paragraph': partial_loc_supported,
            'partial_location_snippet': partial_loc_snippet,
            'marker_and_full_location_same_paragraph': full_loc_supported,
            'full_location_snippet': full_loc_snippet,
            'match_status': match_status,
        })

        md.write(f"## {row['ID']} {label}\n")
        md.write(f"- marker: {marker} ({row['marker_ID']})\n")
        md.write(f"- soma_location: {location} ({row['soma_location_ID']})\n")
        md.write(f"- references: {', '.join(refs) if refs else 'None'}\n")
        md.write(f"- matched_files: {', '.join(matched_files) if matched_files else 'None'}\n")
        md.write(f"- marker_found: {marker_found}\n")
        md.write(f"- location_found: {location_found}\n")
        md.write(f"- location_partial_found: {location_partial_found}\n")
        md.write(f"- marker_and_partial_location_same_paragraph: {partial_loc_supported}\n")
        md.write(f"- marker_and_full_location_same_paragraph: {full_loc_supported}\n")
        md.write(f"- match_status: {match_status}\n")
        if marker_snippet:
            md.write(f"- marker_snippet: {marker_snippet[:240]}\n")
        if location_snippet:
            md.write(f"- location_snippet: {location_snippet[:240]}\n")
        if partial_loc_snippet and not full_loc_supported:
            md.write(f"- partial_location_snippet: {partial_loc_snippet[:240]}\n")
        if full_loc_snippet:
            md.write(f"- full_location_snippet: {full_loc_snippet[:240]}\n")
        md.write('\n')

with out_summary.open('w') as sm:
    sm.write('# PNS 54 Terms Executive Summary\n\n')
    total = sum(status_counts.values())
    sm.write(f'- total_terms: {total}\n')
    sm.write(f"- OK: {status_counts.get('OK', 0)}\n")
    sm.write(f"- PARTIAL: {status_counts.get('PARTIAL', 0)}\n")
    sm.write(f"- NO_MATCH: {status_counts.get('NO_MATCH', 0)}\n\n")
    sm.write('## Why So Many PARTIAL Matches\n')
    sm.write('- Many sources mention markers and locations in the same document but not in the same paragraph with the exact segment-qualified location (e.g., cervical/lumbar/sacral/thoracic DRG), which this analysis requires for OK.\n')
    sm.write('- Some references use general terms like \"dorsal root ganglion\" or \"DRG\" without segment qualifiers, so they satisfy PARTIAL but not OK.\n\n')

    sm.write('## OK\n')
    if status_rows['OK']:
        for item in status_rows['OK']:
            sm.write(f'- {item}\n')
    else:
        sm.write('- None\n')
    sm.write('\n## PARTIAL\n')
    if status_rows['PARTIAL']:
        for item in status_rows['PARTIAL']:
            sm.write(f'- {item}\n')
    else:
        sm.write('- None\n')
    sm.write('\n## NO_MATCH\n')
    if status_rows['NO_MATCH']:
        for item in status_rows['NO_MATCH']:
            sm.write(f'- {item}\n')
    else:
        sm.write('- None\n')

print('wrote', out_md, out_csv, out_summary)
