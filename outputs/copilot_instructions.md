# CL Term Integration Instructions — Myenteric Neurons

This file contains structured information for 17 new Cell Ontology terms (16 myenteric neuron terms + 1 prerequisite general term).

---

## Term 1: Excitatory motor neuron of myenteric plexus

**Preferred Label**: excitatory motor neuron of myenteric plexus

**Definition**: An excitatory motor neuron of the enteric nervous system whose soma resides in the myenteric plexus and whose axon projects to smooth muscle of the muscularis externa. This neuron is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1). Morphologically, it displays stubby Dogiel type I morphology with lamellar dendrite processes and a large soma.

**References**:
- PMID:34170401
- PMID:37355216
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:0007011 (enteric neuron)

**Import Flags**: None

**Synonyms**:
- cholinergic myenteric motor neuron (PMID:37355216)
- cholinergic non-nitrergic myenteric motor neuron (PMID:37355216)
- excitatory enteric motor neuron (PMID:34170401)

---

## Term 2: Inhibitory motor neuron of myenteric plexus

**Preferred Label**: inhibitory motor neuron of myenteric plexus

**Definition**: An inhibitory motor neuron of the enteric nervous system whose soma resides in the myenteric plexus and whose axon projects to smooth muscle of the muscularis externa. This neuron is immunopositive for neuronal nitric oxide synthase (NOS1) and immunonegative for choline acetyltransferase (ChAT). Morphologically, it displays spiny Dogiel type I morphology with characteristic spine-like dendrite projections.

**References**:
- PMID:34170401
- PMID:37355216
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:0007011 (enteric neuron)
- CL:0008015 (inhibitory motor neuron)

**Import Flags**:
- GO: Request creation of `nitric oxide secretion, neurotransmission` GO term analogous to GO:0014055

**Synonyms**:
- nitrergic myenteric motor neuron (PMID:37355216)
- nitrergic motor neuron of myenteric plexus (PMID:37355216)
- NOS1-positive ChAT-negative myenteric motor neuron (PMID:37355216)

---

## Term 3: Intrinsic primary afferent neuron of myenteric plexus

**Preferred Label**: intrinsic primary afferent neuron of myenteric plexus

**Definition**: A sensory neuron of the enteric nervous system whose soma resides in the myenteric plexus and which functions as the afferent limb of intrinsic reflex circuits controlling motility, secretion, and blood flow. This neuron is characterised by Dogiel type II morphology (large smooth soma with multiple long axon-like processes), AH-type electrophysiology (prolonged afterhyperpolarization following an action potential), and is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).

**References**:
- PMID:34170401
- PMID:37355216
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:0007011 (enteric neuron)
- CL:0000101 (sensory neuron)

**Import Flags**: None

**Synonyms**:
- IPAN (PMID:34170401)
- myenteric sensory neuron (PMID:34170401)
- multiaxonal cholinergic myenteric sensory neuron (PMID:37355216)

---

## Term 4: Interneuron of myenteric plexus

**Preferred Label**: interneuron of myenteric plexus

**Definition**: An interneuron of the enteric nervous system whose soma resides in the myenteric plexus. Interneurons of the myenteric plexus integrate sensory input from intrinsic primary afferent neurons (IPANs) and modulate motor output to smooth muscle and secretory epithelia by synapsing onto motor neurons and other interneurons within the plexus.

**References**:
- PMID:34170401
- PMID:40954253
- PMID:32888429

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:0007011 (enteric neuron)
- CL:0000099 (interneuron)

**Import Flags**: None

**Synonyms**:
- enteric interneuron of myenteric plexus (PMID:34170401)

---

## Term 5: Secretomotor/vasodilator neuron of myenteric plexus

**Preferred Label**: secretomotor/vasodilator neuron of myenteric plexus

**Definition**: An enteric neuron whose soma resides in the myenteric plexus and which controls mucosal secretion and blood flow by innervating secretory epithelia and submucosal blood vessels. This neuron is characterised by expression of vasoactive intestinal peptide (VIP). In mouse, two Glp2r+ subtypes have been identified: PSVN1 (VIP+, non-cholinergic) and PSVN2 (ChAT+, cholinergic). In human, only the VIP+ non-cholinergic subtype has been detected.

**References**:
- PMID:34170401
- PMID:32888429
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:0007011 (enteric neuron)

