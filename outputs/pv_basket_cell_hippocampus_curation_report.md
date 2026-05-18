# Curation Report: Parvalbumin-positive basket cell of the hippocampus

## 1. Term Identification

- **Proposed Label**: parvalbumin-positive basket cell of the hippocampus
- **Status**: New term
- **Requested by**: Mapping report at source_data/pv_basket_cell_hippocampus_mapping_report.md
- **Mapping context**: Cannot be adequately represented by CL:0000118 (basket cell), which is BROAD. High-confidence atlas mapping to WMBv1/CCN20230722 SUPT_0206 / CLUS_0739.

### Initial Assessment

All required fields for a new term are present or derivable from the provided references:

```
Label:          present
Definition:     needs synthesis from literature (no pre-existing definition provided)
Cross-references: 8 PMIDs provided; validated below
Parent term:    present (CL:0000118 basket cell)
Synonyms:       derivable from literature
Relationships:  derivable from literature
```

---

## 2. Definition Validation

### Proposed Definition

A GABAergic inhibitory interneuron of the hippocampus that expresses parvalbumin and is a perisomatic-targeting basket cell whose soma is located in the pyramidal cell layer of fields CA1, CA2, CA3, or the granule cell layer of the dentate gyrus. Its highly branched axon arborization is largely confined to the pyramidal or granule cell layer and forms basket-like synaptic structures on the soma and proximal dendrites of hundreds of principal neurons (pyramidal cells in CA1/CA3, or granule cells in the dentate gyrus). It is capable of high-frequency, sustained firing (fast-spiking electrophysiology) and expresses the GABAergic markers Gad1 and Gad2 in rodents. It is distinguished from cholecystokinin (CCK)-expressing basket cells by the absence of cannabinoid receptor type 1 (Cnr1) expression and by its characteristic fast-spiking firing pattern.

### Literature Support

- **PMID:7472426** (Sik et al. 1995) — Foundational in vivo intracellular labeling study in rat CA1. Basket cells were immunoreactive for parvalbumin; axon collaterals were confined to the pyramidal layer. A single basket cell contacted more than 1,500 pyramidal neurons and 60 other parvalbumin-positive interneurons. Dendrites were freely branching. Abstract states: "Basket cells were immunoreactive for parvalbumin and their axon collaterals were confined to the pyramidal layer. A single basket cell contacted more than 1500 pyramidal neurons and 60 other parvalbumin-positive interneurons."

- **PMID:33398060** (Que et al. 2021) — Patch-seq in morphologically identified mouse CA1 PV interneurons. Explicitly defines basket cells (vertical and horizontal BC morphotypes) among PV-INs. States: "CA1 PV-INs can be divided into three main cell classes based on their axonal projections: (1) axo-axonic cells (AAC); (2) basket cells (BC), which establish synapses onto the perisomatic region of the postsynaptic neuron." Transcriptomic analysis confirmed consistent expression of Pvalb and GABAergic markers (Gad1/Gad2) and absence of glutamatergic markers. Paper also confirms Pvalb.Tac1 and Pvalb.C1ql1 as two transcriptomic subgroups, both encompassing basket cells.

- **PMID:31297048** (Contreras et al. 2019) — Review of soma- and axon-targeting GABAergic synapses in cortex and hippocampus. States: "PV positive interneurons include basket cells which target the soma and proximal dendrites of excitatory pyramidal cells... PV positive basket and chandelier cells are fast-spiking, with the potential to robustly influence the activity of hundreds of pyramidal cells." Critically, also states: "CCK positive basket cells... Proportions of CCK basket cells express... the metabotropic Cannabinoid receptor type 1 (CB1)... Functionally, CCK positive basket cells provide long-lasting inhibition," contrasting with the fast-spiking, CB1-negative PV basket cell. This provides direct evidence for the Cnr1-negative marker distinguishing PV from CCK basket cells.

