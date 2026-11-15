#!/usr/bin/env python3
import csv
import urllib.parse as U
from pathlib import Path

ROOT = Path(__file__).resolve().parent
S = {
    r[0]: dict(stars=int(r[1]), forks=int(r[2]), lic=r[3], lang=r[4], push=r[5])
    for r in csv.reader((ROOT / "stats.tsv").open(), delimiter="\t")
}
LICNAME = {"NOASSERTION": "Custom", "none": "None", "OTHER": "Custom"}
AS = "2026-11-15"
ACTIVE_SINCE = "2026-10-16"

# (name, repo, description) — descriptions already include licence/archive/safety flags
C = [
    (
        "Sequence alignment and mapping",
        [
            ("BWA", "lh3/bwa", "Burrows-Wheeler short-read aligner."),
            ("Bowtie 2", "BenLangmead/bowtie2", "Fast gapped short-read aligner."),
            ("HISAT2", "DaehwanKimLab/hisat2", "Graph-based, splice-aware aligner that uses a hierarchical graph FM index."),
            ("minimap2", "lh3/minimap2", "Versatile pairwise aligner for genomic and spliced nucleotide sequences, including long reads. GitHub reports no SPDX licence; the repository LICENSE.txt is the MIT licence."),
            ("STAR", "alexdobin/STAR", "Splice-aware RNA-seq aligner for short reads. Last push 2025-03-18."),
        ],
    ),
    (
        "Variant calling",
        [
            ("bcftools", "samtools/bcftools", "Utilities for variant calling and VCF/BCF manipulation, part of the samtools suite. GitHub reports no SPDX licence; the samtools suite LICENSE is the MIT/Expat licence."),
            ("DeepVariant", "google/deepvariant", "Deep-learning variant caller from Google."),
            ("FreeBayes", "freebayes/freebayes", "Bayesian haplotype-based variant caller."),
            ("GATK", "broadinstitute/gatk", "Broad Institute Genome Analysis Toolkit for variant discovery, versions 4 and later. GitHub reports no SPDX licence; LICENSE.TXT states Apache-2.0."),
            ("htslib", "samtools/htslib", "C library for high-throughput sequencing formats such as SAM, BAM, CRAM and VCF. GitHub reports no SPDX licence; the related samtools LICENSE is the MIT/Expat licence."),
            ("samtools", "samtools/samtools", "Tools for reading, writing and manipulating SAM, BAM and CRAM files. GitHub reports no SPDX licence; the LICENSE file is the MIT/Expat licence."),
        ],
    ),
    (
        "Nanopore and long-read",
        [
            ("Dorado", "nanoporetech/dorado", "Oxford Nanopore's production basecaller. The repository uses the Oxford Nanopore Technologies PLC Public License Version 1.0, which is not an OSI licence. Read it before any commercial use."),
            ("Flye", "mikolmogorov/Flye", "De novo assembler for single-molecule long reads, using repeat graphs. GitHub reports no SPDX licence; the repository LICENSE is BSD-3-Clause."),
            ("Medaka", "nanoporetech/medaka", "Neural-network consensus polishing and variant calling for Oxford Nanopore sequences. The repository uses the Oxford Nanopore Technologies PLC Public License Version 1.0, which is not an OSI licence."),
            ("slow5tools", "hasindu2008/slow5tools", "Toolkit for converting, compressing and viewing SLOW5 and BLOW5 signal files, an open alternative to FAST5."),
        ],
    ),
    (
        "Assembly",
        [
            ("Canu", "marbl/canu", "Long-read assembler for large genomes, descended from the Celera Assembler. GitHub reports no SPDX licence; the distribution is a joint work under GPL-2.0, with some BSD-3-Clause contributions."),
            ("hifiasm", "chhylp123/hifiasm", "Haplotype-resolved assembler for PacBio HiFi reads."),
            ("SPAdes", "ablab/spades", "St. Petersburg genome assembler for short and hybrid reads, including isolate and metagenomic modes. GitHub reports no SPDX licence, so read the repository before you use it commercially."),
        ],
    ),
    (
        "Workflow managers",
        [
            ("Cromwell", "broadinstitute/cromwell", "Scientific workflow engine from the Broad Institute, with first-class support for WDL."),
            ("Galaxy", "galaxyproject/galaxy", "Web platform for accessible, reproducible data-intensive analysis, with a large tool shed for genomics. GitHub reports no SPDX licence, so read the repository before you use it commercially."),
            ("Nextflow", "nextflow-io/nextflow", "Data-driven workflow language and runtime, widely used for genomics pipelines."),
            ("nf-core tools", "nf-core/tools", "Helper CLI for the nf-core community of curated Nextflow pipelines."),
            ("Snakemake", "snakemake/snakemake", "Python-based workflow management system with a large genomics ecosystem."),
        ],
    ),
    (
        "Genome browsers and visualisation",
        [
            ("IGV", "igvteam/igv", "Integrative Genomics Viewer, a desktop app for exploring alignments, variants and annotations."),
            ("JBrowse 2", "GMOD/jbrowse-components", "Modern React-based genome browser from GMOD, the successor to JBrowse 1."),
            ("UCSC kent tools", "ucscGenomeBrowser/kent", "Source for the UCSC Genome Browser and its command-line tools. The default licence is MIT, but the interactive Genome Browser CGI programs and the BLAT/isPCR suite use separate non-commercial licences. Commercial use of those parts needs a licence from UCSC or Kent Informatics."),
        ],
    ),
    (
        "Single-cell and RNA-seq",
        [
            ("kallisto", "pachterlab/kallisto", "Near-optimal RNA-seq transcript quantification with pseudoalignment."),
            ("Salmon", "COMBINE-lab/salmon", "Accurate, fast transcript-level quantification from RNA-seq reads."),
            ("Scanpy", "scverse/scanpy", "Scalable single-cell analysis in Python, part of the scverse ecosystem."),
            ("scvi-tools", "scverse/scvi-tools", "Deep probabilistic models for single-cell and spatial omics."),
            ("Seurat", "satijalab/seurat", "R toolkit for single-cell genomics. GitHub reports no SPDX licence, so read the repository before you use it commercially."),
        ],
    ),
    (
        "Protein structure and AI bio models",
        [
            ("AlphaFold 2", "google-deepmind/alphafold", "Open-source code for AlphaFold 2 structure prediction. The code is Apache-2.0; the model parameters have a separate licence, so check the repository before you use the weights."),
            ("AlphaFold 3", "google-deepmind/alphafold3", "Inference pipeline for AlphaFold 3. The code is Apache-2.0, but the model parameters and outputs are covered by separate non-commercial terms in WEIGHTS_TERMS_OF_USE.md and OUTPUT_TERMS_OF_USE.md."),
            ("Boltz", "jwohlwend/boltz", "Biomolecular interaction models, including structure prediction of complexes."),
            ("ColabFold", "sokrypton/ColabFold", "Accessible protein-folding notebooks and pipeline built around AlphaFold 2 and related models."),
            ("ESM", "Biohub/esm", "Current Evolutionary Scale Modeling codebase, now hosted at Biohub after a move from evolutionaryscale/esm. GitHub reports no SPDX licence; LICENSE.md is the MIT licence. The earlier ESM-2 and ESMFold code lives in the archived facebookresearch/esm repository, also MIT."),
            ("Evo 2", "ArcInstitute/evo2", "Genome language models for modeling and design across domains of life, from the Arc Institute. The code is Apache-2.0. Use sequence models in line with institutional biosafety rules; this list does not cover work on harmful agents."),
            ("Nucleotide Transformer", "instadeepai/nucleotide-transformer", "Foundation models for genomics and transcriptomics from InstaDeep. LICENSE.md is CC BY-NC-SA 4.0, which is not an OSI software licence, and MODEL-LICENSE.md (InstaDeep Open Model Licence v1.0) limits model-weight use to non-commercial purposes unless you have a separate licence."),
            ("OpenFold", "aqlaboratory/openfold", "Trainable, memory-efficient PyTorch reproduction of AlphaFold 2."),
            ("RoseTTAFold", "RosettaCommons/RoseTTAFold", "Deep-learning protein structure prediction from RosettaCommons. Last push 2024-02-15."),
        ],
    ),
    (
        "Synthetic biology and DNA design",
        [
            ("Cas-OFFinder", "snugel/cas-offinder", "Fast search for potential CRISPR off-target sites. GitHub reports no SPDX licence, so read the repository before you use it commercially. Last push 2022-08-31."),
            ("CRISPOR", "maximilianh/crisporWebsite", "Source for the CRISPOR.org CRISPR guide-design website. GitHub reports no SPDX licence, so read the repository before you use it commercially."),
            ("DNA Chisel", "Edinburgh-Genome-Foundry/DnaChisel", "Python DNA sequence optimizer for recoding, constraint satisfaction and synthesis-friendly design."),
            ("OpenCRISPR", "Profluent-AI/OpenCRISPR", "AI-designed CRISPR gene-editing systems from Profluent Bio, including the OpenCRISPR-1 sequence release. GitHub reports no SPDX licence. The authors say the sequences are free for research and commercial use, but commercial therapeutic use requires their licence agreement."),
            ("pydna", "pydna-group/pydna", "Python data structures for double-stranded DNA and simulation of cloning, including Gibson assembly and restriction cloning. GitHub reports no SPDX licence; LICENSE.txt is a BSD-3-Clause licence."),
            ("pySBOL3", "SynBioDex/pySBOL3", "Native Python implementation of the SBOL 3 data standard for synthetic-biology designs."),
        ],
    ),
    (
        "DNA data storage",
        [
            ("Chamaeleo", "ntpz870817/Chamaeleo", "BGI Research library of classical DNA storage codecs for encoding files as DNA sequences and decoding them back. Last push 2025-01-13."),
            ("DNA Fountain", "TeamErlich/dna-fountain", "Original DNA Fountain codec from the Erlich lab, using rateless fountain codes for DNA storage. Last push 2025-07-08. This is the publication codebase; check current Python compatibility before you rely on it."),
        ],
    ),
    (
        "Lab automation",
        [
            ("Opentrons", "Opentrons/opentrons", "Software for writing and running protocols on Opentrons Flex and OT-2 liquid-handling robots."),
            ("PyLabRobot", "PyLabRobot/pylabrobot", "Hardware-agnostic Python SDK for lab automation, covering liquid handlers and related devices."),
        ],
    ),
    (
        "Libraries",
        [
            ("BioSequences.jl", "BioJulia/BioSequences.jl", "Biological sequence types and operations for the Julia language, from BioJulia."),
            ("BiocManager", "Bioconductor/BiocManager", "CRAN package for installing and managing Bioconductor packages. GitHub reports no SPDX licence; Bioconductor packages are typically Artistic-2.0, so read the repository and package DESCRIPTION."),
            ("Biopython", "biopython/biopython", "Widely used Python library for computational biology and bioinformatics. GitHub reports no SPDX licence, so read the Biopython license agreement in the repository before you use it commercially."),
            ("Biotite", "biotite-dev/biotite", "Comprehensive Python library for computational molecular biology, including sequence and structure tools."),
            ("scikit-bio", "scikit-bio/scikit-bio", "Community-driven Python library for bioinformatics, with sequence, phylogeny and diversity analysis."),
        ],
    ),
    (
        "Personal genomics",
        [
            ("allelix", "allelix/allelix", "Open-source toolkit for analysing raw genotype files from consumer DNA tests, designed to run locally. Treat personal genomic files as sensitive data and keep them off shared machines and public issue trackers."),
            ("PGS Catalog Calculator", "PGScatalog/pgsc_calc", "Nextflow pipeline from the Polygenic Score Catalog for calculating polygenic scores. If you run it on a personal genome, treat that file as sensitive data and keep it off shared machines and public issue trackers."),
            ("snps", "apriha/snps", "Python library for reading, writing, merging and remapping SNPs from consumer genotype files, including 23andMe and AncestryDNA exports, plus VCF. Treat personal genomic files as sensitive data and keep them off shared machines and public issue trackers."),
        ],
    ),
    (
        "Public datasets and standards",
        [
            ("1000 Genomes data indexes", "igsr/1000Genomes_data_indexes", "Official index files for 1000 Genomes and International Genome Sample Resource sequence data. Last push 2019-07-15; current data and documentation live on the IGSR website."),
            ("Ensembl VEP", "Ensembl/ensembl-vep", "Ensembl Variant Effect Predictor, for annotating the functional effects of genomic variants."),
            ("GA4GH Phenopackets", "ga4gh/phenopacket-schema", "Schema for sharing clinical phenotype data, a GA4GH standard."),
            ("GA4GH VRS", "ga4gh/vrs", "Variation Representation Specification, a GA4GH standard for representing and identifying sequence variation."),
            ("SRA Tools", "ncbi/sra-tools", "NCBI toolkit for accessing and converting data in the Sequence Read Archive. GitHub reports no SPDX licence, so read the repository before you use it commercially."),
        ],
    ),
]


