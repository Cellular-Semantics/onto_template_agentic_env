#!/usr/bin/env python3
"""
Gene/Protein Lookup Tool

This script extracts gene and protein identifiers from source data and creates
cross-reference tables by querying public databases:
- HGNC (HUGO Gene Nomenclature Committee) - gene symbols and IDs
- UniProt - protein information
- NCBI Gene - gene information
- PRO (Protein Ontology) - protein ontology IDs via OLS4

Usage:
    python scripts/gene_protein_lookup.py [source_file] [--output OUTPUT]
    
Examples:
    python scripts/gene_protein_lookup.py source_data/PNS_54terms.csv
    python scripts/gene_protein_lookup.py source_data/PNS_54terms.csv --output outputs/gene_protein_map.csv
"""

import argparse
import csv
import json
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass
class GeneProteinRecord:
    """A unified record for gene/protein information."""
    # Input identifiers
    source_marker: str = ""
    source_marker_id: str = ""
    
    # HGNC data
    hgnc_id: str = ""
    hgnc_symbol: str = ""
    hgnc_name: str = ""
    
    # NCBI Gene data
    ncbi_gene_id: str = ""
    ncbi_gene_symbol: str = ""
    ncbi_gene_description: str = ""
    
    # UniProt data
    uniprot_ids: list = field(default_factory=list)
    uniprot_names: list = field(default_factory=list)
    
    # Protein Ontology (PRO) data
    pro_id: str = ""
    pro_name: str = ""
    pro_url: str = ""
    
    # Recommended protein ID (PRO if available, otherwise UniProt)
    recommended_protein_id: str = ""
    recommended_protein_source: str = ""
    
    # Synonyms (useful for text matching)
    all_synonyms: list = field(default_factory=list)
    
    # Status
    lookup_status: str = ""
    error_message: str = ""


def make_api_request(url: str, headers: Optional[dict] = None, timeout: int = 30) -> Optional[dict]:
    """Make an API request with error handling and rate limiting."""
    if headers is None:
        headers = {"Accept": "application/json"}
    
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except HTTPError as e:
        if e.code == 404:
            return None
        print(f"  HTTP Error {e.code} for {url}")
        return None
    except URLError as e:
        print(f"  URL Error for {url}: {e.reason}")
        return None
    except json.JSONDecodeError:
        print(f"  JSON decode error for {url}")
        return None
    except Exception as e:
        print(f"  Error for {url}: {e}")
        return None


def lookup_hgnc_by_id(hgnc_id: str) -> Optional[dict]:
    """Look up gene info from HGNC by numeric ID."""
    # Clean the ID - extract just the number
    hgnc_num = re.sub(r'\D', '', hgnc_id)
    if not hgnc_num:
        return None
    
    url = f"https://rest.genenames.org/fetch/hgnc_id/{hgnc_num}"
    headers = {"Accept": "application/json"}
    
    data = make_api_request(url, headers)
    if data and "response" in data and data["response"].get("docs"):
        return data["response"]["docs"][0]
    return None


def lookup_hgnc_by_symbol(symbol: str) -> Optional[dict]:
    """Look up gene info from HGNC by gene symbol."""
    url = f"https://rest.genenames.org/fetch/symbol/{symbol}"
    headers = {"Accept": "application/json"}
    
    data = make_api_request(url, headers)
    if data and "response" in data and data["response"].get("docs"):
        return data["response"]["docs"][0]
    return None


def lookup_ncbi_gene(gene_id: str) -> Optional[dict]:
    """Look up gene info from NCBI Gene."""
    # Use NCBI E-utilities
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id={gene_id}&retmode=json"
    
    data = make_api_request(url)
    if data and "result" in data:
        result = data["result"]
        if gene_id in result:
            return result[gene_id]
    return None


def lookup_uniprot_by_gene(gene_symbol: str, organism: str = "human") -> list:
    """Look up UniProt entries by gene symbol."""
    taxon = "9606" if organism.lower() == "human" else organism
    
    # UniProt REST API query
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene_symbol}+AND+organism_id:{taxon}&format=json&size=5"
    headers = {"Accept": "application/json"}
    
    data = make_api_request(url, headers)
    if data and "results" in data:
        return data["results"]
    return []