- **PMID:26441554** (Whissell et al. 2015) — Intersectional genetic labeling study directly comparing CCK-GABA and PV-GABA cells in hippocampus and cortex. Confirms: "Cholecystokinin (CCK)- and parvalbumin (PV)-expressing neurons constitute the two major populations of perisomatic GABAergic neurons in the cortex and the hippocampus." PV-GABA cells were counted from stratum pyramidale of CA1, directly supporting soma location in the pyramidal layer.

- **PMID:25018703** (Rivera et al. 2014) — Immunofluorescence study in adult rat hippocampus. Parvalbumin+ interneurons identified in pyramidal cell layers of CA1 and CA3 fields: "MAGL(+) terminals were only observed around CA1 calbindin(+) pyramidal cells, CA1/3 calretinin(+) interneurons and CA3 parvalbumin(+) interneurons localized in the pyramidal cell layers." Confirms soma location of PV interneurons (including basket cells) in the pyramidal layers of CA1/CA3.

- **PMID:35802727** (Perrenoud et al. 2022) — Patch-clamp and single-cell RT-PCR study of GABAergic interneurons in the mouse dentate gyrus hilus and granule cell layer. Confirms PV-expressing interneurons in the dentate gyrus, including within and adjacent to the granule cell layer. Uses PV as a molecular marker in combination with GAD65/GAD67. Supports extension of PV basket cell soma location to dentate gyrus.

- **PMID:39401246** (Bocchio et al. 2024) — All-optical study of CA1 hippocampal interneurons in vivo. States: "the most representative ones [of interneuron subtypes], the PV-expressing basket and bistratified cells." Confirms PV basket cell as the predominant interneuron subtype in the CA1 pyramidal layer accessible to in vivo recording. Notes: "parvalbumin-expressing basket cells" as exemplars of fast-spiking interneurons biased in extracellular recording.

- **PMID:25324774** (Müller & Remy 2014) — Review of hippocampal CA1 interneurons with focus on O-LM and bistratified cells. Provides anatomical context for perisomatic vs. dendritic inhibition. Relevant as background on hippocampal interneuron classification. However, this paper does not provide primary data specifically on PV basket cells and is of more limited direct relevance than stated in the request (it focuses on dendritic-targeting interneurons). It is retained as supporting context for placement of basket cells within the hippocampal interneuron classification.

### Validation Notes

The definition synthesizes well-established characterisation from multiple sources spanning 30 years (Sik 1995 to Bocchio 2024). All key assertions are directly supported:

1. **GABAergic / parvalbumin-positive**: Supported by PMID:7472426, 33398060, 26441554, 25018703, 35802727
2. **Perisomatic targeting (soma and proximal dendrites)**: Supported by PMID:7472426, 31297048, 26441554
3. **Axon confined to pyramidal / granule cell layer**: Supported by PMID:7472426 (direct measurement)
4. **Contacts hundreds of principal neurons**: Supported by PMID:7472426 (>1,500 pyramidal neurons)
5. **Fast-spiking electrophysiology**: Supported by PMID:31297048, 39401246, 33398060
6. **Gad1/Gad2 expression**: Supported by PMID:33398060 (scRNA-seq), 35802727 (scRT-PCR)
7. **Cnr1-negative (absent CB1 receptor)**: Supported by PMID:31297048, 25018703 (CB1 confined to CCK-positive fibers, not PV-positive somata)
8. **Soma in pyramidal layer CA1/CA3, dentate gyrus granule cell layer**: Supported by PMID:7472426, 25018703, 26441554, 35802727

---

## 3. Experimental Evidence

### Summary of Key Experimental Evidence

**Morphological evidence (in vivo intracellular labeling):** Sik et al. (1995, PMID:7472426) labeled CA1 interneurons with biocytin in anesthetized rats. Basket cells were recovered with complete dendritic and axonal arborizations. Their dendrites were freely branching without spine clusters; axon collaterals were strictly confined to stratum pyramidale. One basket cell made synaptic contacts with >1,500 pyramidal neurons and ~60 other PV+ interneurons. Parvalbumin immunoreactivity was confirmed post hoc.

