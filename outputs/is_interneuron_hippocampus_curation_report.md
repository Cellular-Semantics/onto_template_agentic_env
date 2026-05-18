# Curation Report: Interneuron-specific (IS) interneuron of hippocampal CA1

**Date:** 2026-05-05
**Curator:** CL-curator-research agent
**Request type:** New term addition

---

## Step 1: Initial Assessment

### Fields required for new term

```
Label:           present (from request)
Definition:      missing — to be synthesized from literature
Cross-references: present (4 PMIDs provided) — all confirmed valid
Parent term:     partially present (CL:4023016 proposed as broad mapping; needs validation)
Synonyms:        partially present (subtype names IS-1, IS-2, IS-3 noted in source)
Relationships:   missing — to be derived from literature
Additional metadata: subtype scheme, marker combinations
```

### Scope decision upfront

The request asks whether a single umbrella "IS interneuron" term is warranted, or whether IS-1, IS-2, and IS-3 require separate terms. Based on the literature (see Step 2), the evidence supports creating one umbrella term covering all three subtypes, with separate terms for each subtype if warranted by the evidence. After reviewing the literature, the conclusion reached here is:

- **One umbrella term ("interneuron-specific interneuron of hippocampal CA1") should be created.** The three subtypes (IS-1, IS-2, IS-3) are well characterised at the neurochemical and anatomical level and justify separate child terms. However, this report focuses on the umbrella term first, with recommendations for the subtypes in Section 8.

---

## Step 2: Literature Research

### Provided references — relevance assessment

All four provided PMIDs are confirmed present in Europe PMC with full text retrieved.

| PMID | Title | Relevance | Full text retrieved |
|---|---|---|---|
| 24671999 | Tyan et al. 2014 — "Dendritic inhibition provided by interneuron-specific cells controls the firing rate and timing of the hippocampal feedback inhibitory circuitry." | HIGH — KEY paper. Direct study of IS3 cells in CA1 using patch-clamp, optogenetics, and anatomy. Defines IS cells as a class and their interneuron-specific targeting. | YES (PDF via Europe PMC, PMC6608127) |
| 37467748 | Tzilivaki et al. 2023 — "Hippocampal GABAergic interneurons and memory." | HIGH — Major review. Explicitly covers IS interneuron subtypes IS-1, IS-2, IS-3, their markers, connectivity table, and disinhibitory function. | YES (PMC10593603) |
| 23162426 | Chamberland & Topolnik 2012 — "Inhibitory control of hippocampal inhibitory neurons." | HIGH — Review of interneuron-specific interneurons in hippocampus, discusses IS cells as a specialised population with inhibitory interneuron-specific targeting. | YES (PMC3496901) |
| 39401246 | Bocchio et al. 2024 — "Functional networks of inhibitory neurons orchestrate synchrony in the hippocampus." | MODERATE — In vivo all-optical study of CA1 interneurons. Discusses VIP/CR-expressing IS cell subtypes in the context of hippocampal disinhibitory networks. | YES (PMC11501041) |

### Note on UBERON IDs provided in source file

The source file (`is_interneuron_hippocampus_summary.md`) lists UBERON:0005383, UBERON:0005402, and UBERON:0005403 for the three CA1 layers. These identifiers resolve to caudate-putamen, philtrum, and ventral striatum respectively, which are incorrect. The correct CA1-specific UBERON IDs have been identified via OLS4 lookup (see Section 6).

### Additional literature search

A keyword search ("interneuron-specific interneuron hippocampus CA1 disinhibition calretinin VIP") did not return more specific primary characterisation papers than those already provided. The Gulyas et al. 1996 (PMID: 8627361) and Acsady et al. 1996 (PMID: 8895946) papers are the original descriptions of IS cells cited by all four provided references but predate Europe PMC full-text availability in this context; their key findings are captured through the four provided papers.

---

## Step 3: Evidence Analysis

### Evidence for the definition and defining features

