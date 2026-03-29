# PNS 54 Terms Validation Report (Local Text Scan)

This report scans local text files in `pdfs/` for marker and location mentions.

## Match Status Definitions
- **OK**: Marker AND full location (with segment qualifier like "cervical DRG") found in same paragraph
- **PARTIAL**: Marker found AND location found somewhere in text, but NOT both in same paragraph with full qualifier
- **NO_MATCH**: Marker or location not found in any reference text

## PROPOSED:0001 cervical dorsal root ganglion BRN3A neuron
- marker: POU4F1 (http://identifiers.org/hgnc/9218)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047, https://doi.org/10.1210/en.2011-1545
- matched_files: j.neuroscience.2017.11.047.txt, en.2011-1545.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: nce, 1:750; chicken anti-NF200 from Millipore, 1:25,000; mouse anti-NF200 (clone N52) from Sigma, 1:600 and rabbit anti-Brn-3a from Merck, 1:200) were diluted in 3% goat serum/0.1% TritonX-100 in PBS and applied over night at 4 C. After rin
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0002 cervical dorsal root ganglion CGRP neuron
- marker: CGRP (https://purl.org/ccf/ASCTB-TEMP_cgrp)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: https://doi.org/10.1016/S0304-3940(00)00772-2, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: uorescence in CIPN rats showed that Nav1.7 was upregulated in small DRG neuron somata, especially those also expressing calcitonin gene-related peptide (CGRP), and in central processes of these cells in the superficial spinal dorsal horn. W
- location_snippet: DRG Voltage-Gated Sodium Channel 1.7 Is Upregulated in Paclitaxel-Induced Neuropathy in Rats and in Humans with Neuropathic
- partial_location_snippet: Chemotherapy-induced peripheral neuropathy (CIPN) is a common adverse effect experienced by cancer patients receiving treatment with paclitaxel. The voltage-gated sodium channel 1.7 (Nav1.7) plays an important role in multiple preclinical m

## PROPOSED:0003 cervical dorsal root ganglion Endothelin 1 neuron
- marker: EDN1 (http://identifiers.org/hgnc/3176)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: https://doi.org/10.1073/pnas.86.19.7634
- matched_files: pnas.86.19.7634.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia. The localiz
- location_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia. The localization of endothelin 1 mRNA and endothelin-like immunoreactivity was investigated in samples of neurologica
- partial_location_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia.

## PROPOSED:0004 cervical dorsal root ganglion Nav1.7 neuron
- marker: SCN9A (http://identifiers.org/hgnc/10597)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3, http://dx.doi.org/10.1038/nn.3602, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: s12264-017-0132-3.txt, JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: genetic studies have demonstrated a critical role of Nav1.7 in pain sensation in humans. Loss-of-function mutations in SCN9A, the gene that codes for Nav1.7 in humans, result in a congenital inability to sense pain and anosmia without affec
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel

## PROPOSED:0005 cervical dorsal root ganglion Nav1.9 neuron
- marker: SCN11A (http://identifiers.org/hgnc/10583)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: http://dx.doi.org/10.1016/S0166-2236(02)02150-1, http://dx.doi.org/10.1038/nn.3602
- matched_files: PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: ed in final edited form as: Pain. 2025 February 01; 166(2): 448–459. doi:10.1097/j.pain.0000000000003394. Persistent (NaV1.9) sodium currents in human dorsal root ganglion neurons Xiulin Zhang1,2, Jane E Hartung1, Michael S Gold1,* 1Departm
- location_snippet: Dib-Hajj SD, Tyrrell L, Cummins TR, Black JA, Wood PM, Waxman SG. Two tetrodotoxin- resistant sodium channels in human dorsal root ganglion neurons. FEBS Lett 1999;462(1– 2):117–120. [PubMed: 10580103] [12]. Fang X, Djouhri L, McMullan S, B
- partial_location_snippet: Despite its potential importance in inflammatory if not neuropathic pain syndromes, virtually all that is known about the biophysical and pharmacological properties of NaV1.9 currents has been obtained through the study of rodent sensory ne

## PROPOSED:0006 cervical dorsal root ganglion NF200 neuron
- marker: Neurofilament 200 (NF200) (https://purl.org/ccf/ASCTB-TEMP_neurofilament-200-nf200-)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3,
- matched_files: s12264-017-0132-3.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: , rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1:400, monoclonal NF200H antibody (1:1000, mouse, Sigma) overnight at 4 (cid:3)C. The sections were then incubated for 2 h at room tempera
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0007 cervical dorsal root ganglion Peripherin neuron
- marker: PRPH (http://identifiers.org/hgnc/9461)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3,
- matched_files: s12264-017-0132-3.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0008 cervical dorsal root ganglion Piezo2 neuron
- marker: PIEZO2 (http://identifiers.org/hgnc/26270)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047
- matched_files: j.neuroscience.2017.11.047.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: Trpv1, TrkA and Nav1.6-1.9 were generated based on the sequences used by the Allen brain atlas. Mouse TrkB, TrkC, Ret, Piezo2 as well as human probes for PIEZO2 and RET were obtained from Dr. Hagen Wende (Institute of Pharmacology, Universi
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0009 cervical dorsal root ganglion RET neuron
- marker: receptor tyrosine kinase RET (https://purl.org/ccf/ASCTB-TEMP_receptor-tyrosine-kinase-ret)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047
- matched_files: j.neuroscience.2017.11.047.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: tors, mechanoreceptors and proprioceptors, based on the presence of TRKA, TRKB and TRKC, respectively. By including the receptor tyrosine kinase RET, which is expressed not only in some of the aforementioned subtypes but also in a substanti
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0010 cervical dorsal root ganglion SP neuron
- marker: substance P (SP) (https://purl.org/ccf/ASCTB-TEMP_substance-p-sp-)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: https://doi.org/10.1016/S0304-3940(00)00772-2
- matched_files: PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: earch University of Pittsburgh School of Medicine, Pittsburgh, PA, United States 2Department of Urology, the Second Hospital of Shandong University, 250032, P.R. China Abstract NaV1.9 is of interest to the pain community for a number of r
- location_snippet: Dib-Hajj SD, Tyrrell L, Cummins TR, Black JA, Wood PM, Waxman SG. Two tetrodotoxin- resistant sodium channels in human dorsal root ganglion neurons. FEBS Lett 1999;462(1– 2):117–120. [PubMed: 10580103] [12]. Fang X, Djouhri L, McMullan S, B
- partial_location_snippet: Despite its potential importance in inflammatory if not neuropathic pain syndromes, virtually all that is known about the biophysical and pharmacological properties of NaV1.9 currents has been obtained through the study of rodent sensory ne

## PROPOSED:0011 cervical dorsal root ganglion TRPV1 neuron
- marker: TRPV1 (http://identifiers.org/hgnc/12716)
- soma_location: cervical dorsal root ganglion (UBERON:0002834)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3, https://doi.org/10.1016/j.neuroscience.2017.11.047, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: s12264-017-0132-3.txt, j.neuroscience.2017.11.047.txt, JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: A for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1:400, monoclonal NF200H antibody (1:1000, mouse, Sigma) overnight at 
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0012 ciliary ganglion VIP-PHI neuron
- marker: VIP (http://identifiers.org/hgnc/12693)
- soma_location: main ciliary ganglion (UBERON:0002058)
- references: https://doi.org/10.1002/ar.21516
- matched_files: PMC8788436.txt, PMC6576920.txt, PMC6569016.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: r in controlling the lens or pupil functions [19]. In rats, a few ciliary ganglia and accessory ciliary neurons exhibit VIP immunoreactivity, while, in contrast, in humans and guinea pigs, this immunoreactivity is noted in the uveal ganglio
- location_snippet: ts (parasympathetic pathway); (3) IML→SCG→targets (sympathetic pathway). Trigeminal nerve branches are also present. CG—ciliary ganglion; ChBF—choroidal blood ﬂow; EWpg—nucleus of Edinger-Westphal; preganglionic division; IML—intermediolate
- full_location_snippet: The CG, as a transfer station for the parasympathetic nerve behind the eye, is mainly involved in ocular accommodation and pupil constriction. Around 3% of the postganglionic neurons from CG in macaques were showed heading toward the sphinc

## PROPOSED:0013 intrinsic cardiac ganglion TH neuron
- marker: TH (http://identifiers.org/hgnc/11782)
- soma_location: cardiac ganglion (UBERON:0014463)
- references: http://dx.doi.org/10.1007/s003800300005
- matched_files: PMC8324809.txt, PMC7712215.txt, PMC11594459.txt
- marker_found: True
- location_found: True
- location_partial_found: False
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: iScience ll OPEN ACCESS Article A single cell transcriptomics map of paracrine networks in the intrinsic cardiac nervous system Alison Moss, Shaina Robbins, Sirisha Achanta, ..., Kalyanam Shivkumar, James S. Schw
- location_snippet: ajanikanth Vadigepalli1,6,* SUMMARY We developed a spatially-tracked single neuron transcriptomics map of an intrinsic cardiac ganglion, the right atrial ganglionic plexus (RAGP) that is a critical mediator of sinoatrial node (SAN) activity
- full_location_snippet: SUMMARY We developed a spatially-tracked single neuron transcriptomics map of an intrinsic cardiac ganglion, the right atrial ganglionic plexus (RAGP) that is a critical mediator of sinoatrial node (SAN) activity. This 3D representation of 

## PROPOSED:0014 lumbar dorsal root ganglion BRN3A neuron
- marker: POU4F1 (http://identifiers.org/hgnc/9218)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047, https://doi.org/10.1210/en.2011-1545
- matched_files: j.neuroscience.2017.11.047.txt, en.2011-1545.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: nce, 1:750; chicken anti-NF200 from Millipore, 1:25,000; mouse anti-NF200 (clone N52) from Sigma, 1:600 and rabbit anti-Brn-3a from Merck, 1:200) were diluted in 3% goat serum/0.1% TritonX-100 in PBS and applied over night at 4 C. After rin
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0015 lumbar dorsal root ganglion CGRP neuron
- marker: CGRP (https://purl.org/ccf/ASCTB-TEMP_cgrp)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: https://doi.org/10.1016/S0304-3940(00)00772-2, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: uorescence in CIPN rats showed that Nav1.7 was upregulated in small DRG neuron somata, especially those also expressing calcitonin gene-related peptide (CGRP), and in central processes of these cells in the superficial spinal dorsal horn. W
- location_snippet: DRG Voltage-Gated Sodium Channel 1.7 Is Upregulated in Paclitaxel-Induced Neuropathy in Rats and in Humans with Neuropathic
- partial_location_snippet: Chemotherapy-induced peripheral neuropathy (CIPN) is a common adverse effect experienced by cancer patients receiving treatment with paclitaxel. The voltage-gated sodium channel 1.7 (Nav1.7) plays an important role in multiple preclinical m

## PROPOSED:0016 lumbar dorsal root ganglion Endothelin 1 neuron
- marker: EDN1 (http://identifiers.org/hgnc/3176)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: https://doi.org/10.1073/pnas.86.19.7634
- matched_files: pnas.86.19.7634.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia. The localiz
- location_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia. The localization of endothelin 1 mRNA and endothelin-like immunoreactivity was investigated in samples of neurologica
- partial_location_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia.

## PROPOSED:0017 lumbar dorsal root ganglion Nav1.7 neuron
- marker: SCN9A (http://identifiers.org/hgnc/10597)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3, http://dx.doi.org/10.1038/nn.3602, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: s12264-017-0132-3.txt, JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: genetic studies have demonstrated a critical role of Nav1.7 in pain sensation in humans. Loss-of-function mutations in SCN9A, the gene that codes for Nav1.7 in humans, result in a congenital inability to sense pain and anosmia without affec
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel

## PROPOSED:0018 lumbar dorsal root ganglion Nav1.9 neuron
- marker: SCN11A (http://identifiers.org/hgnc/10583)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: http://dx.doi.org/10.1016/S0166-2236(02)02150-1, http://dx.doi.org/10.1038/nn.3602
- matched_files: PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: ed in final edited form as: Pain. 2025 February 01; 166(2): 448–459. doi:10.1097/j.pain.0000000000003394. Persistent (NaV1.9) sodium currents in human dorsal root ganglion neurons Xiulin Zhang1,2, Jane E Hartung1, Michael S Gold1,* 1Departm
- location_snippet: Dib-Hajj SD, Tyrrell L, Cummins TR, Black JA, Wood PM, Waxman SG. Two tetrodotoxin- resistant sodium channels in human dorsal root ganglion neurons. FEBS Lett 1999;462(1– 2):117–120. [PubMed: 10580103] [12]. Fang X, Djouhri L, McMullan S, B
- partial_location_snippet: Despite its potential importance in inflammatory if not neuropathic pain syndromes, virtually all that is known about the biophysical and pharmacological properties of NaV1.9 currents has been obtained through the study of rodent sensory ne

## PROPOSED:0019 lumbar dorsal root ganglion NF200 neuron
- marker: Neurofilament 200 (NF200) (https://purl.org/ccf/ASCTB-TEMP_neurofilament-200-nf200-)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3,
- matched_files: s12264-017-0132-3.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: , rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1:400, monoclonal NF200H antibody (1:1000, mouse, Sigma) overnight at 4 (cid:3)C. The sections were then incubated for 2 h at room tempera
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0020 lumbar dorsal root ganglion Peripherin neuron
- marker: PRPH (http://identifiers.org/hgnc/9461)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3,
- matched_files: s12264-017-0132-3.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0021 lumbar dorsal root ganglion Piezo2 neuron
- marker: PIEZO2 (http://identifiers.org/hgnc/26270)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047
- matched_files: j.neuroscience.2017.11.047.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: Trpv1, TrkA and Nav1.6-1.9 were generated based on the sequences used by the Allen brain atlas. Mouse TrkB, TrkC, Ret, Piezo2 as well as human probes for PIEZO2 and RET were obtained from Dr. Hagen Wende (Institute of Pharmacology, Universi
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0022 lumbar dorsal root ganglion RET neuron
- marker: receptor tyrosine kinase RET (https://purl.org/ccf/ASCTB-TEMP_receptor-tyrosine-kinase-ret)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047
- matched_files: j.neuroscience.2017.11.047.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: tors, mechanoreceptors and proprioceptors, based on the presence of TRKA, TRKB and TRKC, respectively. By including the receptor tyrosine kinase RET, which is expressed not only in some of the aforementioned subtypes but also in a substanti
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0023 lumbar dorsal root ganglion SP neuron
- marker: substance P (SP) (https://purl.org/ccf/ASCTB-TEMP_substance-p-sp-)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: https://doi.org/10.1016/S0304-3940(00)00772-2
- matched_files: PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: earch University of Pittsburgh School of Medicine, Pittsburgh, PA, United States 2Department of Urology, the Second Hospital of Shandong University, 250032, P.R. China Abstract NaV1.9 is of interest to the pain community for a number of r
- location_snippet: Dib-Hajj SD, Tyrrell L, Cummins TR, Black JA, Wood PM, Waxman SG. Two tetrodotoxin- resistant sodium channels in human dorsal root ganglion neurons. FEBS Lett 1999;462(1– 2):117–120. [PubMed: 10580103] [12]. Fang X, Djouhri L, McMullan S, B
- partial_location_snippet: Despite its potential importance in inflammatory if not neuropathic pain syndromes, virtually all that is known about the biophysical and pharmacological properties of NaV1.9 currents has been obtained through the study of rodent sensory ne

## PROPOSED:0024 lumbar dorsal root ganglion TRPV1 neuron
- marker: TRPV1 (http://identifiers.org/hgnc/12716)
- soma_location: lumbar dorsal root ganglion (UBERON:0002836)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3, https://doi.org/10.1016/j.neuroscience.2017.11.047, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: s12264-017-0132-3.txt, j.neuroscience.2017.11.047.txt, JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: A for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1:400, monoclonal NF200H antibody (1:1000, mouse, Sigma) overnight at 
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0025 myenteric ganglion ChAT neuron
- marker: CHAT (http://identifiers.org/hgnc/1912)
- soma_location: myenteric nerve plexus of small intestine (UBERON:8410063)
- references: http://dx.doi.org/10.1007/s00418-021-02002-y, https://doi.org/10.1016/j.jcmgh.2023.06.010
- matched_files: s00418-021-02002-y.txt, j.jcmgh.2023.06.010.txt, PMC7610403.txt, PMC8099699.txt, PMC11119846.txt, s00441-020-03279-6.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: rentially in the oral direction (about 50% vs. 30% anally; Brehmer et al. 2005). Immunohisto- chemically, they contain choline acetyltransferase (ChAT), leu-enkephalin (ENK) and, partly, SP (Brehmer et al. 2005; Beck et al. 2009). These che
- location_snippet: 021), respectively. Hairy type I neurons Uniaxonal, short-dendritic neurons (“Dogiel type I”) which project from the myenteric plexus to the mucosa were not included in Dogiel’s classification. These Stach type IV neurons were first observe
- full_location_snippet: jejunal mucosa of four infants. In the human stomach, myenteric neurons innervating mucosal cells were char- acterized immunohistochemically, and these neurons were found to contain ChAT, VIP, gastrin-releasing peptide and neuropeptide Y (A

## PROPOSED:0026 myenteric ganglion ChAT/CALR/SOM/SP neuron
- marker: CHAT (http://identifiers.org/hgnc/1912)
- soma_location: myenteric nerve plexus of small intestine (UBERON:8410063)
- references: http://dx.doi.org/10.1007/s00418-007-0335-1, http://dx.doi.org/10.1007/s00418-021-02002-y
- matched_files: s00418-021-02002-y.txt, PMC7610403.txt, PMC8099699.txt, PMC11119846.txt, s00441-020-03279-6.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: rentially in the oral direction (about 50% vs. 30% anally; Brehmer et al. 2005). Immunohisto- chemically, they contain choline acetyltransferase (ChAT), leu-enkephalin (ENK) and, partly, SP (Brehmer et al. 2005; Beck et al. 2009). These che
- location_snippet: 021), respectively. Hairy type I neurons Uniaxonal, short-dendritic neurons (“Dogiel type I”) which project from the myenteric plexus to the mucosa were not included in Dogiel’s classification. These Stach type IV neurons were first observe
- full_location_snippet: jejunal mucosa of four infants. In the human stomach, myenteric neurons innervating mucosal cells were char- acterized immunohistochemically, and these neurons were found to contain ChAT, VIP, gastrin-releasing peptide and neuropeptide Y (A

## PROPOSED:0027 myenteric ganglion NF200 neuron
- marker: Neurofilament 200 (NF200) (https://purl.org/ccf/ASCTB-TEMP_neurofilament-200-nf200-)
- soma_location: myenteric nerve plexus of small intestine (UBERON:8410063)
- references: https://doi.org/10.1016/j.jcmgh.2023.06.010
- matched_files: j.jcmgh.2023.06.010.txt, PMC7610403.txt, PMC8099699.txt, PMC11119846.txt, s00441-020-03279-6.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: neuropeptide Y [NPY], Layer 4: calbindin [Calb], calretinin [Calret], Layer 5: vasoactive intestinal polypeptide [VIP], neurofilament 200 kD [NF200]). VAChT antisera were used for axonal labeling (in layer 3) but were not reliable for nerve
- location_snippet: olinergic AINs (AIN1-3) distinguished by ENK immunoreactivity, which is abundant in varicose axons projecting orally in myenteric ganglia but not in EMNs. There were 6 classes of uniaxonal neurons tentatively identified as DINs (DIN1-6) whi
- full_location_snippet: Types of Neurons in the Human Colonic Myenteric Plexus Identified by Multilayer Immunohistochemical Coding Background and Aims Gut functions including motility, secretion, and blood flow are largely controlled by the enteric nervous system.

## PROPOSED:0028 myenteric ganglion nNOS neuron
- marker: NOS1 (http://identifiers.org/hgnc/7872)
- soma_location: myenteric nerve plexus of small intestine (UBERON:8410063)
- references: http://dx.doi.org/10.1007/s00418-021-02002-y, http://dx.doi.org/10.1159/000320542, https://doi.org/10.1016/j.jcmgh.2023.06.010
- matched_files: s00418-021-02002-y.txt, j.jcmgh.2023.06.010.txt, PMC7610403.txt, PMC8099699.txt, PMC11119846.txt, s00441-020-03279-6.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: euron with an axon (ax) running to the left (i.e. orally). b Corresponding dem- onstration of staining for neuronal nitric oxide synthase (nNOS). The spiny neuron is positive, the stubby one negative (filled and empty arrowhead, respectivel
- location_snippet: 021), respectively. Hairy type I neurons Uniaxonal, short-dendritic neurons (“Dogiel type I”) which project from the myenteric plexus to the mucosa were not included in Dogiel’s classification. These Stach type IV neurons were first observe
- full_location_snippet: Overall, myenteric neurons can be immunohistochemically grouped into two large populations, namely neurons reac- tive for nNOS or for ChAT, as well as into two smaller populations immunoreactive for both or for neither of these markers, res

## PROPOSED:0029 myenteric ganglion nNOS/ChAT neuron
- marker: NOS1 (http://identifiers.org/hgnc/7872)
- soma_location: myenteric nerve plexus of small intestine (UBERON:8410063)
- references: http://dx.doi.org/10.1007/s00418-021-02002-y, https://doi.org/10.1007/s00441-009-0852-4
- matched_files: s00418-021-02002-y.txt, PMC7610403.txt, PMC8099699.txt, PMC11119846.txt, s00441-020-03279-6.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: euron with an axon (ax) running to the left (i.e. orally). b Corresponding dem- onstration of staining for neuronal nitric oxide synthase (nNOS). The spiny neuron is positive, the stubby one negative (filled and empty arrowhead, respectivel
- location_snippet: 021), respectively. Hairy type I neurons Uniaxonal, short-dendritic neurons (“Dogiel type I”) which project from the myenteric plexus to the mucosa were not included in Dogiel’s classification. These Stach type IV neurons were first observe
- full_location_snippet: Overall, myenteric neurons can be immunohistochemically grouped into two large populations, namely neurons reac- tive for nNOS or for ChAT, as well as into two smaller populations immunoreactive for both or for neither of these markers, res

## PROPOSED:0030 myenteric ganglion nNOS/VIP neuron
- marker: NOS1 (http://identifiers.org/hgnc/7872)
- soma_location: myenteric nerve plexus of small intestine (UBERON:8410063)
- references: http://dx.doi.org/10.1007/s00418-021-02002-y, http://dx.doi.org/10.1159/000320542, https://doi.org/10.1007/s00418-005-0107-8
- matched_files: s00418-021-02002-y.txt, PMC7610403.txt, PMC8099699.txt, PMC11119846.txt, s00441-020-03279-6.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: euron with an axon (ax) running to the left (i.e. orally). b Corresponding dem- onstration of staining for neuronal nitric oxide synthase (nNOS). The spiny neuron is positive, the stubby one negative (filled and empty arrowhead, respectivel
- location_snippet: 021), respectively. Hairy type I neurons Uniaxonal, short-dendritic neurons (“Dogiel type I”) which project from the myenteric plexus to the mucosa were not included in Dogiel’s classification. These Stach type IV neurons were first observe
- full_location_snippet: Overall, myenteric neurons can be immunohistochemically grouped into two large populations, namely neurons reac- tive for nNOS or for ChAT, as well as into two smaller populations immunoreactive for both or for neither of these markers, res

## PROPOSED:0031 myenteric ganglion VIP neuron
- marker: VIP (http://identifiers.org/hgnc/12693)
- soma_location: myenteric nerve plexus of small intestine (UBERON:8410063)
- references: https://doi.org/10.1016/j.jcmgh.2023.06.010
- matched_files: j.jcmgh.2023.06.010.txt, PMC7610403.txt, PMC8099699.txt, PMC11119846.txt, s00441-020-03279-6.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: SOM], neuropeptide Y [NPY], Layer 4: calbindin [Calb], calretinin [Calret], Layer 5: vasoactive intestinal polypeptide [VIP], neurofilament 200 kD [NF200]). VAChT antisera were used for axonal labeling (in layer 3) but were not reliable for
- location_snippet: olinergic AINs (AIN1-3) distinguished by ENK immunoreactivity, which is abundant in varicose axons projecting orally in myenteric ganglia but not in EMNs. There were 6 classes of uniaxonal neurons tentatively identified as DINs (DIN1-6) whi
- full_location_snippet: Types of Neurons in the Human Colonic Myenteric Plexus Identified by Multilayer Immunohistochemical Coding Background and Aims Gut functions including motility, secretion, and blood flow are largely controlled by the enteric nervous system.

## PROPOSED:0032 myenteric ganglion VIP/GAL neuron
- marker: VIP (http://identifiers.org/hgnc/12693)
- soma_location: myenteric nerve plexus of small intestine (UBERON:8410063)
- references: http://dx.doi.org/10.1159/000320542
- matched_files: PMC7610403.txt, PMC8099699.txt, PMC11119846.txt, s00441-020-03279-6.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: True
- match_status: OK
- marker_snippet: 4 were assigned to excitatory motor neurons (Tac1/Calb2), while ENC8 and 9 matched inhibitory motor neurons (Nos1/Gal/Vip/Npy). ENC6, 7 and 12 were mapped to IPANs and expressed Nat Neurosci. Author manuscript; available in PMC 2021 June 0
- location_snippet: F u n d e r s A u t h o r M a n u s c r i p t s Morarach et al. Page 5 indicating the dissection plane to retrieve myenteric plexus of small intestine, flow sorting and single cell RNA-sequencing. d) UMAP representation of sequenced cells w
- full_location_snippet: Figure 5. (See previous page). GDNF and NRTN acutely inﬂuence GCaMP activity of largely nonoverlapping adult distal colon myenteric neuron populations. (A–C) Feature plots show Gfra1 primarily in Nos1/Vip/Gal neurons (A), Gfra2 in Chat neur

## PROPOSED:0033 sacral dorsal root ganglion BRN3A neuron
- marker: POU4F1 (http://identifiers.org/hgnc/9218)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047, https://doi.org/10.1210/en.2011-1545
- matched_files: j.neuroscience.2017.11.047.txt, en.2011-1545.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: nce, 1:750; chicken anti-NF200 from Millipore, 1:25,000; mouse anti-NF200 (clone N52) from Sigma, 1:600 and rabbit anti-Brn-3a from Merck, 1:200) were diluted in 3% goat serum/0.1% TritonX-100 in PBS and applied over night at 4 C. After rin
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0034 sacral dorsal root ganglion CGRP neuron
- marker: CGRP (https://purl.org/ccf/ASCTB-TEMP_cgrp)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: https://doi.org/10.1016/S0304-3940(00)00772-2, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: uorescence in CIPN rats showed that Nav1.7 was upregulated in small DRG neuron somata, especially those also expressing calcitonin gene-related peptide (CGRP), and in central processes of these cells in the superficial spinal dorsal horn. W
- location_snippet: DRG Voltage-Gated Sodium Channel 1.7 Is Upregulated in Paclitaxel-Induced Neuropathy in Rats and in Humans with Neuropathic
- partial_location_snippet: Chemotherapy-induced peripheral neuropathy (CIPN) is a common adverse effect experienced by cancer patients receiving treatment with paclitaxel. The voltage-gated sodium channel 1.7 (Nav1.7) plays an important role in multiple preclinical m

## PROPOSED:0035 sacral dorsal root ganglion Endothelin 1 neuron
- marker: EDN1 (http://identifiers.org/hgnc/3176)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: https://doi.org/10.1073/pnas.86.19.7634
- matched_files: pnas.86.19.7634.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia. The localiz
- location_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia. The localization of endothelin 1 mRNA and endothelin-like immunoreactivity was investigated in samples of neurologica
- partial_location_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia.

## PROPOSED:0036 sacral dorsal root ganglion Nav1.7 neuron
- marker: SCN9A (http://identifiers.org/hgnc/10597)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3, http://dx.doi.org/10.1038/nn.3602, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: s12264-017-0132-3.txt, JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: genetic studies have demonstrated a critical role of Nav1.7 in pain sensation in humans. Loss-of-function mutations in SCN9A, the gene that codes for Nav1.7 in humans, result in a congenital inability to sense pain and anosmia without affec
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel

## PROPOSED:0037 sacral dorsal root ganglion Nav1.9 neuron
- marker: SCN11A (http://identifiers.org/hgnc/10583)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: http://dx.doi.org/10.1016/S0166-2236(02)02150-1, http://dx.doi.org/10.1038/nn.3602
- matched_files: PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: ed in final edited form as: Pain. 2025 February 01; 166(2): 448–459. doi:10.1097/j.pain.0000000000003394. Persistent (NaV1.9) sodium currents in human dorsal root ganglion neurons Xiulin Zhang1,2, Jane E Hartung1, Michael S Gold1,* 1Departm
- location_snippet: Dib-Hajj SD, Tyrrell L, Cummins TR, Black JA, Wood PM, Waxman SG. Two tetrodotoxin- resistant sodium channels in human dorsal root ganglion neurons. FEBS Lett 1999;462(1– 2):117–120. [PubMed: 10580103] [12]. Fang X, Djouhri L, McMullan S, B
- partial_location_snippet: Despite its potential importance in inflammatory if not neuropathic pain syndromes, virtually all that is known about the biophysical and pharmacological properties of NaV1.9 currents has been obtained through the study of rodent sensory ne

## PROPOSED:0038 sacral dorsal root ganglion NF200 neuron
- marker: Neurofilament 200 (NF200) (https://purl.org/ccf/ASCTB-TEMP_neurofilament-200-nf200-)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3,
- matched_files: s12264-017-0132-3.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: , rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1:400, monoclonal NF200H antibody (1:1000, mouse, Sigma) overnight at 4 (cid:3)C. The sections were then incubated for 2 h at room tempera
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0039 sacral dorsal root ganglion Peripherin neuron
- marker: PRPH (http://identifiers.org/hgnc/9461)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3,
- matched_files: s12264-017-0132-3.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0040 sacral dorsal root ganglion Piezo2 neuron
- marker: PIEZO2 (http://identifiers.org/hgnc/26270)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047
- matched_files: j.neuroscience.2017.11.047.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: Trpv1, TrkA and Nav1.6-1.9 were generated based on the sequences used by the Allen brain atlas. Mouse TrkB, TrkC, Ret, Piezo2 as well as human probes for PIEZO2 and RET were obtained from Dr. Hagen Wende (Institute of Pharmacology, Universi
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0041 sacral dorsal root ganglion RET neuron
- marker: receptor tyrosine kinase RET (https://purl.org/ccf/ASCTB-TEMP_receptor-tyrosine-kinase-ret)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047
- matched_files: j.neuroscience.2017.11.047.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: tors, mechanoreceptors and proprioceptors, based on the presence of TRKA, TRKB and TRKC, respectively. By including the receptor tyrosine kinase RET, which is expressed not only in some of the aforementioned subtypes but also in a substanti
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0042 sacral dorsal root ganglion SP neuron
- marker: substance P (SP) (https://purl.org/ccf/ASCTB-TEMP_substance-p-sp-)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: https://doi.org/10.1016/S0304-3940(00)00772-2
- matched_files: PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: earch University of Pittsburgh School of Medicine, Pittsburgh, PA, United States 2Department of Urology, the Second Hospital of Shandong University, 250032, P.R. China Abstract NaV1.9 is of interest to the pain community for a number of r
- location_snippet: Dib-Hajj SD, Tyrrell L, Cummins TR, Black JA, Wood PM, Waxman SG. Two tetrodotoxin- resistant sodium channels in human dorsal root ganglion neurons. FEBS Lett 1999;462(1– 2):117–120. [PubMed: 10580103] [12]. Fang X, Djouhri L, McMullan S, B
- partial_location_snippet: Despite its potential importance in inflammatory if not neuropathic pain syndromes, virtually all that is known about the biophysical and pharmacological properties of NaV1.9 currents has been obtained through the study of rodent sensory ne

## PROPOSED:0043 sacral dorsal root ganglion TRPV1 neuron
- marker: TRPV1 (http://identifiers.org/hgnc/12716)
- soma_location: sacral dorsal root ganglion (UBERON:0002837)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3, https://doi.org/10.1016/j.neuroscience.2017.11.047, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: s12264-017-0132-3.txt, j.neuroscience.2017.11.047.txt, JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: A for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1:400, monoclonal NF200H antibody (1:1000, mouse, Sigma) overnight at 
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0044 thoracic dorsal root ganglion BRN3A neuron
- marker: POU4F1 (http://identifiers.org/hgnc/9218)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047, https://doi.org/10.1210/en.2011-1545
- matched_files: j.neuroscience.2017.11.047.txt, en.2011-1545.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: nce, 1:750; chicken anti-NF200 from Millipore, 1:25,000; mouse anti-NF200 (clone N52) from Sigma, 1:600 and rabbit anti-Brn-3a from Merck, 1:200) were diluted in 3% goat serum/0.1% TritonX-100 in PBS and applied over night at 4 C. After rin
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0045 thoracic dorsal root ganglion CGRP neuron
- marker: CGRP (https://purl.org/ccf/ASCTB-TEMP_cgrp)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: https://doi.org/10.1016/S0304-3940(00)00772-2, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: uorescence in CIPN rats showed that Nav1.7 was upregulated in small DRG neuron somata, especially those also expressing calcitonin gene-related peptide (CGRP), and in central processes of these cells in the superficial spinal dorsal horn. W
- location_snippet: DRG Voltage-Gated Sodium Channel 1.7 Is Upregulated in Paclitaxel-Induced Neuropathy in Rats and in Humans with Neuropathic
- partial_location_snippet: Chemotherapy-induced peripheral neuropathy (CIPN) is a common adverse effect experienced by cancer patients receiving treatment with paclitaxel. The voltage-gated sodium channel 1.7 (Nav1.7) plays an important role in multiple preclinical m

## PROPOSED:0046 thoracic dorsal root ganglion Endothelin 1 neuron
- marker: EDN1 (http://identifiers.org/hgnc/3176)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: https://doi.org/10.1073/pnas.86.19.7634
- matched_files: pnas.86.19.7634.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia. The localiz
- location_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia. The localization of endothelin 1 mRNA and endothelin-like immunoreactivity was investigated in samples of neurologica
- partial_location_snippet: Endothelin 1, an endothelium-derived peptide, is expressed in neurons of the human spinal cord and dorsal root ganglia.

## PROPOSED:0047 thoracic dorsal root ganglion Nav1.7 neuron
- marker: SCN9A (http://identifiers.org/hgnc/10597)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3, http://dx.doi.org/10.1038/nn.3602, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: s12264-017-0132-3.txt, JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: genetic studies have demonstrated a critical role of Nav1.7 in pain sensation in humans. Loss-of-function mutations in SCN9A, the gene that codes for Nav1.7 in humans, result in a congenital inability to sense pain and anosmia without affec
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel

## PROPOSED:0048 thoracic dorsal root ganglion Nav1.9 neuron
- marker: SCN11A (http://identifiers.org/hgnc/10583)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: http://dx.doi.org/10.1016/S0166-2236(02)02150-1, http://dx.doi.org/10.1038/nn.3602
- matched_files: PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: ed in final edited form as: Pain. 2025 February 01; 166(2): 448–459. doi:10.1097/j.pain.0000000000003394. Persistent (NaV1.9) sodium currents in human dorsal root ganglion neurons Xiulin Zhang1,2, Jane E Hartung1, Michael S Gold1,* 1Departm
- location_snippet: Dib-Hajj SD, Tyrrell L, Cummins TR, Black JA, Wood PM, Waxman SG. Two tetrodotoxin- resistant sodium channels in human dorsal root ganglion neurons. FEBS Lett 1999;462(1– 2):117–120. [PubMed: 10580103] [12]. Fang X, Djouhri L, McMullan S, B
- partial_location_snippet: Despite its potential importance in inflammatory if not neuropathic pain syndromes, virtually all that is known about the biophysical and pharmacological properties of NaV1.9 currents has been obtained through the study of rodent sensory ne

## PROPOSED:0049 thoracic dorsal root ganglion NF200 neuron
- marker: Neurofilament 200 (NF200) (https://purl.org/ccf/ASCTB-TEMP_neurofilament-200-nf200-)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3,
- matched_files: s12264-017-0132-3.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: , rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1:400, monoclonal NF200H antibody (1:1000, mouse, Sigma) overnight at 4 (cid:3)C. The sections were then incubated for 2 h at room tempera
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0050 thoracic dorsal root ganglion Peripherin neuron
- marker: PRPH (http://identifiers.org/hgnc/9461)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3,
- matched_files: s12264-017-0132-3.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

## PROPOSED:0051 thoracic dorsal root ganglion Piezo2 neuron
- marker: PIEZO2 (http://identifiers.org/hgnc/26270)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047
- matched_files: j.neuroscience.2017.11.047.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: Trpv1, TrkA and Nav1.6-1.9 were generated based on the sequences used by the Allen brain atlas. Mouse TrkB, TrkC, Ret, Piezo2 as well as human probes for PIEZO2 and RET were obtained from Dr. Hagen Wende (Institute of Pharmacology, Universi
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0052 thoracic dorsal root ganglion RET neuron
- marker: receptor tyrosine kinase RET (https://purl.org/ccf/ASCTB-TEMP_receptor-tyrosine-kinase-ret)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: https://doi.org/10.1016/j.neuroscience.2017.11.047
- matched_files: j.neuroscience.2017.11.047.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: tors, mechanoreceptors and proprioceptors, based on the presence of TRKA, TRKB and TRKC, respectively. By including the receptor tyrosine kinase RET, which is expressed not only in some of the aforementioned subtypes but also in a substanti
- location_snippet: repancies from homoscedasticity or normality. Results Expression of neurotrophin receptors Somatosensory neurons in the dorsal root ganglion (DRG) are a heterogeneous population of cells that can detect and transduce a variety of different 
- partial_location_snippet: Human vs. Mouse Nociceptors - Similarities and Differences Highlights Comparative analysis of TrkA expressing nociceptors in human versus mouse dorsal rot ganglia. Double fluorescence in situ hybridization to assess similarities and differe

## PROPOSED:0053 thoracic dorsal root ganglion SP neuron
- marker: substance P (SP) (https://purl.org/ccf/ASCTB-TEMP_substance-p-sp-)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: https://doi.org/10.1016/S0304-3940(00)00772-2
- matched_files: PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: earch University of Pittsburgh School of Medicine, Pittsburgh, PA, United States 2Department of Urology, the Second Hospital of Shandong University, 250032, P.R. China Abstract NaV1.9 is of interest to the pain community for a number of r
- location_snippet: Dib-Hajj SD, Tyrrell L, Cummins TR, Black JA, Wood PM, Waxman SG. Two tetrodotoxin- resistant sodium channels in human dorsal root ganglion neurons. FEBS Lett 1999;462(1– 2):117–120. [PubMed: 10580103] [12]. Fang X, Djouhri L, McMullan S, B
- partial_location_snippet: Despite its potential importance in inflammatory if not neuropathic pain syndromes, virtually all that is known about the biophysical and pharmacological properties of NaV1.9 currents has been obtained through the study of rodent sensory ne

## PROPOSED:0054 thoracic dorsal root ganglion TRPV1 neuron
- marker: TRPV1 (http://identifiers.org/hgnc/12716)
- soma_location: thoracic dorsal root ganglion (UBERON:0002835)
- references: http://dx.doi.org/10.1007/s12264-017-0132-3, https://doi.org/10.1016/j.neuroscience.2017.11.047, https://doi.org/10.1523/JNEUROSCI.0899-17.2017
- matched_files: s12264-017-0132-3.txt, j.neuroscience.2017.11.047.txt, JNEUROSCI.0899-17.2017.txt, PMC11723807.txt, PMC8929296.txt, 10.1186_1744-8069-3-42.txt, PMC6564303.txt
- marker_found: True
- location_found: False
- location_partial_found: True
- marker_and_partial_location_same_paragraph: True
- marker_and_full_location_same_paragraph: False
- match_status: PARTIAL
- marker_snippet: A for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mixture of primary polyclonal TRPV1 rabbit, Neuromics, Edina, MN) and antibody (1:400, monoclonal NF200H antibody (1:1000, mouse, Sigma) overnight at 
- location_snippet: L A R T I C L E www.neurosci.cn www.springer.com/12264 Expression and Role of Voltage-Gated Sodium Channels in Human Dorsal Root Ganglion Neurons with Special Focus on Nav1.7, Species Differences, and Regulation by Paclitaxel Wonseok Chang1
- partial_location_snippet: Human DRGs were ﬁxed in 4% paraformaldehyde over- night and then sections (12 lm) were cut on a cryostat. The sections were ﬁrst blocked with 2% BSA for 1 h at room temperature, then incubated with peripherin (1:500, rabbit, Sigma) or a mix