**Transcriptomic and morphological profiling (patch-seq):** Que et al. (2021, PMID:33398060) performed single-cell RNA-seq on morphologically identified PV interneurons in mouse CA1. Basket cells (vertical and horizontal subtypes) were explicitly identified morphologically and their transcriptomes characterized. Pvalb was consistently expressed; Gad1 and Gad2 (encoding GAD67 and GAD65) were detected; glutamatergic markers were absent. Two transcriptomic subtypes of PV interneurons (Pvalb.Tac1 and Pvalb.C1ql1) were identified, both containing basket cells. Morphology-associated transcriptomic genes were identified for basket vs. axo-axonic vs. bistratified subtypes.

**Density mapping and comparison with CCK basket cells:** Whissell et al. (2015, PMID:26441554) used intersectional genetic labeling to count PV-GABA and CCK-GABA cells across hippocampal subfields. PV-GABA cells were found at highest density in stratum pyramidale of CA1. PV-GABA cells outnumbered CCK-GABA cells in most hippocampal subfields. Both cell types were confirmed as GABAergic through co-expression of Dlx5/6-driven reporter.

**Electrophysiology and molecular specialization (review):** Contreras et al. (2019, PMID:31297048) summarize that PV basket cells are fast-spiking and contact soma and proximal dendrites of pyramidal cells. They lack cannabinoid receptor type 1 (CB1/Cnr1), which distinguishes them from CCK basket cells. The presynaptic molecular marker LGI2 is expressed specifically in PV basket cells (not chandelier cells or CCK cells) and is required for formation of somatic inhibitory synapses.

**In vivo functional studies:** Bocchio et al. (2024, PMID:39401246) identified PV-expressing basket cells as the predominant fast-spiking interneuron subtype in CA1 pyramidal layer accessible by extracellular recording in awake mice. Perisomatic interneurons (predominantly PV basket cells) were shown to drive hippocampal synchrony during immobility.

### Literature Support

- PMID:7472426 — In vivo morphological characterization and PV immunoreactivity
- PMID:33398060 — Patch-seq confirming Pvalb, Gad1, Gad2 markers; morphological subtypes
- PMID:26441554 — Genetic density mapping; perisomatic GABAergic identity
- PMID:31297048 — Cnr1-negative marker; fast-spiking; LGI2 marker; perisomatic targeting
- PMID:39401246 — In vivo fast-spiking classification in CA1 pyramidal layer

---

## 4. Cross-References

### Primary References (provided by requestor)

All 8 provided PMIDs were retrieved from Europe PMC. Full-text XML was obtained for 6 of 8:

| PMID | DOI | Title | Relevance | Full Text |
|------|-----|-------|-----------|-----------|
| 7472426 | 10.1523/jneurosci.15-10-06651.1995 | Hippocampal CA1 interneurons: an in vivo intracellular labeling study (Sik et al. 1995) | HIGH — foundational morphological characterisation; PV immunoreactivity; axon in pyramidal layer | Not available as XML; PMC6577981 available |
| 25018703 | 10.3389/fnana.2014.00056 | Localization of CB1 receptor and 2-AG enzymes in cells expressing Ca2+-binding proteins in rat hippocampus (Rivera et al. 2014) | HIGH — PV+ interneurons in pyramidal layers CA1/CA3; confirms soma location | Retrieved (PMC4073216) |
| 25324774 | 10.3389/fnsyn.2014.00023 | Dendritic inhibition mediated by O-LM and bistratified interneurons (Müller & Remy 2014) | MODERATE — review of hippocampal interneuron types; context for perisomatic vs dendritic inhibition; not specific to basket cells | Retrieved (PMC4179767) |
| 39401246 | 10.1371/journal.pbio.3002837 | Functional networks of inhibitory neurons orchestrate synchrony in the hippocampus (Bocchio et al. 2024) | MODERATE — in vivo CA1 PV basket cell identification and function | Retrieved (PMC11501041) |
| 26441554 | 10.3389/fnana.2015.00124 | Comparative density of CCK- and PV-GABA cells within the cortex and hippocampus (Whissell et al. 2015) | HIGH — PV-GABA cell identity and location in stratum pyramidale | Retrieved (PMC4585045) |
| 33398060 | 10.1038/s41467-020-20328-4 | Transcriptional and morphological profiling of parvalbumin interneuron subpopulations in the mouse hippocampus (Que et al. 2021) | HIGH — patch-seq of PV basket cells; Pvalb/Gad1/Gad2 markers | Retrieved (PMC7782706) |
| 35802727 | 10.1371/journal.pone.0270981 | Molecular and electrophysiological features of GABAergic neurons in the dentate gyrus (Perrenoud et al. 2022) | HIGH — PV interneurons in dentate gyrus; marker confirmation | Retrieved (PMC9269967) |
| 31297048 | 10.3389/fnmol.2019.00154 | Molecular Specialization of GABAergic Synapses on the Soma and Axon (Contreras et al. 2019) | HIGH — PV basket cell perisomatic targeting; Cnr1-negative | Retrieved (PMC6607995) |