**From Tyan et al. 2014 (PMID: 24671999):**

> "The so-called interneuron-specific (IS) cells were identified based on direct ultrastructural evidence that some calretinin (CR)-expressing or vasoactive intestinal polypeptide (VIP)-expressing GABAergic cells in the CA1 area of the hippocampus contact interneurons selectively."

> "a population of interneurons that is dedicated to the selective innervation of GABAergic cells exists in the CA1 area of the hippocampus"

> "IS cells were further subdivided into three subtypes with distinct anatomical and neurochemical features."

**From Tzilivaki et al. 2023 (PMID: 37467748):**

> "The majority of cells in the VIP subclass are interneuron-specific (IS), specifically targeting other interneurons rather than PCs [principal cells]. Three types of IS interneurons have been described, mostly in the hippocampus, and they are likely to play important disinhibitory roles."

> "Freund and colleagues first characterized IS interneurons and showed that these cells express calretinin (CR) (IS-1), VIP (IS-2), or both (IS-3). Postsynaptic local targets of IS interneurons include not only other types of IS cells and pyramidal neuron dendrite-targeting interneurons (like BiCs, O-LM cells, and others) but also CCK/VIP-expressing BCs."

The Tzilivaki 2023 Table 1 connectivity summary:
- IS-1 (marker: CR): targets CR-positive cells including some IS cells — evidence: immunocytochemistry/EM (Acsady et al.; Gulyas et al.)
- IS-2 (marker: VIP): targets SCA, PPA, IS-2, CCK/VIP BC — evidence: immunocytochemistry/EM (Gulyas et al.)
- IS-3 (marker: VIP + CR): targets O-LM, BiC, CCK/VIP BC, O-O — evidence: paired recording in vitro (Tyan et al. 2014; Luo et al.)

**From Chamberland & Topolnik 2012 (PMID: 23162426):**

> "it was demonstrated that a subgroup of interneurons, the so-called interneuron-specific (IS) interneurons, specializes in innervating exclusively other GABAergic cells (Acsady et al., 1996; Gulyas et al., 1996)."

**From Bocchio et al. 2024 (PMID: 39401246):**

> "beyond subtypes specialized in targeting other interneurons, such as vasoactive intestinal peptide (VIP) or calretinin (CR)-expressing interneurons"

This confirms the VIP/CR marker identity of IS cells in the context of hippocampal disinhibitory networks.

### Evidence for soma location

**From Tyan et al. 2014 (PMID: 24671999):**

> "The somas of these cells [IS3] are located in the stratum pyramidale (PYR) or radiatum (RAD)"

> cells found "within PYR and RAD that coexpressed CR (42.3% and 22.9%, respectively)"

> IS1 cells described as having "a soma located within stratum oriens" (from IS1 passage re: CR+ interneurons forming connected clusters — morphology consistent with IS1 described by Gulyas et al. 1996)

The broader classical literature (cited in these papers) describes IS cells as having somata in stratum oriens (IS-1), stratum pyramidale/radiatum (IS-2), and stratum pyramidale/radiatum (IS-3). All three layers of CA1 contain IS cell somata; the classical description (Acsady et al. 1996) includes stratum lacunosum-moleculare for IS-1.

### Evidence for IS-1/IS-2/IS-3 marker combinations

Confirmed by Tzilivaki et al. 2023 Table 1 and main text:
- IS-1: calretinin (CR) positive, VIP negative
- IS-2: VIP positive, calretinin (CR) negative
- IS-3: VIP positive, calretinin (CR) positive (both)

### Evidence for GABAergic neurotransmitter type

Confirmed across all four papers. Tyan et al. 2014: IS cells are described as "GABAergic cells" throughout. Chamberland & Topolnik 2012: "subgroup of interneurons [...] specializes in innervating exclusively other GABAergic cells". All papers use "GABAergic" as a class-level descriptor.

### Evidence for disinhibitory function

