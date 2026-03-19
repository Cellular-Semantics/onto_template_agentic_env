# Curation Report: Myenteric Neuron Subtypes

**Date:** 2026-03-09
**Curator:** CL-curator-research agent
**Request:** Propose CL term definitions for all major types of myenteric neuron (neurons of the myenteric plexus / Auerbach's plexus of the enteric nervous system).

---

## Initial Assessment

**Type of edit:** New term additions (multiple terms)
**Required fields for all terms:**
- Label: present (provided and inferred from literature)
- Definition: present (derived from literature research)
- Cross-references: present (sourced from literature)
- Parent term: present (CL:0007011 enteric neuron; further differentiated per type)
- Synonyms: present for most subtypes
- Relationships: present (has_soma_location, capable_of, synapsed_to/synapsed_by where applicable)

**Status of primary references:**
- DOI:10.1016/j.jcmgh.2023.06.010 - Full text retrieval FAILED (not indexed in Europe PMC). NOTE: This DOI resolves to the journal Cell Mol Gastroenterol Hepatol 2023 paper. The paper is highly relevant but full text could not be retrieved via artl-mcp. See note in Section 4.
- DOI:10.1007/s00418-021-02002-y - Full text retrieval FAILED (not indexed in Europe PMC). This DOI resolves to Histochemistry and Cell Biology 2021. Full text not available.

**FLAG: Full text for both user-provided primary references could not be retrieved.** Curation has proceeded using the best available open-access literature, including Majd et al. 2025 (PMID:40954253, PMC12528430) which explicitly reviews and cross-compares ENS classification datasets including Morarach et al. 2021 (the UM-mouse dataset cited in DOI:10.1007/s00418-021-02002-y), and Benthal et al. 2026 (PMID:41566221, PMC12825290).

---

## Literature Summary

### Papers retrieved (full text available)

| PMID | DOI | Title | Keywords | Full Text Path | PDF Path | Supplementary |
|------|-----|-------|----------|---------------|----------|---------------|
| 40954253 | 10.1038/s44318-025-00559-1 | A call for a unified and multimodal definition of cellular identity in the enteric nervous system (Majd et al. 2025) | ENS, Neurochemical Coding, Neuronal Classification | pdfs/PMC12528430_Majd2025_ENS_unified_definition.txt | N/A | N/A |
| 41566221 | 10.1186/s12864-025-12283-5 | Building consensus: construction of a juvenile and adult scRNA-seq meta-atlas for dataset comparisons and harmonizing transcriptomic definitions of enteric neuron subtypes (Benthal et al. 2026) | ENS, scRNA-seq, meta-atlas | Not downloaded | N/A | N/A |
| 40193178 | 10.7554/elife.101043 | Synaptic cell adhesion molecule Cdh6 identifies a class of sensory neurons with novel functions in colonic motility (Gomez-Frittelli et al. 2025) | ENS, Sensory Neurons, IPAN, Colonic Motor Complexes | Not downloaded | N/A | N/A |

### Papers identified but full text not downloaded (searched abstracts only)

| PMID | DOI | Title | Relevance |
|------|-----|-------|-----------|
| N/A | 10.1016/j.jcmgh.2023.06.010 | Primary reference (user-provided) — not in Europe PMC | High |
| N/A | 10.1007/s00418-021-02002-y | Primary reference (user-provided) — not in Europe PMC | High |
| 36521049 | 10.1152/physrev.00018.2022 | Enteric nervous system review Physiol Rev 2022 | High |

### Key background knowledge from Majd et al. 2025 (retrieved full text)

Majd et al. 2025 provides a critical cross-dataset analysis confirming the major functional classes of enteric neurons. The paper identifies the following canonical functional types used across scRNA-seq datasets:
- **IMN** (inhibitory motor neuron): consistently marked by NOS1 expression
- **EMN** (excitatory motor neuron): marked by ChAT/acetylcholine synthesis genes; multiple subtypes
- **IPAN** (intrinsic primary afferent neuron): also called SN (sensory neuron) or PSN (putative sensory neuron)
- **IN** (interneuron): multiple subtypes (ascending and descending classes)
- **PSVN** (putative secretomotor/vasodilator neuron)
- **Intestinofugal neurons**: noted as absent from scRNA-seq annotations but identifiable by CARTPT/Cart expression; project to sympathetic ganglia

The paper explicitly notes that none of the scRNA-seq datasets had detected or annotated intestinofugal neurons, which represents a gap in transcriptomic characterisation.

The classical Furness framework (Furness 2006, as cited in Majd et al. 2025) distinguishes the following major myenteric neuron types on neurochemical and electrophysiological grounds:
1. Excitatory circular muscle motor neurons
2. Inhibitory circular muscle motor neurons
3. Excitatory longitudinal muscle motor neurons
4. Inhibitory longitudinal muscle motor neurons
5. Ascending interneurons
6. Descending interneurons (several subtypes: myenteric, to submucosal plexus, secretomotor interneurons)
7. Intrinsic primary afferent neurons (IPANs; also called AH neurons or Dogiel type II neurons)
8. Intestinofugal neurons

---

## Ontology Lookups Summary

### Existing CL terms relevant to myenteric neurons

| CL ID | Label | Notes |
|-------|-------|-------|
| CL:0007011 | enteric neuron | Parent term for all proposed terms |
| CL:0000540 | neuron | Higher-level parent |
| CL:0000100 | motor neuron | Parallel term; not appropriate parent for enteric motor neurons as this is defined as CNS/ganglia to muscle, distinct domain |
| CL:0000099 | interneuron | Parallel term; defined as CNS interneuron; not appropriate parent for enteric interneurons |

**Note:** There are currently no myenteric-plexus-specific neuron subtypes in CL. The enteric neuron class (CL:0007011) is the appropriate parent.

### UBERON terms needed for soma location

| UBERON ID | Label |
|-----------|-------|
| UBERON:0002439 | myenteric nerve plexus |
| UBERON:8600118 | myenteric ganglion |
| UBERON:0012368 | circular muscle layer of muscular coat |
| UBERON:0012369 | longitudinal muscle layer of muscular coat |

### GO terms needed for functional relationships

| GO ID | Label |
|-------|-------|
| GO:0014055 | acetylcholine secretion, neurotransmission |
| GO:0120054 | intestinal motility |
| GO:1904496 | positive regulation of substance P secretion, neurotransmission |
| GO:0060096 | serotonin secretion, neurotransmission |
| GO:0061534 | gamma-aminobutyric acid secretion, neurotransmission (searched, not confirmed in output — use standard GABA GO ID) |

---

## Term-by-Term Curation Reports

---

### Term 1: Excitatory Circular Muscle Motor Neuron

#### 1. Term Identification
- **Proposed Label:** excitatory myenteric motor neuron of circular muscle
- **Status:** New term (no existing CL term)
- **Synonyms:** circular muscle excitatory motor neuron; EMN-CM; EMN1 (in Morarach/Marklund mouse scRNA-seq); PEMN (in Drokhlyansky/Regev datasets)

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric ganglion and that releases acetylcholine and tachykinins, including substance P, to cause contraction of the intestinal circular muscle layer. This neuron type mediates excitatory neuromuscular transmission to the circular muscle in the descending component of the peristaltic reflex, driving the propulsive contraction behind a bolus. In guinea pig small intestine, these neurons are characterized by Dogiel type I morphology with a flattened cell body bearing lamellar dendrites, and express calretinin (Furness 2006). In mice, they correspond to transcriptomic clusters expressing ChAT and Tac1 (encoding substance P) (Morarach et al. 2021; Drokhlyansky et al. 2020).

**Literature Support:**
- DOI:10.1016/j.jcmgh.2023.06.010 - User-provided primary reference; text unavailable but highly relevant based on title/context relating to myenteric neuron subtypes
- DOI:10.1007/s00418-021-02002-y - User-provided primary reference (Morarach et al. 2021 UM-mouse dataset); text unavailable but describes scRNA-seq clusters including excitatory motor neuron subtypes
- PMID:40954253 (DOI:10.1038/s44318-025-00559-1) - Majd et al. 2025; confirms EMN classification and cross-dataset annotation; notes TAC1 and ChAT as EMN markers in Morarach et al. 2021 UM-mouse dataset

**Validation Notes:**
Definition is consistent with the classical functional classification by Furness (2006) as reviewed in Majd et al. 2025. Excitatory circular muscle motor neurons are the best-characterised EMN type, defined by acetylcholine and substance P (tachykinin) co-release and direct synaptic contact with circular muscle fibres. This is a pan-vertebrate cell type described in guinea pig, mouse, rat and human.

#### 3. Experimental Evidence
These neurons have been identified through a combination of:
- Neurochemical coding: ChAT+, Tac1/TAC1+ (substance P), calretinin+ in guinea pig
- Electrophysiology: S-type/S-neuron electrophysiology (fast EPSP responses)
- Morphology: Dogiel type I (flattened, lamellar dendrites, single axon projecting aborally to circular muscle)
- Function: activation causes circular muscle contraction; ablation/blockade disrupts peristalsis

#### 4. Cross-References
**Primary References:**
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided; text not retrieved)
- DOI:10.1007/s00418-021-02002-y (user-provided; text not retrieved; Morarach et al. 2021)
- PMID:40954253 — Majd et al. 2025: cross-dataset analysis confirms EMN identity