def lookup_uniprot_by_hgnc(hgnc_id: str) -> list:
    """Look up UniProt entries by HGNC ID."""
    hgnc_num = re.sub(r'\D', '', hgnc_id)
    if not hgnc_num:
        return []
    
    url = f"https://rest.uniprot.org/uniprotkb/search?query=xref:hgnc-{hgnc_num}+AND+organism_id:9606&format=json&size=5"
    headers = {"Accept": "application/json"}
    
    data = make_api_request(url, headers)
    if data and "results" in data:
        return data["results"]
    return []


def lookup_pro_by_gene_symbol(gene_symbol: str) -> Optional[dict]:
    """Look up Protein Ontology (PRO) entry by gene symbol via OLS4.
    
    Searches for human gene-level PRO entries.
    Returns the PRO ID and name if found.
    """
    # Search OLS4 for PRO entries matching the gene symbol
    query = gene_symbol.upper()
    url = f"https://www.ebi.ac.uk/ols4/api/search?q={query}&ontology=pr&exact=true&rows=15"
    headers = {"Accept": "application/json"}
    
    data = make_api_request(url, headers)
    if not data or "response" not in data:
        return None
    
    docs = data.get("response", {}).get("docs", [])
    
    # First pass: look for human-specific entries
    for doc in docs:
        label = doc.get("label", "")
        obo_id = doc.get("obo_id", "")
        iri = doc.get("iri", "")
        short_form = doc.get("short_form", "")
        
        # Check for human-specific entry
        if "(human)" in label.lower() and obo_id and obo_id.startswith("PR:"):
            return {
                "pro_id": obo_id,
                "pro_name": label,
                "pro_iri": iri,
                "pro_url": f"https://proconsortium.org/cgi-bin/entry_pro?id={short_form}"
            }
    
    # Second pass: look for species-independent (gene-level) entries starting with PR:000
    for doc in docs:
        label = doc.get("label", "")
        obo_id = doc.get("obo_id", "")
        iri = doc.get("iri", "")
        short_form = doc.get("short_form", "")
        
        # Species-independent PRO IDs typically start with PR:000
        if obo_id and obo_id.startswith("PR:000"):
            return {
                "pro_id": obo_id,
                "pro_name": label,
                "pro_iri": iri,
                "pro_url": f"https://proconsortium.org/cgi-bin/entry_pro?id={short_form}"
            }
    
    # Third pass: any valid PRO ID
    for doc in docs:
        label = doc.get("label", "")
        obo_id = doc.get("obo_id", "")
        iri = doc.get("iri", "")
        short_form = doc.get("short_form", "")
        
        if obo_id and obo_id.startswith("PR:"):
            return {
                "pro_id": obo_id,
                "pro_name": label,
                "pro_iri": iri,
                "pro_url": f"https://proconsortium.org/cgi-bin/entry_pro?id={short_form}"
            }
    
    return None


def lookup_pro_by_uniprot(uniprot_id: str) -> Optional[dict]:
    """Look up Protein Ontology (PRO) entry by UniProt ID via OLS4.
    
    Searches for PRO entries that cross-reference the UniProt ID.
    """
    url = f"https://www.ebi.ac.uk/ols4/api/search?q={uniprot_id}&ontology=pr&rows=10"
    headers = {"Accept": "application/json"}
    
    data = make_api_request(url, headers)
    if not data or "response" not in data:
        return None
    
    docs = data.get("response", {}).get("docs", [])
    
    for doc in docs:
        obo_id = doc.get("obo_id", "")
        label = doc.get("label", "")
        iri = doc.get("iri", "")
        short_form = doc.get("short_form", "")
        
        # Check if UniProt ID appears in annotations or xrefs
        if obo_id and obo_id.startswith("PR:"):
            return {
                "pro_id": obo_id,
                "pro_name": label,
                "pro_iri": iri,
                "pro_url": f"https://proconsortium.org/cgi-bin/entry_pro?id={short_form}"
            }
    
    return None
    if data and "results" in data:
        return data["results"]
    return []


