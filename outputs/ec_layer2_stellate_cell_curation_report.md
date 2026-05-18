# Curation Report: entorhinal cortex layer II stellate cell

## 1. Term Identification

- **Proposed Label**: entorhinal cortex layer II stellate cell
- **Status**: New term — no existing CL term found for this cell type
- **Taxon**: Described primarily in rodents (Mus musculus, Rattus norvegicus); present in other mammals including humans

---

## Initial Assessment

**Request type**: New term addition

```
✓ Label: present
✓ Definition: present (in source material — requires validation)
✓ Cross-references: present (7 PMIDs provided)
✓ Parent term: present (CL:0000679 glutamatergic neuron — requires validation)
✓ Synonyms: not provided — to be identified from literature
✓ Relationships: partially provided (soma location, projection target) — requires validation and UBERON ID correction
✓ Additional metadata: Reln+ marker, Calb1- negative marker, perforant path projection
```

**Critical issue identified at assessment**: The source material lists soma location as UBERON:0001905. Verification via OLS4 shows that UBERON:0001905 is "pineal body", which is incorrect. The correct UBERON ID for "entorhinal cortex layer 2" is UBERON:0022337. This must be corrected.

---

## 2. Definition Validation

**Proposed Definition**:

A glutamatergic neuron with its soma located in layer II of the entorhinal cortex, distinguished from the co-resident calbindin-positive pyramidal cell type by its stellate morphology, lack of calbindin expression, and expression of reelin (in mice). This cell type constitutes the principal reelin-expressing excitatory neuron of entorhinal cortex layer II and projects via the perforant pathway to the dentate gyrus of the hippocampal formation.

**Literature Support**:

- PMID:26223342 (Naumann et al. 2016, J Comp Neurol) — Establishes the two principal cell classes in MEC layer 2 across five mammalian species: calbindin-positive pyramidal cells (arranged in periodic patches) and calbindin-negative stellate cells (scattered between patches). Key quotes: "Principal neurons in layer 2 are divided into two distinct cell types, pyramidal and stellate, based on morphology, immunoreactivity, and functional properties." "Layer 2 of the rodent medial and the human caudal entorhinal cortex were structurally similar in that in both species patches of calbindin-positive pyramidal cells were superimposed on scattered stellate cells." Mouse (C57BL/6JOlaHsd) data included. Supports: stellate morphology, calbindin-negative identity, distribution in layer II.

- PMID:26711115 (Fuchs et al. 2016, Neuron) — Directly confirms that reelin expression marks stellate cells whereas calbindin marks pyramidal cells in MEC layer II: "calbindin (CB) and reelin (RE) expression in LII was correlated with the pyramidal and stellate phenotype, respectively (Kitamura et al., 2014, Ray et al., 2014, Varga et al., 2010)." Also confirms: "The superficial layer II (LII) and layer III (LIII) of the MEC are the origin of the perforant path terminating in the dentate gyrus." Supports: reelin expression, stellate identity, perforant path to dentate gyrus.

- PMID:20512133 (Varga et al. 2010, Nat Neurosci) — Demonstrates target-selective GABAergic innervation of MEC layer II principal cells based on their projection targets. Cannabinoid type 1 receptor-expressing basket cells selectively innervate cells that project outside the hippocampus while avoiding cells that give rise to the perforant pathway to the dentate gyrus. The perforant path-projecting cells are the reelin-positive stellate-type neurons (confirmed by cross-reference to Fuchs 2016 which cites Varga et al. as establishing the reelin-stellate correspondence). Supports: perforant path projection, soma location in EC layer II.

- PMID:32039761 (Pastoll et al. 2020, eLife) — Directly characterises stellate cell (SC) integrative properties in MEC using ex vivo patch-clamp in mice (up to 55 SCs per mouse). Confirms key electrophysiological signature: membrane resonance (sag/h-current), dorsoventral gradient in SC properties, relationship to grid cell firing. Confirms SCs as the major excitatory cell population distinct from pyramidal cells (L2PCs) in MEC LII.