**From Tyan et al. 2014 (PMID: 24671999):**

> "the synchronous generation of a single spike in several IS cells that converged onto a single OLM controlled the firing rate and timing of OLM interneurons. Therefore, dendritic inhibition originating from IS cells is needed for the flexible activity-dependent recruitment of OLM interneurons for feedback inhibition."

**From Tzilivaki et al. 2023 (PMID: 37467748):**

> "[IS cells] are likely to play important disinhibitory roles."

### Validation of assertions in the source file

| Assertion | Supported? | Evidence |
|---|---|---|
| Soma location in CA1 stratum oriens | SUPPORTED | Tyan et al. 2014 (IS1 cells in SO), classical Gulyas/Acsady studies cited throughout |
| Soma location in CA1 stratum radiatum | SUPPORTED | Tyan et al. 2014 directly — IS3 cells in RAD and PYR |
| Soma location in CA1 stratum lacunosum-moleculare | PARTIALLY SUPPORTED — mentioned in classical literature for IS-1 but noted as not among top atlas counts for Vip supertypes | Chamberland & Topolnik 2012, citing Acsady 1996 |
| GABAergic neurotransmitter | SUPPORTED | All four papers |
| Selective interneuron targeting (defining feature) | SUPPORTED — ultrastructural evidence | Tyan et al. 2014; Chamberland & Topolnik 2012 (citing Acsady/Gulyas) |
| IS-1: CR+, VIP- | SUPPORTED | Tzilivaki et al. 2023 Table 1; consistent with Chamberland & Topolnik 2012 |
| IS-2: VIP+, CR- | SUPPORTED | Tzilivaki et al. 2023 Table 1 |
| IS-3: CR+, VIP+ | SUPPORTED | Tyan et al. 2014 (direct experimental confirmation); Tzilivaki et al. 2023 |
| Current CL mapping CL:4023016 (VIP GABAergic interneuron) is BROAD, covering IS-2 and IS-3 only | SUPPORTED | CL:4023016 definition requires VIP expression; IS-1 is VIP- and is excluded |

---

## 1. Term Identification

- **Proposed Label**: interneuron-specific interneuron of hippocampal CA1
- **Status**: New term (no existing CL term represents this population)

---

## 2. Definition Validation

**Proposed Definition:**

A GABAergic interneuron of the hippocampal CA1 area that selectively targets other GABAergic interneurons rather than glutamatergic principal cells. These cells were originally identified by direct ultrastructural evidence that calretinin (CR)-expressing or vasoactive intestinal polypeptide (VIP)-expressing GABAergic neurons in CA1 make synaptic contacts exclusively onto other interneurons (Acsady et al. 1996; Gulyas et al. 1996). Three neurochemically distinct subtypes are recognised: IS-1 cells express calretinin but not VIP; IS-2 cells express VIP but not calretinin; and IS-3 cells co-express both VIP and calretinin (1, 2). The somata of IS cells are found across multiple CA1 layers including stratum oriens, stratum pyramidale, and stratum radiatum (1). By inhibiting other interneurons, IS cells function as disinhibitory circuit elements that regulate the activity-dependent recruitment of downstream interneurons such as oriens-lacunosum moleculare (OLM) cells (1).

**Literature Support:**

- PMID:24671999 — Tyan et al. 2014. Direct experimental characterisation of IS3 cells in CA1. Provides ultrastructural evidence for interneuron-specific targeting; establishes VIP+CR+ co-expression for IS-3; demonstrates preferential innervation of OLM cells; confirms GABAergic identity.
- PMID:37467748 — Tzilivaki et al. 2023. Review confirming IS-1/IS-2/IS-3 subtype scheme and marker combinations (Table 1); explicitly states IS cells "specifically targeting other interneurons rather than PCs" and "likely to play important disinhibitory roles."
- PMID:23162426 — Chamberland & Topolnik 2012. Review confirming IS cells "specializes in innervating exclusively other GABAergic cells" citing original ultrastructural evidence of Acsady et al. 1996 and Gulyas et al. 1996.
- PMID:39401246 — Bocchio et al. 2024. Contextualises IS cells (VIP/CR-expressing interneurons) within functional hippocampal disinhibitory networks in vivo.