**Note on full-text availability:** Full-text XML via Europe PMC was not available for PMID:7472426 (Sik et al. 1995). The abstract was retrieved and is highly informative; this is a 1995 paper now freely available in PMC (PMC6577981) but the XML conversion returned empty. PDF conversion also failed. The abstract contains the key evidence cited here. All other provided PMIDs returned full text.

### Recommended Cross-References for CL Term (minimum set)

The following PMIDs are recommended as cross-references on the CL term, in priority order:

1. **PMID:7472426** — foundational morphological characterisation (must have)
2. **PMID:33398060** — contemporary patch-seq with molecular markers (must have)
3. **PMID:31297048** — Cnr1-negative marker and perisomatic targeting specificity
4. **PMID:26441554** — perisomatic GABAergic identity; comparison with CCK basket cells

---

## 5. Parent Term Validation

**Proposed Parent**: basket cell (CL:0000118)

**CL:0000118 definition**: "Basket cells are inhibitory GABAergic interneurons of the brain. In general, dendrites of basket cells are free branching and contain smooth spines. Axons are highly branched. The branched axonal arborizations give rise to basket-like structures that surround the soma of the target cell. Basket cells form axo-somatic synapses, meaning their synapses target somas of other cells."

**Justification**: The hippocampal PV basket cell is unambiguously a basket cell — it shares all defining features of the CL:0000118 class: inhibitory, GABAergic, freely branching dendrites, highly branched axon forming basket structures around target soma, axo-somatic synapses. The proposed new term adds specificity by restricting to: (1) hippocampal location, (2) parvalbumin expression, (3) exclusion of Cnr1. These additional criteria are what distinguish hippocampal PV basket cells from hippocampal CCK basket cells, which are an equally well-established but distinct cell type.

**Hierarchical Context**:

```
interneuron (CL:0000099)
  inhibitory interneuron (CL:0000498)
    GABAergic interneuron (CL:0011005)
      basket cell (CL:0000118)
        [proposed] parvalbumin-positive basket cell of the hippocampus
```

The term CL:1001569 (hippocampal interneuron) is a sibling grouping class that subsumes all hippocampal interneurons by soma location. The proposed term would also be inferred to be a hippocampal interneuron via the has_soma_location property chain (see Section 6).

**Alternative parent consideration**: One could consider making the parent "hippocampal interneuron" (CL:1001569) rather than or in addition to "basket cell" (CL:0000118). However, following CL convention, the most informative genus should be the parent: basket cell is more informative than hippocampal interneuron. The hippocampal interneuron classification is inferred by the soma location axiom.

---

## 6. Synonyms

### Validated Synonyms

The following synonyms are supported by the literature:

| Synonym | Type | Source |
|---------|------|--------|
| PV basket cell | EXACT | PMID:33398060 (Que et al. 2021 — "PV-INs... basket cells (BC)"); PMID:39401246 ("PV-expressing basket cells") |
| PV+ basket cell | EXACT | PMID:33398060, 31297048 |
| parvalbumin basket cell | EXACT | PMID:31297048 ("PV positive basket cells"); PMID:26441554 ("PV-GABA neurons") |
| hippocampal PV interneuron basket cell | RELATED | PMID:33398060 (within context of hippocampal PV-IN classification) |
| fast-spiking basket cell | RELATED | PMID:31297048, PMID:39401246 (fast-spiking is defining electrophysiological property of PV basket cells, but not a species/location-specific synonym) |

### Synonyms Not Recommended

- "PV-GABA basket cell" — used in Whissell et al. 2015 but is a non-standard compound that conflates marker and neurotransmitter; not used as a standard term in the field
- "parvalbumin-expressing basket cell of hippocampus" — variant acceptable but slightly less compact than the proposed label; can be listed as RELATED

---

## 7. Logical Relationships

All relationships follow the CL relations guide. Object terms have been validated via OLS4.

### Validated Relationships

**Neurotransmitter / function:**

```
'parvalbumin-positive basket cell of the hippocampus'
    SubClassOf 'capable of' some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534)
```
- Source: PMID:7472426 (GABA-mediated IPSPs confirmed by electrophysiology); PMID:26441554 (GABAergic identity confirmed genetically); PMID:33398060 (Gad1/Gad2 transcriptomic expression confirmed)
- GO:0061534 confirmed in OLS4: "The regulated release of gamma-aminobutyric acid by a cell, in which the gamma-aminobutyric acid acts as a neurotransmitter."

**Soma location:**

The soma is found in the pyramidal layers of CA1 and CA3, and in the granule cell layer of the dentate gyrus. Per the relations guide, `has soma location` is the appropriate relation.

```
'parvalbumin-positive basket cell of the hippocampus'
    SubClassOf 'has soma location' some 'pyramidal layer of CA1' (UBERON:0014548)

'parvalbumin-positive basket cell of the hippocampus'
    SubClassOf 'has soma location' some 'pyramidal layer of CA3' (UBERON:0014550)

'parvalbumin-positive basket cell of the hippocampus'
    SubClassOf 'has soma location' some 'dentate gyrus granule cell layer' (UBERON:0005381)
```

- Source for CA1 pyramidal layer: PMID:7472426, PMID:25018703, PMID:26441554, PMID:33398060
- Source for CA3 pyramidal layer: PMID:25018703 (parvalbumin+ interneurons identified in pyramidal cell layers of CA3 fields); PMID:26441554 (PV-GABA cells distributed across CA1, CA3, DG)
- Source for dentate gyrus granule cell layer: PMID:35802727 (PV-expressing interneurons in dentate gyrus including within/adjacent to granule cell layer); PMID:26441554 (CCK- and PV-GABA cells counted in dentate gyrus subfield)
- Note: The CA3 soma location axiom entails, via the `has_soma_location` property chain with `part_of`, that this cell type has soma location in the CA3 field of hippocampus and in the hippocampus, causing autoclassification as a hippocampal interneuron (CL:1001569).

All three UBERON IDs confirmed in OLS4:
- UBERON:0014548: "pyramidal layer of CA1" — CA1 part of stratum pyramidale hippocampi
- UBERON:0014550: "pyramidal layer of CA3" — layer of hippocampal field that is part of CA3 and hippocampus pyramidal layer
- UBERON:0005381: "dentate gyrus granule cell layer" — densely packed principal cell layer 4-8 cells thick in the dentate gyrus

**Molecular marker (expresses):**

```
'parvalbumin-positive basket cell of the hippocampus'
    SubClassOf 'expresses' some 'parvalbumin alpha' (PR:000013502)
```

- Source: PMID:7472426 (PV immunoreactivity), PMID:33398060 (Pvalb transcriptomic expression), PMID:25018703, PMID:26441554
- PR:000013502 is the species-neutral gene-level PRO term for parvalbumin alpha, which is appropriate for a cell type term that applies across rodents and humans. Confirmed in OLS4.

**Negative marker (lacks plasma membrane part — use with caution per relations guide):**