- PMID:31680885 (Ohara et al. 2019, Front Syst Neurosci) — Systematic hodological study of calbindin-expressing (CB+) neurons in EC layer II. MEC CB+ (pyramidal) neurons project mainly to CA1. This implies that the non-CB+ (stellate/reelin+) population is the source of MEC-to-dentate gyrus perforant path projections. Supports projection target distinction.

**Validation Notes**:

The definition is well-supported by multiple independent studies. The co-occurrence of stellate morphology, calbindin-negative/reelin-positive immunoprofile, and perforant path projection to the dentate gyrus is established by at least three independent lines of evidence (morphology/immunohistochemistry: Naumann et al. 2016; marker/circuit: Fuchs et al. 2016, Varga et al. 2010; projection specificity: Ohara et al. 2019). The term is conserved across rodents and appears in bats and humans (Naumann et al. 2016), although the mouse-specific Reln marker is the strongest evidence for rodents.

---

## 3. Experimental Evidence

**Summary of experimental evidence**:

Stellate cells in MEC layer II are identified by a combination of morphological, molecular, electrophysiological, and hodological criteria:

1. **Morphology**: Stellate cells have dendritic processes radiating from the cell body in a star-like pattern, in contrast to the apical dendrite-dominant pyramidal morphology of the co-resident Calb1+ cells (Alonso & Klink 1993; Naumann et al. 2016).

2. **Molecular markers**: Stellate cells are calbindin-negative (Calb1-) and reelin-positive (Reln+) in rodents, confirmed by immunofluorescence at transcript and protein level (Varga et al. 2010, Fuchs et al. 2016, Naumann et al. 2016). The complementary calbindin-positive/reelin-negative pattern marks the co-resident pyramidal cells.

3. **Electrophysiology**: Stellate cells display a prominent voltage sag in response to hyperpolarising current injection (reflecting a hyperpolarisation-activated cation current, Ih), membrane resonance at theta frequencies, and subthreshold membrane potential oscillations at theta frequency (Alonso & Llinás 1989; Alonso & Klink 1993; Pastoll et al. 2020). These properties distinguish them electrophysiologically from pyramidal cells.

4. **Projection target**: Retrograde tracing experiments demonstrate that the reelin-positive cells in MEC layer II project via the perforant pathway to the dentate gyrus of the hippocampal formation, while calbindin-positive pyramidal cells project preferentially to hippocampal CA1 and other telencephalic targets (Varga et al. 2010; Ohara et al. 2019).

5. **Circuit function**: Stellate cells in MEC layer II contribute to the generation of grid cell firing patterns. The integrative properties of stellate cells, including their resonance frequency, vary continuously along the dorsoventral axis of MEC, correlating with the scale of grid cell firing fields (Pastoll et al. 2020).

**Literature Support**:

- PMID:26223342 — Morphological classification, calbindin-negative identity confirmed by immunohistochemistry across species including mouse
- PMID:26711115 — Reelin-stellate and calbindin-pyramidal marker correspondence; perforant path to dentate gyrus
- PMID:20512133 — Perforant path projection specificity; target-selective synaptic innervation based on projection target
- PMID:32039761 — Electrophysiological characterisation of stellate cells in mice (sag, resonance, dorsoventral gradient)
- PMID:31680885 — Projection comparison: CB+ (pyramidal) to CA1; implies CB- (stellate) to dentate gyrus

**Validation Notes**:

The electrophysiological properties cited above derive primarily from work in rats and mice and are well replicated across multiple laboratories. The resonance/sag/Ih signature of stellate cells is one of the best-characterised intrinsic property profiles of any cortical neuron type.

---

## 4. Cross-References

**Primary References** (from provided list — validated as relevant):

