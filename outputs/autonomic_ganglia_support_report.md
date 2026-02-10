# Autonomic Ganglia Support Evidence (from autonomic_ganglia report + retrieved PMCs)

This report lists supplemental publications referenced in `pdfs/autonomic_ganglia_neurochemical_markers_report.md` and maps them to rows in `source_data/PNS_54terms.csv` by soma location.
These are SUPPORTING references; they do not replace the primary references in each row.

## main ciliary ganglion
Rows:
- PROPOSED:0012 ciliary ganglion VIP-PHI neuron | marker: VIP

Supporting publications:
- Ocular Autonomic Nervous System: An Update from Anatomy to Physiological Functions | PMCID: PMC8788436 | DOI: 10.3390/vision6010006
  Note: Review mentions VIP immunoreactivity in ciliary ganglion context; supports VIP marker in ciliary ganglion neurons.
- VIP modulates neuronal nicotinic acetylcholine receptor function by a cyclic AMP-dependent mechanism | PMCID: PMC6576920 | DOI: 10.1523/jneurosci.14-06-03540.1994
  Note: Ciliary ganglion neurons; VIP as functional modulator. PDF not retrieved due to PMC access error.
- Catecholaminergic properties of cholinergic neurons and synapses in adult rat ciliary ganglion | PMCID: PMC6569016 | DOI: 10.1523/jneurosci.07-11-03574.1987
  Note: Ciliary ganglion neurons with cholinergic marker ChAT and TH; general ciliary ganglion marker context.

## cardiac ganglion
Rows:
- PROPOSED:0013 intrinsic cardiac ganglion TH neuron | marker: TH

Supporting publications:
- A single cell transcriptomics map of paracrine networks in the intrinsic cardiac nervous system | PMCID: PMC8324809 | DOI: 10.1016/j.isci.2021.102713
  Note: Intrinsic cardiac ganglia show cholinergic and catecholaminergic (TH) markers and their co-expression.
- The Intrinsic Cardiac Nervous System and Its Role in Cardiac Pacemaking and Conduction | PMCID: PMC7712215 | DOI: 10.3390/jcdd7040054
  Note: Review summarizing cardiac ganglia neurochemical phenotypes including cholinergic and catecholaminergic markers.
- Remodeling of the Intracardiac Ganglia During the Development of Cardiovascular Autonomic Dysfunction in Type 2 Diabetes: Molecular Mechanisms and Therapeutics | PMCID: PMC11594459 | DOI: 10.3390/ijms252212464
  Note: Review on intracardiac ganglia structure and parasympathetic postganglionic neurons; contextual support for intrinsic cardiac ganglia.

## myenteric nerve plexus of small intestine
Rows:
- PROPOSED:0025 myenteric ganglion ChAT neuron | marker: CHAT
- PROPOSED:0026 myenteric ganglion ChAT/CALR/SOM/SP neuron | marker: CHAT
- PROPOSED:0027 myenteric ganglion NF200 neuron | marker: Neurofilament 200 (NF200)
- PROPOSED:0028 myenteric ganglion nNOS neuron | marker: NOS1
- PROPOSED:0029 myenteric ganglion nNOS/ChAT neuron | marker: NOS1
- PROPOSED:0030 myenteric ganglion nNOS/VIP neuron | marker: NOS1
- PROPOSED:0031 myenteric ganglion VIP neuron | marker: VIP
- PROPOSED:0032 myenteric ganglion VIP/GAL neuron | marker: VIP

Supporting publications:
- Diversification of molecularly defined myenteric neuron classes revealed by single-cell RNA sequencing | PMCID: PMC7610403 | DOI: 10.1038/s41593-020-00736-x
  Note: Myenteric neuron classes with markers including ChAT, NOS1, VIP, GAL (context for myenteric plexus markers).
- scRNA-Seq Reveals New Enteric Nervous System Roles for GDNF, NRTN, and TBX3 | PMCID: PMC8099699 | DOI: 10.1016/j.jcmgh.2020.12.014
  Note: Myenteric neuron subtype markers including NOS1, VIP and other transcriptional markers; supports myenteric plexus marker usage.
- The Imperative for Innovative Enteric Nervous System–Intestinal Organoid Co-Culture Models | PMCID: PMC11119846 | DOI: 10.3390/cells13100820
  Note: Review mentioning myenteric and submucosal neuron diversity and neurotransmitters including VIP.
- The diversity of neuronal phenotypes in rodent and human autonomic ganglia | PMCID: PMC7584561 | DOI: 10.1007/s00441-020-03279-6
  Note: Review covering autonomic ganglia marker phenotypes; contextual support for autonomic markers.

## Retrieval status
- PDFs downloaded to `pdfs/` for PMCID: PMC8788436, PMC6576920, PMC8324809, PMC7712215, PMC11594459, PMC11119846, PMC7610403, PMC8099699, PMC6569016, PMC7584561.
- Full-text extraction via `artl-mcp` failed for PMC6576920 (unexpected response type). PDF is present locally.