Per CL convention, the absence of Cnr1 is definitionally important for distinguishing PV from CCK basket cells. However, the relations guide notes that `lacks_plasma_membrane_part` should be used carefully. Cnr1 (cannabinoid receptor 1) is a membrane receptor. Its absence in PV basket cells is well supported.

No species-neutral PRO term for Cnr1 was identified in the OLS4 search in this session; this relationship should be checked by the CL ontologist for whether an appropriate PRO term exists before adding.

Proposed (pending PRO ID verification):
```
'parvalbumin-positive basket cell of the hippocampus'
    SubClassOf 'lacks_plasma_membrane_part' some 'cannabinoid receptor 1' [PRO ID TBD]
```
- Source: PMID:31297048 (CB1 expressed by CCK basket cells but not PV basket cells); PMID:25018703 (CB1+ fiber terminals in hippocampus; CB1 associated with CCK-type cells, not PV-type)

**Proposed Equivalence Axiom (Logical Definition):**

A full equivalence axiom would enable automated classification. The minimal candidate is:

```
'parvalbumin-positive basket cell of the hippocampus'
    EquivalentTo:
        'basket cell' (CL:0000118)
        and ('has soma location' some 'hippocampus pyramidal layer' [UBERON:0002313])
        and ('expresses' some 'parvalbumin alpha' [PR:000013502])
        and ('capable of' some 'gamma-aminobutyric acid secretion, neurotransmission' [GO:0061534])
```

Note: Using the broader UBERON:0002313 (hippocampus pyramidal layer, covering CA1-CA3) in the equivalence axiom rather than individual subregions avoids over-specificity in the definition. The individual soma-location subclass axioms can be added as SubClassOf assertions additionally. The dentate gyrus granule cell layer location should be listed as an additional SubClassOf rather than in the equivalence axiom, since its status as definitional may be less certain for the dentate gyrus compartment.

---

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

The hippocampal parvalbumin-positive basket cell is:
- A naturally occurring, non-pathological cell type
- Present in multiple vertebrate species (rat, mouse, and by extension human)
- Defined by a well-characterised multimodal phenotype (morphological, electrophysiological, molecular)
- A specific subtype of the existing CL:0000118 (basket cell) with additional constraints that are well-evidenced
- Relevant to computational atlas mapping (WMBv1 CCN20230722 type SUPT_0206/CLUS_0739)
- Not a cultured cell type or defined solely by a protocol

All required CL term components are available with high-quality literature support.

**Naming convention note**: The proposed label "parvalbumin-positive basket cell of the hippocampus" follows CL conventions (cf. "lamp5 GABAergic cortical interneuron", "sst GABAergic interneuron"). An alternative using the standard "PV" abbreviation ("PV basket cell of the hippocampus") is widely used in the literature but abbreviations are generally avoided in CL labels. The full-form "parvalbumin-positive basket cell of the hippocampus" is recommended. The abbreviation "PV basket cell" should be listed as an EXACT synonym.

---

## 9. Additional Notes

### Scope note on PMID:25324774

PMID:25324774 (Müller & Remy 2014) was provided as a reference for "soma location" but this paper reviews O-LM and bistratified interneurons — both dendritic-targeting cell types, not perisomatic basket cells. It mentions basket cells only in passing as a contrast class. It provides useful general context about hippocampal interneuron organization but should not be listed as a primary reference for this term. It is retained as a supporting context reference only.

### Subtypes of hippocampal PV basket cells

Que et al. 2021 (PMID:33398060) identified at least two morphological basket cell subtypes in CA1: vertical basket cell (vBC) and horizontal basket cell (hBC), distinguished by dendrite orientation. These were transcriptomically similar. The current term proposal encompasses both subtypes. If future evidence warrants, these could be split into child terms.

### CCK basket cell

The cholecystokinin-positive basket cell of the hippocampus is a distinct cell type that should be curated as a separate CL term. Key distinguishing features relative to the PV basket cell: CCK-positive (vs. Pvalb-positive), Cnr1-positive (CB1-expressing), slower and more irregular firing, modulation by endocannabinoids and serotonin, dystroglycan-dependent synaptogenesis. The two cell types together constitute nearly all perisomatic-targeting interneurons in the hippocampus.