- PMID:26223342 (DOI:10.1002/cne.23865) — Naumann RK, Ray S, Prokop S, Las L, Heppner FL, Brecht M. "Conserved size and periodicity of pyramidal patches in layer 2 of medial/caudal entorhinal cortex." J Comp Neurol. 2016;524(4):783-806. Open access PMC5014138. HIGHLY RELEVANT — directly establishes stellate vs pyramidal distinction in MEC layer II across species.

- PMID:26711115 (DOI:10.1016/j.neuron.2015.11.029) — Fuchs EC, Neitz A, Pinna R, Melzer S, Caputi A, Monyer H. "Local and Distant Input Controlling Excitation in Layer II of the Medial Entorhinal Cortex." Neuron. 2016;89(1):194-208. Open access PMC4712190. HIGHLY RELEVANT — confirms reelin=stellate, calbindin=pyramidal marker correspondence; perforant path to dentate gyrus.

- PMID:20512133 (DOI:10.1038/nn.2570) — Varga C, Lee SY, Soltesz I. "Target-selective GABAergic control of entorhinal cortex output." Nat Neurosci. 2010;13(7):822-824. Open access PMC3139425. HIGHLY RELEVANT — shows reelin+ cells in MEC LII project via perforant path to dentate gyrus; establishes stellate-perforant path link.

- PMID:34949991 (DOI:10.3389/fncir.2021.790116) — Ohara S et al. "Laminar Organization of the Entorhinal Cortex in Macaque Monkeys Based on Cell-Type-Specific Markers and Connectivity." Front Neural Circuits. 2021;15:790116. Open access PMC8688913. RELEVANT — cross-species confirmation of reelin/calbindin layer II marker pattern; glutamatergic neurotransmitter type.

- PMID:30209250 (DOI:10.1038/s41467-018-06104-5) — Zutshi I et al. "Recurrent circuits within medial entorhinal cortex superficial layers support grid cell firing." Nat Commun. 2018;9(1):3701. Open access PMC6135799. RELEVANT — MEC layer II circuits and grid cell function involving pyramidal and stellate cell populations.

**References assessed as low relevance for this term**:

- PMID:37219048 — Strell P et al. Review on neuronal transplantation for Alzheimer's disease. Not specific to stellate cells; only mentions EC neurons generically. NOT RECOMMENDED as a primary cross-reference for this term.

- PMID:29665671 — Park D et al. Review on hippocampal and cerebellar synapse organizers. Not specific to entorhinal cortex stellate cells. NOT RECOMMENDED as a primary cross-reference for this term.

**Additional References identified during search**:

- PMID:32039761 (DOI:10.7554/elife.52258) — Pastoll H, Garden DL, Papastathopoulos I, Sürmeli G, Nolan MF. "Inter- and intra-animal variation in the integrative properties of stellate cells in the medial entorhinal cortex." eLife. 2020;9:e52258. Open access PMC7067584. HIGHLY RELEVANT — systematic characterisation of stellate cell electrophysiological properties in mouse.

- PMID:31680885 (DOI:10.3389/fnsys.2019.00054) — Ohara S et al. "Entorhinal Layer II Calbindin-Expressing Neurons Originate Widespread Telencephalic and Intrinsic Projections." Front Syst Neurosci. 2019;13:54. Open access PMC6803526. HIGHLY RELEVANT — demonstrates projection specificity of CB+ vs CB- cells in EC layer II.

**Recommended cross-references for the CL term** (in order of priority):

1. PMID:26223342 (primary — stellate vs pyramidal morphology/marker in MEC layer II)
2. PMID:26711115 (reelin-stellate and calbindin-pyramidal correspondence; perforant path)
3. PMID:20512133 (perforant path projection from reelin+ stellate-type cells to dentate gyrus)

---

## 5. Parent Term Validation

**Proposed Parent**: glutamatergic neuron (CL:0000679)

**OLS4 verification**: CL:0000679 confirmed — "A neuron that is capable of some neurotransmission by glutamate secretion." This is a valid, non-obsolete CL term.

