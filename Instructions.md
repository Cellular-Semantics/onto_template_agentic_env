# Instructions.md

<!-- Project-specific instructions go here -->

## Persistent Rules For Gene/Protein Mapping

1. For `gene_protein_map.csv`, resolve `pro_id` and `pro_name` using OLS4 via MCP only.
2. Do not infer or construct Protein Ontology IDs from UniProt accessions.
3. For default template population, use gene-level Protein Ontology classes (`PR:000...`), not organism-specific entries (`PR:<UniProt>`).
4. Treat organism-specific PRO terms as optional and include them only if explicitly requested.
5. Every chosen `pro_id` must be auditable from OLS4 MCP output (matched `curie` and label).
6. When helpful, provide the PRO Consortium URL form for verification:
   - `https://proconsortium.org/cgi-bin/entry_pro?id=PR_########`

## Current Project

<!-- Describe the template(s) you are working with -->

## Template State

<!-- Describe what fields are populated vs. need to be filled -->

## Special Requirements

<!-- Any constraints, preferences, or notes for the agent -->