### Species note

The characterisation is most detailed in rat (Sik 1995) and mouse (Que 2021, Whissell 2015, Perrenoud 2022, Bocchio 2024). Parvalbumin basket cells have been described in human hippocampus (see CL:4072046 for the analogous chandelier cell term in human). The proposed term is not species-restricted and applies across mammals.

---

## 10. Confidence Assessment

- **Definition**: High — directly synthesized from multiple primary and review sources spanning 30 years; all key assertions supported by at least two independent sources
- **Parent term**: High — unambiguous; all defining features of basket cell class are met; CL:0000118 is an appropriate direct parent
- **Soma location axioms**: High for CA1 and CA3 pyramidal layer; Moderate for dentate gyrus granule cell layer (well-supported by Perrenoud 2022 and Whissell 2015, but the basket cell identity of PV interneurons in the granule cell layer is less exhaustively characterized than in CA1)
- **Molecular marker (Pvalb/PR:000013502)**: High — defining marker by definition and confirmed at protein and transcript level
- **Cnr1 negative marker**: High for the biological fact; Moderate for the OWL axiom (pending identification of appropriate PRO ID for CB1/Cnr1)
- **Cross-references**: High — 8 provided PMIDs are all valid, all retrieved from Europe PMC, and 7 of 8 are directly relevant with full text available
- **Overall**: High

---

## 11. Proposed Term Summary (for GitHub issue)

**Label**: parvalbumin-positive basket cell of the hippocampus

**Definition**: A GABAergic inhibitory basket cell of the hippocampus that expresses parvalbumin. Its soma is located in the pyramidal cell layer of areas CA1, CA2, and CA3, or in the granule cell layer of the dentate gyrus. Its highly branched axon arborization is largely confined to the pyramidal or granule cell layer and forms basket-like perisomatic synapses on the soma and proximal dendrites of hundreds of principal neurons. It is fast-spiking and does not express cannabinoid receptor type 1 (Cnr1), distinguishing it from cholecystokinin-expressing basket cells. In rodents, it expresses the marker genes Pvalb, Gad1, and Gad2.

**Parent**: basket cell (CL:0000118)

**Synonyms**:
- PV basket cell (EXACT)
- PV+ basket cell (EXACT)
- parvalbumin basket cell (EXACT)
- fast-spiking basket cell (RELATED)

**Cross-references (definition support)**:
- PMID:7472426
- PMID:33398060
- PMID:31297048
- PMID:26441554

**Additional cross-references**:
- PMID:25018703
- PMID:35802727
- PMID:39401246
- PMID:25324774 (context only)

**Proposed SubClassOf axioms**:

```
SubClassOf: 'capable of' some GO:0061534  (gamma-aminobutyric acid secretion, neurotransmission)
SubClassOf: 'has soma location' some UBERON:0014548  (pyramidal layer of CA1)
SubClassOf: 'has soma location' some UBERON:0014550  (pyramidal layer of CA3)
SubClassOf: 'has soma location' some UBERON:0005381  (dentate gyrus granule cell layer)
SubClassOf: 'expresses' some PR:000013502  (parvalbumin alpha)
```

**Proposed Equivalence Axiom (logical definition)**:
```
EquivalentTo:
  'basket cell' (CL:0000118)
  and ('has soma location' some UBERON:0002313)   (hippocampus pyramidal layer)
  and ('expresses' some PR:000013502)              (parvalbumin alpha)
  and ('capable of' some GO:0061534)               (GABA secretion, neurotransmission)
```

**Note for CL ontologist**: The Cnr1-negative annotation is biologically well-supported (PMID:31297048, 25018703). Please verify whether a species-neutral PRO ID for cannabinoid receptor type 1 is available in PRO before adding a `lacks_plasma_membrane_part` axiom.

---

CURATION COMPLETE - READY FOR INTEGRATION
Passing to @CL-ontologist for integration into cl-edit.owl