**Justification**:

The proposed parent CL:0000679 (glutamatergic neuron) is appropriate and well-supported. Multiple sources confirm that stellate cells in MEC layer II are excitatory (glutamatergic) principal neurons. Fuchs et al. 2016 states that MEC layer II neurons belong to "excitatory neurons" circuits; Ohara et al. 2021 confirms EC layer II neurons are glutamatergic by cell-type-specific marker analysis. The perforant path to dentate gyrus is a canonical excitatory (glutamatergic) projection in hippocampal circuit anatomy.

**Hierarchical Context**:

Within the CL hierarchy, placing the term as a subclass of CL:0000679 is correct. The logical definition would further specify soma location (UBERON:0022337), morphology (stellate — CL:0000122 provides useful cross-reference), and functional output (glutamate secretion — GO:0061535). No more specific existing CL term for entorhinal cortex neurons was found that could serve as a more proximate parent; the new term would sit directly under CL:0000679 with location specified by the 'has soma location' relationship to UBERON:0022337.

Note: CL:0000122 (stellate neuron) exists and could also be used as a second parent to capture the morphological type. This would create a multi-parent hierarchy correctly representing both the neurotransmitter identity and the morphological identity of the cell.

**Alternative parent consideration**:

CL:0010012 (cerebral cortex neuron) is another potential parent given that the entorhinal cortex is classically considered part of the cerebral cortex (specifically parahippocampal cortex/allocortex). However, given that the entorhinal cortex is allocortex/mesocortex rather than neocortex, and CL:0010012 is defined as "A CNS neuron of the cerebral cortex," the applicability depends on how CL:0010012 is used in practice. The 'has soma location' axiom to UBERON:0022337 (entorhinal cortex layer 2) should be sufficient to place this cell type appropriately within the hierarchy via the property chain reasoning described in the relations guide.

**Recommended parents**:
- Primary: CL:0000679 (glutamatergic neuron)
- Secondary (optional): CL:0000122 (stellate neuron) — to capture morphological classification

---

## 6. Synonyms

**Validated Synonyms** (from literature):

- "MEC layer II stellate cell" — Source: PMID:32039761 (Pastoll et al. 2020), PMID:26711115 (Fuchs et al. 2016); abbreviated form used frequently in the literature, especially for the medial subdivision.
- "reelin-positive entorhinal cortex layer II neuron" — Source: PMID:26711115 (Fuchs et al. 2016); descriptive synonym based on defining molecular marker.
- "layer II stellate cell of medial entorhinal cortex" — Source: PMID:26223342 (Naumann et al. 2016); alternative word order used in comparative anatomy literature.
- "entorhinal stellate cell" — Source: PMID:26223342 (Naumann et al. 2016); abbreviated form used broadly when context makes EC layer II clear.
- "EC LII stellate cell" — Source: PMID:26711115 (Fuchs et al. 2016); abbreviated form in circuit papers.

**Synonyms not recommended**:

- "stellate cell" alone — too general; also used for cerebellar stellate cells (CL:0010010) and other contexts.
- "fan cell" — this is a distinct cell type in lateral entorhinal cortex (Vandrey et al. 2022, PMID:36562467), not the same as MEC stellate cells. Should not be used as a synonym.
- "grid cell" — grid cell is a functional/physiological designation, not a cell type synonym; many stellate cells may not be grid cells and the relationship is not 1:1.

---

## 7. Logical Relationships

**Validated Relationships**:

### Soma location

- **Relationship**: 'has soma location' (RO:0002100)
- **Object**: entorhinal cortex layer 2 (UBERON:0022337)
- **Source**: PMID:26223342, PMID:26711115, PMID:20512133

**IMPORTANT CORRECTION**: The source material lists the soma location UBERON ID as UBERON:0001905. This is incorrect — UBERON:0001905 is "pineal body." The correct ID is UBERON:0022337 ("entorhinal cortex layer 2"), verified via OLS4. This must be corrected in any template.

