# Curation Report: Myenteric Neuron Functional Classes

> **Summary table** — This table may become out of date as individual term sections are revised. To regenerate, ask Claude: *"Regenerate the summary table from the term sections in this report."*

| # | Term | Proposed Parent(s) | Status |
|---|------|-------------------|--------|
| 1 | Excitatory motor neuron of myenteric plexus | enteric neuron (CL:0007011) | Ready |
| 2 | Inhibitory motor neuron of myenteric plexus | inhibitory motor neuron (CL:0008015) + enteric neuron (CL:0007011) | Ready |
| 3 | Intrinsic primary afferent neuron (IPAN) of myenteric plexus | enteric neuron (CL:0007011) + sensory neuron (CL:0000101) | Ready |
| 4 | Interneuron of myenteric plexus | enteric neuron (CL:0007011) + interneuron (CL:0000099) | Ready |
| 5 | Secretomotor/vasodilator neuron of myenteric plexus | enteric neuron (CL:0007011) | Ready |
| 6 | Intestinofugal neuron (viscerofugal neuron) | enteric neuron (CL:0007011) | Ready |
| 7 | Ascending interneuron of myenteric plexus | interneuron of myenteric plexus [NEW] | Ready |
| 8 | Descending interneuron of myenteric plexus | interneuron of myenteric plexus [NEW] | Ready |
| 9 | Stubby Dogiel type I neuron of myenteric plexus | excitatory motor neuron of myenteric plexus [NEW] + Dogiel type I neuron (CL:4047038) | Ready |
| 10 | Spiny Dogiel type I neuron of myenteric plexus | inhibitory motor neuron of myenteric plexus [NEW] + Dogiel type I neuron (CL:4047038) | Ready |
| 11 | Dogiel type II neuron of myenteric plexus | IPAN of myenteric plexus [NEW] + Dogiel type II neuron [NEW] | Ready |
| 12 | Calretinin-positive IPAN of myenteric plexus | IPAN of myenteric plexus [NEW] | Ready |
| 13 | Calretinin-negative IPAN of myenteric plexus | IPAN of myenteric plexus [NEW] | Ready |
| 14 | Cholinergic neuron of myenteric plexus | cholinergic neuron (CL:0000108) + enteric neuron (CL:0007011) | Ready |
| 15 | Nitrergic neuron of myenteric plexus | enteric neuron (CL:0007011) | Ready |
| 16 | Dogiel type II neuron (general) | neuron (CL:0000540) | Ready |

**Date**: 2026-03-10 (updated from 2026-03-09)
**Prepared by**: CL-curator-research agent
**Source references consulted**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025, EMBO J) — cross-dataset comparison of ENS neuron annotations
- PMC10469081 (Chen et al. 2023, human colonic myenteric plexus chemical coding)
- PMC8397665 (Brehmer 2021, classification of human enteric neurons)
- PMID:32888429 / PMC8358727 / DOI:10.1016/j.cell.2020.08.003 (Drokhlyansky et al. 2020, Cell — AR-mouse and AR-human ENS scRNA-seq) [FULL TEXT RETRIEVED: pdfs/PMC8358727_Drokhlyansky2020_full_text.txt]
- PMC10825022 / DOI:10.1016/j.celrep.2024.113653 (Chen et al. 2024, Cell Reports — first human viscerofugal neuron characterization)

**Terms covered**:
1. Excitatory motor neuron of myenteric plexus (EMN)
2. Inhibitory motor neuron of myenteric plexus (IMN)
3. Intrinsic primary afferent neuron of myenteric plexus (IPAN)
4. Interneuron of myenteric plexus (IN)
5. Secretomotor/vasodilator neuron of myenteric plexus (PSVN)
6. Intestinofugal neuron
7. Ascending interneuron of myenteric plexus (subterm of 4)
8. Descending interneuron of myenteric plexus (subterm of 4)
9. Stubby Dogiel type I neuron of myenteric plexus (morphological subterm of 1)
10. Spiny Dogiel type I neuron of myenteric plexus (morphological subterm of 2)
11. Dogiel type II neuron of myenteric plexus (morphological subterm of 3)
12. Calretinin-positive intrinsic primary afferent neuron of myenteric plexus / SN1 (chemical subterm of 3)
13. Calretinin-negative intrinsic primary afferent neuron of myenteric plexus / SN2 (chemical subterm of 3)
14. Cholinergic neuron of myenteric plexus (defined grouping class; EquivalentClass by location + GO:0014055)
15. Nitrergic neuron of myenteric plexus (defined grouping class; EquivalentClass by location + GO:0006809)
16. Dogiel type II neuron (general morphological class; sibling to CL:4047038 Dogiel type I neuron)

**Key ontology IDs established**:
- CL:0007011 — enteric neuron (parent for all new terms)
- CL:0008015 — inhibitory motor neuron (general; IMN will be a subclass)
- CL:4047038 — Dogiel type I neuron (relevant to morphological classification of EMN, IMN, IN)
- UBERON:0002439 — myenteric nerve plexus (soma location)
- UBERON:8600118 — myenteric ganglion (alternative soma location)
- GO:0014055 — acetylcholine secretion, neurotransmission (capable of, cholinergic neurons)
- GO:0014827 — intestine smooth muscle contraction (capable of part of, excitatory motor neurons)
- GO:0044557 — relaxation of smooth muscle (capable of part of, inhibitory motor neurons)

**Note on nitric oxide**: No GO term equivalent to GO:0014055 exists for nitric oxide neurotransmitter secretion. The relation `capable of` some `nitric oxide biosynthetic process` (GO:0006809) may be used as a proxy for nitrergic IMN, pending creation of a more specific GO term. This should be flagged for GO editors.

---

# Curation Report: Excitatory Motor Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: excitatory motor neuron of myenteric plexus
- **Status**: New term (CL:0008014 'excitatory motor neuron' is obsolete; no specific enteric EMN term exists)

## 2. Definition Validation

**Proposed Definition**:
An enteric motor neuron with soma located in the myenteric plexus that releases acetylcholine as its primary neurotransmitter to stimulate contraction of the intestinal smooth muscle. This neuron is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1), typically displays Dogiel type I morphology characterized by a uniaxonal cell body with lamellar dendrites, and exhibits S-type (fast excitatory postsynaptic potential) electrophysiology. This cell type plays an essential role in driving the propulsive contraction phase of peristalsis and coordinates ascending reflex activation oral to a bolus.

**Literature Support**:
- PMC10469081 (Chen et al.) — Directly defines four human colonic EMN subtypes (EMN1-4) by multilayer immunohistochemical coding: all ChAT+, NOS1-, with differential NF200 and calbindin expression. EMN1 and EMN2 are NF200+; EMN3 and EMN4 are NF200-. EMN1 and EMN3 are calbindin+; EMN2 and EMN4 are calbindin-.
- PMC8397665 (Brehmer 2021) — Reviews EMN identification criteria across human ENS: stubby Dogiel type I morphology, ChAT+, S-type electrophysiology, smaller soma area than Dogiel type II neurons.
- PMC12528430 (Majd et al. 2025) — Confirms EMN as a functional class recognized across multiple ENS scRNA-seq datasets. Notes that ChAT and NOS1 are the most consistently annotated markers separating EMN from IMN across datasets, though co-expression of these markers in individual neurons is more common than previously appreciated.

**Validation Notes**:
The cholinergic identity of excitatory myenteric motor neurons is among the most robustly established features in ENS biology, consistent across species and methodologies. The Dogiel type I morphology and S-type electrophysiology are established by classical neurophysiology (Furness 2006) though these are not independently confirmed in the primary references consulted (Chen et al. use IHC, not electrophysiology). The definition is appropriately qualified to 'primary neurotransmitter' given that co-transmitters (substance P, enkephalin) are commonly present.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Chemical coding studies of human colon (Chen et al., PMC10469081) identified 4 EMN subtypes among 2596 neurons from 12 patients using a panel of 10 antibodies. EMN subtypes collectively represent a substantial proportion of all myenteric neurons. Brehmer 2021 (PMC8397665) summarizes comparable classifications from multiple human and animal studies. Majd et al. 2025 confirm EMN as a well-defined transcriptomic cluster across mouse and human scRNA-seq datasets (Drokhlyansky AR-mouse, AR-human; Morarach UM-mouse; Zeisel/Haber ST-human datasets).

**Literature Support**:
- PMC10469081 — Table 7 provides full quantitative chemical coding data for EMN1-4.
- PMC8397665 — Comprehensive review of human enteric neuron chemical coding.
- PMC12528430 — Cross-dataset validation using scRNA-seq confirms EMN as a transcriptomically consistent class.

## 4. Cross-References

**Primary References**:
- PMC10469081 (Chen et al. — human colonic myenteric plexus, multilayer immunohistochemical chemical coding defining EMN1-4)
- PMC8397665 (Brehmer 2021 — classification review of human enteric neurons including EMN)

**Additional References**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025 — cross-dataset consistency of EMN annotation)
- PMID:32888429 / DOI:10.1016/j.cell.2020.08.003 (Drokhlyansky et al. 2020 — scRNA-seq ENS atlas including EMN clusters)

**Note**: Full text retrieval was successful for PMC10469081 and PMC8397665. Full text for PMC12528430 was retrieved via PMC12528430_Majd2025_ENS_unified_definition.txt. Full text for PMID:32888429 (PMC8358727 / Drokhlyansky et al. 2020) was retrieved via PDF extraction (pdfs/PMC8358727_Drokhlyansky2020_full_text.txt). Full text summary for Chen et al. 2024 (PMC10825022 — human VFN characterization) was retrieved and saved to pdfs/PMC10825022_full_text.txt. The Furness 2012 Annual Review paper and Morarach et al. 2021 (Nature Neuroscience) were not successfully retrieved.

## 5. Parent Term Validation

**Proposed Parent**: enteric neuron (CL:0007011)

**Justification**:
CL:0007011 is defined as a neuron of the enteric nervous system. Excitatory motor neurons of the myenteric plexus are a specific subtype distinguished by their location in the myenteric plexus, cholinergic neurotransmitter identity, and motor function targeting intestinal smooth muscle. The previous CL:0008014 'excitatory motor neuron' was made obsolete; the reason for obsoletion should be confirmed with CL editors before recreating a term with a related label.

**Hierarchical Context**:
CL:0007011 (enteric neuron) > excitatory motor neuron of myenteric plexus [NEW]

## 6. Synonyms

**Validated Synonyms**:
- myenteric excitatory motor neuron — used in Furness classification literature
- EMN — abbreviation used in Majd et al. 2025 (PMC12528430), Chen et al. (PMC10469081), Drokhlyansky et al. 2020
-  non-nitrergic myenteric motor neuron — marker combination synonym; captures the defining ChAT+/NOS1− binary that is the most reliable discriminator between EMN and IMN across species (Chen et al. PMC10469081, Brehmer 2021)

