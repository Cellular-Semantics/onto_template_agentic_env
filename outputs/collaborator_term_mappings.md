# Collaborator Term Mappings to Proposed CL Terms

**Date**: 2026-03-10
**Source report**: `outputs/myenteric_neurons_curation_report.md`

This table maps each collaborator-proposed term to the most specific available CL term from the curation report, with status indicated for each mapping term.

## Status key

| Status | Meaning |
|---|---|
| **In report** | Term is proposed in the curation report and ready (or near-ready) for CL integration |
| **Suggested addition** | Term not currently in the report; addition recommended to improve mapping specificity |
| **No mapping** | No proposed CL term covers this population; see notes for reason |

---

## Mapping Table

| Collaborator term | Best CL mapping | Mapping term status | Notes |
|---|---|---|---|
| myenteric ganglion ChAT neuron | cholinergic neuron of myenteric plexus | **In report** | Grouping class (defined by `capable of` GO:0014055 + myenteric location). ChAT alone does not discriminate between EMN, IPAN, and ascending interneuron. More specific mapping requires NOS1 co-expression status and morphology. |
| myenteric ganglion ChAT/CALR/SOM/SP neuron | calretinin-positive intrinsic primary afferent neuron of myenteric plexus | **In report** | Specific mapping. ChAT+/calretinin+ combination is the defining signature of SN1 (Chen et al.). SOM and SP are additional IPAN co-markers consistent with this assignment. |
| myenteric ganglion NF200 neuron | — | **No mapping** | Polyphyletic. NF200 expression is found in NF200+ excitatory motor neuron subsets (Chen EMN1/EMN2), NF200+ inhibitory motor neuron subsets (Chen IMN1/IMN2), and both IPAN subtypes (SN1/SN2). NF200 reflects axon calibre, not cell identity, and cannot discriminate between functional classes. No valid single-class mapping is possible. |
| myenteric ganglion nNOS neuron | nitrergic neuron of myenteric plexus | **In report** | Grouping class (defined by `capable of` GO:0006809 + myenteric location). NOS1 alone does not discriminate between inhibitory motor neurons and NOS1+ descending interneurons. More specific mapping requires ChAT co-expression status and functional target (smooth muscle vs. interneuron). |
| myenteric ganglion nNOS/ChAT neuron | — | **No mapping** | Co-expressing neurons are acknowledged in EMN and IMN definitions via 'primary neurotransmitter' language (Majd et al. 2025 note ChAT/NOS1 co-expression is more common than the strict binary suggests), but no separate term is proposed for the co-expressing intermediate population. |
| myenteric ganglion nNOS/VIP neuron | VIP-positive inhibitory motor neuron of myenteric plexus | **Suggested addition** | NOS1+/VIP+ is the chemical code of Chen IMN1 and IMN3 (the VIP-expressing IMN subsets, regardless of NF200 status). A grouping term for NOS1+/ChAT−/VIP+ inhibitory motor neurons could be defined without NF200, providing a specific mapping. Not currently in the report. |
| myenteric ganglion VIP neuron | nitrergic neuron of myenteric plexus | **In report** (approximate) | VIP is a co-transmitter of NOS1+ inhibitory motor neurons and is not expressed as a sole identifier of a clean functional class. The nitrergic grouping class is the best available mapping. If 'VIP-positive inhibitory motor neuron of myenteric plexus' is added (see row above), that would be a more specific mapping for VIP+ neurons confirmed to be NOS1+. VIP is also expressed in PSVN neurons, so VIP alone without NOS1 confirmation remains ambiguous. |
| myenteric ganglion VIP/GAL neuron | inhibitory motor neuron of myenteric plexus | **In report** (approximate) | VIP+galanin co-expression has been reported in a subset of nitrergic inhibitory motor neurons. Galanin was not included in Chen et al.'s antibody panel, so no Chen subtype maps directly. The inhibitory motor neuron class is the best available mapping. A dedicated 'galanin-positive inhibitory motor neuron of myenteric plexus' term would require additional literature support. |

---

## Summary

| Mapping quality | Count | Collaborator terms |
|---|---|---|
| Specific mapping (in report) | 1 | ChAT/CALR/SOM/SP |
| Grouping class mapping (in report) | 3 | ChAT, nNOS, VIP |
| Approximate mapping (in report) | 1 | VIP/GAL |
| Improved by suggested addition | 2 | nNOS/VIP, VIP |
| No mapping possible | 2 | NF200, nNOS/ChAT |

---

## Suggested Addition Detail

### VIP-positive inhibitory motor neuron of myenteric plexus

- **Proposed label**: VIP-positive inhibitory motor neuron of myenteric plexus
- **Proposed parent**: inhibitory motor neuron of myenteric plexus [NEW — in report]
- **Chemical code**: NOS1+, ChAT−, VIP+
- **Corresponds to**: Chen et al. IMN1 + IMN3 (both NOS1+/VIP+; differ only by NF200 status, which is not used here)
- **Rationale**: VIP is a signaling peptide with discrete categorical expression (unlike NF200, which is structural and continuous). VIP IHC is technically reliable and the VIP+/NOS1+ combination is well-replicated across human and animal ENS studies (Brehmer 2021, Chen et al.). Defining this subtype without NF200 avoids the axon-calibre confound.
- **Collaborator mappings enabled**: 'myenteric ganglion nNOS/VIP neuron' (specific); 'myenteric ganglion VIP neuron' (if NOS1 co-expression is confirmed in that dataset)
- **Cross-species note**: VIP expression in NOS1+ myenteric neurons has been reported in human, guinea pig, and mouse. Cross-species support is stronger than for NF200-based splits.
- **Status**: Recommended for addition to curation report. A full curation report entry should be written before CL integration.