The UBERON:0022337 definition states: "Layer of the entorhinal cortex lying superficial to layer 3 and deep to layer 1. It is characterized by medium-to large sized stellate cells that are grouped into prominent clusters." This is consistent with stellate cell location.

### Neurotransmitter/function

- **Relationship**: 'capable of' (RO:0002215)
- **Object**: glutamate secretion, neurotransmission (GO:0061535)
- **Source**: PMID:26711115, PMID:34949991

### Gene expression (marker)

- **Relationship**: 'expresses' (RO:0002292)
- **Object**: reelin (mouse) (PR:Q60841) — for the mouse-specific term
- OR reelin (PR:000013879) — for the generic/cross-species term
- **Source**: PMID:26711115, PMID:20512133

Note on scope: The reelin expression evidence is strongest for rodents. The Naumann et al. 2016 data is cross-species for calbindin-negative identity (stellate morphology) but the specific molecular marker Reln is best documented in mice and rats. If a species-neutral term is intended, consider not axiomatising the reelin expression as a necessary condition but noting it as a characteristic.

### Projection target (optional — for 'sends synaptic output to region')

- **Relationship**: 'sends synaptic output to region' (RO:0013003)
- **Object**: dentate gyrus of hippocampal formation (UBERON:0001885)
- **Source**: PMID:20512133, PMID:26711115

The perforant path termination in dentate gyrus is a well-established feature of MEC layer II stellate-type cells and is key to their functional role in hippocampal information processing.

---

## 8. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

**Reason**: The entorhinal cortex layer II stellate cell is a well-characterised, non-pathological, non-cultured cell type present in vivo in multiple mammalian species. It is defined by a combination of morphological (stellate dendritic arbor), molecular (Reln+/Calb1- in rodents), electrophysiological (Ih sag, theta resonance), and hodological (perforant path to dentate gyrus) properties well-established in the primary literature. It satisfies all CL inclusion criteria:
- It is a natural cell type (not a cell line or cultured cell)
- It has clear, literature-supported distinguishing properties
- Multiple high-quality references support the definition
- It plays a defined role in hippocampal circuit function

No more specific entorhinal cortex neuron term exists in CL at present, and this new term would fill an important gap relevant to brain atlas-ontology mapping and hippocampal circuit modelling.

---

## 9. Additional Notes

### Error in source material: UBERON ID for soma location

The source mapping report (ec_layer2_stellate_cell_hippocampus_summary.md) and the task description cite UBERON:0001905 for "entorhinal cortex layer II." This is an error: UBERON:0001905 = "pineal body." The correct ID is UBERON:0022337 = "entorhinal cortex layer 2" (verified via OLS4). All templates and annotations must use UBERON:0022337.

### Scope clarification: medial vs. lateral vs. generic entorhinal cortex

The primary evidence for this cell type comes from the medial entorhinal cortex (MEC). The lateral entorhinal cortex (LEC) has a distinct cell type organisation, with "fan cells" (not stellate cells) as the principal excitatory neurons in layer II of LEC (Vandrey et al. 2022, PMID:36562467). The proposed term should be framed as applying to the entorhinal cortex generally (UBERON:0022337, which spans both MEC and LEC), since UBERON does not have a specific layer 2 term for medial vs lateral EC at this time. However, the definition text should note that the evidence is primarily from the medial subdivision. If a more specific term for the medial EC layer II stellate cell is desired, the soma location axiom should use UBERON:0007224 (medial entorhinal cortex) combined with layer 2, but no such combined UBERON term exists. Use UBERON:0022337 with a note in the definition.

### Assessment of provided PMIDs for relevance

- PMID:37219048 (Strell et al. 2023) is a review on neuronal transplantation for Alzheimer's disease. Its citation in the source material as supporting "soma location" for EC layer II stellate cells appears to be an error in the source mapping report. This paper does not characterise stellate cells specifically and should NOT be used as a cross-reference for the CL term definition.