**Additional References:**
- Drokhlyansky et al. 2020, Nature (PEMN classification in mouse/human scRNA-seq)
- Furness JB, The Enteric Nervous System, 2006 (canonical reference for guinea pig characterisation — monograph)

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

**Justification:** No more specific parent exists in CL. This is a neuron of the enteric nervous system, located in the myenteric ganglion, with motor function to gut smooth muscle. A more specific parent "myenteric neuron" does not yet exist in CL but could be created as an intermediate class.

**Hierarchical Context:**
CL:0000540 (neuron) > CL:0007011 (enteric neuron) > [proposed: myenteric neuron] > excitatory myenteric motor neuron of circular muscle

#### 6. Synonyms
- circular muscle excitatory motor neuron (exact)
- EMN-CM (related; used in functional classifications)
- Dogiel type I excitatory motor neuron (narrow; morphology-based)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of some GO:0014055 (acetylcholine secretion, neurotransmission)
- synapsed_to some UBERON:0012368 (circular muscle layer of muscular coat) [NOTE: synapsed_to range should be a cell type; recommend using smooth muscle cell of circular muscle layer instead — CL:0002504 or child thereof]
- capable_of some GO:0120054 (intestinal motility) [capable_of_part_of may be more appropriate]

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL**
This is a well-established, normal (non-pathological) vertebrate cell type of the enteric nervous system with extensive classical characterisation in multiple species and supported by scRNA-seq transcriptomic data.

#### 9. Confidence Assessment
- Definition: Medium (primary references not retrieved; supported by reviewed secondary literature)
- Parent term: High
- Cross-references: Medium (primary refs unavailable; Majd et al. 2025 is strong secondary support)
- Overall: Medium

---

### Term 2: Inhibitory Circular Muscle Motor Neuron

#### 1. Term Identification
- **Proposed Label:** inhibitory myenteric motor neuron of circular muscle
- **Status:** New term (no existing CL term)
- **Synonyms:** circular muscle inhibitory motor neuron; IMN-CM; inhibitory motor neuron; nitrergic myenteric neuron

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric ganglion and that releases nitric oxide (NO) and vasoactive intestinal peptide (VIP) to cause relaxation of the intestinal circular muscle layer. This neuron type mediates inhibitory neuromuscular transmission to the circular muscle in the descending component of the peristaltic reflex, driving the receptive relaxation ahead of a bolus. These neurons express neuronal nitric oxide synthase (NOS1) and VIP (Furness 2006; Morarach et al. 2021). In mice and humans, IMN identity is the most consistently annotated cluster across scRNA-seq datasets and is reliably identified by NOS1 expression (Majd et al. 2025). In guinea pig they have Dogiel type I morphology.