**Import Flags**: None

**Synonyms**:
- PSVN (PMID:34170401)
- VIP-positive secretomotor neuron (PMID:32888429)

---

## Term 6: Intestinofugal neuron

**Preferred Label**: intestinofugal neuron

**Definition**: An enteric neuron whose soma resides in the myenteric plexus of the intestine and whose axon projects outside the gut wall to synapse on neurons in prevertebral sympathetic ganglia (celiac, superior mesenteric, or inferior mesenteric ganglia). This neuron provides a pathway for gut-to-brain communication via sympathetic prevertebral ganglia. In humans, 89% are immunopositive for choline acetyltransferase (ChAT); CART (cocaine- and amphetamine-regulated transcript) is NOT a human marker (0% CART+) but is present in rodent viscerofugal neurons.

**References**:
- PMID:38292899
- PMID:34170401
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location
- UBERON:0002262 (celiac ganglion) — axon target
- UBERON:0005479 (superior mesenteric ganglion) — axon target
- UBERON:0005480 (inferior mesenteric ganglion) — axon target

**Parent CL Terms**:
- CL:0007011 (enteric neuron)

**Import Flags**: None

**Synonyms**:
- viscerofugal neuron (PMID:38292899)
- VFN (PMID:38292899)
- cholinergic viscerofugal neuron (PMID:38292899)

---

## Term 7: Ascending interneuron of myenteric plexus

**Preferred Label**: ascending interneuron of myenteric plexus

**Definition**: An interneuron of the myenteric plexus whose axon projects orally (in the ascending direction) along the gut axis. This neuron is immunopositive for choline acetyltransferase (ChAT) and enkephalin (ENK), and forms the excitatory limb of ascending reflex pathways that coordinate peristalsis.

**References**:
- PMID:34170401
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- interneuron of myenteric plexus [NEW Term 4]

**Import Flags**: None

**Synonyms**:
- cholinergic enkephalinergic myenteric interneuron (PMID:34170401)
- ascending myenteric interneuron (PMID:34170401)

---

## Term 8: Descending interneuron of myenteric plexus

**Preferred Label**: descending interneuron of myenteric plexus

**Definition**: An interneuron of the myenteric plexus whose axon projects aborally (in the descending direction) along the gut axis. This neuron class encompasses multiple chemically diverse subtypes including serotonergic (5-HT+), nitrergic (NOS1+), and other populations, forming the inhibitory limb of descending reflex pathways.

**References**:
- PMID:34170401
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- interneuron of myenteric plexus [NEW Term 4]

**Import Flags**: None

**Synonyms**:
- descending myenteric interneuron (PMID:34170401)

---

## Term 9: Stubby Dogiel type I neuron of myenteric plexus

**Preferred Label**: stubby Dogiel type I neuron of myenteric plexus

**Definition**: A Dogiel type I neuron of the myenteric plexus characterised by stubby (lamellar) dendrite morphology with broad, flattened dendritic expansions. This neuron is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1), corresponding to excitatory motor neurons of the enteric nervous system.

**References**:
- PMID:34170401
- PMID:37355216

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:4047038 (Dogiel type I neuron)
- excitatory motor neuron of myenteric plexus [NEW Term 1]

**Import Flags**:
- PATO: Investigate term for lamellar dendrite morphology

**Synonyms**:
- stubby Dogiel I neuron (PMID:34170401)
- lamellar Dogiel type I neuron (PMID:34170401)

---

## Term 10: Spiny Dogiel type I neuron of myenteric plexus

**Preferred Label**: spiny Dogiel type I neuron of myenteric plexus

**Definition**: A Dogiel type I neuron of the myenteric plexus characterised by spiny (spine-like) dendrite morphology with numerous short projections along the dendrites. This neuron is immunopositive for neuronal nitric oxide synthase (NOS1) and immunonegative for choline acetyltransferase (ChAT), corresponding to inhibitory motor neurons of the enteric nervous system.

**References**:
- PMID:34170401
- PMID:37355216

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:4047038 (Dogiel type I neuron)
- inhibitory motor neuron of myenteric plexus [NEW Term 2]

**Import Flags**:
- PATO: Investigate term for spine-like dendrite morphology

**Synonyms**:
- spiny Dogiel I neuron (PMID:34170401)

---

## Term 11: Dogiel type II neuron of myenteric plexus

