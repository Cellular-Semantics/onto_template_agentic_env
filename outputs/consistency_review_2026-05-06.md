# Consistency Review — Hippocampal Cell Curation Reports
*Date: 2026-05-06 · Reviewer: orchestrator + ontology-term-lookup + general-purpose agents*

---

## Scope

This review checks consistency between the two curation reports in `outputs/` and their source mapping files in `source_data/`, with independent verification of all ontology IDs via OLS4 and literature metadata via Europe PMC.

---

## 1. entorhinal cortex layer II stellate cell

### Source file: `source_data/ec_layer2_stellate_cell_hippocampus_summary.md`
### Report: `outputs/ec_layer2_stellate_cell_curation_report.md`

#### UBERON IDs

| ID | Source claim | OLS4 actual label | Status |
|----|---|---|---|
| UBERON:0001905 | entorhinal cortex layer II (soma location) | **pineal body** | ❌ WRONG in source |
| UBERON:0022337 | entorhinal cortex layer 2 (curation correction) | **entorhinal cortex layer 2** | ✅ Correct |
| UBERON:0001885 | dentate gyrus of hippocampal formation | **dentate gyrus of hippocampal formation** | ✅ Correct |

**Action required:** Replace UBERON:0001905 → UBERON:0022337 in all templates. Curation report correctly identifies and corrects this error.

#### CL IDs

| ID | Claimed label | OLS4 actual label | Status |
|----|---|---|---|
| CL:0000679 | glutamatergic neuron (proposed parent) | **glutamatergic neuron** | ✅ Correct |
| CL:0000122 | stellate neuron (optional second parent) | **stellate neuron** | ✅ Correct |

#### Literature year discrepancy

| PMID | Source mapping file | Curation report | Europe PMC `pubYear` | Verdict |
|------|---|---|---|---|
| 26223342 | "Naumann et al. **2015**" | "Naumann et al. **2016**" | **2016** | Curation report correct — "2015" in source is the electronic ahead-of-print date; official publication is March 2016, J Comp Neurol 524(4):783-806 |

#### Cross-reference quality

The curation report correctly identifies two PMIDs in the source as non-relevant:
- PMID:37219048 — neuronal transplantation review; does not characterise EC layer II stellate cells
- PMID:29665671 — hippocampal/cerebellar synapse organiser review; does not characterise stellate cells

These should **not** be used as cross-references for the CL term.

#### Overall assessment

**The curation report is consistent and correct.** All corrections (UBERON ID, year, cross-reference curation) are verified. Report is ready for template integration.

---

## 2. interneuron-specific (IS) interneuron of hippocampal CA1

### Source file: `source_data/is_interneuron_hippocampus_summary.md`
### Report: `outputs/is_interneuron_hippocampus_curation_report.md`

#### UBERON IDs

| ID | Source claim | OLS4 actual label | Status |
|----|---|---|---|
| UBERON:0005383 | stratum oriens of CA1 | **caudate-putamen** | ❌ WRONG in source |
| UBERON:0005402 | stratum radiatum of CA1 | **philtrum** | ❌ WRONG in source |
| UBERON:0005403 | stratum lacunosum-moleculare of CA1 | **ventral striatum** | ❌ WRONG in source |
| UBERON:0014552 | CA1 stratum oriens (curation correction) | **CA1 stratum oriens** | ✅ Correct |
| UBERON:0014554 | CA1 stratum radiatum (curation correction) | **CA1 stratum radiatum** | ✅ Correct |
| UBERON:0014548 | pyramidal layer of CA1 (curation addition) | **pyramidal layer of CA1** | ✅ Correct |
| UBERON:0014557 | CA1 stratum lacunosum moleculare (curation correction) | **CA1 stratum lacunosum moleculare** | ✅ Correct |

**Action required:** All three source UBERON IDs are completely wrong (they resolve to a striatal structure, a facial feature, and another striatal structure). Replace with the corrected IDs from the curation report.

#### CL IDs

| ID | Claimed label | OLS4 actual label | Status |
|----|---|---|---|
| CL:4023016 | VIP GABAergic interneuron (source broad mapping, rejected) | **VIP GABAergic interneuron** | ✅ Label correct; correctly rejected as parent |
| CL:1001569 | hippocampal interneuron (proposed parent) | **hippocampal interneuron** | ✅ Correct |
| CL:0011005 | GABAergic interneuron (proposed co-parent) | **GABAergic interneuron** | ✅ Correct |
| CL:0000099 | interneuron (proposed `synapsed to` object) | **interneuron** | ✅ Correct |

**Note on CL:4023016 rejection:** The curation report correctly rejects CL:4023016 as the umbrella parent because IS-1 cells are VIP-negative (CR+/VIP−) and would be excluded. The recommended parent CL:1001569 (hippocampal interneuron) correctly covers all three IS subtypes.

#### Overall assessment

**The curation report is consistent and correct.** All three source UBERON IDs are verified as wrong; all four proposed replacement/correction IDs are verified as correct. Parent term change (CL:4023016 → CL:1001569 + CL:0011005) is well-justified and ontologically sound.

---

## Summary table

| Check | EC stellate | IS interneuron |
|---|---|---|
| UBERON IDs in source | ❌ UBERON:0001905 is pineal body | ❌ All 3 IDs wrong (striatum, lip, striatum) |
| UBERON corrections in report | ✅ UBERON:0022337 verified | ✅ All 4 corrected IDs verified |
| CL parent IDs | ✅ CL:0000679, CL:0000122 verified | ✅ CL:1001569, CL:0011005 verified |
| Literature year | ⚠ Source says 2015; correct year is 2016 (Naumann) | N/A |
| Cross-reference quality | ⚠ 2 of 7 source PMIDs not relevant (correctly flagged) | ✅ All 4 provided PMIDs confirmed relevant |
| Definitions | ✅ Well-supported by literature | ✅ Well-supported by literature |
| Reports ready for integration | ✅ YES | ✅ YES |

---

## Actions for template editors

1. **EC stellate cell template**: Use UBERON:0022337 (not UBERON:0001905) for soma location. Use 2016 as Naumann year. Do not include PMID:37219048 or PMID:29665671 as cross-references.
2. **IS interneuron template**: Replace all three source UBERON IDs with UBERON:0014552/0014554/0014548 as appropriate. Use CL:1001569 and CL:0011005 as parents (not CL:4023016). Note UBERON:0014557 (SLM) should be included with low confidence flag.