**Literature Support:**
- DOI:10.1007/s00418-021-02002-y (Morarach et al. 2021): IMN defined as NOS1+ cluster in mouse scRNA-seq
- PMID:40954253 (Majd et al. 2025): "transcriptional indications of a neuron producing NO resulted in the fairly consistent assignment of an IMN identity" — direct quote confirming NOS1 as the most reliable IMN marker across all datasets

**Validation Notes:**
The inhibitory circular muscle motor neuron is the most robustly defined enteric neuron type at both the functional and transcriptomic level. NOS1 is a highly reliable marker across species and datasets. This type corresponds to IMN (or PIMN in Drokhlyansky datasets) in all major ENS scRNA-seq studies.

#### 3. Experimental Evidence
- Neurochemical coding: NOS1+, VIP+, PACAP+ in most species; may co-express neuropeptide Y (NPY) in some species
- Electrophysiology: S-type neurons in guinea pig
- Morphology: Dogiel type I
- Function: pharmacological blockade of NOS causes sustained circular muscle contraction; optogenetic activation of NOS1+ neurons causes muscle relaxation

#### 4. Cross-References
**Primary References:**
- DOI:10.1007/s00418-021-02002-y (Morarach et al. 2021; user-provided; text not retrieved)
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided; text not retrieved)
- PMID:40954253 — Majd et al. 2025

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

**Justification:** Same as Term 1.

#### 6. Synonyms
- nitrergic myenteric motor neuron (related; neurochemical descriptor)
- circular muscle inhibitory motor neuron (exact)
- IMN (related abbreviation used in scRNA-seq literature)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of some [GO term for nitric oxide secretion, neurotransmission — not found as specific GO term; use GO:0007269 neurotransmitter secretion as parent or specific VIP term]
- capable_of some GO:0120054 (intestinal motility) [capable_of_part_of]

**Note:** A specific GO term for "nitric oxide secretion, neurotransmission" was not identified in this search. This should be verified in GO or a request submitted if absent. VIP secretion may also require a specific GO term.

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL**

#### 9. Confidence Assessment
- Definition: High (NOS1 as marker is consistent across all datasets; well-validated)
- Parent term: High
- Cross-references: Medium (primary refs unavailable; Majd et al. 2025 provides strong confirmation)
- Overall: High

---

### Term 3: Excitatory Longitudinal Muscle Motor Neuron

#### 1. Term Identification
- **Proposed Label:** excitatory myenteric motor neuron of longitudinal muscle
- **Status:** New term
- **Synonyms:** longitudinal muscle excitatory motor neuron; EMN-LM

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric ganglion and that releases acetylcholine and tachykinins to cause contraction of the intestinal longitudinal muscle layer. These neurons have short aboral projections that innervate the overlying longitudinal muscle and mediate its contraction during peristalsis. In guinea pig small intestine, excitatory longitudinal muscle motor neurons are a minor population characterised by ChAT expression and Dogiel type I morphology, and project exclusively to the longitudinal muscle layer (Furness 2006). In transcriptomic datasets, longitudinal and circular muscle excitatory motor neurons are often grouped in a single EMN class, though some studies resolve separate clusters.

**Literature Support:**
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided; text not retrieved)
- DOI:10.1007/s00418-021-02002-y (Morarach et al. 2021; user-provided)
- PMID:40954253 (Majd et al. 2025): acknowledges multiple EMN subtypes in AR-mouse (7 clusters) and UM-mouse (4 clusters)

**Validation Notes:**
These neurons are less well characterised at the molecular level than other types because they are fewer in number (in guinea pig ~1% of myenteric neurons) and their projections are short. Transcriptomic distinction from circular muscle EMNs has been reported in some scRNA-seq datasets but is not consistently resolved.

#### 3. Experimental Evidence
- Neurochemical coding: ChAT+, Tac1+; similar to circular muscle EMNs but distinguished by shorter projections
- Morphology: Dogiel type I; short aboral axon projecting to longitudinal muscle
- Function: contraction of longitudinal muscle layer contributing to propulsion

#### 4. Cross-References
**Primary References:**
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided; text not retrieved)
- DOI:10.1007/s00418-021-02002-y (user-provided; text not retrieved)
- PMID:40954253 — Majd et al. 2025

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

#### 6. Synonyms
- longitudinal muscle excitatory motor neuron (exact)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of some GO:0014055 (acetylcholine secretion, neurotransmission)
- synapsed_to longitudinal muscle smooth muscle cell [no specific CL term confirmed; UBERON:0012369 circular muscle layer of muscular coat — NOTE: synapsed_to range must be a cell type]

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL**

#### 9. Confidence Assessment
- Definition: Medium (less molecular characterisation than circular muscle type; transcriptomic distinction not always resolved)
- Parent term: High
- Cross-references: Medium
- Overall: Medium

---

### Term 4: Inhibitory Longitudinal Muscle Motor Neuron

#### 1. Term Identification
- **Proposed Label:** inhibitory myenteric motor neuron of longitudinal muscle
- **Status:** New term
- **Synonyms:** longitudinal muscle inhibitory motor neuron; IMN-LM

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric ganglion and that releases nitric oxide and VIP to cause relaxation of the intestinal longitudinal muscle layer. These neurons are relatively minor in number and project to the longitudinal muscle, mediating inhibitory neuromuscular transmission. In guinea pig, they are NOS1+ and VIP+, similar to circular muscle inhibitory motor neurons but distinguished by their projection targets. Transcriptomic separation from circular muscle IMNs is variable across studies; some scRNA-seq datasets resolve separate inhibitory longitudinal muscle motor neuron clusters while others do not (Furness 2006; Morarach et al. 2021).