**Preferred Label**: Dogiel type II neuron of myenteric plexus

**Definition**: An intrinsic primary afferent neuron of the myenteric plexus characterised by Dogiel type II morphology: a large, smooth, oval soma bearing multiple long axon-like processes that extend without branching until they reach their targets in both the myenteric and submucosal plexuses and the mucosa. The soma lacks the dendrites characteristic of Dogiel type I neurons and is larger in cross-sectional area than either motor neuron type. This neuron is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1). It exhibits AH-type electrophysiology, characterised by a prolonged afterhyperpolarization (AHP) following an action potential. Substance P (encoded by TAC1) expression has been reported in subsets across species.

**References**:
- PMID:34170401
- PMID:37355216
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- Dogiel type II neuron [NEW Term 16 — prerequisite]
- intrinsic primary afferent neuron of myenteric plexus [NEW Term 3]

**Import Flags**: None

**Synonyms**:
- type II myenteric neuron (PMID:34170401)
- multiaxonal myenteric sensory neuron (PMID:34170401)
- AH-type myenteric neuron (PMID:34170401)

---

## Term 12: Calretinin-positive intrinsic primary afferent neuron of myenteric plexus

**Preferred Label**: calretinin-positive intrinsic primary afferent neuron of myenteric plexus

**Definition**: An intrinsic primary afferent neuron of the myenteric plexus that is immunopositive for calretinin. This neuron shares the Dogiel type II morphology and AH-type electrophysiology of all myenteric IPANs, and is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).

**References**:
- PMID:37355216
- PMID:34170401
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- intrinsic primary afferent neuron of myenteric plexus [NEW Term 3]

**Import Flags**:
- PRO: Find term for calretinin (CALB2 gene product) for `expresses` relation

**Synonyms**:
- SN1 (PMID:37355216)
- calretinin-positive myenteric sensory neuron (PMID:37355216)

---

## Term 13: Calretinin-negative intrinsic primary afferent neuron of myenteric plexus

**Preferred Label**: calretinin-negative intrinsic primary afferent neuron of myenteric plexus

**Definition**: An intrinsic primary afferent neuron of the myenteric plexus that lacks calretinin expression. This neuron shares the Dogiel type II morphology and AH-type electrophysiology of all myenteric IPANs, and is immunopositive for choline acetyltransferase (ChAT) and immunonegative for neuronal nitric oxide synthase (NOS1).

**References**:
- PMID:37355216
- PMID:34170401
- PMID:40954253

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- intrinsic primary afferent neuron of myenteric plexus [NEW Term 3]

**Import Flags**: None

**Synonyms**:
- SN2 (PMID:37355216)
- calretinin-negative myenteric sensory neuron (PMID:37355216)

---

## Term 14: Cholinergic neuron of myenteric plexus

**Preferred Label**: cholinergic neuron of myenteric plexus

**Definition**: An enteric neuron whose soma resides in the myenteric plexus and which is capable of acetylcholine secretion, neurotransmission. This is a defined grouping class that autoclassifies excitatory motor neurons, intrinsic primary afferent neurons, ascending interneurons, and their morphological/chemical subterms.

**References**:
- PMID:37355216
- PMID:34170401

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:0007011 (enteric neuron)
- CL:0000108 (cholinergic neuron)

**Import Flags**:
- Defined class (EquivalentTo): enteric neuron AND `has soma location` UBERON:0002439 AND `capable of` GO:0014055

**Synonyms**:
- ChAT-positive myenteric neuron (PMID:37355216)

---

## Term 15: Nitrergic neuron of myenteric plexus

**Preferred Label**: nitrergic neuron of myenteric plexus

**Definition**: An enteric neuron whose soma resides in the myenteric plexus and which is capable of nitric oxide biosynthetic process. This is a defined grouping class that autoclassifies inhibitory motor neurons and spiny Dogiel type I neurons.

**References**:
- PMID:37355216
- PMID:34170401

**UBERON Terms**:
- UBERON:0002439 (myenteric nerve plexus) — soma location

**Parent CL Terms**:
- CL:0007011 (enteric neuron)

**Import Flags**:
- Defined class (EquivalentTo): enteric neuron AND `has soma location` UBERON:0002439 AND `capable of` GO:0006809
- GO: Update axiom to specific `nitric oxide secretion, neurotransmission` GO term when created