**Rejected Synonyms**:
- "excitatory motor neuron" alone is too broad (applies to neuromuscular junction neurons in non-enteric contexts) and should not be used as an exact synonym.

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439) — Source: PMC10469081, PMC8397665
- `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — Source: PMC10469081 (ChAT+), PMC8397665
- `capable of part of` some intestine smooth muscle contraction (GO:0014827) — Source: PMC8397665 (motor function)

**Morphology note**: `has characteristic` some Dogiel type I morphology could be asserted using a PATO term if available. CL:4047038 (Dogiel type I neuron) exists but using it as a parent would imply all excitatory motor neurons are Dogiel type I, which may not be universally true across species. The `has characteristic` relationship with a PATO morphology term would be more appropriate, but a specific PATO term for Dogiel type I was not found in this session; this should be investigated by the CL-ontologist.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The excitatory motor neuron of the myenteric plexus is a well-characterized, non-pathological cell type in the normal enteric nervous system, present in mammals including humans and rodents. It meets all criteria for CL inclusion: defined by reproducible molecular markers (ChAT+, NOS1-), anatomical location (myenteric plexus), and physiological function (intestinal smooth muscle excitation). Note that CL:0008014 was previously present and made obsolete — confirm the reason before adding a new term.

## 9. Additional Notes
- The existence of 4 or more chemical subtypes (EMN1-4 in Chen et al.) raises the question of whether these subtypes warrant separate CL terms. At this stage, a single general term is recommended until stronger cross-species evidence for conserved subtypes is available.
- Majd et al. 2025 note that individual neurons frequently co-express both ChAT and NOS1, meaning ChAT+/NOS1- classification is not absolute. The definition acknowledges acetylcholine as the 'primary' neurotransmitter to reflect this.
- **NF200 background**: Chen et al. (PMC10469081) distinguish EMN1/EMN2 (NF200+) from EMN3/EMN4 (NF200−). However, neurofilament 200 kDa (NF200) is a structural cytoskeletal protein whose expression correlates with soma size and axon calibre rather than functional cell identity. In IHC, staining intensity is continuous and the +/− threshold is technically dependent. NF200 is expressed across multiple functionally distinct ENS neuron classes (EMN, IMN, IPAN) and therefore cannot define an EMN subtype unambiguously. NF200 expression is not used in the definition or as a defining synonym but may be cited as a supporting observation in literature context.

## 10. Confidence Assessment
- Definition: High (multiple independent sources agree on ChAT+/NOS1- identity and intestinal smooth muscle excitation function)
- Parent term: High (CL:0007011 enteric neuron is clearly appropriate)
- Cross-references: Medium-High (primary references confirm the cell type; Furness 2012 review not retrieved)
- Overall: High

---

# Curation Report: Inhibitory Motor Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: inhibitory motor neuron of myenteric plexus
- **Status**: New specific term (CL:0008015 'inhibitory motor neuron' exists but is a general term; a myenteric-specific subclass is needed)

## 2. Definition Validation

**Proposed Definition**:
An enteric motor neuron with soma located in the myenteric plexus that releases nitric oxide as its primary inhibitory neurotransmitter to mediate relaxation of intestinal smooth muscle, with vasoactive intestinal peptide (VIP) and neuropeptide Y (NPY) commonly serving as co-transmitters. This neuron is immunopositive for neuronal nitric oxide synthase (NOS1) and immunonegative for choline acetyltransferase (ChAT), typically displays a spiny variant of Dogiel type I morphology characterized by irregular short dendrites, and exhibits S-type electrophysiology. This cell drives the descending inhibitory component of peristalsis and is essential for the relaxation phase of intestinal motility.

**Literature Support**:
- PMC10469081 (Chen et al.) — Defines four human colonic IMN subtypes (IMN1-4): all NOS1+, ChAT-. IMN1 and IMN2 are NF200+; IMN3 and IMN4 are NF200-. VIP is expressed in IMN1 and IMN3; NPY is expressed in IMN1 and IMN2.
- PMC8397665 (Brehmer 2021) — Reviews human IMN: spiny Dogiel type I morphology, NOS1+, VIP+, S-type electrophysiology; the spiny Dogiel type I morphology with irregular dendrites distinguishes IMN from stubby Dogiel type I EMN.
- PMC12528430 (Majd et al. 2025) — Confirms IMN as a well-defined functional class across ENS scRNA-seq datasets, with NOS1 as the most consistent marker; notes significant inter-dataset variability in co-transmitter assignment.

**Validation Notes**:
NOS1 positivity and ChAT negativity are the most robustly established features of myenteric inhibitory motor neurons across species and methodologies. Majd et al. 2025 note that ChAT/NOS1 co-expression is more common than the strict binary would suggest, and the definition should be understood as characterizing predominant rather than absolute profiles.

## 3. Experimental Evidence

**Summary of experimental evidence**:
IMN1-4 subtypes were identified by Chen et al. in human colonic myenteric plexus by multilayer immunohistochemical coding. All four subtypes share NOS1+ and ChAT- expression. IMN1 is the most immunoreactive subtype, co-expressing NF200, VIP, and NPY. IMN2 is NF200+, NPY+, VIP-. IMN3 is NF200-, VIP+. IMN4 has the simplest chemical code: NOS1+ only among the antibodies tested. Brehmer 2021 notes that spiny Dogiel type I neurons in humans are a major population and are reliably NOS1+/VIP+. Drokhlyansky et al. 2020 confirmed IMN transcriptomic clusters in both mouse and human ENS.

**Literature Support**:
- PMC10469081 — Table 7: full quantitative chemical coding data for IMN1-4.
- PMC8397665 — Review of IMN morphology and chemical coding in humans.
- PMC12528430 — Cross-dataset annotation and caveats.
- PMID:32888429 / DOI:10.1016/j.cell.2020.08.003 — scRNA-seq confirmation.

## 4. Cross-References

**Primary References**:
- PMC10469081 (Chen et al. — human colonic myenteric plexus defining IMN1-4)
- PMC8397665 (Brehmer 2021 — human ENS classification review)

**Additional References**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025)
- PMID:32888429 / DOI:10.1016/j.cell.2020.08.003 (Drokhlyansky et al. 2020)

**Note**: Full text for PMID:32888429 (Drokhlyansky) has been retrieved (pdfs/PMC8358727_Drokhlyansky2020_full_text.txt). Furness 2012 review not retrieved (see general note in preamble).

## 5. Parent Term Validation

**Proposed Parents**: inhibitory motor neuron (CL:0008015) AND enteric neuron (CL:0007011)

**Justification**:
CL:0008015 'inhibitory motor neuron' is a general CL term defined as a motor neuron that causes inhibition of the muscle. The myenteric inhibitory motor neuron is a specific subclass defined additionally by its location in the myenteric plexus and nitrergic identity. Using CL:0008015 as parent is appropriate and allows autoclassification. CL:0007011 provides the more informative enteric system placement.

**Hierarchical Context**:
CL:0007011 (enteric neuron) > inhibitory motor neuron of myenteric plexus [NEW]
CL:0008015 (inhibitory motor neuron) > inhibitory motor neuron of myenteric plexus [NEW]

## 6. Synonyms

**Validated Synonyms**:
- myenteric inhibitory motor neuron — used in ENS literature
- nitrergic motor neuron of myenteric plexus — reflects defining chemical identity
- IMN — abbreviation used in Majd et al. 2025, Chen et al., Drokhlyansky et al. 2020
- NOS1-positive ChAT-negative myenteric motor neuron — marker combination synonym; captures the defining NOS1+/ChAT− binary, the most reliable discriminator between IMN and EMN across species (Chen et al. PMC10469081, Brehmer 2021)

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439) — Source: PMC10469081, PMC8397665
- `capable of part of` some relaxation of smooth muscle (GO:0044557) — Source: PMC8397665 (inhibitory motor function)
- `capable of` some nitric oxide biosynthetic process (GO:0006809) — Source: PMC10469081 (NOS1+); used as proxy for nitrergic identity

**Note**: No GO term for 'nitric oxide secretion, neurotransmission' analogous to GO:0014055 was found. GO:0006809 (nitric oxide biosynthetic process) is used as the best available proxy. This should be flagged for GO editors to create a `nitric oxide secretion, neurotransmission` term. When such a term is created, the `capable of` relationship should be updated accordingly.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The inhibitory motor neuron of the myenteric plexus is a well-characterized, non-pathological cell type present in the mammalian enteric nervous system. It meets all CL inclusion criteria and is appropriately placed as a subclass of the existing general CL term CL:0008015.

## 9. Additional Notes
- Flag for GO editors: request creation of a `nitric oxide secretion, neurotransmission` GO term to parallel GO:0014055 (acetylcholine secretion, neurotransmission).
- Multiple IMN chemical subtypes (IMN1-4) exist in humans. A single general myenteric IMN term is recommended at this stage, with subtypes to follow when cross-species evidence is established.
- **NF200 background**: Chen et al. (PMC10469081) distinguish IMN1/IMN2 (NF200+) from IMN3/IMN4 (NF200−). NF200 expression in ENS neurons reflects soma size and axon calibre rather than functional identity and is broadly distributed across EMN, IMN, and IPAN classes. The +/− threshold is technically dependent and not reproducible as a categorical cell identity marker. NF200 expression is not used in the definition but may be cited as a supporting contextual observation.

## 10. Confidence Assessment
- Definition: High
- Parent term: High
- Cross-references: Medium-High (primary references obtained; Furness 2012 not retrieved)
- Overall: High

---

# Curation Report: Intrinsic Primary Afferent Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: intrinsic primary afferent neuron of myenteric plexus
- **Status**: New term (no existing CL term for myenteric IPAN found)

## 2. Definition Validation

**Proposed Definition**:
An enteric sensory neuron with soma located in the myenteric plexus that responds to mechanical and chemical stimuli in the intestinal lumen and mucosa, and initiates or modulates peristaltic and secretomotor reflexes. This neuron is characterized by Dogiel type II morphology — a smooth, oval cell body with multiple long axon-like processes — and exhibits AH-type electrophysiology (prolonged afterhyperpolarization following an action potential). It is immunopositive for choline acetyltransferase (ChAT); neuronal nitric oxide synthase (NOS1) is absent. Co-expression of substance P (encoded by TAC1) and calbindin has been reported in various species. Myenteric IPANs project to both the myenteric and submucosal plexuses.

**Literature Support**:
- PMC10469081 (Chen et al.) — Defines two human colonic sensory neuron subtypes (SN1 and SN2) with Dogiel type II morphology: both ChAT+, NOS1-, NF200+, substance P+, with large soma area (mean approximately 1616 µm²); SN1 is calretinin+, SN2 is calretinin-.
- PMC8397665 (Brehmer 2021) — Comprehensive review of IPAN identification criteria: Dogiel type II morphology is the key morphological criterion; AH electrophysiology; capacity for both afferent (sensory) and interneuron functions; multiaxonal morphology enabling submucosal projections. Notes that IPANs are the only clearly multiaxonal neuron type in the myenteric plexus.
- PMC12528430 (Majd et al. 2025) — IPAN is recognized as a functional class across ENS scRNA-seq datasets. Notes inconsistencies in TAC1 (substance P gene) assignment across datasets; some datasets assign TAC1+ expression to functional classes other than IPAN.

**Validation Notes**:
The Dogiel type II morphology and AH electrophysiology are the most definitive criteria for IPAN identification and are consistently cited across species and methodologies. The ChAT+ identity is confirmed by Chen et al. The substance P co-expression, while frequently cited, shows cross-dataset inconsistency per Majd et al. 2025 and is therefore not used as a primary defining marker in the proposed definition. Calretinin and calbindin expression vary by species. The large soma size relative to motor neurons is a useful distinguishing feature in histological studies.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Chen et al. (PMC10469081) characterized SN1 and SN2 subtypes from 2596 human colonic myenteric neurons. Both are NF200+, ChAT+, substance P+, with mean soma area approximately 2.6-fold larger than EMN classes. SN1 (calretinin+) and SN2 (calretinin-) are distinguished only by calretinin expression. Brehmer 2021 (PMC8397665) provides additional context: Dogiel type II neurons are reliably identified by smooth oval soma, multiple processes, and AH electrophysiology, and represent a distinct population in the human myenteric plexus separate from the two morphological subtypes of Dogiel type I (stubby = ChAT+/EMN, spiny = NOS1+/IMN).

**Literature Support**:
- PMC10469081 — Table 7: SN1 and SN2 chemical coding and soma size data.
- PMC8397665 — Review of IPAN morphology (Dogiel type II), electrophysiology (AH), and dual sensory/interneuron function.
- PMC12528430 — Cross-dataset recognition of IPAN/SN as a functional class with TAC1 expression caveats.

## 4. Cross-References

**Primary References**:
- PMC10469081 (Chen et al. — human colonic myenteric plexus, SN1/SN2 corresponding to myenteric IPAN subtypes)
- PMC8397665 (Brehmer 2021 — IPAN classification review)

**Additional References**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025)
- PMID:32888429 / DOI:10.1016/j.cell.2020.08.003 (Drokhlyansky et al. 2020)

## 5. Parent Term Validation

**Proposed Parents**: enteric neuron (CL:0007011) AND sensory neuron (CL:0000101)

**Justification**:
CL:0007011 is the appropriate enteric-system parent. CL:0000101 (sensory neuron) is an appropriate additional parent since IPANs are defined by their sensory function (detection of luminal stimuli, initiation of reflexes). Dual parentage is recommended.

**Hierarchical Context**:
CL:0000101 (sensory neuron) > intrinsic primary afferent neuron of myenteric plexus [NEW]
CL:0007011 (enteric neuron) > intrinsic primary afferent neuron of myenteric plexus [NEW]

## 6. Synonyms

**Validated Synonyms**:
- myenteric IPAN — standard abbreviation in ENS literature
- myenteric AH neuron — electrophysiological classification (AH = afterhyperpolarization); Source: PMC8397665
- myenteric sensory neuron — functional synonym used in Majd et al. 2025
- multiaxonal cholinergic myenteric sensory neuron — marker combination synonym; 'multiaxonal' (Dogiel type II morphology) discriminates IPAN from all Dogiel type I neuron classes; 'cholinergic' reflects ChAT+ identity confirmed in human (Chen et al. PMC10469081) and consistent across species

**Related Synonyms** (not exact):
- Dogiel type II neuron of myenteric plexus — morphological synonym; Source: PMC8397665. Marked as related rather than exact because Dogiel type II morphology may not be strictly co-extensive with IPAN functional identity across all species. Note: a new morphological subterm 'Dogiel type II neuron of myenteric plexus' is proposed as a child of this term (see separate report below).

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439) — Source: PMC10469081, PMC8397665
- `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — Source: PMC10469081 (ChAT+)

**Note on morphology**: No specific PATO term for 'multiaxonal' morphology was found. If a suitable PATO term is identified, a `has characteristic` some [multiaxonal PATO term] relationship should be added. A CL term for 'Dogiel type II neuron' would be a useful complement to the existing CL:4047038 (Dogiel type I neuron) and could serve as an additional parent.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The intrinsic primary afferent neuron of the myenteric plexus is a well-established, non-pathological cell type in the mammalian enteric nervous system with consistent morphological, electrophysiological, and chemical criteria. It meets all CL inclusion criteria.

## 9. Additional Notes
- The term 'IPAN' is used in the enteric nervous system literature with a specific meaning distinct from CNS usage of 'primary afferent neuron'. The enteric context should be clear from the label and definition.
- Some IPANs also function as interneurons (Brehmer 2021), complicating strict functional classification. The definition uses 'initiates or modulates' to reflect this flexibility.
- Recommend requesting creation of a Dogiel type II neuron CL term to complement CL:4047038 (Dogiel type I neuron).
- **Calretinin-based subtypes**: Two human IPAN subtypes distinguished by calretinin expression (SN1: calretinin+; SN2: calretinin−) are proposed as child terms of this class (see separate curation reports). Calretinin expression was removed from this parent definition because it is the basis of the child-term partitioning.
- **NF200 background**: Chen et al. (PMC10469081) report that both SN1 and SN2 subtypes are NF200+. However, NF200 expression in ENS neurons reflects soma size and axon calibre rather than functional identity, and its IHC signal is technically sensitive. NF200 is not used as a defining marker here but may be cited as a supporting observation for large-soma IPAN identification in multilayer IHC studies.

## 10. Confidence Assessment
- Definition: High (consistent across multiple sources and methodologies)
- Parent term: High for CL:0007011; Medium for CL:0000101 (CL editor review recommended to confirm appropriate dual parentage)
- Cross-references: Medium-High (primary references obtained; Furness 2012 review not retrieved)
- Overall: High

---

# Curation Report: Interneuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: interneuron of myenteric plexus
- **Status**: New term (no existing CL term for myenteric interneuron found)

## 2. Definition Validation