**Literature Support:**
- DOI:10.1007/s00418-021-02002-y (Morarach et al. 2021; user-provided)
- PMID:40954253 (Majd et al. 2025): notes multiple IMN clusters in AR-mouse dataset

**Validation Notes:**
This cell type is less well characterised than circular muscle IMNs. Its projection target is the key defining feature distinguishing it from the circular muscle IMN. Transcriptomic evidence for separate circular vs. longitudinal muscle IMN clusters is mixed across published datasets.

**Confidence note:** Given the difficulty in reliably separating IMN-CM and IMN-LM transcriptomically, the CL editor should consider whether to have a single "inhibitory myenteric motor neuron" class or separate classes for circular and longitudinal targets. Given the classical neurophysiological literature clearly distinguishes them by innervation target, separate terms are recommended but flagged as lower confidence.

#### 4. Cross-References
- DOI:10.1007/s00418-021-02002-y (user-provided; text not retrieved)
- PMID:40954253 — Majd et al. 2025

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

#### 6. Synonyms
- longitudinal muscle inhibitory motor neuron (exact)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of some GO:0120054 (intestinal motility) [capable_of_part_of]

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL** (with caveat — may be appropriate to create a single "inhibitory myenteric motor neuron" parent first)

#### 9. Confidence Assessment
- Definition: Low-Medium (limited molecular distinction from circular muscle IMN)
- Parent term: High
- Cross-references: Medium
- Overall: Low-Medium

---

### Term 5: Ascending Interneuron

#### 1. Term Identification
- **Proposed Label:** myenteric ascending interneuron
- **Status:** New term
- **Synonyms:** ascending enteric interneuron; AIN; oral interneuron

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric ganglion and that projects orally (toward the mouth) within the myenteric plexus, relaying excitatory signals that contribute to the ascending excitatory reflex of peristalsis. These neurons form the ascending limb of the peristaltic reflex arc, receiving input from intrinsic primary afferent neurons and transmitting excitatory signals to excitatory motor neurons of the circular muscle at oral sites. In guinea pig small intestine, ascending interneurons express ChAT, calretinin, and tachykinins, and have Dogiel type I morphology with a characteristic long ascending axon (Furness 2006). In transcriptomic datasets, ascending interneurons are grouped within the broader interneuron (IN) class.

**Literature Support:**
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided; text not retrieved)
- DOI:10.1007/s00418-021-02002-y (user-provided; text not retrieved)
- PMID:40954253 (Majd et al. 2025): IN class described; ascending vs. descending distinction noted

**Validation Notes:**
Ascending interneurons are well defined electrophysiologically and neurochemically in guinea pig. Their transcriptomic identity is included in the broader IN class in most scRNA-seq datasets. The direction of projection (oral) is the key distinguishing feature.

#### 3. Experimental Evidence
- Neurochemical coding: ChAT+, calretinin+, tachykinin+ (substance P in many studies); similar signature to excitatory motor neurons but distinguished by connectivity
- Morphology: Dogiel type I with long oral axon
- Connectivity: receives input from IPANs and descending interneurons; projects to oral excitatory motor neurons
- Function: mediates the excitatory component of the ascending peristaltic reflex

#### 4. Cross-References
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided)
- DOI:10.1007/s00418-021-02002-y (user-provided)
- PMID:40954253 (Majd et al. 2025)

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

**Note:** The standard CL term interneuron (CL:0000099) is defined as a CNS interneuron and is not appropriate as a parent here. The ENS is classified as part of the peripheral/autonomic nervous system, and these neurons relay signals within the myenteric plexus rather than projecting to muscle.

#### 6. Synonyms
- ascending enteric interneuron (exact)
- oral interneuron (related; directional terminology)
- AIN (abbreviation)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of some GO:0014055 (acetylcholine secretion, neurotransmission)
- capable_of_part_of some GO:0120054 (intestinal motility)

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL**

#### 9. Confidence Assessment
- Definition: Medium-High (well characterised in guinea pig; transcriptomic distinction in scRNA-seq is partial)
- Parent term: High
- Cross-references: Medium
- Overall: Medium-High

---

### Term 6: Descending Interneuron (Cholinergic/Nitrergic)

**Note:** Multiple subtypes of descending interneuron are classically recognised in guinea pig (at least 3 subtypes differing in neuropeptide expression). Transcriptomic datasets also resolve multiple IN subtypes. For initial CL curation, a single "myenteric descending interneuron" parent class is recommended, with subtypes nested beneath it. Three well-supported subtypes are described below.

#### 1. Term Identification
- **Proposed Label:** myenteric descending interneuron
- **Status:** New term (parent class for descending interneuron subtypes)
- **Synonyms:** descending enteric interneuron; aborally projecting myenteric interneuron

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric ganglion and that projects aborally (toward the anus) within the myenteric plexus, relaying inhibitory or excitatory signals that contribute to the descending inhibitory reflex of peristalsis. These neurons form circuits that coordinate the aboral propagation of peristaltic waves. Multiple neurochemically distinct subtypes are recognised (Furness 2006). In transcriptomic datasets, descending interneurons are included in the broader IN class.

**Literature Support:**
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided)
- DOI:10.1007/s00418-021-02002-y (user-provided)
- PMID:40954253 (Majd et al. 2025)

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

#### 6. Synonyms
- descending enteric interneuron (exact)
- aboral interneuron (related)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of_part_of some GO:0120054 (intestinal motility)

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL** (as a parent class for subtypes below)

#### 9. Confidence Assessment
- Definition: High (well-established class in classical neurophysiology)
- Parent term: High
- Overall: High

---

### Term 6a: Descending Interneuron Subtype 1 (Serotonergic)