def k(n):
    if n >= 1e6:
        return f"{n/1e6:.2f}M"
    if n >= 1000:
        return f"{n/1000:.1f}k"
    return str(n)


def anchor(n):
    return n.lower().replace(",", "").replace(" ", "-")


def fact(text):
    return f'<span class="dna-fact">{text}</span>'


def estimate(text):
    return f'<span class="dna-est">{text}</span>'


def goal(text):
    return f'<span class="dna-goal">{text}</span>'


tools = [t for _, ts in C for t in ts]
missing = [t[1] for t in tools if t[1] not in S]
if missing:
    raise SystemExit(f"missing stats for: {missing}")

urls = [f"https://github.com/{t[1]}" for t in tools]
if len(urls) != len(set(urls)):
    raise SystemExit("duplicate GitHub URLs")

tot = sum(S[t[1]]["stars"] for t in tools)
forks = sum(S[t[1]]["forks"] for t in tools)
langs = sorted({S[t[1]]["lang"] for t in tools if S[t[1]]["lang"] not in ("", "none")})
active = sum(1 for t in tools if S[t[1]]["push"] >= ACTIVE_SINCE)

o = []
o.append(
    f"""<div align="center">

# Awesome Craft DNA [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source tools for DNA, genomics and synthetic biology.

<img src="assets/craft-dna.svg" alt="Pixel-art laboratory scene with a rotating double helix and a generic sequencer reading coloured bases" width="100%">

![Tools](https://img.shields.io/badge/tools-{len(tools)}-6366f1?style=for-the-badge)
[![Categories](https://img.shields.io/badge/categories-{len(C)}-0ea5e9?style=for-the-badge)](#contents)
[![Combined stars](https://img.shields.io/badge/combined_stars-{k(tot)}-f59e0b?style=for-the-badge&logo=github)](#-leaderboard)
[![Stars](https://img.shields.io/github/stars/EdisonTKPcom/Awesome-Craft-DNA?style=for-the-badge&color=22c55e)](https://github.com/EdisonTKPcom/Awesome-Craft-DNA/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/EdisonTKPcom/Awesome-Craft-DNA?style=for-the-badge&color=ec4899)](https://github.com/EdisonTKPcom/Awesome-Craft-DNA/commits/main)

</div>

This list covers open-source software for reading, writing, analysing and designing DNA, RNA and proteins: aligners, variant callers, long-read tools, assemblers, workflow managers, genome browsers, single-cell and RNA-seq packages, structure and sequence models, synthetic-biology design tools, DNA storage codecs, lab automation, libraries, personal-genomics utilities, and public datasets and standards. Every entry below has a public repository that was checked on {AS}. Check each project's licence, including any separate terms for model weights, before you use it.

**Biosafety and ethics:** this list is for research, engineering and education. It is not guidance on pathogen enhancement, gain-of-function work, or the design of harmful biological agents, and it does not list tools whose purpose is that work. Sequence models and gene-editing design tools can be dual-use. Use them only in line with the law, institutional biosafety rules, and each project's own terms.

**Privacy:** personal and consumer genomic files are sensitive. Prefer tools that run on a machine you control, do not upload raw genotypes to a third-party service unless you understand and accept that service's terms, and never post those files in public issues, chats or repositories.

Related lists: [Awesome Craft](https://github.com/EdisonTKPcom/Awesome-Craft), [Awesome Craft AI](https://github.com/EdisonTKPcom/Awesome-Craft-AI), [Awesome Craft EV](https://github.com/EdisonTKPcom/Awesome-Craft-EV).

## Contents
"""
)
o += ["- [Dashboard](#dashboard)"] + [f"- [{n}](#{anchor(n)})" for n, _ in C]
o.append("\n## Dashboard\n")
o.append(
    f"""<style>
.dna-fact{{border-bottom:3px solid #0f172a;padding-bottom:1px}}
.dna-goal{{border-bottom:3px dashed #0f172a;padding-bottom:1px}}
.dna-est{{border-bottom:3px dotted #0f172a;padding-bottom:1px}}
</style>

<table>
<tr>
<td align="center"><h2>{fact(str(len(tools)))}</h2>listed projects</td>
<td align="center"><h2>{fact(str(len(C)))}</h2>categories</td>
<td align="center"><h2>{estimate(k(tot))}</h2>combined GitHub stars</td>
<td align="center"><h2>{estimate(k(forks))}</h2>combined forks</td>
<td align="center"><h2>{estimate(f"{active}/{len(tools)}")}</h2>pushed in the last 30 days</td>
<td align="center"><h2>{fact(str(len(langs)))}</h2>languages</td>
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

- Star counts, fork counts, licences, primary languages and last-push dates are {fact("FACT")} values from the GitHub REST API (`GET /repos/{{owner}}/{{repo}}`) on {AS}.
- Combined stars ({estimate(k(tot))}) and combined forks ({estimate(k(forks))}) are {estimate("ESTIMATE")}s: the arithmetic sum of those per-repository FACT counts, with no weighting and no unique-user deduplication. A person who stars two projects is counted twice.
- Pushed in the last 30 days ({estimate(f"{active}/{len(tools)}")}) is an {estimate("ESTIMATE")}: the number of listed repositories whose FACT `pushed_at` date is on or after {ACTIVE_SINCE}.
- Language and category counts, and the licence badges, are {estimate("ESTIMATE")}s of FACT fields. Star badges next to each entry update live and may differ from this snapshot.
"""
)
top = sorted(tools, key=lambda t: -S[t[1]]["stars"])[:10]
mx = S[top[0][1]]["stars"]
o.append(
    '### 🏆 Leaderboard\n\nStar counts in this table are FACT values from the snapshot. The bars are only a visual scale.\n\n<table>\n<tr><th>Rank</th><th>Project</th><th>Kind</th><th align="right">Stars</th><th></th></tr>'
)
kind = {t[1]: n for n, ts in C for t in ts}
for i, t in enumerate(top, 1):
    s = S[t[1]]["stars"]
    bar = "█" * max(1, round(s / mx * 20))
    medal = ["🥇", "🥈", "🥉"][i - 1] if i < 4 else i
    o.append(
        f'<tr><td align="center">{medal}</td><td><b>{t[0]}</b></td><td>{kind[t[1]]}</td><td align="right">{fact(k(s))}</td><td><code>{bar}</code></td></tr>'
    )