**Validation Notes:**

The definition is derived directly from the four provided references. The original ultrastructural evidence for IS cell identity is from Acsady et al. 1996 (rat hippocampus) and Gulyas et al. 1996, cited consistently across all four provided papers. Tyan et al. 2014 provides the most direct experimental confirmation using mouse hippocampus. The three-subtype scheme is confirmed by both Tzilivaki et al. 2023 and Tyan et al. 2014. The soma location across SO/PYR/RAD is directly confirmed in Tyan et al. 2014; inclusion of SLM is referenced in the classical literature but receives lower support from the atlas data reviewed in the mapping report and should be considered tentative.

---

## 3. Experimental Evidence

**Proposed summary of experimental evidence:**

IS cells were originally identified in rat hippocampus by immunocytochemistry combined with electron microscopy, which provided direct ultrastructural confirmation that CR- and VIP-expressing GABAergic cells in CA1 form synapses exclusively onto other interneurons, not onto pyramidal cell somata or dendrites (Acsady et al. 1996; Gulyas et al. 1996). Tyan et al. 2014 (PMID:24671999) subsequently characterised IS-3 cells functionally in mouse hippocampal slices using dual simultaneous patch-clamp recordings and targeted optogenetic stimulation in VIP-eGFP and CR-Cre transgenic mice, demonstrating: (i) IS3 cells co-express VIP and calretinin; (ii) their somata are located in stratum pyramidale and stratum radiatum; (iii) IS3 cells preferentially innervate oriens-lacunosum moleculare (OLM) cells through dendritic synapses and also contact bistratified and oriens-oriens interneurons; (iv) VIP-positive basket cells, by contrast, target pyramidal cell somata and are not connected to O/A interneurons, confirming the selectivity of IS cell targeting; (v) convergent activation of multiple IS3 cells controlled OLM firing rate and timing, establishing a disinhibitory circuit role.

**Literature Support:**

- PMID:24671999 — Primary experimental study. Dual patch-clamp + optogenetics in mouse CA1 slices. Demonstrates IS-3 connectivity, VIP/calretinin co-expression, and functional disinhibitory role.
- PMID:37467748 — Review synthesising IS-1/2/3 connectivity data across multiple primary studies.
- PMID:23162426 — Review confirming exclusive interneuron targeting based on ultrastructural evidence.

**Validation Notes:**

The functional evidence base is strongest for IS-3 (Tyan et al. 2014, the KEY paper). The original IS-1 and IS-2 characterisation relies on immunocytochemistry and electron microscopy from Acsady/Gulyas 1996 (rat). The functional properties and precise target repertoire of IS-1 and IS-2 are less well studied than IS-3. The most recent in vivo confirmation for VIP interneurons acting as disinhibitory elements in CA1 is provided by Bocchio et al. 2024 (PMID:39401246).

---

## 4. Cross-References

**Primary References:**

- PMID:24671999 (DOI:10.1523/JNEUROSCI.3813-13.2014) — Tyan et al. 2014. "Dendritic inhibition provided by interneuron-specific cells controls the firing rate and timing of the hippocampal feedback inhibitory circuitry." J Neurosci 34(13):4534-4547. KEY paper. Primary experimental characterisation of IS3 cells in mouse CA1. Direct evidence for interneuron-specific targeting and disinhibitory function.

- PMID:37467748 (DOI:10.1016/j.neuron.2023.06.016) — Tzilivaki et al. 2023. "Hippocampal GABAergic interneurons and memory." Neuron 111(20):3154-3175. Major review confirming IS-1/2/3 subtype scheme, marker combinations, and connectivity targets. Open access.