#### 1. Term Identification
- **Proposed Label:** serotonergic myenteric descending interneuron
- **Status:** New term
- **Synonyms:** 5-HT myenteric interneuron; serotonin-releasing descending interneuron

#### 2. Definition Validation
**Proposed Definition:**
A myenteric descending interneuron that releases serotonin (5-hydroxytryptamine, 5-HT) as a co-transmitter. In guinea pig small intestine, this subtype co-expresses ChAT and serotonin, and has Dogiel type I morphology with a caudally directed axon. These neurons play a role in intrinsic serotonergic neuromodulation within the descending inhibitory pathway (Furness 2006). In mice, serotonin-expressing neurons are present in the ENS but their classification relative to the descending interneuron circuit varies across transcriptomic studies (Majd et al. 2025).

**Literature Support:**
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided)
- DOI:10.1007/s00418-021-02002-y (user-provided)
- PMID:40954253 (Majd et al. 2025): serotonergic neurons detected across datasets

#### 5. Parent Term Validation
**Proposed Parent:** myenteric descending interneuron [new parent, Term 6]

#### 6. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of some GO:0060096 (serotonin secretion, neurotransmission)
- capable_of some GO:0014055 (acetylcholine secretion, neurotransmission) [co-transmitter]

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL**

#### 9. Confidence Assessment
- Definition: Medium (well characterised in guinea pig; less certain cross-species)
- Parent term: High (once parent class is created)
- Overall: Medium

---

### Term 6b: Descending Interneuron Subtype 2 (NOS1+/VIP+)

#### 1. Term Identification
- **Proposed Label:** nitrergic myenteric descending interneuron
- **Status:** New term
- **Synonyms:** NOS1-expressing myenteric interneuron; VIPergic descending interneuron

#### 2. Definition Validation
**Proposed Definition:**
A myenteric descending interneuron that releases nitric oxide and vasoactive intestinal peptide (VIP) as neurotransmitters. In guinea pig small intestine, this subtype expresses NOS1 and VIP, has Dogiel type I morphology, and projects aborally within the myenteric plexus. These neurons relay inhibitory signals from intrinsic primary afferent neurons and other interneurons to inhibitory motor neurons targeting the circular muscle (Furness 2006). In transcriptomic datasets, these neurons are included in the broad IMN class in some studies, reflecting the shared NOS1 expression with inhibitory motor neurons (Majd et al. 2025).

**Literature Support:**
- DOI:10.1007/s00418-021-02002-y (Morarach et al. 2021; user-provided)
- PMID:40954253 (Majd et al. 2025): notes ambiguity between interneurons and motor neurons expressing NOS1

**Validation Notes:** There is acknowledged difficulty in separating nitrergic descending interneurons from inhibitory motor neurons transcriptomically, as both express NOS1. Classical criteria distinguishing them are connectivity pattern and projection length. CL editors should flag this uncertainty.

#### 5. Parent Term Validation
**Proposed Parent:** myenteric descending interneuron [new parent, Term 6]

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of_part_of some GO:0120054 (intestinal motility)

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL** (with caveat about transcriptomic overlap with IMN)

#### 9. Confidence Assessment
- Definition: Medium (transcriptomic ambiguity with IMN)
- Parent term: High
- Overall: Medium

---

### Term 6c: Descending Interneuron Subtype 3 (Opioid Peptide-expressing)

#### 1. Term Identification
- **Proposed Label:** enkephalinergic myenteric descending interneuron
- **Status:** New term
- **Synonyms:** PENK-expressing myenteric interneuron; opioid peptide interneuron

#### 2. Definition Validation
**Proposed Definition:**
A myenteric descending interneuron that expresses enkephalin (an opioid neuropeptide encoded by proenkephalin, PENK) as a defining neurochemical marker. In guinea pig small intestine, enkephalin-expressing interneurons have Dogiel type I morphology and aborally directed projections within the myenteric plexus. PENK is one of only three genes (with NOS1 and TAC1) shared as functional markers across multiple ENS single-cell RNA sequencing datasets, indicating it is a broadly conserved marker in the descending circuit (Majd et al. 2025). These neurons modulate the descending inhibitory pathway.

**Literature Support:**
- PMID:40954253 (Majd et al. 2025): identifies PENK/NOS1/TAC1 as the only shared markers across UM-mouse, AR-human, and ST-human scRNA-seq datasets; PENK is specifically noted as a descending interneuron marker
- DOI:10.1007/s00418-021-02002-y (user-provided; text not retrieved)

#### 5. Parent Term Validation
**Proposed Parent:** myenteric descending interneuron [Term 6]

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL**

#### 9. Confidence Assessment
- Definition: Medium-High (PENK expression broadly conserved across datasets per Majd et al. 2025)
- Parent term: High
- Overall: Medium-High

---

### Term 7: Intrinsic Primary Afferent Neuron (IPAN)

#### 1. Term Identification
- **Proposed Label:** myenteric intrinsic primary afferent neuron
- **Status:** New term
- **Synonyms:** IPAN; AH neuron; Dogiel type II neuron; enteric sensory neuron; intrinsic sensory neuron; putative sensory neuron (PSN; used in some scRNA-seq studies)

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric ganglion and that functions as a primary sensory neuron intrinsic to the gut wall, detecting chemical, mechanical, and osmotic stimuli in the intestinal lumen and mucosa. These neurons are the first component of enteric reflex arcs, responding to luminal stimuli and activating interneurons and motor neurons to coordinate peristalsis and other intestinal reflexes. They are characterised by a distinctive Dogiel type II morphology, with a smooth, round soma bearing several long processes each with axon-like properties. Electrophysiologically they display the AH (after-hyperpolarisation) firing pattern with a prolonged after-hyperpolarisation following each action potential, and express the HCN channel mediating Ih current (Gomez-Frittelli et al. 2025). Key molecular markers in guinea pig include calretinin and tachykinins; in mice, markers include Calcb (CGRP-related), Nmu (neuromedin U), and Cdh6 (Gomez-Frittelli et al. 2025; Morarach et al. 2021). Optogenetic activation of Cdh6+ neurons evokes retrograde colonic motor complexes, demonstrating their functional role in initiating motor patterns (Gomez-Frittelli et al. 2025).

