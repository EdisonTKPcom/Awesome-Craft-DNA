<div align="center">

# Awesome Craft DNA [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source tools for DNA, genomics and synthetic biology.

<img src="assets/craft-dna.svg" alt="Pixel-art laboratory scene with a rotating double helix and a generic sequencer reading coloured bases" width="100%">

![Tools](https://img.shields.io/badge/tools-63-6366f1?style=for-the-badge)
[![Categories](https://img.shields.io/badge/categories-14-0ea5e9?style=for-the-badge)](#contents)
[![Combined stars](https://img.shields.io/badge/combined_stars-101.9k-f59e0b?style=for-the-badge&logo=github)](#-leaderboard)
[![Stars](https://img.shields.io/github/stars/EdisonTKPcom/Awesome-Craft-DNA?style=for-the-badge&color=22c55e)](https://github.com/EdisonTKPcom/Awesome-Craft-DNA/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/EdisonTKPcom/Awesome-Craft-DNA?style=for-the-badge&color=ec4899)](https://github.com/EdisonTKPcom/Awesome-Craft-DNA/commits/main)

</div>

This list covers open-source software for reading, writing, analysing and designing DNA, RNA and proteins: aligners, variant callers, long-read tools, assemblers, workflow managers, genome browsers, single-cell and RNA-seq packages, structure and sequence models, synthetic-biology design tools, DNA storage codecs, lab automation, libraries, personal-genomics utilities, and public datasets and standards. Every entry below has a public repository that was checked on 2026-11-15. Check each project's licence, including any separate terms for model weights, before you use it.

**Biosafety and ethics:** this list is for research, engineering and education. It is not guidance on pathogen enhancement, gain-of-function work, or the design of harmful biological agents, and it does not list tools whose purpose is that work. Sequence models and gene-editing design tools can be dual-use. Use them only in line with the law, institutional biosafety rules, and each project's own terms.

**Privacy:** personal and consumer genomic files are sensitive. Prefer tools that run on a machine you control, do not upload raw genotypes to a third-party service unless you understand and accept that service's terms, and never post those files in public issues, chats or repositories.


## Contents

- [Dashboard](#dashboard)
- [Sequence alignment and mapping](#sequence-alignment-and-mapping)
- [Variant calling](#variant-calling)
- [Nanopore and long-read](#nanopore-and-long-read)
- [Assembly](#assembly)
- [Workflow managers](#workflow-managers)
- [Genome browsers and visualisation](#genome-browsers-and-visualisation)
- [Single-cell and RNA-seq](#single-cell-and-rna-seq)
- [Protein structure and AI bio models](#protein-structure-and-ai-bio-models)
- [Synthetic biology and DNA design](#synthetic-biology-and-dna-design)
- [DNA data storage](#dna-data-storage)
- [Lab automation](#lab-automation)
- [Libraries](#libraries)
- [Personal genomics](#personal-genomics)
- [Public datasets and standards](#public-datasets-and-standards)
- [Related lists](#related-lists)
- [Star history](#star-history)


## Dashboard

<style>
.dna-fact{border-bottom:3px solid #0f172a;padding-bottom:1px}
.dna-goal{border-bottom:3px dashed #0f172a;padding-bottom:1px}
.dna-est{border-bottom:3px dotted #0f172a;padding-bottom:1px}
</style>

<table>
<tr>
<td align="center"><h2><span class="dna-fact">63</span></h2>listed projects</td>
<td align="center"><h2><span class="dna-fact">14</span></h2>categories</td>
<td align="center"><h2><span class="dna-est">101.9k</span></h2>combined GitHub stars</td>
<td align="center"><h2><span class="dna-est">25.0k</span></h2>combined forks</td>
<td align="center"><h2><span class="dna-est">39/63</span></h2>pushed in the last 30 days</td>
<td align="center"><h2><span class="dna-fact">14</span></h2>languages</td>
</tr>
</table>

**Evidence tags**

<table>
<tr><th>Tag</th><th>Style</th><th>Meaning</th></tr>
<tr><td><span class="dna-fact">FACT</span></td><td>solid underline</td><td>A measured figure, with the source named.</td></tr>
<tr><td><span class="dna-goal">GOAL</span></td><td>dashed underline</td><td>A stated roadmap or plan, not a result.</td></tr>
<tr><td><span class="dna-est">ESTIMATE</span></td><td>dotted underline</td><td>A sum or count we computed from the facts.</td></tr>
</table>

This snapshot has no GOAL figures. None of the dashboard numbers come from project roadmaps.

**Sources and method**

- Star counts, fork counts, licences, primary languages and last-push dates are <span class="dna-fact">FACT</span> values from the GitHub REST API (`GET /repos/{owner}/{repo}`) on 2026-11-15.
- Combined stars (<span class="dna-est">101.9k</span>) and combined forks (<span class="dna-est">25.0k</span>) are <span class="dna-est">ESTIMATE</span>s: the arithmetic sum of those per-repository FACT counts, with no weighting and no unique-user deduplication. A person who stars two projects is counted twice.
- Pushed in the last 30 days (<span class="dna-est">39/63</span>) is an <span class="dna-est">ESTIMATE</span>: the number of listed repositories whose FACT `pushed_at` date is on or after 2026-10-16.
- Language and category counts, and the licence badges, are <span class="dna-est">ESTIMATE</span>s of FACT fields. Star badges next to each entry update live and may differ from this snapshot.

### 🏆 Leaderboard

Star counts in this table are FACT values from the snapshot. The bars are only a visual scale.

<table>
<tr><th>Rank</th><th>Project</th><th>Kind</th><th align="right">Stars</th><th></th></tr>
<tr><td align="center">🥇</td><td><b>AlphaFold 2</b></td><td>Protein structure and AI bio models</td><td align="right"><span class="dna-fact">14.9k</span></td><td><code>████████████████████</code></td></tr>
<tr><td align="center">🥈</td><td><b>AlphaFold 3</b></td><td>Protein structure and AI bio models</td><td align="right"><span class="dna-fact">8.8k</span></td><td><code>████████████</code></td></tr>
<tr><td align="center">🥉</td><td><b>Biopython</b></td><td>Libraries</td><td align="right"><span class="dna-fact">5.3k</span></td><td><code>███████</code></td></tr>
<tr><td align="center">4</td><td><b>Evo 2</b></td><td>Protein structure and AI bio models</td><td align="right"><span class="dna-fact">4.3k</span></td><td><code>██████</code></td></tr>
<tr><td align="center">5</td><td><b>Boltz</b></td><td>Protein structure and AI bio models</td><td align="right"><span class="dna-fact">4.3k</span></td><td><code>██████</code></td></tr>
<tr><td align="center">6</td><td><b>DeepVariant</b></td><td>Variant calling</td><td align="right"><span class="dna-fact">3.8k</span></td><td><code>█████</code></td></tr>
<tr><td align="center">7</td><td><b>Nextflow</b></td><td>Workflow managers</td><td align="right"><span class="dna-fact">3.5k</span></td><td><code>█████</code></td></tr>
<tr><td align="center">8</td><td><b>OpenFold</b></td><td>Protein structure and AI bio models</td><td align="right"><span class="dna-fact">3.5k</span></td><td><code>█████</code></td></tr>
<tr><td align="center">9</td><td><b>ESM</b></td><td>Protein structure and AI bio models</td><td align="right"><span class="dna-fact">3.0k</span></td><td><code>████</code></td></tr>
<tr><td align="center">10</td><td><b>ColabFold</b></td><td>Protein structure and AI bio models</td><td align="right"><span class="dna-fact">3.0k</span></td><td><code>████</code></td></tr>
</table>


### Stars by category

These category totals are ESTIMATE sums of the per-repository FACT star counts.

```mermaid
pie showData
    title Combined GitHub stars by category
    "Sequence alignment and mapping" : 7684
    "Variant calling" : 10557
    "Nanopore and long-read" : 2479
    "Assembly" : 2498
    "Workflow managers" : 9738
    "Genome browsers and visualisation" : 1348
    "Single-cell and RNA-seq" : 8881
    "Protein structure and AI bio models" : 45057
    "Synthetic biology and DNA design" : 1983
    "DNA data storage" : 208
    "Lab automation" : 1187
    "Libraries" : 7760
    "Personal genomics" : 342
    "Public datasets and standards" : 2205
```

### Licences

![Custom](https://img.shields.io/badge/Custom-19-64748b?style=flat-square) ![MIT](https://img.shields.io/badge/MIT-15-64748b?style=flat-square) ![Apache-2.0](https://img.shields.io/badge/Apache--2.0-11-64748b?style=flat-square) ![BSD-3-Clause](https://img.shields.io/badge/BSD--3--Clause-9-64748b?style=flat-square) ![GPL-3.0](https://img.shields.io/badge/GPL--3.0-4-64748b?style=flat-square) ![None](https://img.shields.io/badge/None-3-64748b?style=flat-square) ![BSD-2-Clause](https://img.shields.io/badge/BSD--2--Clause-1-64748b?style=flat-square) ![AGPL-3.0](https://img.shields.io/badge/AGPL--3.0-1-64748b?style=flat-square)

These badge counts are ESTIMATE tallies of the SPDX identifier GitHub returned for each repository. "Custom" or "None" means GitHub could not match a standard SPDX licence. Dorado and Medaka use the Oxford Nanopore Technologies PLC Public License Version 1.0, which is not an OSI licence. Nucleotide Transformer code is CC BY-NC-SA 4.0, and its model weights use the InstaDeep Open Model Licence v1.0, which is limited to non-commercial use unless you have a separate licence. AlphaFold 3 code is Apache-2.0, but its model parameters and outputs have separate non-commercial terms. The UCSC kent tree is mixed: most command-line tools are MIT, while the Genome Browser CGIs and BLAT/isPCR are under non-commercial licences. OpenCRISPR has no SPDX licence file; commercial therapeutic use requires Profluent's licence agreement. Read each project licence, and any weight or output terms, before you use it commercially.

## Sequence alignment and mapping

- [Bowtie 2](https://github.com/BenLangmead/bowtie2) - Fast gapped short-read aligner. ![Stars](https://img.shields.io/github/stars/BenLangmead/bowtie2?style=flat-square&label=%E2%AD%90)
- [BWA](https://github.com/lh3/bwa) - Burrows-Wheeler short-read aligner. ![Stars](https://img.shields.io/github/stars/lh3/bwa?style=flat-square&label=%E2%AD%90)
- [HISAT2](https://github.com/DaehwanKimLab/hisat2) - Graph-based, splice-aware aligner that uses a hierarchical graph FM index. ![Stars](https://img.shields.io/github/stars/DaehwanKimLab/hisat2?style=flat-square&label=%E2%AD%90)
- [minimap2](https://github.com/lh3/minimap2) - Versatile pairwise aligner for genomic and spliced nucleotide sequences, including long reads. GitHub reports no SPDX licence; the repository LICENSE.txt is the MIT licence. ![Stars](https://img.shields.io/github/stars/lh3/minimap2?style=flat-square&label=%E2%AD%90)
- [STAR](https://github.com/alexdobin/STAR) - Splice-aware RNA-seq aligner for short reads. Last push 2025-03-18. ![Stars](https://img.shields.io/github/stars/alexdobin/STAR?style=flat-square&label=%E2%AD%90)

## Variant calling

- [bcftools](https://github.com/samtools/bcftools) - Utilities for variant calling and VCF/BCF manipulation, part of the samtools suite. GitHub reports no SPDX licence; the samtools suite LICENSE is the MIT/Expat licence. ![Stars](https://img.shields.io/github/stars/samtools/bcftools?style=flat-square&label=%E2%AD%90)
- [DeepVariant](https://github.com/google/deepvariant) - Deep-learning variant caller from Google. ![Stars](https://img.shields.io/github/stars/google/deepvariant?style=flat-square&label=%E2%AD%90)
- [FreeBayes](https://github.com/freebayes/freebayes) - Bayesian haplotype-based variant caller. ![Stars](https://img.shields.io/github/stars/freebayes/freebayes?style=flat-square&label=%E2%AD%90)
- [GATK](https://github.com/broadinstitute/gatk) - Broad Institute Genome Analysis Toolkit for variant discovery, versions 4 and later. GitHub reports no SPDX licence; LICENSE.TXT states Apache-2.0. ![Stars](https://img.shields.io/github/stars/broadinstitute/gatk?style=flat-square&label=%E2%AD%90)
- [htslib](https://github.com/samtools/htslib) - C library for high-throughput sequencing formats such as SAM, BAM, CRAM and VCF. GitHub reports no SPDX licence; the related samtools LICENSE is the MIT/Expat licence. ![Stars](https://img.shields.io/github/stars/samtools/htslib?style=flat-square&label=%E2%AD%90)
- [samtools](https://github.com/samtools/samtools) - Tools for reading, writing and manipulating SAM, BAM and CRAM files. GitHub reports no SPDX licence; the LICENSE file is the MIT/Expat licence. ![Stars](https://img.shields.io/github/stars/samtools/samtools?style=flat-square&label=%E2%AD%90)

## Nanopore and long-read

- [Dorado](https://github.com/nanoporetech/dorado) - Oxford Nanopore's production basecaller. The repository uses the Oxford Nanopore Technologies PLC Public License Version 1.0, which is not an OSI licence. Read it before any commercial use. ![Stars](https://img.shields.io/github/stars/nanoporetech/dorado?style=flat-square&label=%E2%AD%90)
- [Flye](https://github.com/mikolmogorov/Flye) - De novo assembler for single-molecule long reads, using repeat graphs. GitHub reports no SPDX licence; the repository LICENSE is BSD-3-Clause. ![Stars](https://img.shields.io/github/stars/mikolmogorov/Flye?style=flat-square&label=%E2%AD%90)
- [Medaka](https://github.com/nanoporetech/medaka) - Neural-network consensus polishing and variant calling for Oxford Nanopore sequences. The repository uses the Oxford Nanopore Technologies PLC Public License Version 1.0, which is not an OSI licence. ![Stars](https://img.shields.io/github/stars/nanoporetech/medaka?style=flat-square&label=%E2%AD%90)
- [slow5tools](https://github.com/hasindu2008/slow5tools) - Toolkit for converting, compressing and viewing SLOW5 and BLOW5 signal files, an open alternative to FAST5. ![Stars](https://img.shields.io/github/stars/hasindu2008/slow5tools?style=flat-square&label=%E2%AD%90)

## Assembly

- [Canu](https://github.com/marbl/canu) - Long-read assembler for large genomes, descended from the Celera Assembler. GitHub reports no SPDX licence; the distribution is a joint work under GPL-2.0, with some BSD-3-Clause contributions. ![Stars](https://img.shields.io/github/stars/marbl/canu?style=flat-square&label=%E2%AD%90)
- [hifiasm](https://github.com/chhylp123/hifiasm) - Haplotype-resolved assembler for PacBio HiFi reads. ![Stars](https://img.shields.io/github/stars/chhylp123/hifiasm?style=flat-square&label=%E2%AD%90)
- [SPAdes](https://github.com/ablab/spades) - St. Petersburg genome assembler for short and hybrid reads, including isolate and metagenomic modes. GitHub reports no SPDX licence, so read the repository before you use it commercially. ![Stars](https://img.shields.io/github/stars/ablab/spades?style=flat-square&label=%E2%AD%90)

## Workflow managers

- [Cromwell](https://github.com/broadinstitute/cromwell) - Scientific workflow engine from the Broad Institute, with first-class support for WDL. ![Stars](https://img.shields.io/github/stars/broadinstitute/cromwell?style=flat-square&label=%E2%AD%90)
- [Galaxy](https://github.com/galaxyproject/galaxy) - Web platform for accessible, reproducible data-intensive analysis, with a large tool shed for genomics. GitHub reports no SPDX licence, so read the repository before you use it commercially. ![Stars](https://img.shields.io/github/stars/galaxyproject/galaxy?style=flat-square&label=%E2%AD%90)
- [Nextflow](https://github.com/nextflow-io/nextflow) - Data-driven workflow language and runtime, widely used for genomics pipelines. ![Stars](https://img.shields.io/github/stars/nextflow-io/nextflow?style=flat-square&label=%E2%AD%90)
- [nf-core tools](https://github.com/nf-core/tools) - Helper CLI for the nf-core community of curated Nextflow pipelines. ![Stars](https://img.shields.io/github/stars/nf-core/tools?style=flat-square&label=%E2%AD%90)
- [Snakemake](https://github.com/snakemake/snakemake) - Python-based workflow management system with a large genomics ecosystem. ![Stars](https://img.shields.io/github/stars/snakemake/snakemake?style=flat-square&label=%E2%AD%90)

## Genome browsers and visualisation

- [IGV](https://github.com/igvteam/igv) - Integrative Genomics Viewer, a desktop app for exploring alignments, variants and annotations. ![Stars](https://img.shields.io/github/stars/igvteam/igv?style=flat-square&label=%E2%AD%90)
- [JBrowse 2](https://github.com/GMOD/jbrowse-components) - Modern React-based genome browser from GMOD, the successor to JBrowse 1. ![Stars](https://img.shields.io/github/stars/GMOD/jbrowse-components?style=flat-square&label=%E2%AD%90)
- [UCSC kent tools](https://github.com/ucscGenomeBrowser/kent) - Source for the UCSC Genome Browser and its command-line tools. The default licence is MIT, but the interactive Genome Browser CGI programs and the BLAT/isPCR suite use separate non-commercial licences. Commercial use of those parts needs a licence from UCSC or Kent Informatics. ![Stars](https://img.shields.io/github/stars/ucscGenomeBrowser/kent?style=flat-square&label=%E2%AD%90)

## Single-cell and RNA-seq

- [kallisto](https://github.com/pachterlab/kallisto) - Near-optimal RNA-seq transcript quantification with pseudoalignment. ![Stars](https://img.shields.io/github/stars/pachterlab/kallisto?style=flat-square&label=%E2%AD%90)
- [Salmon](https://github.com/COMBINE-lab/salmon) - Accurate, fast transcript-level quantification from RNA-seq reads. ![Stars](https://img.shields.io/github/stars/COMBINE-lab/salmon?style=flat-square&label=%E2%AD%90)
- [Scanpy](https://github.com/scverse/scanpy) - Scalable single-cell analysis in Python, part of the scverse ecosystem. ![Stars](https://img.shields.io/github/stars/scverse/scanpy?style=flat-square&label=%E2%AD%90)
- [scvi-tools](https://github.com/scverse/scvi-tools) - Deep probabilistic models for single-cell and spatial omics. ![Stars](https://img.shields.io/github/stars/scverse/scvi-tools?style=flat-square&label=%E2%AD%90)
- [Seurat](https://github.com/satijalab/seurat) - R toolkit for single-cell genomics. GitHub reports no SPDX licence, so read the repository before you use it commercially. ![Stars](https://img.shields.io/github/stars/satijalab/seurat?style=flat-square&label=%E2%AD%90)

## Protein structure and AI bio models

- [AlphaFold 2](https://github.com/google-deepmind/alphafold) - Open-source code for AlphaFold 2 structure prediction. The code is Apache-2.0; the model parameters have a separate licence, so check the repository before you use the weights. ![Stars](https://img.shields.io/github/stars/google-deepmind/alphafold?style=flat-square&label=%E2%AD%90)
- [AlphaFold 3](https://github.com/google-deepmind/alphafold3) - Inference pipeline for AlphaFold 3. The code is Apache-2.0, but the model parameters and outputs are covered by separate non-commercial terms in WEIGHTS_TERMS_OF_USE.md and OUTPUT_TERMS_OF_USE.md. ![Stars](https://img.shields.io/github/stars/google-deepmind/alphafold3?style=flat-square&label=%E2%AD%90)
- [Boltz](https://github.com/jwohlwend/boltz) - Biomolecular interaction models, including structure prediction of complexes. ![Stars](https://img.shields.io/github/stars/jwohlwend/boltz?style=flat-square&label=%E2%AD%90)
- [ColabFold](https://github.com/sokrypton/ColabFold) - Accessible protein-folding notebooks and pipeline built around AlphaFold 2 and related models. ![Stars](https://img.shields.io/github/stars/sokrypton/ColabFold?style=flat-square&label=%E2%AD%90)
- [ESM](https://github.com/Biohub/esm) - Current Evolutionary Scale Modeling codebase, now hosted at Biohub after a move from evolutionaryscale/esm. GitHub reports no SPDX licence; LICENSE.md is the MIT licence. The earlier ESM-2 and ESMFold code lives in the archived facebookresearch/esm repository, also MIT. ![Stars](https://img.shields.io/github/stars/Biohub/esm?style=flat-square&label=%E2%AD%90)
- [Evo 2](https://github.com/ArcInstitute/evo2) - Genome language models for modeling and design across domains of life, from the Arc Institute. The code is Apache-2.0. Use sequence models in line with institutional biosafety rules; this list does not cover work on harmful agents. ![Stars](https://img.shields.io/github/stars/ArcInstitute/evo2?style=flat-square&label=%E2%AD%90)
- [Nucleotide Transformer](https://github.com/instadeepai/nucleotide-transformer) - Foundation models for genomics and transcriptomics from InstaDeep. LICENSE.md is CC BY-NC-SA 4.0, which is not an OSI software licence, and MODEL-LICENSE.md (InstaDeep Open Model Licence v1.0) limits model-weight use to non-commercial purposes unless you have a separate licence. ![Stars](https://img.shields.io/github/stars/instadeepai/nucleotide-transformer?style=flat-square&label=%E2%AD%90)
- [OpenFold](https://github.com/aqlaboratory/openfold) - Trainable, memory-efficient PyTorch reproduction of AlphaFold 2. ![Stars](https://img.shields.io/github/stars/aqlaboratory/openfold?style=flat-square&label=%E2%AD%90)
- [RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold) - Deep-learning protein structure prediction from RosettaCommons. Last push 2024-02-15. ![Stars](https://img.shields.io/github/stars/RosettaCommons/RoseTTAFold?style=flat-square&label=%E2%AD%90)

## Synthetic biology and DNA design

- [Cas-OFFinder](https://github.com/snugel/cas-offinder) - Fast search for potential CRISPR off-target sites. GitHub reports no SPDX licence, so read the repository before you use it commercially. Last push 2022-08-31. ![Stars](https://img.shields.io/github/stars/snugel/cas-offinder?style=flat-square&label=%E2%AD%90)
- [CRISPOR](https://github.com/maximilianh/crisporWebsite) - Source for the CRISPOR.org CRISPR guide-design website. GitHub reports no SPDX licence, so read the repository before you use it commercially. ![Stars](https://img.shields.io/github/stars/maximilianh/crisporWebsite?style=flat-square&label=%E2%AD%90)
- [DNA Chisel](https://github.com/Edinburgh-Genome-Foundry/DnaChisel) - Python DNA sequence optimizer for recoding, constraint satisfaction and synthesis-friendly design. ![Stars](https://img.shields.io/github/stars/Edinburgh-Genome-Foundry/DnaChisel?style=flat-square&label=%E2%AD%90)
- [OpenCRISPR](https://github.com/Profluent-AI/OpenCRISPR) - AI-designed CRISPR gene-editing systems from Profluent Bio, including the OpenCRISPR-1 sequence release. GitHub reports no SPDX licence. The authors say the sequences are free for research and commercial use, but commercial therapeutic use requires their licence agreement. ![Stars](https://img.shields.io/github/stars/Profluent-AI/OpenCRISPR?style=flat-square&label=%E2%AD%90)
- [pydna](https://github.com/pydna-group/pydna) - Python data structures for double-stranded DNA and simulation of cloning, including Gibson assembly and restriction cloning. GitHub reports no SPDX licence; LICENSE.txt is a BSD-3-Clause licence. ![Stars](https://img.shields.io/github/stars/pydna-group/pydna?style=flat-square&label=%E2%AD%90)
- [pySBOL3](https://github.com/SynBioDex/pySBOL3) - Native Python implementation of the SBOL 3 data standard for synthetic-biology designs. ![Stars](https://img.shields.io/github/stars/SynBioDex/pySBOL3?style=flat-square&label=%E2%AD%90)

## DNA data storage

- [Chamaeleo](https://github.com/ntpz870817/Chamaeleo) - BGI Research library of classical DNA storage codecs for encoding files as DNA sequences and decoding them back. Last push 2025-01-13. ![Stars](https://img.shields.io/github/stars/ntpz870817/Chamaeleo?style=flat-square&label=%E2%AD%90)
- [DNA Fountain](https://github.com/TeamErlich/dna-fountain) - Original DNA Fountain codec from the Erlich lab, using rateless fountain codes for DNA storage. Last push 2025-07-08. This is the publication codebase; check current Python compatibility before you rely on it. ![Stars](https://img.shields.io/github/stars/TeamErlich/dna-fountain?style=flat-square&label=%E2%AD%90)

## Lab automation

- [Opentrons](https://github.com/Opentrons/opentrons) - Software for writing and running protocols on Opentrons Flex and OT-2 liquid-handling robots. ![Stars](https://img.shields.io/github/stars/Opentrons/opentrons?style=flat-square&label=%E2%AD%90)
- [PyLabRobot](https://github.com/PyLabRobot/pylabrobot) - Hardware-agnostic Python SDK for lab automation, covering liquid handlers and related devices. ![Stars](https://img.shields.io/github/stars/PyLabRobot/pylabrobot?style=flat-square&label=%E2%AD%90)

## Libraries

- [BiocManager](https://github.com/Bioconductor/BiocManager) - CRAN package for installing and managing Bioconductor packages. GitHub reports no SPDX licence; Bioconductor packages are typically Artistic-2.0, so read the repository and package DESCRIPTION. ![Stars](https://img.shields.io/github/stars/Bioconductor/BiocManager?style=flat-square&label=%E2%AD%90)
- [Biopython](https://github.com/biopython/biopython) - Widely used Python library for computational biology and bioinformatics. GitHub reports no SPDX licence, so read the Biopython license agreement in the repository before you use it commercially. ![Stars](https://img.shields.io/github/stars/biopython/biopython?style=flat-square&label=%E2%AD%90)
- [BioSequences.jl](https://github.com/BioJulia/BioSequences.jl) - Biological sequence types and operations for the Julia language, from BioJulia. ![Stars](https://img.shields.io/github/stars/BioJulia/BioSequences.jl?style=flat-square&label=%E2%AD%90)
- [Biotite](https://github.com/biotite-dev/biotite) - Comprehensive Python library for computational molecular biology, including sequence and structure tools. ![Stars](https://img.shields.io/github/stars/biotite-dev/biotite?style=flat-square&label=%E2%AD%90)
- [scikit-bio](https://github.com/scikit-bio/scikit-bio) - Community-driven Python library for bioinformatics, with sequence, phylogeny and diversity analysis. ![Stars](https://img.shields.io/github/stars/scikit-bio/scikit-bio?style=flat-square&label=%E2%AD%90)

## Personal genomics

- [allelix](https://github.com/allelix/allelix) - Open-source toolkit for analysing raw genotype files from consumer DNA tests, designed to run locally. Treat personal genomic files as sensitive data and keep them off shared machines and public issue trackers. ![Stars](https://img.shields.io/github/stars/allelix/allelix?style=flat-square&label=%E2%AD%90)
- [PGS Catalog Calculator](https://github.com/PGScatalog/pgsc_calc) - Nextflow pipeline from the Polygenic Score Catalog for calculating polygenic scores. If you run it on a personal genome, treat that file as sensitive data and keep it off shared machines and public issue trackers. ![Stars](https://img.shields.io/github/stars/PGScatalog/pgsc_calc?style=flat-square&label=%E2%AD%90)
- [snps](https://github.com/apriha/snps) - Python library for reading, writing, merging and remapping SNPs from consumer genotype files, including 23andMe and AncestryDNA exports, plus VCF. Treat personal genomic files as sensitive data and keep them off shared machines and public issue trackers. ![Stars](https://img.shields.io/github/stars/apriha/snps?style=flat-square&label=%E2%AD%90)

## Public datasets and standards

- [1000 Genomes data indexes](https://github.com/igsr/1000Genomes_data_indexes) - Official index files for 1000 Genomes and International Genome Sample Resource sequence data. Last push 2019-07-15; current data and documentation live on the IGSR website. ![Stars](https://img.shields.io/github/stars/igsr/1000Genomes_data_indexes?style=flat-square&label=%E2%AD%90)
- [Ensembl VEP](https://github.com/Ensembl/ensembl-vep) - Ensembl Variant Effect Predictor, for annotating the functional effects of genomic variants. ![Stars](https://img.shields.io/github/stars/Ensembl/ensembl-vep?style=flat-square&label=%E2%AD%90)
- [GA4GH Phenopackets](https://github.com/ga4gh/phenopacket-schema) - Schema for sharing clinical phenotype data, a GA4GH standard. ![Stars](https://img.shields.io/github/stars/ga4gh/phenopacket-schema?style=flat-square&label=%E2%AD%90)
- [GA4GH VRS](https://github.com/ga4gh/vrs) - Variation Representation Specification, a GA4GH standard for representing and identifying sequence variation. ![Stars](https://img.shields.io/github/stars/ga4gh/vrs?style=flat-square&label=%E2%AD%90)
- [SRA Tools](https://github.com/ncbi/sra-tools) - NCBI toolkit for accessing and converting data in the Sequence Read Archive. GitHub reports no SPDX licence, so read the repository before you use it commercially. ![Stars](https://img.shields.io/github/stars/ncbi/sra-tools?style=flat-square&label=%E2%AD%90)

## Related lists

Other lists in the Awesome Craft series:

- [Awesome Craft](https://github.com/EdisonTKPcom/Awesome-Craft) - A curated list of open-source, self-hostable alternatives to popular SaaS tools.
- [Awesome Craft Agents](https://github.com/EdisonTKPcom/Awesome-Craft-Agents) - A curated list of open-source chat apps, coding agents, self-hosted agent bots, workflow automation and image-generation UIs.
- [Awesome Craft AI](https://github.com/EdisonTKPcom/Awesome-Craft-AI) - A curated list of open-source, self-hostable AI runtimes, servers, Hugging Face libraries and related infrastructure.
- [Awesome Craft BSC](https://github.com/EdisonTKPcom/Awesome-Craft-BSC) - A curated list of verified open-source clients, SDKs, dev tools and protocol code for BNB Smart Chain and opBNB.
- [Awesome Craft Creative](https://github.com/EdisonTKPcom/Awesome-Craft-Creative) - A curated list of open-source creative apps, including the storytold Craft App Suite and tools for photo, video, animation, 3D, audio and design.
- [Awesome Craft CUDA](https://github.com/EdisonTKPcom/Awesome-Craft-CUDA) - A curated list of open-source CUDA learning material, kernel libraries, tooling and portability projects.
- [Awesome Craft DeepSeek](https://github.com/EdisonTKPcom/Awesome-Craft-DeepSeek) - A curated list of official DeepSeek repositories and open-source harnesses, serving engines, eval tools and fine-tuning stacks that work with DeepSeek models.
- [Awesome Craft DevOps](https://github.com/EdisonTKPcom/Awesome-Craft-DevOps) - A curated list of open-source, self-hostable alternatives to popular DevOps and hosting SaaS tools.
- [Awesome Craft Ethereum](https://github.com/EdisonTKPcom/Awesome-Craft-Ethereum) - A curated list of verified open-source Ethereum clients, SDKs, dev frameworks, wallets and security tools.
- [Awesome Craft EV](https://github.com/EdisonTKPcom/Awesome-Craft-EV) - A curated list of open-source software and hardware for electric vehicles and charging.
- [Awesome Craft Hardware](https://github.com/EdisonTKPcom/Awesome-Craft-Hardware) - A curated list of open-source tools for PCB, FPGA, ASIC and chip design.
- [Awesome Craft Hyperliquid](https://github.com/EdisonTKPcom/Awesome-Craft-Hyperliquid) - A curated list of verified open-source SDKs, node tools, analytics and community libraries for the Hyperliquid ecosystem.
- [Awesome Craft Jarvis](https://github.com/EdisonTKPcom/Awesome-Craft-Jarvis) - A curated list of open-source tools to run a personal JARVIS-style AI assistant locally, including dashboards, agent runtimes, voice, MCP connections and memory.
- [Awesome Craft Malaysia](https://github.com/EdisonTKPcom/Awesome-Craft-Malaysia) - A curated list of open-source tools useful to Malaysian SMEs, with verified MyInvois support called out separately.
- [Awesome Craft Mars](https://github.com/EdisonTKPcom/Awesome-Craft-Mars) - A curated list of open-source tools and open data for Mars missions and settlement planning.
- [Awesome Craft Neuro](https://github.com/EdisonTKPcom/Awesome-Craft-Neuro) - A curated list of open-source tools for brain-computer interfaces, electrophysiology and neurotechnology.
- [Awesome Craft Robotics](https://github.com/EdisonTKPcom/Awesome-Craft-Robotics) - A curated list of open-source robotics software and hardware, including Microduck, Unitree SDKs, open humanoids, arms, simulation and middleware.
- [Awesome Craft Solana](https://github.com/EdisonTKPcom/Awesome-Craft-Solana) - A curated list of verified open-source Solana clients, SDKs, frameworks, explorers and program libraries.
- [Awesome Craft Space](https://github.com/EdisonTKPcom/Awesome-Craft-Space) - A curated list of open-source tools for spaceflight and rockets, covering orbit simulation, telemetry, launch data and more.
- [Awesome Craft Starlink](https://github.com/EdisonTKPcom/Awesome-Craft-Starlink) - A curated list of open-source tools for Starlink and other LEO satellite internet systems.
- [Awesome Craft Web3](https://github.com/EdisonTKPcom/Awesome-Craft-Web3) - A curated list of open-source DEX protocol code, self-custody software, indexers, frameworks and Blockchain infrastructure.

## Star history

[![Star History Chart](https://api.star-history.com/chart?repos=EdisonTKPcom/Awesome-Craft-DNA&amp;type=Date)](https://www.star-history.com/#EdisonTKPcom/Awesome-Craft-DNA&Date)

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

<div align="center">

If this list helped you find a tool, give it a ⭐ so others can find it.

</div>