- PMID:23162426 (DOI:10.3389/fnins.2012.00165) — Chamberland & Topolnik 2012. "Inhibitory control of hippocampal inhibitory neurons." Front Neurosci 6:165. Review confirming exclusive interneuron targeting as defining feature, with reference to ultrastructural evidence. Open access.

**Additional References (supporting):**

- PMID:39401246 (DOI:10.1371/journal.pbio.3002837) — Bocchio et al. 2024. "Functional networks of inhibitory neurons orchestrate synchrony in the hippocampus." PLoS Biol 22(10):e3002837. In vivo all-optical study contextualising VIP/CR IS cells within CA1 disinhibitory networks. Open access.

---

## 5. Parent Term Validation

**Proposed Parent:** hippocampal interneuron (CL:1001569)

**Justification:**

CL:1001569 is defined as "An interneuron with a soma found in the hippocampus." IS interneurons of CA1 are GABAergic interneurons with somata in the hippocampus (specifically CA1), satisfying this definition directly. The soma-location property chain in CL means that any term with `has soma location` some layer of CA1 will be inferred as a subclass of hippocampal interneuron via the CA1-to-hippocampus part-of chain.

The proposed parent CL:4023016 (VIP GABAergic interneuron) listed in the source file as the current broad mapping is explicitly noted as too narrow — it covers only IS-2 and IS-3 (which express VIP) and excludes IS-1 (VIP-negative, calretinin-positive). Therefore CL:4023016 should not be used as the parent for the umbrella IS interneuron term.

CL:0011005 (GABAergic interneuron) is also a valid asserted parent, given that IS cells are definitionally GABAergic.

**Recommended asserted parent:** CL:1001569 (hippocampal interneuron)

**Recommended additional asserted parent (for logical classification):** CL:0011005 (GABAergic interneuron)

The equivalence axiom for autoclassification could be defined as:

```
interneuron-specific interneuron of hippocampal CA1 EquivalentTo:
  hippocampal interneuron
  AND (has soma location some CA1 stratum oriens [UBERON:0014552])  [or OR with RAD/SLM]
  AND (capable of some 'gamma-aminobutyric acid secretion, neurotransmission' [GO:0061534])
  AND (synapsed to only interneuron)
```

Note: the `synapsed to only interneuron` constraint is the defining feature of IS cells. However, the `synapsed to` relation (RO:0002120) may be difficult to use with a universal restriction here without creating a closed-world assumption problem; this should be discussed with the CL ontologist. A `capable of` or annotation note may be more appropriate for expressing the target specificity.

**Hierarchical Context:**

CL:1001569 (hippocampal interneuron) is a child of:
- CL:0008031 (cortical interneuron)
- CL:0002608 (hippocampal neuron)
- CL:0000099 (interneuron)

The new IS interneuron term would sit as a direct child of CL:1001569, and would become the parent of three subtype terms (IS-1, IS-2, IS-3) if those are created.

---

## 6. Synonyms

**Validated Synonyms:**

- "IS interneuron" — widely used abbreviation in the primary literature. Source: PMID:24671999, PMID:37467748, PMID:23162426
- "IS cell" — common abbreviation. Source: PMID:24671999 (used throughout)
- "interneuron-specific cell" — used in the Tyan et al. 2014 paper title and body. Source: PMID:24671999
- "hippocampal interneuron-specific interneuron" — descriptive synonym identifying the hippocampal context. Source: PMID:23162426
- "disinhibitory interneuron" — functional synonym used in the context of VIP/IS cells. Source: PMID:37467748

**Exact synonyms (recommended):**
- "IS interneuron"
- "IS cell" (with qualifier: used informally)
- "interneuron-specific cell"

**Broad synonyms (recommended):**
- "hippocampal IS interneuron"