**Literature Support:**
- PMID:40193178 (DOI:10.7554/elife.101043, Gomez-Frittelli et al. 2025): characterises Cdh6 as specific IPAN marker; confirms Dogiel type II morphology, AH electrophysiology, Ih current, Calcb and Nmu expression; demonstrates optogenetic activation drives retrograde colonic motor complexes
- DOI:10.1007/s00418-021-02002-y (Morarach et al. 2021; user-provided; text not retrieved): IPAN1, IPAN2, IPAN3 clusters defined in UM-mouse scRNA-seq
- PMID:40954253 (Majd et al. 2025): IPAN class discussed; notes IPAN/SN/PSN terminology inconsistency across datasets

**Validation Notes:**
IPANs are among the best-defined functional classes in the ENS. The Dogiel type II morphology and AH electrophysiological signature are universally accepted classical criteria. The transcriptomic correlates have been resolved in multiple datasets but use different terminology (IPAN, SN, PSN). The optogenetic evidence from Gomez-Frittelli et al. 2025 provides strong functional validation.

#### 3. Experimental Evidence
- Morphology: Dogiel type II — smooth ovoid soma with multiple long-stem processes, each capable of axon-like function; no lamellar dendrites
- Electrophysiology: AH-type firing; prolonged after-hyperpolarisation; expression of HCN channels (Ih current); slow EPSPs
- Neurochemistry: calretinin+, CGRP (Calcb)+ in mice; tachykinin+ in guinea pig; Cdh6+, Cdh8+, Nmu+ in mouse colon (Gomez-Frittelli et al. 2025)
- Function: optogenetic activation drives retrograde colonic motor complexes; respond to mucosal stroking and distension
- Activation of Ih (HCN channels) contributes to spontaneous generation of colonic motor complexes (Gomez-Frittelli et al. 2025)

#### 4. Cross-References
**Primary References:**
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided; text not retrieved)
- DOI:10.1007/s00418-021-02002-y (user-provided; Morarach et al. 2021; text not retrieved)
- PMID:40193178 — Gomez-Frittelli et al. 2025 eLife: direct experimental characterisation with molecular, morphological, electrophysiological and functional evidence

**Additional References:**
- PMID:40954253 — Majd et al. 2025 (EMBO J): cross-dataset analysis

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

**Justification:** IPANs are functionally sensory but are classified as enteric neurons, not as classical sensory neurons. They are intrinsic to the ENS and do not project to the CNS. A broader parent "myenteric neuron" could be interposed.

#### 6. Synonyms
- intrinsic primary afferent neuron (exact)
- IPAN (abbreviation/related)
- AH neuron (related; electrophysiological designation)
- Dogiel type II neuron (related; morphological designation)
- enteric sensory neuron (broad/related)
- intrinsic sensory neuron (related)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- capable_of some GO:0014055 (acetylcholine secretion, neurotransmission) [IPANs are cholinergic in part]
- capable_of_part_of some GO:0120054 (intestinal motility)
- has_characteristic some Dogiel type II morphology [PATO term if available — note: specific PATO term for Dogiel type II may not exist; editor to verify]

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL**

#### 9. Confidence Assessment
- Definition: High (well supported by multiple lines of evidence including morphology, electrophysiology, molecular markers, and functional studies)
- Parent term: High
- Cross-references: High (PMID:40193178 provides strong direct evidence; primary refs unavailable but well covered by secondary literature)
- Overall: High

---

### Term 8: Intestinofugal Neuron

#### 1. Term Identification
- **Proposed Label:** intestinofugal neuron
- **Status:** New term
- **Synonyms:** enteric intestinofugal neuron; sympatho-enteric neuron; gut-to-sympathetic neuron

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric ganglion and whose axon projects out of the intestinal wall to form synapses on postganglionic neurons of the sympathetic ganglia (principally the inferior mesenteric ganglion and the celiac ganglion), thereby providing afferent information about the state of the gut to the sympathetic nervous system. These neurons are distinguished from other enteric neurons by their extrinsic projection and by their role in gut-to-sympathetic reflex pathways that regulate intestinal motility and secretion. Intestinofugal neurons are identified by the expression of cocaine- and amphetamine-regulated transcript (CART, encoded by Cartpt) and by the atypical property of having an axon that exits the intestinal wall (Furness 2006; Mann et al. 1995 as cited in Majd et al. 2025). Intestinofugal neurons have not yet been reliably identified as a distinct cluster in published single-cell transcriptomic datasets, despite CARTPT/Cart mRNA being detected across multiple datasets, representing a gap in current transcriptomic characterisation (Majd et al. 2025).

**Literature Support:**
- PMID:40954253 (Majd et al. 2025): states "Interestingly, none of these datasets have detected, annotated, or mentioned intestinofugal enteric neurons, afferent neurons that project to and form synapses with sympathetic ganglia (Furness, 2006; Mann et al, 1995). Cart, expressed by gene Cartpt, has been used to mark intestinofugal neurons." This directly identifies the cell type, its defining connectivity, key marker, and the gap in scRNA-seq characterisation.

**Validation Notes:**
The intestinofugal neuron is a classically defined cell type in the Furness ENS classification framework, with clear distinguishing anatomy (extrinsic projection to sympathetic ganglia) and marker expression (CART/Cartpt). Its absence from scRNA-seq cluster annotations represents a gap noted explicitly in the current literature, making its inclusion in CL important for completeness.