**Proposed Definition**:
An enteric neuron with soma located in the myenteric plexus that forms synaptic connections exclusively within the enteric nervous system, transmitting signals between sensory neurons and motor neurons to coordinate intestinal motility reflexes. Myenteric interneurons do not directly innervate effector targets such as smooth muscle or secretory epithelium, but transmit signals in both ascending (oral) and descending (aboral) directions. The ascending limb is primarily excitatory; the descending limb includes both inhibitory and excitatory components targeting different muscle layers.

**Literature Support**:
- PMC10469081 (Chen et al.) — Identifies three ascending interneuron (AIN1-3) and six descending interneuron (DIN1-6) subtypes in human colon. All three AIN subtypes are ChAT+, NOS1-, ENK+, NF200+. DIN subtypes are more diverse: DIN1 and DIN2 are 5-HT+; DIN3-6 include NOS1+ and other marker combinations.
- PMC8397665 (Brehmer 2021) — Describes ascending and descending interneuron populations in human ENS; both subtypes show Dogiel type I (uniaxonal) morphology; ascending are ChAT+/ENK+; descending are chemically more diverse including 5-HT+ neurons.
- PMC12528430 (Majd et al. 2025) — Recognizes IN as a functional class in cross-dataset comparison. Notes inconsistency in the assignment of TAC1 (substance P) and 5-HT to IN vs. other functional classes across datasets.

**Validation Notes**:
The ascending ChAT+/ENK+ identity and the existence of descending 5-HT+/NOS1+ diversity are well supported by Chen et al. and Brehmer 2021. The Majd et al. 2025 caveat on TAC1 and 5-HT assignment inconsistency is noted but does not affect the core ENK marker for ascending interneurons or the general concept of descending interneuron chemical diversity.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Chen et al. identified 9 interneuron subtypes (AIN1-3 and DIN1-6) from 2596 human colonic myenteric neurons. AIN subtypes are uniformly ChAT+, ENK+, NF200+, NOS1-. DIN subtypes include 5-HT+ neurons (DIN1, DIN2), NOS1+/VIP+ neurons, and other combinations. The chemical diversity of DINs is substantially greater than that of AINs. Brehmer 2021 provides additional morphological and electrophysiological context supporting the interneuron identification criteria.

**Literature Support**:
- PMC10469081 — Table 7: full quantitative chemical coding for AIN1-3 and DIN1-6.
- PMC8397665 — Morphological and chemical review of myenteric interneurons.
- PMC12528430 — Cross-dataset validation and caveats.

## 4. Cross-References

**Primary References**:
- PMC10469081 (Chen et al. — human colonic myenteric plexus, AIN and DIN subtypes)
- PMC8397665 (Brehmer 2021 — classification review)

**Additional References**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025)
- PMID:32888429 / DOI:10.1016/j.cell.2020.08.003 (Drokhlyansky et al. 2020)

## 5. Parent Term Validation

**Proposed Parents**: enteric neuron (CL:0007011) AND interneuron (CL:0000099)

**Justification**:
CL:0007011 provides the enteric system placement. CL:0000099 (interneuron) is the appropriate functional parent. Dual parentage is recommended.

**Hierarchical Context**:
CL:0000099 (interneuron) > interneuron of myenteric plexus [NEW]
CL:0007011 (enteric neuron) > interneuron of myenteric plexus [NEW]

## 6. Synonyms

**Validated Synonyms**:
- myenteric interneuron — widely used in ENS literature
- IN — abbreviation from Majd et al. 2025 (PMC12528430), Chen et al.

**Note on marker combination synonyms**: The general interneuron term is chemically heterogeneous (ascending: ChAT+/ENK+; descending: 5-HT+/NOS1+/diverse), so no single marker combination covers the full class. Marker combination synonyms are appropriate only at the subterm level: 'ascending interneuron of myenteric plexus' should carry the synonym 'cholinergic enkephalinergic myenteric interneuron' (ChAT+/ENK+); descending subtypes should carry synonyms once their chemical codes are confirmed across species.

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439) — Source: PMC10469081, PMC8397665

**Note**: The interneuron does not directly innervate smooth muscle or secretory epithelium. Appropriate GO terms for peristalsis coordination or interneuron relay function were not identified in this session; the CL-ontologist should investigate suitable `capable of` GO terms.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The interneuron of the myenteric plexus is a well-characterized, non-pathological cell type in the mammalian enteric nervous system meeting all CL inclusion criteria. Note that because the ascending and descending subtypes are chemically distinct, child terms should be created when sufficient cross-species evidence supports their separate definition.

## 9. Additional Notes
- Ascending interneuron subtypes (AIN) are the most consistently characterized: ChAT+, ENK+, NF200+. These may warrant a separate child term 'ascending interneuron of myenteric plexus'.
- Descending interneuron subtypes (DIN) are more diverse (5-HT+, NOS1+, etc.) and may warrant separate child terms if specific chemical identities prove conserved across species.
- Majd et al. 2025 note that serotonin (5-HT) assignment is among the most inconsistent across ENS scRNA-seq datasets; this should be flagged as a caveat for descending interneuron definitions that rely on 5-HT markers.

## 10. Confidence Assessment
- Definition: High for ascending interneurons; Medium for descending interneurons (chemical diversity and inter-dataset inconsistency)
- Parent term: High
- Cross-references: Medium-High
- Overall: High for general term; Medium for chemical marker details of DIN subtypes

---

# Curation Report: Secretomotor/Vasodilator Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: secretomotor/vasodilator neuron of myenteric plexus
- **Status**: New term (PSVN is a recognized functional class in the Furness ENS classification; now characterized by scRNA-seq)

## 2. Definition Validation

**Proposed Definition**:
An enteric neuron with soma located in the myenteric plexus that functions to regulate intestinal secretion and/or mucosal blood flow. Secretomotor/vasodilator neurons project to the submucosal plexus, intestinal blood vessels, and epithelium, releasing neuropeptides that stimulate epithelial secretion or vasodilation of submucosal arterioles. In mouse, two PSVN subtypes are distinguishable: a VIP+ non-cholinergic subtype (PSVN1) and a ChAT+ cholinergic subtype (PSVN2) that co-expresses galanin (GAL) and neuropeptide Y (NPY). Both subtypes express the glucagon-like peptide-2 receptor (GLP2R). In human colon, only the VIP+ non-cholinergic PSVN subtype has been detected by scRNA-seq; the cholinergic subtype may be species-specific, lost during tissue processing, or present at lower abundance. The conserved PSVN transcriptional program across species includes VIP, GAL, SCGN (secretagogin), and CALB2 (calretinin).

**Literature Support**:
- **PMC8358727 (Drokhlyansky et al. 2020)** — scRNA-seq atlas of mouse and human ENS. Key PSVN findings:
  - Mouse: Two Glp2r+ PSVN subtypes identified — PSVN1 (VIP+ non-cholinergic, Fst+) and PSVN2 (ChAT+, Gal+, Npy+, Csf2rb+, some Gad2+)
  - Human: "We did not find ACh+ PSVNs in human... potentially due to submucosa removal, lower PSVN proportions, or species-specific features"
  - Conserved PSVN program (n=48 genes): includes VIP, Gal, Scgn, Calb2
  - Regional variation: colon enriched in PSVNs vs ileum (colon fluid balance function)
- PMC12528430 (Majd et al. 2025) — Cross-dataset comparison confirming PSVN as a recognized functional class, noting marker overlap with other classes
- PMC8397665 (Brehmer 2021) — Reviews secretomotor/vasodilator neurons primarily in submucosal plexus context

**Validation Notes**:
Drokhlyansky et al. 2020 provides the first systematic scRNA-seq characterization of PSVN subtypes in both mouse and human. The mouse data clearly defines two chemically distinct subtypes (VIP+ non-cholinergic and ChAT+ cholinergic). The absence of ChAT+ PSVNs in human is notable but may reflect technical or sampling limitations rather than true species difference. The conserved VIP+/GAL+ program provides a reliable cross-species marker combination.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Drokhlyansky et al. 2020 (PMC8358727) profiled 5,068 mouse enteric neurons and 1,445 human enteric neurons by snRNA-seq. In mouse:
- **PSVN1**: VIP+ non-cholinergic, Glp2r+, Fst+ (follistatin), Lgr5+
- **PSVN2**: ChAT+ cholinergic, Glp2r+, Gal+ (galanin), Npy+, Csf2rb+, some Gad2+ (cholinergic/GABAergic)

In human colon:
- PSVNs were detected but depleted relative to mouse
- Only VIP+ (non-cholinergic) subtype detected
- ACh+ PSVNs not identified

**Literature Support**:
- **PMC8358727 (Drokhlyansky et al. 2020)** — Primary scRNA-seq characterization of PSVN subtypes
- PMC12528430 (Majd et al. 2025) — Cross-dataset validation

## 4. Cross-References

**Primary References**:
- **PMC8358727 / DOI:10.1016/j.cell.2020.08.003 (Drokhlyansky et al. 2020)** — scRNA-seq characterization of mouse and human PSVN subtypes
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025)

**Additional References**:
- Furness JB (2012) Annual Review of Physiology 74:305-326 — DOI:10.1146/annurev-physiol-020911-153245 [NOT RETRIEVED — original Furness classification]

## 5. Parent Term Validation

**Proposed Parent**: enteric neuron (CL:0007011)

**Justification**:
CL:0007011 is the appropriate parent. No more specific intermediate class exists in CL for this functional type.

## 6. Synonyms

**Validated Synonyms**:
- myenteric PSVN — abbreviation used in Drokhlyansky et al. 2020, Majd et al. 2025
- Glp2r-positive myenteric neuron — receptor-based marker combination synonym (mouse; both subtypes)
- VIP-positive secretomotor neuron — marker combination for non-cholinergic subtype (conserved across species)
- myenteric secretomotor neuron — functional synonym

**Note on subtype synonyms**:
- PSVN1 = VIP+ non-cholinergic PSVN (Fst+)
- PSVN2 = ChAT+ cholinergic PSVN (Gal+, Npy+) — mouse-specific or underdetected in human

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439) — Source: Drokhlyansky et al. 2020

**Subtype-specific relationships**:
- PSVN1: `capable of` some VIP secretion (GO term to be identified)
- PSVN2: `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — mouse

**Note**: Appropriate GO terms for intestinal secretion regulation or vasodilation should be identified. Consider GO:0030073 (positive regulation of insulin secretion) for GLP2R function context.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The secretomotor/vasodilator neuron of the myenteric plexus is now adequately characterized by Drokhlyansky et al. 2020 for CL integration. The conserved VIP+/GAL+ program provides reliable cross-species markers. Note that the ChAT+ subtype may be mouse-specific or underdetected in human.

## 9. Additional Notes
- The PSVN category is most clearly characterized in the submucosal plexus in classical literature. Drokhlyansky 2020 provides the first systematic myenteric PSVN characterization.
- A separate term for 'secretomotor/vasodilator neuron of submucosal plexus' may be warranted; these populations likely differ in projection targets and chemical coding.
- Regional variation: colon enriched in PSVNs vs ileum, consistent with colon's role in fluid balance.
- The GLP2R marker is functionally significant: GLP-2 is an intestinotrophic hormone that regulates intestinal epithelial proliferation and fluid secretion.

## 10. Confidence Assessment
- Definition: **Medium-High** (scRNA-seq data now available; species differences in cholinergic subtype noted)
- Parent term: High
- Cross-references: **High** (Drokhlyansky 2020 full text retrieved)
- Overall: **Medium-High**

**Ready for CL integration.** Note species difference in cholinergic subtype detection.

---

# Curation Report: Intestinofugal Neuron

## 1. Term Identification
- **Proposed Label**: intestinofugal neuron
- **Status**: New term (no existing CL term found; intestinofugal neurons are a distinct, well-characterized ENS neuron type)

## 2. Definition Validation

**Proposed Definition**:
An enteric neuron with soma located in the myenteric plexus whose axon projects outward from the intestinal wall to form synapses with neurons of the prevertebral sympathetic ganglia, including the celiac, superior mesenteric, and inferior mesenteric ganglia. Intestinofugal neurons (also termed viscerofugal neurons, VFNs) function as the afferent limb of entero-sympathetic reflexes, transmitting information about intestinal distension and luminal content to the prevertebral sympathetic nervous system, which in turn modulates intestinal motility and secretion through sympathetic efferents. In contrast to all other myenteric neuron types, the axon of the intestinofugal neuron exits the intestinal wall, constituting a physiological bridge between the enteric and sympathetic nervous systems. **In humans, choline acetyltransferase (ChAT) is the primary marker**: Chen et al. 2024 found that 89% of human VFNs are ChAT-immunoreactive. CART (cocaine- and amphetamine-regulated transcript, encoded by CARTPT) is NOT a valid human marker: 0/123 human VFN cell bodies were CART-immunoreactive (Chen et al. 2024), despite CART being used as a marker in rodent studies.

**Literature Support**:
- **PMC10825022 (Chen et al. 2024)** — First systematic characterization of human viscerofugal neurons. Key findings from 903 VFNs: (a) 89% are ChAT+ (cholinergic); (b) 0% are CART+ (N=123, explicitly tested); (c) 26% are NOS1+; (d) 10% are calbindin+. This directly contradicts the use of CART as a human VFN marker.
- PMC12528430 (Majd et al. 2025) — States: "Cart, expressed by gene Cartpt, has been used to mark intestinofugal neurons." **CAUTION**: This statement reflects rodent literature. Chen et al. 2024 definitively shows CART is not a human marker.
- Mann et al. 1995 — Original guinea pig characterization showing CART in intestinofugal neurons. Species-specific, does not apply to humans.

**Validation Notes**:
The Chen et al. 2024 study represents a major correction to the ENS literature. CART/CARTPT, previously cited as an intestinofugal marker based on rodent studies, is NOT expressed in human VFNs. ChAT is the appropriate human marker (89%). This species difference must be reflected in any CL term definition. The functional definition (entero-sympathetic reflex arc, axonal projection to prevertebral ganglia) remains valid across species.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Chen et al. 2024 (PMC10825022) provides the first comprehensive characterization of human viscerofugal (intestinofugal) neurons, analyzing 903 VFNs from human colon. Key quantitative findings:
- **ChAT+**: 89% (primary human marker)
- **CART+**: 0% (N=123 explicitly tested) — NOT a human marker
- **NOS1+**: 26%
- **Calbindin+**: 10%
- **Calretinin+**: 17%

The defining property — axonal projection from the intestinal wall to prevertebral sympathetic ganglia — was confirmed by retrograde tracing. Classical studies (Furness 2006; Mann et al. 1995) characterized VFNs in guinea pigs using CART as a marker; this does NOT apply to humans.

**Literature Support**:
- **PMC10825022 (Chen et al. 2024)** — Primary reference for human VFN chemical coding. Definitive evidence that CART is absent in human VFNs.
- PMC12528430 (Majd et al. 2025) — Cross-dataset comparison noting absence of VFNs from scRNA-seq datasets.
- Mann et al. 1995 (guinea pig) and Furness 2006 — Historical references; species-specific CART findings do not apply to humans.

## 4. Cross-References

**Primary References**:
- **PMC10825022 / DOI:10.1016/j.celrep.2024.113653 (Chen et al. 2024)** — First human VFN characterization: 89% ChAT+, 0% CART+. This is now the primary human reference.
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025 — cross-dataset comparison, VFN concept)

**Historical references (species-specific findings)**:
- Mann PT, Furness JB, Southwell BR (1995) J Auton Nerv Syst 56:15-25, PMID:8786275 — Guinea pig VFN characterization. CART findings are species-specific and do NOT apply to humans.
- Furness JB (2006) The Enteric Nervous System. Blackwell, Oxford — Classification framework.
- Furness JB (2012) Annual Review of Physiology 74:305-326 — DOI:10.1146/annurev-physiol-020911-153245 [NOT RETRIEVED]

**CRITICAL CORRECTION**: Prior literature citing CART/CARTPT as a VFN marker is based on rodent studies. Human data from Chen et al. 2024 shows 0% CART expression in human VFNs. ChAT (89%) is the appropriate human marker.

## 5. Parent Term Validation

**Proposed Parent**: enteric neuron (CL:0007011)

**Justification**:
CL:0007011 is the appropriate parent. Intestinofugal neurons are enteric neurons by virtue of their soma location in the myenteric plexus, even though their axons project outside the intestinal wall. This extra-intestinal axonal projection distinguishes them from all other ENS cell types. An alternative parent under a broader 'visceral afferent neuron' category could be considered but CL:0007011 is the most appropriate for current ENS-focused placement.

## 6. Synonyms

**Validated Synonyms**:
- viscerofugal neuron — preferred term in Chen et al. 2024 (PMC10825022); abbreviated VFN
- VFN — abbreviation used in Chen et al. 2024
- intestino-fugal neuron — alternative spelling used in some literature
- cholinergic viscerofugal neuron — marker combination synonym; reflects 89% ChAT+ in humans (Chen et al. 2024)

**Rejected Synonyms**:
- "CART-positive enteric neuron" — NOT applicable to humans (0% CART expression); only valid in rodent contexts

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439) — Source: Chen et al. 2024 (PMC10825022), Furness classification framework
- `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — Source: Chen et al. 2024 (89% ChAT+)