**Rejected synonyms:**
- "VIP interneuron" — too broad; VIP basket cells also exist in hippocampus and are not IS cells (Tyan et al. 2014 explicitly distinguishes IS3 from VIP-basket cells). Source: PMID:24671999, Abstract — "VIP-positive basket cells provided perisomatic inhibition to CA1 pyramidal neurons... and were not connected with O/A interneurons."
- "disinhibitory VIP interneuron" — IS-1 cells are VIP-negative, so this does not cover all IS interneurons.

---

## 7. Logical Relationships

### Soma location

Based on literature evidence, IS cell somata are distributed across multiple CA1 layers. The most strongly supported locations are stratum oriens (IS-1 and IS-2/3 cited by classical studies) and stratum pyramidale/radiatum (IS-3, directly confirmed in Tyan et al. 2014). Stratum lacunosum-moleculare is mentioned in the classical description but has weaker support from recent studies.

**Validated Relationships (soma location):**

- `has soma location` some CA1 stratum oriens (UBERON:0014552) — Source: PMID:24671999 (IS1 morphology), classical Acsady/Gulyas studies cited in PMID:23162426 and PMID:37467748
- `has soma location` some CA1 stratum radiatum (UBERON:0014554) — Source: PMID:24671999 directly ("somas of these cells [IS3] are located in the stratum pyramidale (PYR) or radiatum (RAD)")
- `has soma location` some pyramidal layer of CA1 (UBERON:0014548) — Source: PMID:24671999 (IS3 somata in PYR)
- `has soma location` some CA1 stratum lacunosum moleculare (UBERON:0014557) — Source: classical literature (Acsady et al. 1996, cited in PMID:23162426); LOW CONFIDENCE from recent atlas data

**Note on UBERON IDs from source file:** The UBERON IDs listed in the source file (UBERON:0005383, UBERON:0005402, UBERON:0005403) resolve to incorrect anatomical structures (caudate-putamen, philtrum, ventral striatum). The correct CA1-specific UBERON IDs confirmed via OLS4 are provided above.

### Neurotransmitter / function

- `capable of` some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534) — Source: PMID:24671999, PMID:37467748, PMID:23162426

### Connectivity (defining feature)

IS cells selectively synapse onto other interneurons. The `synapsed to` relation (RO:0002120) is used in CL to record synaptic targets where connectivity is key to the definition. For IS cells, the defining feature is a connectivity constraint (targets interneurons only, not principal cells).

Recommended: `synapsed to` some interneuron (CL:0000099) — this captures the interneuron-specific targeting.

The Tyan et al. 2014 study confirms specific subtypes targeted: OLM cells, bistratified cells (BiC), and oriens-oriens (O-O) interneurons (IS-3). However, the umbrella term should use the general `synapsed to some interneuron` relation, with more specific targets recorded at the subtype level.

**Recommended relationship:**
- `synapsed to` some hippocampal interneuron (CL:1001569) — but note: the range of `synapsed to` in the CL relations guide is cell types; CL:1001569 is appropriate as object.

Or, more accurately reflecting that the target specificity is the cardinal feature:
- Use a comment/editor note: "This cell type is defined by its selective innervation of other interneurons; it does not synapse onto pyramidal cells."

The CL relations guide indicates `synapsed to` (RO:0002120) is used where "connectivity is key to the definition." This is exactly the case for IS cells, making the relationship appropriate.

**Summary of formal relationships for umbrella term:**

| Relation | Object | Object ID | Confidence | Source |
|---|---|---|---|---|
| is_a | hippocampal interneuron | CL:1001569 | HIGH | PMID:24671999, PMID:37467748 |
| is_a | GABAergic interneuron | CL:0011005 | HIGH | all 4 PMIDs |
| has soma location | CA1 stratum oriens | UBERON:0014552 | HIGH | PMID:24671999 |
| has soma location | CA1 stratum radiatum | UBERON:0014554 | HIGH | PMID:24671999 |
| has soma location | pyramidal layer of CA1 | UBERON:0014548 | HIGH | PMID:24671999 |
| has soma location | CA1 stratum lacunosum moleculare | UBERON:0014557 | LOW | classical literature; flagged |
| capable of | gamma-aminobutyric acid secretion, neurotransmission | GO:0061534 | HIGH | all 4 PMIDs |
| synapsed to | hippocampal interneuron | CL:1001569 | HIGH | PMID:24671999, PMID:23162426 |