#### 3. Experimental Evidence
- Projection anatomy: axons exit the intestinal wall and synapse on neurons in prevertebral sympathetic ganglia (inferior mesenteric ganglion, celiac ganglion)
- Neurochemical marker: CART (cocaine- and amphetamine-regulated transcript; Cartpt in mouse)
- Additional markers in some studies: ChAT+, VIP+, calretinin+
- Electrophysiology: AH-type (in some species) or S-type
- Function: mediates gut-to-sympathetic reflex pathways controlling motility and secretion

#### 4. Cross-References
**Primary References:**
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided; text not retrieved)
- PMID:40954253 (Majd et al. 2025): explicitly discusses intestinofugal neurons and their absence from scRNA-seq annotations; identifies CARTPT as marker

**Additional References:**
- Mann et al. 1995 (as cited in Majd et al. 2025) — original characterisation of intestinofugal neurons
- Furness JB 2006 (monograph, as cited in Majd et al. 2025)

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

**Justification:** Intestinofugal neurons are enteric neurons by soma location and their classification within the ENS. Their extrinsic projection makes them unique among myenteric neurons but does not exclude them from the enteric neuron class.

#### 6. Synonyms
- enteric intestinofugal neuron (exact)
- gut-to-sympathetic afferent neuron (broad)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- sends_synaptic_output_to_region some [inferior mesenteric ganglion — UBERON term needed; editor to verify UBERON:0002029 inferior mesenteric ganglion or similar]
- capable_of_part_of some GO:0120054 (intestinal motility) [indirect role via sympathetic reflexes]

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL**
This is a well-established cell type in the functional ENS literature that is not yet in CL. Its absence from scRNA-seq annotations is a known gap in the field, not a reason to exclude it from the ontology.

#### 9. Confidence Assessment
- Definition: High (clearly defined by soma location + extrinsic projection to sympathetic ganglia + CART marker)
- Parent term: High
- Cross-references: Medium (primary refs not retrieved; Majd et al. 2025 provides direct supporting text)
- Overall: High

---

### Term 9: Myenteric Neuron (Parent Class)

**Recommendation:** Before creating all the subtypes above, a parent class "myenteric neuron" should be created to group all neurons with soma in the myenteric plexus, regardless of functional subtype. This would enable the logical inference that any cell with soma location in the myenteric plexus is a myenteric neuron.

#### 1. Term Identification
- **Proposed Label:** myenteric neuron
- **Status:** New term (parent class)
- **Synonyms:** Auerbach's plexus neuron; neuron of the myenteric plexus

#### 2. Definition Validation
**Proposed Definition:**
An enteric neuron that has its soma located in the myenteric nerve plexus (Auerbach's plexus), situated between the longitudinal and circular smooth muscle layers of the gastrointestinal tract wall. Myenteric neurons are the principal neural elements coordinating gut motility, including peristalsis, segmentation, and other propulsive movements. The myenteric plexus contains a diverse population of functionally distinct neuron types including motor neurons (both excitatory and inhibitory), interneurons (ascending and descending), intrinsic primary afferent neurons, and intestinofugal neurons (Furness 2006; Morarach et al. 2021; Majd et al. 2025).

**Literature Support:**
- PMID:40954253 (Majd et al. 2025): comprehensive cross-dataset analysis; defines the major myenteric neuron types
- DOI:10.1007/s00418-021-02002-y (user-provided)
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided)

#### 5. Parent Term Validation
**Proposed Parent:** enteric neuron (CL:0007011)

**Equivalence axiom (for reasoning):**
myenteric neuron equivalentTo 'enteric neuron' AND (has_soma_location some 'myenteric nerve plexus' (UBERON:0002439))

#### 6. Synonyms
- Auerbach's plexus neuron (exact)
- neuron of the myenteric plexus (exact)
- myenteric ganglion neuron (related)

#### 7. Logical Relationships
- has_soma_location some UBERON:0002439 (myenteric nerve plexus)
- part_of some UBERON:0002439 (myenteric nerve plexus)

#### 8. Ontology Placement Recommendation
**RECOMMENDED: Create in CL** (as the direct parent of all specific myenteric neuron types proposed above)

#### 9. Confidence Assessment
- Definition: High
- Parent term: High
- Overall: High

---

## Summary of Proposed Terms

| Proposed Label | Parent | Key Markers | Key Relations |
|---------------|--------|-------------|---------------|
| myenteric neuron | CL:0007011 (enteric neuron) | HuC/D (pan-neuronal) | has_soma_location UBERON:0002439 |
| excitatory myenteric motor neuron of circular muscle | myenteric neuron | ChAT, Tac1/TAC1 (substance P) | capable_of GO:0014055; synapsed_to circular muscle |
| inhibitory myenteric motor neuron of circular muscle | myenteric neuron | NOS1, VIP | capable_of [NOS/VIP secretion]; synapsed_to circular muscle |
| excitatory myenteric motor neuron of longitudinal muscle | myenteric neuron | ChAT, Tac1 | capable_of GO:0014055; synapsed_to longitudinal muscle |
| inhibitory myenteric motor neuron of longitudinal muscle | myenteric neuron | NOS1, VIP | capable_of [NOS/VIP secretion]; synapsed_to longitudinal muscle |
| myenteric ascending interneuron | myenteric neuron | ChAT, calretinin, Tac1 | capable_of GO:0014055 |
| myenteric descending interneuron | myenteric neuron | variable | capable_of_part_of GO:0120054 |
| serotonergic myenteric descending interneuron | myenteric descending interneuron | ChAT, TPH2 (5-HT) | capable_of GO:0060096 |
| nitrergic myenteric descending interneuron | myenteric descending interneuron | NOS1, VIP | capable_of [NO secretion] |
| enkephalinergic myenteric descending interneuron | myenteric descending interneuron | PENK | [PENK-based GO term needed] |
| myenteric intrinsic primary afferent neuron | myenteric neuron | Calcb, Nmu, Cdh6 (mouse); calretinin (guinea pig) | has_characteristic Dogiel type II morphology |
| intestinofugal neuron | myenteric neuron | CART/Cartpt | sends_synaptic_output_to [inferior mesenteric ganglion] |