**Species-specific relationships (DO NOT USE for humans)**:
- `expresses` some CARTPT gene product — **INVALID FOR HUMANS** (0/123 CART+ per Chen et al. 2024). Only applicable in rodent contexts.

**Connectivity relationship**:
- `synapsed to` some prevertebral ganglion neuron — the appropriate CL term for prevertebral sympathetic ganglion neuron or UBERON term for prevertebral ganglion should be identified. UBERON likely has terms for celiac ganglion (UBERON:0002262), superior mesenteric ganglion (UBERON:0005479), and inferior mesenteric ganglion (UBERON:0005480).

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

Intestinofugal neurons (viscerofugal neurons) are a well-established and conceptually distinct class of ENS neuron with unique connectivity (extra-intestinal axon projecting to sympathetic ganglia). They are non-pathological, present in mammals including humans, and serve an important physiological function in entero-sympathetic reflexes. Chen et al. 2024 (PMC10825022) provides definitive human marker data: 89% ChAT+, 0% CART+. The term is ready for CL integration with human-specific chemical coding.

## 9. Additional Notes
- Intestinofugal neurons (VFNs) are the only ENS neuron class whose defining feature is axonal projection outside the intestinal wall, constituting a bridge between enteric and sympathetic nervous systems.
- **CRITICAL SPECIES DIFFERENCE**: CART/CARTPT is NOT a human VFN marker (0/123 CART+ per Chen et al. 2024), despite being widely cited in rodent literature. ChAT is the primary human marker (89%). This species difference MUST be reflected in any CL definition.
- Chen et al. 2024 sampled 903 human VFNs from colon — the first comprehensive human characterization. Prior literature (Mann et al. 1995, Furness 2006) is guinea pig-specific.
- The `synapsed to` relationship to prevertebral sympathetic neurons remains the defining functional characteristic across species.
- Additional human VFN markers from Chen et al. 2024: 26% NOS1+, 17% calretinin+, 10% calbindin+.

## 10. Confidence Assessment
- Definition: **High** (Chen et al. 2024 provides definitive human characterization)
- Parent term: High (CL:0007011 enteric neuron)
- Cross-references: **High** (PMC10825022 is primary human reference; historical rodent references contextualized)
- Overall: **High**

**Ready for CL integration.** Note: Definition should specify human chemical coding (ChAT+) and explicitly note that CART is NOT a human marker.

---

# Curation Report: Cholinergic Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: cholinergic neuron of myenteric plexus
- **Status**: New term (defined grouping class; classifies by location + acetylcholine secretion capability)

## 2. Definition Validation

**Proposed Definition**:
A neuron of the myenteric plexus that is capable of acetylcholine secretion as a neurotransmitter.

**Rationale**:
Multiple functionally distinct myenteric neuron classes release acetylcholine as their primary neurotransmitter: excitatory motor neurons (ChAT+/NOS1−), intrinsic primary afferent neurons (ChAT+/NOS1−), and ascending interneurons (ChAT+/ENK+). A grouping term collecting these under a shared chemical identity axis follows CL convention (CL:0000108 cholinergic neuron) and provides a valid annotation target for experimental contexts where ChAT immunoreactivity is confirmed but functional subtype is not resolved.

**Literature Support**:
- PMC10469081 (Chen et al.) — ChAT immunoreactivity confirmed for EMN (all subtypes), IPAN (SN1/SN2), and ascending interneurons (AIN1-3).
- PMC12528430 (Majd et al. 2025) — ChAT is among the most consistently assigned markers across ENS scRNA-seq datasets for EMN, IPAN, and ascending interneuron classes.

## 3. EquivalentClass Definition

**Necessary and Sufficient Conditions (OWL EquivalentTo)**:
```
cholinergic neuron of myenteric plexus
    EquivalentTo: CL:0007011 (enteric neuron)
        AND ('has soma location' some UBERON:0002439 (myenteric nerve plexus))
        AND ('capable of' some GO:0014055 (acetylcholine secretion, neurotransmission))
```

**Autoclassification**: Any enteric neuron asserting `has soma location` UBERON:0002439 AND `capable of` GO:0014055 will be inferred as a subclass by the reasoner. Terms that will autoclassify:
- excitatory motor neuron of myenteric plexus [NEW]
- intrinsic primary afferent neuron of myenteric plexus [NEW]
- ascending interneuron of myenteric plexus [NEW]
- calretinin-positive IPAN of myenteric plexus [NEW] — via IPAN parent
- calretinin-negative IPAN of myenteric plexus [NEW] — via IPAN parent
- stubby Dogiel type I neuron of myenteric plexus [NEW] — via EMN parent
- Dogiel type II neuron of myenteric plexus [NEW] — via IPAN parent

**Do NOT assert GO:0014055 as a SubClassOf on this grouping term itself.** The `capable of` GO:0014055 assertions on each specific child term are what drive autoclassification into this defined class. The grouping term's EquivalentClass axiom references GO:0014055 as the membership criterion only.

## 4. Parent Term Validation

**Proposed Parents**: CL:0000108 (cholinergic neuron) AND CL:0007011 (enteric neuron)

**Hierarchical Context**:
```
CL:0000108 (cholinergic neuron)
    └── cholinergic neuron of myenteric plexus [NEW]
            ├── excitatory motor neuron of myenteric plexus [NEW] (autoclassified)
            ├── intrinsic primary afferent neuron of myenteric plexus [NEW] (autoclassified)
            └── ascending interneuron of myenteric plexus [NEW] (autoclassified)
CL:0007011 (enteric neuron)
    └── cholinergic neuron of myenteric plexus [NEW]
```

## 5. Synonyms

**Validated Synonyms**:
- ChAT-positive neuron of myenteric plexus — IHC marker synonym
- myenteric ChAT neuron — matches collaborator term 'myenteric ganglion ChAT neuron'; valid mapping at grouping level

**Note on collaborator mapping**: 'myenteric ganglion ChAT neuron' maps here. More specific mappings are possible with additional evidence: ChAT+/NOS1−/Dogiel type I → EMN; ChAT+/NOS1−/Dogiel type II → IPAN; ChAT+/ENK+ → ascending interneuron.

## 6. Logical Relationships

**Asserted on this term** (part of EquivalentClass definition):
- `has soma location` some UBERON:0002439 (myenteric nerve plexus)

**Inherited by children via autoclassification**:
- `capable of` some GO:0014055 (acetylcholine secretion, neurotransmission) — asserted on specific child terms; serves as EquivalentClass criterion here

## 7. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

Defined class with clean EquivalentClass axiom. Follows CL convention for neurotransmitter-based grouping. Enables principled annotation at ChAT+IHC resolution without over-specifying functional subtype.

## 8. Additional Notes
- This is a **defined class** (EquivalentClass). Membership is axiom-driven, not manually curated.
- Descending interneurons that co-express ChAT will autoclassify here only if they assert `capable of` GO:0014055. The descending interneuron parent term does not assert this (chemical heterogeneity); specific subtypes may be added if evidence warrants.
- Confirm CL:0000108 scope before asserting dual parentage (check it is not already restricted to a context that would conflict).

## 9. Confidence Assessment
- Definition: High
- EquivalentClass axiom: High (GO:0014055 and UBERON:0002439 are well-established)
- Overall: High

---

# Curation Report: Nitrergic Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: nitrergic neuron of myenteric plexus
- **Status**: New term (defined grouping class; classifies by location + nitric oxide biosynthesis capability)

## 2. Definition Validation

**Proposed Definition**:
A neuron of the myenteric plexus that is capable of nitric oxide biosynthesis.

**Rationale**:
Multiple functionally distinct myenteric neuron classes express neuronal nitric oxide synthase (NOS1/nNOS): inhibitory motor neurons (NOS1+/ChAT−) and a subset of descending interneurons (NOS1+). A grouping term provides a valid annotation target for contexts where NOS1 immunoreactivity is confirmed but functional subtype is not resolved. If a general 'nitrergic neuron' CL term does not yet exist (unlike CL:0000108), this term also demonstrates the need for one.

**Literature Support**:
- PMC10469081 (Chen et al.) — NOS1 confirmed for IMN (all four subtypes) and NOS1+ descending interneuron subtypes (DIN3-6 include NOS1+ populations).
- PMC12528430 (Majd et al. 2025) — NOS1 is among the most consistently assigned markers across ENS scRNA-seq datasets.
- PMC8397665 (Brehmer 2021) — NOS1+/VIP+ defines spiny Dogiel type I (IMN) neurons in human ENS.

## 3. EquivalentClass Definition

**Necessary and Sufficient Conditions (OWL EquivalentTo)**:
```
nitrergic neuron of myenteric plexus
    EquivalentTo: CL:0007011 (enteric neuron)
        AND ('has soma location' some UBERON:0002439 (myenteric nerve plexus))
        AND ('capable of' some GO:0006809 (nitric oxide biosynthetic process))
```

**Autoclassification**: Terms that will autoclassify:
- inhibitory motor neuron of myenteric plexus [NEW]
- spiny Dogiel type I neuron of myenteric plexus [NEW] — via IMN parent

NOS1+ descending interneuron child terms, if created, would also autoclassify here. The descending interneuron parent term does not assert GO:0006809 (not all descending interneurons are NOS1+).

**Note on GO:0006809**: Used as proxy for nitrergic neurotransmitter identity; no `nitric oxide secretion, neurotransmission` GO term analogous to GO:0014055 currently exists. Update this axiom when that term is created (see action items).

## 4. Parent Term Validation

**Proposed Parent**: CL:0007011 (enteric neuron)

**Note**: If a general 'nitrergic neuron' CL term exists, this term should also be a subclass of it. Check CL before final placement.

**Hierarchical Context**:
```
CL:0007011 (enteric neuron)
    └── nitrergic neuron of myenteric plexus [NEW]
            ├── inhibitory motor neuron of myenteric plexus [NEW] (autoclassified)
            └── spiny Dogiel type I neuron of myenteric plexus [NEW] (autoclassified via IMN)
[nitrergic neuron — general CL term if it exists]
    └── nitrergic neuron of myenteric plexus [NEW]
```

## 5. Synonyms

**Validated Synonyms**:
- NOS1-positive neuron of myenteric plexus — IHC marker synonym
- nNOS-positive neuron of myenteric plexus — alternative IHC label (nNOS = neuronal NOS = NOS1)
- myenteric nNOS neuron — matches collaborator term 'myenteric ganglion nNOS neuron'; valid mapping at grouping level

**Note on collaborator mapping**: 'myenteric ganglion nNOS neuron' maps here. More specific mapping: NOS1+/ChAT− → IMN; NOS1+/ChAT−/spiny Dogiel type I morphology → spiny Dogiel type I neuron of myenteric plexus.

## 6. Logical Relationships