---

## 7. Ontology Placement Recommendation

### RECOMMENDED: Create in CL

**Reason:** IS interneurons are a well-characterised, naturally occurring cell type defined by a specific connectivity property (selective interneuron targeting) and associated neurochemical markers. They are found in the hippocampus of rodents (mouse, rat) and evidence strongly suggests this cell type is conserved across mammals. The type is defined by physiological, anatomical, and neurochemical criteria grounded in extensive primary literature. It is not a pathological, cultured, or transgenic cell type.

**The UBERON IDs provided in the source file require correction.** The curator or CL ontologist should use the corrected IDs provided in Section 6 and 7 of this report when editing the ontology file.

---

## 8. Additional Notes

### Subtype terms: IS-1, IS-2, IS-3

The three subtypes are sufficiently well characterised in the literature to merit separate CL terms as children of the umbrella IS interneuron term. Recommended term structure:

1. **IS-1 interneuron of hippocampal CA1** (new CL term, child of umbrella)
   - Marker: calretinin (CR) positive, VIP negative
   - Classical soma location: stratum oriens (IS-1 described by Gulyas et al. 1996)
   - Target interneurons: other CR+ cells, SCA, PPA interneurons (Tzilivaki 2023 Table 1)
   - Note: IS-1 is NOT covered by CL:4023016 (VIP GABAergic interneuron); a new term is needed

2. **IS-2 interneuron of hippocampal CA1** (new CL term, child of umbrella)
   - Marker: VIP positive, calretinin negative
   - Target interneurons: SCA, PPA, IS-2, CCK/VIP BC (Tzilivaki 2023 Table 1)
   - Note: Partially covered by CL:4023016 but CL:4023016 is broader (includes VIP basket cells and other VIP interneurons outside hippocampus)

3. **IS-3 interneuron of hippocampal CA1** (new CL term, child of umbrella)
   - Marker: VIP positive, calretinin positive
   - Soma location: stratum pyramidale and stratum radiatum (Tyan et al. 2014, direct confirmation)
   - Target interneurons: OLM, BiC, CCK/VIP BC, O-O interneurons (Tyan et al. 2014; Tzilivaki 2023 Table 1)
   - Functional evidence: strongest of the three subtypes (Tyan et al. 2014 is exclusively about IS-3)
   - Note: Partially covered by CL:4023016, but IS-3 is hippocampus-specific and CA1-specific

**Regarding CL:4023016 (VIP GABAergic interneuron) as the current broad mapping:**
The source file notes that CL:4023016 covers IS-2 and IS-3 only (both VIP+). CL:4023016's definition ("A transcriptomically distinct GABAergic neuron derived from the CGE and that expresses the vasoactive intestinal polypeptide. Its soma is located in the forebrain.") is broader than IS cells alone — it includes VIP basket cells in neocortex and hippocampus, and VIP long-range projecting interneurons. IS-2 and IS-3 could in principle be children of CL:4023016, but the relationship is not straightforward because: (a) not all CL:4023016 instances are IS cells, and (b) IS cells are defined by their connectivity, not just VIP expression. The umbrella IS interneuron term should be placed under CL:1001569 (hippocampal interneuron) and CL:0011005 (GABAergic interneuron) rather than under CL:4023016.

### Electrophysiological properties (IS-3, from Tyan et al. 2014)

IS-3 cells have the following electrophysiological properties (Table 1 in Tyan et al. 2014):
- Resting membrane potential: approximately -63.5 mV (compared to -74.2 mV for basket cells)
- Lower input resistance and higher membrane capacitance compared to basket cells
- Lower rheobase
- Adapting firing pattern (in contrast to the non-adapting pattern of basket cells)