def extract_hgnc_id_from_url(url: str) -> Optional[str]:
    """Extract HGNC ID from identifiers.org URL."""
    # Pattern: http://identifiers.org/hgnc/12345
    match = re.search(r'hgnc[:/](\d+)', url, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def extract_ncbi_gene_id_from_url(url: str) -> Optional[str]:
    """Extract NCBI Gene ID from URL."""
    # Pattern: https://www.ncbi.nlm.nih.gov/gene/12345
    match = re.search(r'ncbi\.nlm\.nih\.gov/gene/(\d+)', url, re.IGNORECASE)
    if match:
        return match.group(1)
    
    # Pattern: http://identifiers.org/ncbigene/12345
    match = re.search(r'ncbigene[:/](\d+)', url, re.IGNORECASE)
    if match:
        return match.group(1)
    
    return None


def extract_uniprot_id_from_url(url: str) -> Optional[str]:
    """Extract UniProt ID from URL."""
    # Pattern: https://www.uniprot.org/uniprot/P12345
    match = re.search(r'uniprot[:/]([A-Z0-9]+)', url, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def process_marker(marker: str, marker_id: str) -> GeneProteinRecord:
    """Process a marker and its ID to create a comprehensive record."""
    record = GeneProteinRecord(
        source_marker=marker,
        source_marker_id=marker_id
    )
    
    try:
        # Check if it's an HGNC ID
        hgnc_id = extract_hgnc_id_from_url(marker_id)
        if hgnc_id:
            record.hgnc_id = f"HGNC:{hgnc_id}"
            print(f"  Looking up HGNC:{hgnc_id}...")
            
            hgnc_data = lookup_hgnc_by_id(hgnc_id)
            if hgnc_data:
                record.hgnc_symbol = hgnc_data.get("symbol", "")
                record.hgnc_name = hgnc_data.get("name", "")
                
                # Get NCBI Gene ID from HGNC cross-refs
                if "entrez_id" in hgnc_data:
                    record.ncbi_gene_id = str(hgnc_data["entrez_id"])
                
                # Collect synonyms
                synonyms = []
                if "alias_symbol" in hgnc_data:
                    synonyms.extend(hgnc_data["alias_symbol"])
                if "prev_symbol" in hgnc_data:
                    synonyms.extend(hgnc_data["prev_symbol"])
                if "alias_name" in hgnc_data:
                    synonyms.extend(hgnc_data["alias_name"])
                record.all_synonyms = synonyms
                
                time.sleep(0.2)  # Rate limiting
                
                # Look up UniProt by HGNC
                print(f"  Looking up UniProt for {record.hgnc_symbol}...")
                uniprot_results = lookup_uniprot_by_hgnc(hgnc_id)
                if uniprot_results:
                    for entry in uniprot_results:
                        if "primaryAccession" in entry:
                            record.uniprot_ids.append(entry["primaryAccession"])
                        if "proteinDescription" in entry:
                            desc = entry["proteinDescription"]
                            if "recommendedName" in desc and "fullName" in desc["recommendedName"]:
                                record.uniprot_names.append(desc["recommendedName"]["fullName"]["value"])
                
                record.lookup_status = "success"
            else:
                record.lookup_status = "hgnc_not_found"
                record.error_message = f"HGNC ID {hgnc_id} not found"
        
        # Check if it's a gene symbol (no URL pattern matched)
        elif not marker_id.startswith("http") and marker.isupper() and len(marker) <= 10:
            print(f"  Looking up gene symbol: {marker}...")
            hgnc_data = lookup_hgnc_by_symbol(marker)
            if hgnc_data:
                record.hgnc_id = f"HGNC:{hgnc_data.get('hgnc_id', '').replace('HGNC:', '')}"
                record.hgnc_symbol = hgnc_data.get("symbol", "")
                record.hgnc_name = hgnc_data.get("name", "")
                
                if "entrez_id" in hgnc_data:
                    record.ncbi_gene_id = str(hgnc_data["entrez_id"])
                
                record.lookup_status = "success"
            else:
                record.lookup_status = "symbol_not_found"
                record.error_message = f"Gene symbol {marker} not found in HGNC"
        
        # Check for NCBI Gene ID
        ncbi_id = extract_ncbi_gene_id_from_url(marker_id)
        if ncbi_id:
            record.ncbi_gene_id = ncbi_id
            print(f"  Looking up NCBI Gene: {ncbi_id}...")
            ncbi_data = lookup_ncbi_gene(ncbi_id)
            if ncbi_data:
                record.ncbi_gene_symbol = ncbi_data.get("name", "")
                record.ncbi_gene_description = ncbi_data.get("description", "")
                record.lookup_status = "success"
        
        # Check for UniProt ID
        uniprot_id = extract_uniprot_id_from_url(marker_id)
        if uniprot_id:
            record.uniprot_ids.append(uniprot_id)
            record.lookup_status = "success"
        
        # If nothing found, mark as unresolved
        if not record.lookup_status:
            record.lookup_status = "unresolved"
            record.error_message = "Could not identify ID type or lookup failed"
        
        # Look up Protein Ontology (PRO) ID if we have a gene symbol
        if record.hgnc_symbol and record.lookup_status == "success":
            time.sleep(0.2)  # Rate limiting
            print(f"  Looking up PRO for {record.hgnc_symbol}...")
            pro_data = lookup_pro_by_gene_symbol(record.hgnc_symbol)
            if pro_data:
                record.pro_id = pro_data.get("pro_id", "")
                record.pro_name = pro_data.get("pro_name", "")
                record.pro_url = pro_data.get("pro_url", "")
            elif record.uniprot_ids:
                # Try looking up PRO by UniProt ID
                for uniprot_id in record.uniprot_ids[:2]:
                    time.sleep(0.1)
                    pro_data = lookup_pro_by_uniprot(uniprot_id)
                    if pro_data:
                        record.pro_id = pro_data.get("pro_id", "")
                        record.pro_name = pro_data.get("pro_name", "")
                        record.pro_url = pro_data.get("pro_url", "")
                        break
        
        # Set recommended protein ID: PRO if available, otherwise first UniProt
        if record.pro_id:
            record.recommended_protein_id = record.pro_id
            record.recommended_protein_source = "PRO"
        elif record.uniprot_ids:
            record.recommended_protein_id = f"UniProtKB:{record.uniprot_ids[0]}"
            record.recommended_protein_source = "UniProt"
        else:
            record.recommended_protein_id = ""
            record.recommended_protein_source = ""
    
    except Exception as e:
        record.lookup_status = "error"
        record.error_message = str(e)
    
    return record


def extract_markers_from_csv(filepath: str) -> list[tuple[str, str, str]]:
    """Extract unique markers and their IDs from a CSV file.
    
    Returns list of (marker, marker_id, source_row_id) tuples.
    """
    markers = []
    seen = set()
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Try common column names
            marker = row.get("marker", row.get("Marker", row.get("gene", row.get("Gene", ""))))
            marker_id = row.get("marker_ID", row.get("marker_id", row.get("gene_id", row.get("Gene_ID", ""))))
            row_id = row.get("ID", row.get("id", row.get("term_id", "")))
            
            if marker and (marker, marker_id) not in seen:
                seen.add((marker, marker_id))
                markers.append((marker, marker_id, row_id))
    
    return markers


def generate_mapping_table(records: list[GeneProteinRecord], output_path: str):
    """Generate a CSV mapping table from the records."""
    fieldnames = [
        "source_marker", "source_marker_id",
        "hgnc_id", "hgnc_symbol", "hgnc_name",
        "ncbi_gene_id", "ncbi_gene_symbol",
        "pro_id", "pro_name",
        "uniprot_ids", "uniprot_names",
        "recommended_protein_id", "recommended_protein_source",
        "all_synonyms",
        "lookup_status", "error_message"
    ]
    
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for record in records:
            writer.writerow({
                "source_marker": record.source_marker,
                "source_marker_id": record.source_marker_id,
                "hgnc_id": record.hgnc_id,
                "hgnc_symbol": record.hgnc_symbol,
                "hgnc_name": record.hgnc_name,
                "ncbi_gene_id": record.ncbi_gene_id,
                "ncbi_gene_symbol": record.ncbi_gene_symbol,
                "pro_id": record.pro_id,
                "pro_name": record.pro_name,
                "uniprot_ids": "|".join(record.uniprot_ids),
                "uniprot_names": "|".join(record.uniprot_names),
                "recommended_protein_id": record.recommended_protein_id,
                "recommended_protein_source": record.recommended_protein_source,
                "all_synonyms": "|".join(record.all_synonyms),
                "lookup_status": record.lookup_status,
                "error_message": record.error_message
            })
    
    print(f"\nMapping table saved to: {output_path}")


def generate_markdown_report(records: list[GeneProteinRecord], output_path: str):
    """Generate a markdown report from the records."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Gene/Protein Mapping Report\n\n")
        f.write(f"Generated from source data. Total unique markers: {len(records)}\n\n")
        
        # Summary
        success = sum(1 for r in records if r.lookup_status == "success")
        failed = len(records) - success
        pro_found = sum(1 for r in records if r.pro_id)
        uniprot_fallback = sum(1 for r in records if r.recommended_protein_source == "UniProt")
        
        f.write("## Summary\n\n")
        f.write(f"- ✅ Successfully resolved: {success}\n")
        f.write(f"- ❌ Failed/Unresolved: {failed}\n")
        f.write(f"- 🧬 PRO IDs found: {pro_found}\n")
        f.write(f"- 📦 UniProt fallback: {uniprot_fallback}\n\n")
        
        # Recommended Protein IDs (main table for ontology use)
        f.write("## Recommended Protein IDs for Ontology Use\n\n")
        f.write("Use `recommended_protein_id` column - PRO if available, otherwise UniProt.\n\n")
        f.write("| Source Marker | HGNC Symbol | Recommended Protein ID | Source | PRO Name |\n")
        f.write("|---------------|-------------|------------------------|--------|----------|\n")
        
        for r in records:
            if r.lookup_status == "success":
                pro_name = r.pro_name[:40] + "..." if len(r.pro_name) > 40 else r.pro_name
                f.write(f"| {r.source_marker} | {r.hgnc_symbol or '-'} | {r.recommended_protein_id or '-'} | {r.recommended_protein_source or '-'} | {pro_name or '-'} |\n")
        
        # Full details table
        f.write("\n## Full Resolved Markers\n\n")
        f.write("| Source Marker | HGNC Symbol | HGNC Name | NCBI Gene ID | UniProt IDs |\n")
        f.write("|---------------|-------------|-----------|--------------|-------------|\n")
        
        for r in records:
            if r.lookup_status == "success":
                uniprot = ", ".join(r.uniprot_ids[:3]) if r.uniprot_ids else "-"
                f.write(f"| {r.source_marker} | {r.hgnc_symbol or '-'} | {r.hgnc_name or '-'} | {r.ncbi_gene_id or '-'} | {uniprot} |\n")
        
        # Synonyms section (useful for text searching)
        f.write("\n## Synonym Reference (for text searching)\n\n")
        for r in records:
            if r.lookup_status == "success" and r.all_synonyms:
                f.write(f"### {r.hgnc_symbol}\n")
                f.write(f"- **Official name:** {r.hgnc_name}\n")
                f.write(f"- **Synonyms:** {', '.join(r.all_synonyms)}\n\n")
        
        # Failed lookups
        if failed > 0:
            f.write("\n## Unresolved Markers\n\n")
            f.write("| Source Marker | Source ID | Status | Error |\n")
            f.write("|---------------|-----------|--------|-------|\n")
            
            for r in records:
                if r.lookup_status != "success":
                    f.write(f"| {r.source_marker} | {r.source_marker_id[:50]}... | {r.lookup_status} | {r.error_message} |\n")
    
    print(f"Markdown report saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Look up gene/protein information from source data markers"
    )
    parser.add_argument(
        "source_file",
        help="Path to source CSV file with marker columns"
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Output path for mapping table (default: outputs/gene_protein_map.csv)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["csv", "markdown", "both"],
        default="both",
        help="Output format (default: both)"
    )
    
    args = parser.parse_args()
    
    source_path = Path(args.source_file)
    if not source_path.exists():
        print(f"Error: Source file not found: {source_path}")
        sys.exit(1)
    
    # Set default output paths
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    csv_output = args.output or str(output_dir / "gene_protein_map.csv")
    md_output = csv_output.replace(".csv", "_report.md")
    
    print(f"Processing: {source_path}")
    print("-" * 50)
    
    # Extract markers
    markers = extract_markers_from_csv(str(source_path))
    print(f"Found {len(markers)} unique markers\n")
    
    # Process each marker
    records = []
    for i, (marker, marker_id, row_id) in enumerate(markers, 1):
        print(f"[{i}/{len(markers)}] Processing: {marker}")
        record = process_marker(marker, marker_id)
        records.append(record)
        time.sleep(0.3)  # Rate limiting between requests
    
    # Generate outputs
    print("\n" + "-" * 50)
    if args.format in ["csv", "both"]:
        generate_mapping_table(records, csv_output)
    
    if args.format in ["markdown", "both"]:
        generate_markdown_report(records, md_output)
    
    print("\nDone!")


if __name__ == "__main__":
    main()