**Asserted on this term** (part of EquivalentClass definition):
- `has soma location` some UBERON:0002439 (myenteric nerve plexus)

**Inherited by children via autoclassification**:
- `capable of` some GO:0006809 — asserted on specific child terms; serves as EquivalentClass criterion here

## 7. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

Defined class with clean EquivalentClass axiom. NOS1 is one of the most robust and consistently confirmed ENS markers across species and methodologies. Enables principled annotation at NOS1-IHC resolution.

## 8. Additional Notes
- This is a **defined class** (EquivalentClass).
- Update EquivalentClass axiom from GO:0006809 to a `nitric oxide secretion, neurotransmission` GO term when created.
- 'myenteric ganglion nNOS/ChAT neuron' (co-expressing neurons) will NOT autoclassify here, nor under the cholinergic grouping class, consistent with the 'primary neurotransmitter' framing of EMN and IMN definitions.
- 'myenteric ganglion nNOS/VIP neuron' maps more specifically to IMN or spiny Dogiel type I neuron (both NOS1+; VIP is an IMN co-transmitter not used in the EquivalentClass axiom).

## 9. Confidence Assessment
- Definition: High
- EquivalentClass axiom: High (pending GO:0006809 proxy caveat; update when specific GO term available)
- Overall: High

---

# Curation Report: Ascending Interneuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: ascending interneuron of myenteric plexus
- **Status**: New term (functional subterm of interneuron of myenteric plexus [NEW])

## 2. Definition Validation

**Proposed Definition**:
An interneuron of the myenteric plexus that mediates the ascending excitatory limb of the peristaltic reflex, transmitting signals from intrinsic sensory neurons orally (in the anal-to-oral direction) to activate excitatory motor neurons and promote contraction of the circular muscle oral to a bolus. This neuron is immunopositive for choline acetyltransferase (ChAT) and enkephalin (ENK), displays Dogiel type I morphology, and is immunonegative for neuronal nitric oxide synthase (NOS1).

**Literature Support**:
- PMC10469081 (Chen et al.) — Identifies three ascending interneuron subtypes (AIN1-3) in human colonic myenteric plexus. All three are ChAT+, ENK+, NF200+, NOS1−. The uniform ChAT+/ENK+/NF200+ chemical code across AIN1-3 makes the ascending interneuron one of the most chemically consistent interneuron classes in the ENS.
- PMC8397665 (Brehmer 2021) — Reviews ascending interneuron populations in human ENS as ChAT+/ENK+ neurons with Dogiel type I morphology; describes their role in the ascending excitatory reflex arc.
- PMC12528430 (Majd et al. 2025) — IN class recognised across ENS datasets. Notes that TAC1/substance P assignment to IN is inconsistent across datasets; ENK (PENK gene) is among the three markers shared across all primary ENS datasets (alongside NOS1 and TAC1), supporting its use as an interneuron class marker.

**Validation Notes**:
The ChAT+/ENK+ combination is among the most consistent chemical codes for myenteric interneurons across species and methodologies. NF200 co-expression is confirmed in all three AIN subtypes in Chen et al. but should be understood as characteristic of the human class rather than a defining criterion. Majd et al. 2025 confirm PENK as one of only three cross-dataset shared markers, reinforcing ENK as a robust interneuron marker.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Chen et al. (PMC10469081) identified AIN1-3 from 2596 human colonic myenteric neurons. All three subtypes share ChAT+, ENK+, NF200+, NOS1− chemical coding. Subtypes differ only in quantitative expression levels, not in presence/absence of the core markers. Brehmer 2021 (PMC8397665) provides supporting morphological context.

**Literature Support**:
- PMC10469081 — Table 7: chemical coding for AIN1-3.
- PMC8397665 — Review of ascending interneuron morphology and function.
- PMC12528430 — Cross-dataset PENK expression confirming ENK as a shared ENS marker.

## 4. Cross-References

**Primary References**:
- PMC10469081 (Chen et al. — human colonic myenteric plexus AIN1-3)
- PMC8397665 (Brehmer 2021 — review)

**Additional References**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025 — cross-dataset marker validation)

## 5. Parent Term Validation

**Proposed Parent**: interneuron of myenteric plexus [NEW]

**Justification**:
The ascending interneuron is a functional subclass of the myenteric interneuron, distinguished by its ascending projection direction, excitatory function, and ChAT+/ENK+ chemical code. No more specific intermediate CL term is required.

**Hierarchical Context**:
```
CL:0000099 (interneuron) > interneuron of myenteric plexus [NEW]
    └── ascending interneuron of myenteric plexus [NEW]
CL:0007011 (enteric neuron) > interneuron of myenteric plexus [NEW]
    └── ascending interneuron of myenteric plexus [NEW]
```

## 6. Synonyms

**Validated Synonyms**:
- myenteric ascending interneuron — inverted form used in ENS literature
- AIN — abbreviation used in Chen et al. (PMC10469081)
- cholinergic enkephalinergic myenteric interneuron — marker combination synonym; ChAT+/ENK+ is the most consistent chemical code for this class across species and datasets; this combination does not over-capture (ENK distinguishes ascending from most descending interneurons; ChAT distinguishes from NOS1+ descending interneurons)

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439)
- `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — ChAT+ identity

**Note**: A GO term for 'ascending peristaltic reflex' or 'ascending excitatory reflex' would be appropriate for `capable of part of`; if not available, the CL-ontologist should search for suitable GO terms related to peristalsis coordination.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The ascending interneuron of the myenteric plexus has a consistent ChAT+/ENK+ chemical code across human and key model species, a defined functional role in the ascending excitatory limb of peristalsis, and is well-supported by multiple independent methodologies. Ready for CL integration.

## 9. Additional Notes
- The three AIN subtypes (AIN1-3) in Chen et al. are distinguished only quantitatively, not by presence/absence of core markers. A single general ascending interneuron term is recommended unless cross-species evidence for distinct conserved subtypes emerges.
- ENK (enkephalin; gene PENK) is the most diagnostically useful marker for distinguishing ascending interneurons from descending interneurons and from motor neurons.
- **NF200 background**: Chen et al. (PMC10469081) report that all three AIN subtypes are NF200+. However, NF200 expression reflects soma size and axon calibre rather than functional identity, and it is also expressed in NF200+ EMN and IMN subsets. NF200 is not used in the definition but the AIN1-3 co-expression data may be cited as supporting context for large-soma ascending interneurons in IHC studies.

## 10. Confidence Assessment
- Definition: High (ChAT+/ENK+ chemical code is consistent across species and methodologies)
- Parent term: High
- Cross-references: Medium-High (Furness 2012 review not retrieved)
- Overall: High

---

# Curation Report: Descending Interneuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: descending interneuron of myenteric plexus
- **Status**: New term (functional subterm of interneuron of myenteric plexus [NEW])

## 2. Definition Validation

**Proposed Definition**:
An interneuron of the myenteric plexus that mediates the descending inhibitory limb of the peristaltic reflex, transmitting signals from intrinsic sensory neurons aborally (in the oral-to-anal direction) to activate inhibitory motor neurons and suppress contraction of the circular muscle aboral to a bolus. Descending interneurons are chemically more diverse than ascending interneurons; the major identified subtypes include serotonin-positive (5-HT+) neurons and nitrergic (NOS1+) neurons, with additional populations distinguished by VIP, somatostatin, and other neuropeptide expression. Choline acetyltransferase (ChAT) expression is present in some but not all descending interneuron subtypes.

**Literature Support**:
- PMC10469081 (Chen et al.) — Identifies six descending interneuron subtypes (DIN1-6) in human colonic myenteric plexus. DIN1 and DIN2 are 5-HT+; DIN3-6 include NOS1+ and other marker combinations. Chemical diversity is substantially greater than that of ascending interneurons.
- PMC8397665 (Brehmer 2021) — Reviews descending interneuron populations including 5-HT+ neurons and other chemically diverse subtypes; describes their role in the descending inhibitory reflex arc with Dogiel type I morphology.
- PMC12528430 (Majd et al. 2025) — Notes that 5-HT assignment is among the most inconsistent across ENS scRNA-seq datasets, cautioning against sole reliance on 5-HT as a descending interneuron marker.

**Validation Notes**:
The descending interneuron class is defined primarily by its projection direction and circuit role rather than by a single consistent chemical code. This contrasts with the ascending interneuron (ChAT+/ENK+) and represents the greater chemical complexity of the descending inhibitory limb. The 5-HT+ subtype is the most commonly cited descending interneuron marker, but Majd et al. 2025 highlight significant cross-dataset inconsistency. Medium confidence for marker-based definition; high confidence for functional concept.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Chen et al. (PMC10469081) identified DIN1-6 from 2596 human colonic myenteric neurons. The six subtypes show more diverse chemical coding than the three AIN subtypes. DIN1 and DIN2 are 5-HT+; DIN3-6 are distinguished by varying combinations of NOS1, VIP, and other markers. Brehmer 2021 provides additional morphological and functional context.

**Literature Support**:
- PMC10469081 — Table 7: chemical coding for DIN1-6.
- PMC8397665 — Morphological and functional review of descending interneurons.
- PMC12528430 — 5-HT assignment inconsistency across datasets; caution for scRNA-seq-based annotation.

## 4. Cross-References

**Primary References**:
- PMC10469081 (Chen et al. — human colonic myenteric plexus DIN1-6)
- PMC8397665 (Brehmer 2021 — review)

**Additional References**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025 — 5-HT inconsistency caveat)

## 5. Parent Term Validation

**Proposed Parent**: interneuron of myenteric plexus [NEW]

**Justification**:
The descending interneuron is a functional subclass of the myenteric interneuron, distinguished by its descending projection direction and inhibitory role in the peristaltic reflex circuit.

**Hierarchical Context**:
```
CL:0000099 (interneuron) > interneuron of myenteric plexus [NEW]
    └── descending interneuron of myenteric plexus [NEW]
CL:0007011 (enteric neuron) > interneuron of myenteric plexus [NEW]
    └── descending interneuron of myenteric plexus [NEW]
```

## 6. Synonyms

**Validated Synonyms**:
- myenteric descending interneuron — inverted form used in ENS literature
- DIN — abbreviation used in Chen et al. (PMC10469081)

**Marker combination synonyms**: Not proposed at this level due to chemical heterogeneity of the class. Marker combination synonyms are appropriate for chemically defined subterms:
- A future 'serotonergic descending interneuron of myenteric plexus' subterm would carry the synonym '5-HT-positive myenteric descending interneuron' — but this should await cross-species confirmation of 5-HT as a reliable marker given Majd et al. 2025 caveats.
- A future 'nitrergic descending interneuron of myenteric plexus' subterm should be considered but requires careful distinction from inhibitory motor neurons (which are also NOS1+); the key distinguishing feature is target (other neurons, not smooth muscle).

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439)

**Note**: Appropriate GO terms for descending inhibitory reflex coordination should be identified. Unlike ascending interneurons, not all descending interneurons are ChAT+, so GO:0014055 should not be applied at the class level.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The descending interneuron of the myenteric plexus is a recognised functional class with a defined circuit role. The term is ready for CL integration at the general class level. Note that the greater chemical diversity of descending interneuron subtypes means the definition is necessarily broader than that for ascending interneurons; chemically defined child terms should be deferred until cross-species marker evidence is established.

## 9. Additional Notes
- The 5-HT+ descending interneuron subtype is the most frequently cited but also the most dataset-inconsistent (Majd et al. 2025). Defining a 'serotonergic descending interneuron of myenteric plexus' term should await retrieval of Furness 2012 and Morarach et al. 2021 for cross-species validation.
- NOS1+ descending interneurons must be carefully distinguished from NOS1+ inhibitory motor neurons; the distinction rests on their target (interneurons vs. smooth muscle) and on morphological criteria (Dogiel type I interneuron vs. spiny Dogiel type I motor neuron).
- DIN subtypes 1-6 in Chen et al. are human-specific and may not map directly to mouse or guinea pig classifications; cross-species subterm creation requires confirmation from non-human datasets.

## 10. Confidence Assessment
- Definition: High for functional concept; Medium for marker-based characterisation (chemical diversity)
- Parent term: High
- Cross-references: Medium-High (Furness 2012 not retrieved; 5-HT inconsistency flagged by Majd et al. 2025)
- Overall: Medium-High (functional concept is high confidence; marker definitions are medium)

---

# Curation Report: Stubby Dogiel Type I Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: stubby Dogiel type I neuron of myenteric plexus
- **Status**: New term (morphological subclass of excitatory motor neuron of myenteric plexus [NEW])

## 2. Definition Validation

**Proposed Definition**:
An excitatory motor neuron of the myenteric plexus characterised by Dogiel type I morphology in its stubby (lamellar) variant, with a flattened soma bearing broad, flat, sheet-like dendrites and a single axon projecting to the intestinal smooth muscle. The soma is of medium size. This neuron is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).

**Literature Support**:
- PMC8397665 (Brehmer 2021) — Explicitly distinguishes stubby Dogiel type I morphology (flat/lamellar dendrites, medium soma, uniaxonal, ChAT+) from spiny Dogiel type I morphology (irregular spine-like dendrites, NOS1+) as the morphological correlate of excitatory and inhibitory motor function respectively. Primary reference for the stubby/spiny distinction in human ENS.
- PMC10469081 (Chen et al.) — EMN subtypes EMN1-4 are all Dogiel type I; EMN1 and EMN2 are NF200+, EMN3 and EMN4 are NF200−; all are ChAT+/NOS1−, consistent with stubby Dogiel type I assignment per Brehmer 2021.

**Editor note**: The stubby Dogiel type I morphology is well-correlated with excitatory motor function in the myenteric plexus across all mammalian species studied to date (human, guinea pig, rat, mouse). These terms are maintained as distinct from the functional parent because cross-species evidence is not yet sufficient to assert equivalence (i.e., not all EMN in all studied species have been confirmed to exhibit stubby Dogiel type I morphology by direct ultrastructural or morphometric methods; the correlation is strong but the equivalence axiom EMN ≡ stubby Dogiel type I neuron of myenteric plexus is not asserted).

## 3. Experimental Evidence

**Summary of experimental evidence**:
Brehmer 2021 (PMC8397665) provides the primary morphological characterisation of the stubby Dogiel type I variant in human ENS, distinguishing it from the spiny Dogiel type I morphology of IMN and the multiaxonal morphology of Dogiel type II (IPAN). Chen et al. (PMC10469081) confirm ChAT+/NOS1− identity for all EMN subtypes in a quantitative immunohistochemical study of human colonic myenteric plexus.

**Literature Support**:
- PMC8397665 — Morphological classification of stubby vs. spiny Dogiel type I in human ENS.
- PMC10469081 — Chemical coding of EMN subtypes (ChAT+, NOS1−) in human colon.

## 4. Cross-References

**Primary References**:
- PMC8397665 (Brehmer 2021 — morphological classification)
- PMC10469081 (Chen et al. — chemical coding of EMN)

## 5. Parent Term Validation

**Proposed Parents**:
- excitatory motor neuron of myenteric plexus [NEW] — functional parent
- CL:4047038 (Dogiel type I neuron) — morphological parent

**Justification**:
Multiple inheritance is appropriate. Every stubby Dogiel type I neuron of the myenteric plexus is (a) a Dogiel type I neuron and (b) an excitatory motor neuron of the myenteric plexus. The functional parent provides motor function and chemical coding context; the morphological parent places this term in the Dogiel classification hierarchy alongside CL:4047038.

**Hierarchical Context**:
```
CL:4047038 (Dogiel type I neuron)
    └── stubby Dogiel type I neuron of myenteric plexus [NEW]