o.append("</table>\n")
o.append("\n### Stars by category\n")
o.append(
    "These category totals are ESTIMATE sums of the per-repository FACT star counts.\n\n```mermaid\npie showData\n    title Combined GitHub stars by category"
)
for n, ts in C:
    o.append(f'    "{n}" : {sum(S[t[1]]["stars"] for t in ts)}')
o.append("```\n")
lc = {}
for t in tools:
    L = LICNAME.get(S[t[1]]["lic"], S[t[1]]["lic"])
    lc[L] = lc.get(L, 0) + 1
o.append(
    "### Licences\n\n"
    + " ".join(
        f"![{L}](https://img.shields.io/badge/{U.quote(str(L).replace('-', '--'))}-{c}-64748b?style=flat-square)"
        for L, c in sorted(lc.items(), key=lambda x: -x[1])
    )
    + "\n\nThese badge counts are ESTIMATE tallies of the SPDX identifier GitHub returned for each repository. "
    + '"Custom" or "None" means GitHub could not match a standard SPDX licence. '
    + "Dorado and Medaka use the Oxford Nanopore Technologies PLC Public License Version 1.0, which is not an OSI licence. "
    + "Nucleotide Transformer code is CC BY-NC-SA 4.0, and its model weights use the InstaDeep Open Model Licence v1.0, which is limited to non-commercial use unless you have a separate licence. "
    + "AlphaFold 3 code is Apache-2.0, but its model parameters and outputs have separate non-commercial terms. "
    + "The UCSC kent tree is mixed: most command-line tools are MIT, while the Genome Browser CGIs and BLAT/isPCR are under non-commercial licences. "
    + "OpenCRISPR has no SPDX licence file; commercial therapeutic use requires Profluent's licence agreement. "
    + "Read each project licence, and any weight or output terms, before you use it commercially.\n"
)
for n, ts in C:
    o.append(f"## {n}\n")
    for t in sorted(ts, key=lambda t: t[0].lower()):
        desc = t[2]
        if not desc.endswith("."):
            desc += "."
        o.append(
            f"- [{t[0]}](https://github.com/{t[1]}) - {desc} ![Stars](https://img.shields.io/github/stars/{t[1]}?style=flat-square&label=%E2%AD%90)"
        )
    o.append("")
o.append(
    "## Contributing\n\nContributions welcome! Read the [contribution guidelines](contributing.md) first.\n\n"
    '<div align="center">\n\n'
    "If this list helped you find a tool, give it a ⭐ so others can find it.\n\n"
    "</div>\n"
)
(ROOT / "README.md").write_text("\n".join(o))
print(
    f"wrote README.md tools={len(tools)} stars={tot} "
    f"forks={forks} langs={len(langs)} active={active}/{len(tools)}"
)
for n, ts in C:
    print(f"  {n}: {len(ts)}  stars={sum(S[t[1]]['stars'] for t in ts)}")