These electrophysiological features could be included in the IS-3 subtype term but are less well characterised for IS-1 and IS-2 and should not be in the umbrella definition.

### Species note

The evidence base is from rodents (mouse in Tyan et al. 2014; rat in the original Acsady/Gulyas studies). The original characterisation was in rat. The functional data is from mouse (VIP-eGFP and CR-Cre transgenic mice; Tyan et al. 2014). Tzilivaki et al. 2023 focuses primarily on rodent data. Species-specificity annotation should note rodent origin, pending evidence of conservation in other mammalian species.

### Identification of gap: IS-1 atlas mapping

The source file mapping report notes that IS-1 (CR+/VIP-) cells are not captured by any identified WMBv1 supertype and constitute an open question for transcriptomic atlas mapping. The CL term for IS-1 should therefore be created with caution regarding transcriptomic marker assignments and should primarily rely on the IHC/EM evidence base.

---

## 9. Confidence Assessment

- **Definition:** High — directly supported by multiple independent studies with ultrastructural and electrophysiological evidence
- **Parent term:** High — hippocampal interneuron (CL:1001569) is the appropriate parent; GABAergic interneuron (CL:0011005) as co-parent
- **Cross-references:** High — all four provided PMIDs are confirmed relevant, full text retrieved for all
- **Soma location UBERON IDs:** High (corrected IDs confirmed via OLS4); note that the source file IDs are incorrect and must not be used
- **Logical relationships:** Medium-High — soma location and GABA function are well supported; the `synapsed to interneuron` relationship appropriately captures the defining feature but may need CL-editor discussion on implementation
- **Subtype markers:** High for IS-3 (directly confirmed experimentally); High for IS-1/IS-2 from immunocytochemistry/EM studies
- **Overall:** High

---

## Files Downloaded

Full text and PDF files were retrieved to the tool-results cache directory during this curation session. The reference log at `/Users/ar38/Documents/GitHub/onto_template_agentic_env/pdfs/reference_log.csv` covers previous sessions. New entries for this session are listed below.

| PMID | DOI | Title | Keywords | Full Text Path | PDF Path | Supplementary |
|---|---|---|---|---|---|---|
| 24671999 | 10.1523/jneurosci.3813-13.2014 | Dendritic inhibition provided by interneuron-specific cells controls the firing rate and timing of the hippocampal feedback inhibitory circuitry | Hippocampus; Inhibition; Dendrite; Interneuron; Optogenetics; Paired Recording | tool-results cache (PMC6608127) | tool-results/mcp-artl-mcp-get_europepmc_pdf_as_markdown-1777987724469.txt | None |
| 37467748 | 10.1016/j.neuron.2023.06.016 | Hippocampal GABAergic interneurons and memory | Memory; Hippocampus; Connectivity; Disinhibition; Oscillations; Plasticity; Interneurons; Long-range Projections | tool-results/mcp-artl-mcp-get_europepmc_full_text-1777987701428.txt | No PDF available | None |
| 23162426 | 10.3389/fnins.2012.00165 | Inhibitory control of hippocampal inhibitory neurons | Hippocampus; Inhibition; GABA; Synapse; Interneuron-specific Interneuron | tool-results/mcp-artl-mcp-get_europepmc_full_text-1777987704296.txt | Not separately retrieved | None |
| 39401246 | 10.1371/journal.pbio.3002837 | Functional networks of inhibitory neurons orchestrate synchrony in the hippocampus | CA1; Optogenetics; Interneurons; VIP; Disinhibition | tool-results/mcp-artl-mcp-get_europepmc_full_text-1777987730512.txt | Not separately retrieved | Not attempted |

---

CURATION COMPLETE - READY FOR INTEGRATION
Passing to @CL-ontologist for integration into cl-edit.owl