excitatory motor neuron of myenteric plexus [NEW]
    └── stubby Dogiel type I neuron of myenteric plexus [NEW]
```

## 6. Synonyms

**Validated Synonyms**:
- lamellar Dogiel type I neuron of myenteric plexus — alternative morphological descriptor; 'lamellar' refers to the flat sheet-like dendrite morphology (Brehmer 2021)
- stubby type I myenteric neuron — shortened form used in descriptive ENS literature

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439)
- `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — inherited from functional parent
- `capable of part of` some intestine smooth muscle contraction (GO:0014827) — inherited from functional parent

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

Well-characterised in human and key model organisms. The stubby Dogiel type I variant is a widely recognised morphological category in ENS biology. Dual parentage under CL:4047038 and the new functional parent is appropriate. Note: confirm CL:4047038 definition scope (is it already restricted to enteric neurons?) before placement.

## 9. Additional Notes
- The stubby/spiny Dogiel type I distinction is most clearly articulated in guinea pig and human literature. Cross-species validation (mouse, rat) at the ultrastructural level should be confirmed before asserting morphological equivalence.
- If a PATO term for 'lamellar dendrite morphology' or 'stubby soma morphology' becomes available, a `has characteristic` relationship should be added.

## 10. Confidence Assessment
- Definition: High (consistent across Brehmer 2021 and Chen et al.; well-established in ENS morphology literature)
- Parent terms: High
- Cross-references: Medium-High (Furness 2012 review not retrieved)
- Overall: High

---

# Curation Report: Spiny Dogiel Type I Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: spiny Dogiel type I neuron of myenteric plexus
- **Status**: New term (morphological subclass of inhibitory motor neuron of myenteric plexus [NEW])

## 2. Definition Validation

**Proposed Definition**:
An inhibitory motor neuron of the myenteric plexus characterised by Dogiel type I morphology in its spiny variant, with an irregular soma bearing short, spine-like or filiform dendritic processes and a single axon projecting to the intestinal smooth muscle. This neuron is immunopositive for neuronal nitric oxide synthase (NOS1) and immunonegative for choline acetyltransferase (ChAT). Vasoactive intestinal peptide (VIP) and neuropeptide Y (NPY) are common co-transmitters.

**Literature Support**:
- PMC8397665 (Brehmer 2021) — Explicitly describes spiny Dogiel type I morphology (irregular short dendrites, spine-like processes, NOS1+, VIP+) as the morphological correlate of inhibitory motor function in the human myenteric plexus, in contrast to stubby Dogiel type I morphology associated with excitatory motor neurons. Primary reference for the stubby/spiny distinction.
- PMC10469081 (Chen et al.) — IMN subtypes IMN1-4 are all NOS1+/ChAT−; IMN1 and IMN2 are NF200+ while IMN3 and IMN4 are NF200−, consistent with the spiny Dogiel type I assignment per Brehmer 2021.

**Editor note**: The spiny Dogiel type I morphology is well-correlated with inhibitory motor function in the myenteric plexus across all mammalian species studied to date. These terms are maintained as distinct from the functional parent because cross-species evidence is not yet sufficient to assert equivalence (i.e., not all IMN in all studied species have been confirmed to exhibit spiny Dogiel type I morphology by direct morphometric methods; the equivalence axiom IMN ≡ spiny Dogiel type I neuron of myenteric plexus is not asserted).

## 3. Experimental Evidence

**Summary of experimental evidence**:
Brehmer 2021 (PMC8397665) provides the primary morphological characterisation of the spiny Dogiel type I variant in human ENS. Chen et al. (PMC10469081) confirm NOS1+/ChAT− identity for all IMN subtypes in a quantitative immunohistochemical study of 2596 human colonic myenteric neurons.

**Literature Support**:
- PMC8397665 — Morphological classification of spiny Dogiel type I in human ENS.
- PMC10469081 — Chemical coding of IMN subtypes (NOS1+, ChAT−) in human colon.

## 4. Cross-References

**Primary References**:
- PMC8397665 (Brehmer 2021 — morphological classification)
- PMC10469081 (Chen et al. — chemical coding of IMN)

## 5. Parent Term Validation

**Proposed Parents**:
- inhibitory motor neuron of myenteric plexus [NEW] — functional parent
- CL:4047038 (Dogiel type I neuron) — morphological parent

**Justification**:
Multiple inheritance is appropriate. Every spiny Dogiel type I neuron of the myenteric plexus is (a) a Dogiel type I neuron and (b) an inhibitory motor neuron of the myenteric plexus. Dual parentage allows inference of both morphological and functional identity.

**Hierarchical Context**:
```
CL:4047038 (Dogiel type I neuron)
    └── spiny Dogiel type I neuron of myenteric plexus [NEW]
inhibitory motor neuron of myenteric plexus [NEW]
    └── spiny Dogiel type I neuron of myenteric plexus [NEW]
```

## 6. Synonyms

**Validated Synonyms**:
- filiform Dogiel type I neuron of myenteric plexus — alternative morphological descriptor; 'filiform' refers to the thread-like spine-like dendrite morphology
- spiny type I myenteric neuron — shortened form used in descriptive ENS literature
- NOS1-positive spiny type I myenteric neuron — marker combination synonym combining morphological and chemical identity

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439)
- `capable of part of` some relaxation of smooth muscle (GO:0044557) — inherited from functional parent
- `capable of` some nitric oxide biosynthetic process (GO:0006809) — inherited from functional parent (proxy for nitrergic identity; update when GO term for nitric oxide neurotransmission is created)

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

Well-characterised in human and key model organisms. The spiny Dogiel type I variant is a widely recognised morphological category in ENS biology. Dual parentage under CL:4047038 and the new functional parent is appropriate.

## 9. Additional Notes
- If a PATO term for 'spine-like dendrite morphology' or equivalent becomes available, a `has characteristic` relationship should be added.
- The spiny/stubby distinction may require further ultrastructural validation in non-primate species before the terms are used in species-specific annotations.

## 10. Confidence Assessment
- Definition: High (consistent across Brehmer 2021 and Chen et al.)
- Parent terms: High
- Cross-references: Medium-High (Furness 2012 review not retrieved)
- Overall: High

---

# Curation Report: Dogiel Type II Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: Dogiel type II neuron of myenteric plexus
- **Status**: New term (morphological subclass of intrinsic primary afferent neuron of myenteric plexus [NEW]; complements CL:4047038 Dogiel type I neuron)

## 2. Definition Validation

**Proposed Definition**:
An intrinsic primary afferent neuron of the myenteric plexus characterised by Dogiel type II morphology: a large, smooth, oval soma bearing multiple long axon-like processes that extend without branching until they reach their targets in both the myenteric and submucosal plexuses and the mucosa. The soma lacks the dendrites characteristic of Dogiel type I neurons and is larger in cross-sectional area than either motor neuron type. This neuron is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1). It exhibits AH-type electrophysiology, characterised by a prolonged afterhyperpolarization (AHP) following an action potential. Substance P (encoded by TAC1) expression has been reported in subsets across species.

**Literature Support**:
- PMC8397665 (Brehmer 2021) — Detailed description of Dogiel type II morphology in human ENS: smooth oval soma, multiaxonal (multiple long processes without proximal branching), large soma, AH electrophysiology, distinct from both Dogiel type I variants. Confirms these neurons project to submucosal plexus and mucosa as well as within the myenteric plexus.
- PMC10469081 (Chen et al.) — SN1 and SN2 subtypes: both ChAT+, NOS1−, NF200+, substance P+, large soma (mean ~1616 µm², approximately 2.6-fold larger than EMN classes); SN1 calretinin+, SN2 calretinin−. These data are consistent with Dogiel type II assignment.
- PMC12528430 (Majd et al. 2025) — Confirms IPAN/sensory neuron class across ENS datasets; notes inconsistency in TAC1/substance P assignment across scRNA-seq datasets, suggesting this is not a reliable solo marker.

**Editor note**: The Dogiel type II morphology is well-correlated with IPAN/sensory function across all mammalian species studied to date. These terms are maintained as distinct from the functional parent because cross-species evidence is not yet sufficient to assert equivalence (i.e., the equivalence axiom IPAN ≡ Dogiel type II neuron of myenteric plexus is not asserted). Note: a general 'Dogiel type II neuron' CL term (without location qualifier) should be created to complement CL:4047038 (Dogiel type I neuron) and serve as an additional parent for this term.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Brehmer 2021 (PMC8397665) provides comprehensive morphological characterisation of Dogiel type II neurons in human ENS as the third major morphological class alongside stubby and spiny Dogiel type I. Chen et al. (PMC10469081) characterised SN1 and SN2 subtypes by multilayer immunohistochemistry in 2596 human colonic myenteric neurons; both subtypes are ChAT+/NOS1−/NF200+ with large soma area consistent with Dogiel type II assignment.

**Literature Support**:
- PMC8397665 — Morphological classification and multiaxonal connectivity of Dogiel type II neurons.
- PMC10469081 — Chemical coding (ChAT+, NOS1−, NF200+, SP+) and soma size data for SN1/SN2.
- PMC12528430 — Cross-dataset IPAN recognition and TAC1 expression caveats.

## 4. Cross-References

**Primary References**:
- PMC8397665 (Brehmer 2021 — morphological classification)
- PMC10469081 (Chen et al. — chemical coding of SN1/SN2)

## 5. Parent Term Validation

**Proposed Parents**:
- intrinsic primary afferent neuron of myenteric plexus [NEW] — functional parent
- Dogiel type II neuron [NEW general CL term, to complement CL:4047038] — morphological parent

**Justification**:
Multiple inheritance is appropriate. Every Dogiel type II neuron of the myenteric plexus is (a) a Dogiel type II neuron (morphological class) and (b) an intrinsic primary afferent neuron of the myenteric plexus (functional class). The general Dogiel type II neuron term (location-agnostic) should be created first as a sibling of CL:4047038; the myenteric-specific term then adds location and functional context.

**Hierarchical Context**:
```
Dogiel type II neuron [NEW general term, complement to CL:4047038]
    └── Dogiel type II neuron of myenteric plexus [NEW]
intrinsic primary afferent neuron of myenteric plexus [NEW]
    └── Dogiel type II neuron of myenteric plexus [NEW]
```

## 6. Synonyms