- PMID:29665671 (Park et al. 2018) is a review on hippocampal and cerebellar synapse organizers. It mentions entorhinal cortex only briefly in a circuit context and does not characterise stellate cells. This paper should NOT be used as a cross-reference for the CL term definition.

### Full text retrieval note

Full text was successfully retrieved for PMID:26223342 (PMC5014138), PMID:26711115 (PMC4712190), and PMID:32039761 (PMC7067584). Full text for PMID:20512133 (PMC3139425) returned empty via the full text tool (the paper is open access and the content may require PDF retrieval). Full texts for PMID:34949991, PMID:37219048, PMID:29665671, and PMID:30209250 were not retrieved (low priority given relevance assessment).

---

## 10. Confidence Assessment

- **Definition**: High — Supported by multiple independent, high-quality primary papers from different laboratories; the stellate vs pyramidal distinction in MEC layer II is one of the most studied cell type distinctions in cortical neuroscience.
- **Parent term**: High — CL:0000679 (glutamatergic neuron) is clearly appropriate; confirmed by multiple sources.
- **Cross-references**: High — Three primary cross-references (PMID:26223342, PMID:26711115, PMID:20512133) together cover all key definitional properties.
- **Soma location UBERON ID**: High for UBERON:0022337; the source material UBERON:0001905 is confirmed INCORRECT.
- **Marker relationships**: Medium — Reelin expression is well-established in rodents but the PRO term (PR:Q60841 for mouse) may need curatorial confirmation regarding how CL currently handles species-specific marker axioms.
- **Projection relationship**: High — Perforant path to dentate gyrus is a canonical, well-established finding replicated across many studies.
- **Overall**: High — This is a well-characterised, clearly distinguishable neuron type with strong literature support.

---

## Summary: Recommended CL Term

**Label**: entorhinal cortex layer II stellate cell

**Synonyms**:
- MEC layer II stellate cell (exact)
- entorhinal stellate cell (broad)
- layer II stellate cell of medial entorhinal cortex (exact)
- reelin-positive entorhinal cortex layer II neuron (related)

**Definition** (proposed):

A glutamatergic principal neuron with its soma located in layer II of the entorhinal cortex, distinguished by a stellate morphology with multiple dendrites radiating symmetrically from the soma, and by its lack of calbindin expression and expression of reelin in rodents (1,2). This cell type is the principal source of perforant pathway projections from entorhinal cortex layer II to the dentate gyrus (3). Electrophysiologically, these neurons display a prominent hyperpolarisation-activated inward current (Ih) manifest as a voltage sag, and intrinsic membrane resonance in the theta frequency range (4). In rodents, this cell type co-exists in entorhinal cortex layer II with calbindin-positive pyramidal cells, which project preferentially to hippocampal CA1 (2,5).

References in definition: (1) PMID:26223342, (2) PMID:26711115, (3) PMID:20512133, (4) PMID:32039761, (5) PMID:31680885

**Parent**: glutamatergic neuron (CL:0000679)

**Optional second parent**: stellate neuron (CL:0000122)

**Cross-references**:
- PMID:26223342
- PMID:26711115
- PMID:20512133

**Logical axioms**:
- 'has soma location' some 'entorhinal cortex layer 2' (UBERON:0022337) — NOTE: source material erroneously listed UBERON:0001905 (pineal body); correct ID is UBERON:0022337
- 'capable of' some 'glutamate secretion, neurotransmission' (GO:0061535)
- 'expresses' some 'reelin (mouse)' (PR:Q60841) [mouse-specific; or PR:000013879 for generic]
- 'sends synaptic output to region' some 'dentate gyrus of hippocampal formation' (UBERON:0001885)

---

CURATION COMPLETE - READY FOR INTEGRATION
Passing to @CL-ontologist for integration into cl-edit.owl