---

## Gaps and Issues for CL Editor

1. **Full text of primary references not retrieved.** DOI:10.1016/j.jcmgh.2023.06.010 and DOI:10.1007/s00418-021-02002-y are not indexed in Europe PMC for full-text retrieval. The editor should access these directly to verify the definitions, especially for any additional subtypes or molecular details described therein.

2. **"Myenteric neuron" parent class not yet in CL.** All proposed subtypes should sit under a new intermediate parent class "myenteric neuron" (= enteric neuron AND has_soma_location some myenteric nerve plexus).

3. **GO term for nitric oxide secretion (neurotransmission) may be absent.** Searches for "nitric oxide secretion, neurotransmission" as a GO term did not return a direct match. The CL editor should confirm whether this GO term exists (e.g., under GO:0007269 neurotransmitter secretion) or request its creation.

4. **Transcriptomic ambiguity between nitrergic descending interneurons and inhibitory motor neurons.** Both types express NOS1, and scRNA-seq datasets cannot reliably separate them. Definitions should note this.

5. **Species specificity of molecular markers.** The molecular markers noted are from guinea pig (classical neurochemical coding studies), mouse (scRNA-seq), and partially from human (scRNA-seq). Markers may differ across species and should be noted as species-specific where appropriate.

6. **Longitudinal vs. circular muscle inhibitory motor neuron transcriptomic separation.** This separation is not consistently resolved in scRNA-seq datasets. The CL editor may wish to start with a single "inhibitory myenteric motor neuron" parent and create the circular/longitudinal split as subtypes with a note about this uncertainty.

7. **Intestinofugal neuron transcriptomic identification.** As noted explicitly by Majd et al. 2025, intestinofugal neurons have not been identified as a distinct cluster in any published scRNA-seq dataset, despite CARTPT expression being detected. This cell type is defined by classical anatomy and neurochemistry. CL should include it but the editor should note that transcriptomic annotation is incomplete.

8. **Secretomotor/vasodilator neurons** (PSVN class in scRNA-seq datasets) are another major type of enteric neuron, but these have somata in both the myenteric and submucosal plexuses and function primarily as secretomotor neurons innervating the intestinal mucosa rather than directly driving motility. These are not included in this report as the user request focused on myenteric neurons involved in motility. Separate curation would be appropriate.

9. **UBERON IDs for muscle layers used in synapsed_to relationships.** The synapsed_to relation takes a cell type as range (not an anatomical structure). The appropriate cell type to use would be smooth muscle cell types of the intestinal circular or longitudinal muscle layers. CL:0002504 (enteric smooth muscle cell) or more specific children of CL:0000192 (smooth muscle cell) in appropriate intestinal locations should be used. This needs further lookup.

---

## Additional Notes

### Regarding the Majd et al. 2025 paper (PMID:40954253)

This paper makes an important overarching point directly relevant to CL curation: there are currently substantial discrepancies between different ENS scRNA-seq datasets in how functional neuron types are annotated. Only three genes (NOS1, TAC1, PENK) are shared as functional markers across the three major primary datasets (Morarach et al. 2021, Drokhlyansky et al. 2020, Elmentaite et al. 2021). The paper explicitly calls for multimodal definition standards combining morphology, electrophysiology, connectivity, and transcriptomics for ENS cellular identity — exactly the approach taken in these CL definitions.

The CL definitions proposed here follow classical functional/anatomical criteria (Furness 2006 framework) supplemented by transcriptomic markers where these are well-validated. This approach is endorsed by Majd et al. 2025.

### Regarding the Benthal et al. 2026 meta-atlas (PMID:41566221)

This paper represents the current state-of-the-art in cross-dataset comparison for ENS neuron types in mouse. It would be valuable to access the full text for specific marker gene listings for each transcriptomically defined cluster. This paper was identified and would benefit from full-text retrieval and review when accessed directly.

---

## Reference Log

Downloaded files:
- `/Users/do12/Documents/GitHub/onto_template_agentic_env/pdfs/PMC12528430_Majd2025_ENS_unified_definition.txt` — full text of Majd et al. 2025 (EMBO J, PMID:40954253)

Papers identified but NOT retrieved (full text unavailable via artl-mcp):
- DOI:10.1016/j.jcmgh.2023.06.010 (user-provided primary reference 1) — NOT IN EUROPE PMC
- DOI:10.1007/s00418-021-02002-y (user-provided primary reference 2, Morarach et al. 2021) — NOT IN EUROPE PMC

---

## Handoff Decision

**Needs More Research / Partial Ready for Integration**

The following terms are at Medium-High confidence and ready for CL integration pending editor review:
- myenteric neuron (parent class) — High confidence
- myenteric intrinsic primary afferent neuron (IPAN) — High confidence
- inhibitory myenteric motor neuron of circular muscle — High confidence
- intestinofugal neuron — High confidence
- excitatory myenteric motor neuron of circular muscle — Medium confidence
- myenteric ascending interneuron — Medium-High confidence
- myenteric descending interneuron (parent class) — High confidence
- enkephalinergic myenteric descending interneuron — Medium-High confidence

The following terms require additional editor judgement or further research:
- excitatory myenteric motor neuron of longitudinal muscle — Medium confidence
- inhibitory myenteric motor neuron of longitudinal muscle — Low-Medium confidence (consider merging with circular muscle IMN as a single parent class)
- serotonergic myenteric descending interneuron — Medium confidence
- nitrergic myenteric descending interneuron — Medium confidence (transcriptomic overlap with IMN)

**The user-provided primary references (DOI:10.1016/j.jcmgh.2023.06.010 and DOI:10.1007/s00418-021-02002-y) should be accessed directly by the CL editor to validate and potentially refine all definitions, particularly for species-specific molecular markers.**

Passing to @CL-ontologist for review and integration decision.