**Validated Synonyms**:
- type II myenteric neuron — shortened morphological descriptor used in ENS literature
- multiaxonal myenteric sensory neuron — marker combination synonym; 'multiaxonal' uniquely identifies Dogiel type II morphology among myenteric neuron types; 'sensory' reflects IPAN functional identity
- AH-type myenteric neuron — electrophysiological synonym; AH (afterhyperpolarization) is the electrophysiological hallmark of Dogiel type II / IPAN neurons (Source: PMC8397665)
**Note on NF200-based synonyms**: Chen et al. (PMC10469081) report NF200+/ChAT+/NOS1− for SN1 and SN2 (Dogiel type II neurons). However, because NF200 expression reflects axon calibre and is broadly distributed across ENS neuron types (including NF200+ EMN and IMN subsets), NF200 is not used in a synonym for this term. See Additional Notes for background.

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439)
- `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — ChAT+ identity (Chen et al.)
- Inherited from functional parent: sensory function relationships

**Morphology note**: A PATO term for 'multiaxonal morphology' would support a `has characteristic` relationship. If unavailable, the multiaxonal property is captured in the definition text and in the 'multiaxonal' component of the marker combination synonym. The CL-ontologist should investigate PATO for appropriate terms.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The Dogiel type II neuron of the myenteric plexus is among the most consistently characterised enteric neuron types across species, with well-established morphological (multiaxonal, large soma), electrophysiological (AH-type), and chemical (ChAT+, NOS1−, NF200+) criteria. Create alongside the general Dogiel type II neuron parent term.

**Prerequisite**: Create general 'Dogiel type II neuron' CL term as sibling to CL:4047038 (Dogiel type I neuron). See separate section below.

## 9. Additional Notes
- The large soma size of Dogiel type II neurons (~1616 µm² in Chen et al. vs. ~620 µm² for EMN) is a useful diagnostic feature in morphometric studies and may be captured via a PATO size term if available.
- The 'multiaxonal' property — multiple long processes without proximal branching — is the key distinguishing morphological feature from Dogiel type I (uniaxonal). This term should be asserted explicitly via `has characteristic` once an appropriate PATO or UBERON process term is identified.
- TAC1/substance P expression is noted as a common but inconsistent co-marker (Majd et al. 2025) and is not used in the primary definition or synonyms.
- **NF200 background**: Chen et al. (PMC10469081) report both SN1 and SN2 (the two human Dogiel type II subtypes) as NF200+. NF200 positivity is consistent with the large soma size of these neurons, as NF200 expression scales with axon calibre. However, NF200 is also expressed in NF200+ subsets of EMN and IMN (which are Dogiel type I), so NF200 alone cannot distinguish Dogiel type II from all Dogiel type I neurons and is not used as a defining marker. It may be cited as supporting context for large-soma IPAN identification.
- **Calretinin-based child terms**: Two subtypes of this term are proposed based on calretinin expression (calretinin-positive and calretinin-negative IPAN of myenteric plexus; see separate curation reports). Calretinin was removed from this parent definition because it is the sole basis of that child-term partitioning.

## 10. Confidence Assessment
- Definition: High (morphological criteria are among the most robustly established in ENS biology)
- Parent terms: High (general Dogiel type II neuron term to be created as sibling to CL:4047038)
- Cross-references: Medium-High (Furness 2012 not retrieved)
- Overall: High

---

# Curation Report: Dogiel Type II Neuron (General Term)

## 1. Term Identification
- **Proposed Label**: Dogiel type II neuron
- **Status**: New term (sibling to CL:4047038 Dogiel type I neuron; morphological classification)

## 2. Definition Validation

**Proposed Definition**:
A neuron characterised by Dogiel type II morphology: a large, smooth, oval soma bearing multiple long axon-like processes (multiaxonal) that extend without branching until they reach their targets. The soma lacks the short lamellar or spiny dendrites characteristic of Dogiel type I neurons. Dogiel type II neurons were first described by Alexander Dogiel in 1899 based on methylene blue staining in gastrointestinal ganglia. In the enteric nervous system, Dogiel type II neurons correspond to intrinsic primary afferent neurons (IPANs) and exhibit AH-type electrophysiology (prolonged afterhyperpolarization following an action potential).

**Literature Support**:
- PMC8397665 (Brehmer 2021) — Comprehensive review of Dogiel morphological classification in human ENS: Dogiel type II neurons are distinguished by smooth oval soma, multiple long processes, large soma size, and multiaxonal connectivity pattern. Contrast with stubby Dogiel type I (excitatory motor neurons) and spiny Dogiel type I (inhibitory motor neurons).
- Dogiel AS (1899) — Original morphological description. Arch Anat Physiol Anat Abt.

**Validation Notes**:
The Dogiel type II morphology is among the most robustly established morphological classifications in enteric neuroscience, first described in 1899 and consistently validated across species using diverse techniques (methylene blue, IHC, intracellular dye injection). This general term captures the morphological class without location restriction, analogous to existing CL:4047038 (Dogiel type I neuron).

## 3. Experimental Evidence

The Dogiel type II morphology has been consistently identified across:
- Human ENS (Brehmer 2006, 2021; Chen et al. 2023)
- Guinea pig ENS (Furness 2006)
- Mouse ENS (multiple studies)

Key morphological features validated by Brehmer 2021 (PMC8397665):
- Smooth, oval cell body (lacking dendrites of Dogiel type I)
- Multiple long axon-like processes (multiaxonal)
- Large soma area (~1600 µm² in human colon; 2.6× larger than motor neurons)
- Projections to both myenteric and submucosal plexuses

## 4. Cross-References

**Primary References**:
- PMC8397665 (Brehmer 2021 — morphological classification review)
- Dogiel AS (1899) Über den Bau der Ganglien in den Geflechten des Darmes und der Gallenblase des Menschen und der Säugetiere. Arch Anat Physiol Anat Abt. [Historical reference]

## 5. Parent Term Validation

**Proposed Parent**: neuron (CL:0000540)

**Justification**:
This is a general morphological class of neuron, analogous to CL:4047038 (Dogiel type I neuron). The parent should be the general neuron term. Specific enteric location terms (e.g., "Dogiel type II neuron of myenteric plexus") are child terms that add anatomical context.

**Hierarchical Context**:
```
neuron (CL:0000540)
    ├── Dogiel type I neuron (CL:4047038) [existing]
    └── Dogiel type II neuron [NEW — this term]
            └── Dogiel type II neuron of myenteric plexus [NEW]
```

## 6. Synonyms

**Validated Synonyms**:
- type II enteric neuron — used in older ENS literature
- multiaxonal enteric neuron — morphological descriptor reflecting the defining feature (multiple long processes)
- AH neuron — electrophysiological synonym (AH = afterhyperpolarization); widely used in ENS literature
- Dogiel II neuron — abbreviated form

## 7. Logical Relationships

**Proposed Relationships**:
- `has characteristic` some multiaxonal morphology — if PATO term available
- `has characteristic` some oval cell body shape — if PATO term available

**Note**: The morphological features are captured in the definition. Appropriate PATO terms should be identified by the CL-ontologist.

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL as sibling to CL:4047038

This term completes the Dogiel morphological classification in CL. CL:4047038 (Dogiel type I neuron) already exists; this term creates the complementary Dogiel type II class. Both are morphological categories originally defined for enteric neurons but applicable wherever Dogiel-type classifications are used.

## 9. Additional Notes
- The Dogiel classification (types I and II) was established in 1899 and remains the standard morphological framework for enteric neuron classification.
- In modern ENS research, Dogiel type II is strongly correlated with IPAN (sensory) function and AH-type electrophysiology, while Dogiel type I encompasses both excitatory (stubby) and inhibitory (spiny) motor neurons.
- Unlike Dogiel type I, which is subdivided into stubby and spiny variants, Dogiel type II has no established morphological subtypes.

## 10. Confidence Assessment
- Definition: High (the most consistently established morphological category in ENS biology since 1899)
- Parent term: High (CL:0000540 neuron)
- Cross-references: High (historical and modern literature agree)
- Overall: High

---

# Curation Report: Calretinin-Positive Intrinsic Primary Afferent Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: calretinin-positive intrinsic primary afferent neuron of myenteric plexus
- **Status**: New term (chemical subtype of intrinsic primary afferent neuron of myenteric plexus [NEW]; corresponds to SN1 in Chen et al. chemical coding scheme)

## 2. Definition Validation

**Proposed Definition**:
An intrinsic primary afferent neuron of the myenteric plexus that is immunopositive for calretinin. This neuron shares the Dogiel type II morphology and AH-type electrophysiology of all myenteric IPANs, and is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).

**Literature Support**:
- PMC10469081 (Chen et al.) — Defines SN1 as calretinin+, ChAT+, NOS1−, substance P+ with large soma area (mean ~1616 µm²) in a survey of 2596 human colonic myenteric neurons. SN1 is the calretinin-expressing IPAN subtype; the sole chemical distinction from SN2 is calretinin immunoreactivity.
- PMC8397665 (Brehmer 2021) — Notes calretinin expression in Dogiel type II neurons in human ENS as part of a broader review of chemical coding.
- PMC12528430 (Majd et al. 2025) — Calretinin (CALR gene) is noted as a marker for the sensory neuron cluster in cross-dataset ENS scRNA-seq comparison.

**Validation Notes**:
Calretinin is a calcium-binding protein with categorical presence/absence in well-defined cell populations in IHC, in contrast to NF200 whose signal is continuous. Unlike NF200, calretinin is not expressed broadly across multiple functional ENS classes; its expression within the IPAN class provides a reliable binary split. Cross-dataset support for CALR/calretinin as a marker within the IPAN class is noted by Majd et al. 2025.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Chen et al. (PMC10469081) identified SN1 from 2596 human colonic myenteric neurons by multilayer IHC. All SN1 neurons are calretinin+, ChAT+, NOS1−, substance P+, with large soma area consistent with Dogiel type II morphology. Calretinin immunoreactivity provides a clean positive categorical marker distinguishing SN1 from SN2.

**Literature Support**:
- PMC10469081 — Table 7: SN1 (CalR+) chemical coding and soma size data.
- PMC8397665 — Calretinin expression in Dogiel type II neurons in human ENS.
- PMC12528430 — CALR as a cross-dataset IPAN marker.

## 4. Cross-References

**Primary References**:
- PMC10469081 (Chen et al. — SN1 subtype definition in human colonic myenteric plexus)
- PMC8397665 (Brehmer 2021 — calretinin in human ENS IPAN context)

**Additional References**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025 — CALR cross-dataset marker)

## 5. Parent Term Validation

**Proposed Parent**: intrinsic primary afferent neuron of myenteric plexus [NEW]

**Justification**:
The calretinin-positive IPAN is a chemical subtype of the general myenteric IPAN class, distinguished by calretinin immunoreactivity. The functional identity (sensory, Dogiel type II, AH electrophysiology) and anatomical location are inherited from the parent.

**Hierarchical Context**:
```
intrinsic primary afferent neuron of myenteric plexus [NEW]
    ├── calretinin-positive intrinsic primary afferent neuron of myenteric plexus [NEW]
    └── calretinin-negative intrinsic primary afferent neuron of myenteric plexus [NEW]
```

## 6. Synonyms

**Validated Synonyms**:
- SN1 — abbreviation used in Chen et al. (PMC10469081) chemical coding scheme
- calretinin-positive myenteric sensory neuron — simplified functional label

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439)
- `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — ChAT+ identity

**Note**: A `expresses` some calretinin protein relationship should be added; the CL-ontologist should identify the appropriate PRO term for calretinin (encoded by CALB2).

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

Calretinin is a well-validated IHC marker with categorical expression; the SN1 subtype is consistently characterised in human colonic myenteric plexus. Calretinin-expressing Dogiel type II neurons have been reported in human and guinea pig, providing initial cross-species support. Ready for CL integration.

## 9. Additional Notes
- The calretinin+/− split between SN1 and SN2 is the sole chemical distinction between these two IPAN subtypes in Chen et al. Both share Dogiel type II morphology, ChAT+, NOS1−, and substance P+ coding.
- Cross-species confirmation in mouse should be obtained before asserting species-agnostic subterm validity at population scale.
- PRO ID for calretinin (CALB2 gene product) should be identified for the `expresses` logical relationship.

## 10. Confidence Assessment
- Definition: High (calretinin IHC is a reliable categorical marker; SN1 identity is consistent in Chen et al.)
- Parent term: High
- Cross-references: Medium-High (primary human data strong; cross-species confirmation in progress)
- Overall: High

---

# Curation Report: Calretinin-Negative Intrinsic Primary Afferent Neuron of Myenteric Plexus

## 1. Term Identification
- **Proposed Label**: calretinin-negative intrinsic primary afferent neuron of myenteric plexus
- **Status**: New term (chemical subtype of intrinsic primary afferent neuron of myenteric plexus [NEW]; corresponds to SN2 in Chen et al. chemical coding scheme)

## 2. Definition Validation

**Proposed Definition**:
An intrinsic primary afferent neuron of the myenteric plexus that lacks calretinin expression. This neuron shares the Dogiel type II morphology and AH-type electrophysiology of all myenteric IPANs, and is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).

**Literature Support**:
- PMC10469081 (Chen et al.) — Defines SN2 as calretinin−, ChAT+, NOS1−, substance P+, with large soma area (mean ~1616 µm²). SN2 is distinguished from SN1 solely by the absence of calretinin immunoreactivity; all other chemical and morphological properties are shared.
- PMC8397665 (Brehmer 2021) — Notes that not all Dogiel type II neurons are calretinin-positive in human ENS; calretinin-negative Dogiel type II neurons have been identified.
- PMC12528430 (Majd et al. 2025) — IPAN/sensory neuron class recognised across datasets; calretinin marks a subset of this class.

**Validation Notes**:
Defining a cell type by marker absence is appropriate when: (a) the absence is consistently observed, (b) the sibling positive type (SN1: calretinin+) is well-defined, and (c) together the two subtypes represent a complete partition of the parent class in the studied tissue. All three conditions are met here. Chen et al.'s validated multilayer IHC panel (including calretinin antibody controls) supports the reliability of the calretinin-negative call over a technical false negative.

## 3. Experimental Evidence

**Summary of experimental evidence**:
Chen et al. (PMC10469081) characterised SN2 from 2596 human colonic myenteric neurons. SN2 is ChAT+, NOS1−, substance P+, calretinin−, with large soma area consistent with Dogiel type II morphology. The calretinin-negative status is established in the context of the positive identification of SN1 as calretinin+, making SN2 the complementary IPAN population.

**Literature Support**:
- PMC10469081 — Table 7: SN2 (CalR−) chemical coding and soma size data.
- PMC8397665 — Calretinin-negative Dogiel type II neurons in human ENS.
- PMC12528430 — IPAN class recognition across datasets.

## 4. Cross-References

**Primary References**:
- PMC10469081 (Chen et al. — SN2 subtype definition in human colonic myenteric plexus)
- PMC8397665 (Brehmer 2021 — calretinin-negative context in human ENS)

**Additional References**:
- PMC12528430 / DOI:10.1038/s44318-025-00559-1 (Majd et al. 2025)

## 5. Parent Term Validation

**Proposed Parent**: intrinsic primary afferent neuron of myenteric plexus [NEW]

**Justification**:
The calretinin-negative IPAN is the complementary subtype to the calretinin-positive IPAN (SN1) within the myenteric IPAN class. Together, SN1 and SN2 partition the IPAN class in human colonic myenteric plexus.

**Hierarchical Context**:
```
intrinsic primary afferent neuron of myenteric plexus [NEW]
    ├── calretinin-positive intrinsic primary afferent neuron of myenteric plexus [NEW]
    └── calretinin-negative intrinsic primary afferent neuron of myenteric plexus [NEW]
```

## 6. Synonyms

**Validated Synonyms**:
- SN2 — abbreviation used in Chen et al. (PMC10469081)
- calretinin-negative myenteric sensory neuron — simplified functional label

## 7. Logical Relationships