**Synonyms**:
- NOS1-positive myenteric neuron (PMID:37355216)
- nNOS-positive myenteric neuron (PMID:37355216)

---

## Term 16: Dogiel type II neuron (PREREQUISITE — Create First)

**Preferred Label**: Dogiel type II neuron

**Definition**: A neuron characterised by Dogiel type II morphology: a large, smooth, oval soma bearing multiple long axon-like processes (multiaxonal) that extend without branching until they reach their targets. The soma lacks the short lamellar or spiny dendrites characteristic of Dogiel type I neurons. Dogiel type II neurons were first described by Alexander Dogiel in 1899 based on methylene blue staining in gastrointestinal ganglia. In the enteric nervous system, Dogiel type II neurons correspond to intrinsic primary afferent neurons (IPANs) and exhibit AH-type electrophysiology (prolonged afterhyperpolarization following an action potential).

**References**:
- PMID:34170401

**UBERON Terms**: None (general morphological class, not location-specific)

**Parent CL Terms**:
- CL:0000540 (neuron)

**Import Flags**:
- Create as sibling to CL:4047038 (Dogiel type I neuron)
- PATO: Investigate term for multiaxonal morphology

**Synonyms**:
- type II enteric neuron (PMID:34170401)
- multiaxonal enteric neuron (PMID:34170401)
- AH neuron (PMID:34170401)
- Dogiel II neuron (PMID:34170401)

---

# Term Creation Order

**Phase 1 — Prerequisites**:
1. Term 16: Dogiel type II neuron (sibling to CL:4047038)

**Phase 2 — Functional Classes**:
2. Term 1: Excitatory motor neuron of myenteric plexus
3. Term 2: Inhibitory motor neuron of myenteric plexus
4. Term 3: Intrinsic primary afferent neuron of myenteric plexus
5. Term 4: Interneuron of myenteric plexus
6. Term 5: Secretomotor/vasodilator neuron of myenteric plexus
7. Term 6: Intestinofugal neuron

**Phase 3 — Interneuron Subtypes** (require Term 4):
8. Term 7: Ascending interneuron of myenteric plexus
9. Term 8: Descending interneuron of myenteric plexus

**Phase 4 — Morphological Subtypes** (require Phase 2 terms + CL:4047038):
10. Term 9: Stubby Dogiel type I neuron of myenteric plexus
11. Term 10: Spiny Dogiel type I neuron of myenteric plexus
12. Term 11: Dogiel type II neuron of myenteric plexus

**Phase 5 — Chemical Subtypes** (require Term 3):
13. Term 12: Calretinin-positive IPAN of myenteric plexus
14. Term 13: Calretinin-negative IPAN of myenteric plexus

**Phase 6 — Defined Grouping Classes**:
15. Term 14: Cholinergic neuron of myenteric plexus
16. Term 15: Nitrergic neuron of myenteric plexus

---

# Action Items Before Integration

1. **CL:0008014 Check**: Confirm reason for obsoletion before creating Term 1 (excitatory motor neuron of myenteric plexus)
2. **CL:4047038 Scope**: Confirm whether Dogiel type I neuron is already restricted to enteric neurons
3. **CL:0000108 Scope**: Confirm scope before asserting dual parentage on cholinergic grouping class
4. **General Nitrergic Neuron**: Check whether a general 'nitrergic neuron' CL term exists
5. **PRO Import**: Look up calretinin (CALB2 gene product) for Term 12
6. **PATO Terms**: Investigate terms for:
   - Lamellar dendrite morphology (Term 9)
   - Spine-like dendrite morphology (Term 10)
   - Multiaxonal morphology (Terms 11, 16)
7. **GO Request**: Request creation of `nitric oxide secretion, neurotransmission` GO term

---

# Reference Summary

| PMID | Citation | Use |
|------|----------|-----|
| 40954253 | Majd et al. 2025 | Cross-dataset ENS comparison, marker inconsistencies |
| 37355216 | Chen et al. 2023 | Human colonic myenteric neuron IHC (2596 neurons) |
| 34170401 | Brehmer 2021 | Human enteric neuron morphological classification |
| 32888429 | Drokhlyansky et al. 2020 | Mouse/human ENS scRNA-seq, PSVN subtypes |
| 38292899 | Chen et al. 2024 | Human VFN characterization (89% ChAT+, 0% CART+) |