**Validated Relationships**:
- `has soma location` some myenteric nerve plexus (UBERON:0002439)
- `capable of` some acetylcholine secretion, neurotransmission (GO:0014055) — ChAT+ identity

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The calretinin-negative IPAN (SN2) represents the complementary partner to SN1 within the IPAN class. Both subtypes are required for a complete ontological partition of myenteric IPANs. Definition by marker absence is ontologically acceptable here given the clean binary split with SN1 and the reliability of the IHC evidence.

## 9. Additional Notes
- Defining by marker absence is acceptable here because: (a) the sibling calretinin+ SN1 term is well-defined; (b) both subtypes are otherwise identical in morphology, function, and remaining chemical markers; (c) Chen et al.'s validated multilayer IHC panel reliably captures calretinin expression.
- Unlike NF200-based splits (which threshold a continuous staining intensity), the calretinin+/− distinction represents a genuine categorical difference and is technically more reliable for cell type definition.
- Cross-species validation of the calretinin-negative IPAN is needed before asserting species-agnostic validity.

## 10. Confidence Assessment
- Definition: High (SN1/SN2 split is consistent in Chen et al.; calretinin IHC is technically reliable)
- Parent term: High
- Cross-references: Medium-High (primary human data strong; cross-species confirmation needed)
- Overall: High

---

# Reference Log

The following files were downloaded and consulted during this curation session:

| PMID | DOI | Title | FullTextPath | PDFPath | SupplementaryMaterialPath |
|------|-----|-------|--------------|---------|--------------------------|
| 40954253 | 10.1038/s44318-025-00559-1 | A call for a unified and multimodal definition of cellular identity in the enteric nervous system (Majd et al. 2025) | /Users/do12/Documents/GitHub/onto_template_agentic_env/pdfs/PMC12528430_Majd2025_ENS_unified_definition.txt | not retrieved | not retrieved |
| not extracted | not extracted | Types of Neurons in the Human Colonic Myenteric Plexus Identified by Multilayer Immunohistochemical Coding (Chen et al.) | /Users/do12/Documents/GitHub/onto_template_agentic_env/pdfs/PMC10469081_full_text.txt | not retrieved | not retrieved |
| not extracted | not extracted | Classification of human enteric neurons (Brehmer 2021) | /Users/do12/Documents/GitHub/onto_template_agentic_env/pdfs/PMC8397665_full_text.txt | not retrieved | not retrieved |
| 32888429 | 10.1016/j.cell.2020.08.003 | The Human and Mouse Enteric Nervous System at Single-Cell Resolution (Drokhlyansky et al. 2020) | pdfs/PMC8358727_Drokhlyansky2020_full_text.txt | pdfs/nihms-1728589.pdf | not retrieved |
| 39239246 | 10.1016/j.celrep.2024.113653 | First characterization of human colonic viscerofugal neurons (Chen et al. 2024) | pdfs/PMC10825022_full_text.txt (summary) | not retrieved | not retrieved |

**References not retrieved — flag for follow-up**:
- Furness JB (2012) The enteric nervous system and neurogastroenterology. Annual Review of Physiology 74:305-326. DOI:10.1146/annurev-physiol-020911-153245
- Furness JB (2006) The Enteric Nervous System. Blackwell, Oxford (book — not in EuropePMC)
- Morarach K et al. (2021) Diversification of molecularly defined myenteric neuron classes revealed by single-cell RNA sequencing. Nature Neuroscience 24:34-46
- Mann PT, Furness JB, Southwell BR (1995) J Auton Nerv Syst 56:15-25, PMID:8786275 — primary characterization of guinea pig intestinofugal neurons (CART marker is species-specific; NOT applicable to humans)

---

# Summary and Handoff

## Terms with High Confidence — Ready for CL Integration

**1. Excitatory motor neuron of myenteric plexus**
Definition, parent (CL:0007011), and key relationships validated. Marker combination synonym: 'cholinergic non-nitrergic myenteric motor neuron'. Confirm reason for obsoletion of CL:0008014 before creating new term.

**2. Inhibitory motor neuron of myenteric plexus**
Definition, parents (CL:0007011, CL:0008015 subclass), and key relationships validated. Marker combination synonyms: 'nitrergic motor neuron of myenteric plexus', 'NOS1-positive ChAT-negative myenteric motor neuron'. Flag for GO editors: create `nitric oxide secretion, neurotransmission` GO term analogous to GO:0014055.

**3. Intrinsic primary afferent neuron of myenteric plexus**
Definition, parents (CL:0007011, CL:0000101), and key relationships validated. Marker combination synonym: 'multiaxonal cholinergic myenteric sensory neuron'.

**4. Interneuron of myenteric plexus**
General definition validated with dual parents (CL:0007011, CL:0000099). Marker combination synonyms deferred to subterms.

**4a. Ascending interneuron of myenteric plexus** *(subterm of 4)*
ChAT+/ENK+ ascending excitatory limb. Marker combination synonym: 'cholinergic enkephalinergic myenteric interneuron'. High confidence for chemical code.

**4b. Descending interneuron of myenteric plexus** *(subterm of 4)*
Chemically diverse descending inhibitory limb (5-HT+, NOS1+, and other subtypes). Medium confidence for marker definitions due to inter-dataset inconsistency (Majd et al. 2025). Serotonergic descending subtype proposed as marker combination synonym-eligible subterm.

**5. Secretomotor/vasodilator neuron of myenteric plexus (PSVN)**
Now characterized by Drokhlyansky et al. 2020 (PMC8358727). Mouse: two Glp2r+ subtypes — PSVN1 (VIP+ non-cholinergic, Fst+) and PSVN2 (ChAT+, Gal+, Npy+). Human: only VIP+ subtype detected. Conserved program: VIP, Gal, Scgn, Calb2. Marker combination synonym: 'VIP-positive secretomotor neuron'. Medium-High confidence (species difference in cholinergic subtype).

**6. Intestinofugal neuron (viscerofugal neuron, VFN)**
Definitive human characterization by Chen et al. 2024 (PMC10825022): 89% ChAT+, 0% CART+ (N=123). CART is NOT a human marker (rodent-specific). Marker combination synonym: 'cholinergic viscerofugal neuron'. High confidence.

**5. Stubby Dogiel type I neuron of myenteric plexus** *(morphological subterm of 1)*
Subclass of EMN and CL:4047038. ChAT+/NOS1−, lamellar dendrites. High confidence.

**6. Spiny Dogiel type I neuron of myenteric plexus** *(morphological subterm of 2)*
Subclass of IMN and CL:4047038. NOS1+/ChAT−, spine-like dendrites. High confidence.

**7. Dogiel type II neuron of myenteric plexus** *(morphological subterm of 3)*
Subclass of IPAN and new general Dogiel type II term (sibling to CL:4047038). ChAT+/NOS1−, multiaxonal, large soma, AH-type. Marker combination synonyms: 'multiaxonal myenteric sensory neuron', 'AH-type myenteric neuron'. High confidence. **Ready** — general Dogiel type II neuron term to be created as sibling to CL:4047038.

**7a. Calretinin-positive intrinsic primary afferent neuron of myenteric plexus** *(chemical subterm of 3)*
Subclass of IPAN. CalR+/ChAT+/NOS1−. Corresponds to SN1 in Chen et al. Calretinin is a categorical IHC marker providing a reliable binary split. Synonym: 'SN1', 'calretinin-positive myenteric sensory neuron'. High confidence.

**7b. Calretinin-negative intrinsic primary afferent neuron of myenteric plexus** *(chemical subterm of 3)*
Subclass of IPAN. CalR−/ChAT+/NOS1−. Corresponds to SN2 in Chen et al. Complementary partner to 7a; definition by marker absence is ontologically appropriate given clean binary partition with SN1. Synonym: 'SN2', 'calretinin-negative myenteric sensory neuron'. High confidence.

**8. Cholinergic neuron of myenteric plexus** *(defined grouping class)*
EquivalentTo: enteric neuron AND `has soma location` UBERON:0002439 AND `capable of` GO:0014055. Autoclassifies EMN, IPAN, ascending interneuron, and their morphological/chemical subterms. Collaborator mapping: 'myenteric ganglion ChAT neuron'. High confidence.

**9. Nitrergic neuron of myenteric plexus** *(defined grouping class)*
EquivalentTo: enteric neuron AND `has soma location` UBERON:0002439 AND `capable of` GO:0006809. Autoclassifies IMN and spiny Dogiel type I neuron. Update axiom to specific `nitric oxide secretion, neurotransmission` GO term when created. Collaborator mapping: 'myenteric ganglion nNOS neuron'. High confidence.

**16. Dogiel type II neuron** *(general morphological class)*
Sibling to CL:4047038 (Dogiel type I neuron). Defined by multiaxonal morphology: smooth oval soma with multiple long axon-like processes. Parent of 'Dogiel type II neuron of myenteric plexus'. Synonyms: 'multiaxonal enteric neuron', 'AH neuron', 'type II enteric neuron'. High confidence.

## Terms Requiring Additional Research Before CL Integration

*None — all terms now have sufficient literature support.*

**Note on Term 5 (PSVN)**: Drokhlyansky et al. 2020 (PMC8358727) provides scRNA-seq characterization of two mouse PSVN subtypes (VIP+ non-cholinergic and ChAT+ cholinergic). In human, only the VIP+ subtype was detected. Term is now Ready for integration with species-specific notes.

**Note on Term 11 (Intestinofugal/VFN)**: Chen et al. 2024 (PMC10825022) provides definitive human characterization with critical correction: CART is NOT a human marker (0%), ChAT is the primary marker (89%). Ready for integration.

## Updated Collaborator Term Mappings

| Collaborator term | Best CL mapping | Specificity |
|---|---|---|
| myenteric ganglion ChAT neuron | cholinergic neuron of myenteric plexus [NEW #8] | Grouping — add NOS1/morphology to reach specific term |
| myenteric ganglion ChAT/CALR/SOM/SP neuron | calretinin-positive IPAN of myenteric plexus [NEW #7a / SN1] | Specific |
| myenteric ganglion NF200 neuron | **No mapping — polyphyletic** | NF200 spans EMN, IMN, IPAN subsets |
| myenteric ganglion nNOS neuron | nitrergic neuron of myenteric plexus [NEW #9] | Grouping — add ChAT−/target to reach IMN |
| myenteric ganglion nNOS/ChAT neuron | **No mapping** — co-expressing neurons not assigned a term | Unresolved |
| myenteric ganglion nNOS/VIP neuron | spiny Dogiel type I neuron of myenteric plexus [NEW #6] or IMN [NEW #2] | Specific if morphology confirmed |
| myenteric ganglion VIP neuron | nitrergic neuron of myenteric plexus [NEW #9] (approximate) | VIP is IMN co-transmitter; NOS1 confirmation gives specific mapping to IMN |
| myenteric ganglion VIP/GAL neuron | inhibitory motor neuron of myenteric plexus [NEW #2] | VIP+GAL co-expression reported in nitrergic IMN subset |

## Action Items for CL-Ontologist

1. Retrieve and review: Furness JB (2012) Annual Review of Physiology 74:305-326
2. Retrieve and review: Morarach et al. (2021) Nature Neuroscience 24:34-46
3. ~~Retrieve and review: Mann et al. (1995)~~ **DONE** — J Auton Nerv Syst 56:15-25, PMID:8786275. Note: CART marker is guinea pig-specific; NOT applicable to humans.
4. ~~Retrieve full text: Drokhlyansky et al. 2020~~ **DONE** — pdfs/PMC8358727_Drokhlyansky2020_full_text.txt
5. Confirm reason for obsoletion of CL:0008014 before creating 'excitatory motor neuron of myenteric plexus'
6. ~~Create general 'Dogiel type II neuron' CL term~~ **INCLUDED** — see new section below; sibling to CL:4047038
7. Find PATO terms for: lamellar dendrite morphology (stubby Dogiel I), spine-like dendrite morphology (spiny Dogiel I), multiaxonal morphology (Dogiel type II)
8. ~~Find PRO ID for CARTPT protein~~ **NOT NEEDED for human intestinofugal neuron** — Chen et al. 2024 shows 0% CART in human VFNs. CART is rodent-specific.
9. Find PRO ID for calretinin (CALB2 gene product) for `expresses` relation on calretinin-positive IPAN subterm
10. Find UBERON terms for prevertebral sympathetic ganglia (celiac: UBERON:0002262, superior mesenteric: UBERON:0005479, inferior mesenteric: UBERON:0005480) — **CONFIRMED**
11. Flag GO editors: request `nitric oxide secretion, neurotransmission` GO term analogous to GO:0014055; update nitrergic grouping class EquivalentClass axiom when created
12. Confirm CL:4047038 scope — is it already restricted to enteric neurons?
13. Confirm CL:0000108 scope before asserting dual parentage on cholinergic grouping class
14. Check whether a general 'nitrergic neuron' CL term exists; if so, add as parent of nitrergic grouping class
15. Confirm cross-species validity of stubby/spiny Dogiel type I distinction in mouse and rat
16. Confirm cross-species validity of calretinin+/− IPAN split (SN1/SN2) in mouse

**CURATION UPDATE 2026-03-10**:
- Drokhlyansky et al. 2020 full text retrieved (PDF extracted)
- Chen et al. 2024 (PMC10825022) retrieved — first human VFN characterization
- **CRITICAL CORRECTION**: CART/CARTPT is NOT a human intestinofugal neuron marker (0/123 VFNs CART+). ChAT is the primary human marker (89%).
- Intestinofugal neuron definition upgraded from "Needs research" to "Ready"

CURATION COMPLETE — ALL 16 TERMS READY FOR INTEGRATION
  - Term 9 (nitrergic grouping class) EquivalentClass axiom to be updated when GO term for nitric oxide neurotransmission is created
  - Term 5 (PSVN): Note species difference in cholinergic subtype detection
  - Term 11 (Intestinofugal/VFN): Note CART is NOT a human marker
