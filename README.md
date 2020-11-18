# RAD Allele Dropout Remedy (RADADOR)
A Pipeline Using Transcriptome or Genome Sequences to Obtain More Shared Loci for Outgroup Species in RAD-Seq

by Wenbin Zhou

This pipeline can be applied to RAD-seq experiments missing closely related outgroup, largely increasing the number of shared loci in outgroup. It helps obtain more informative sites in outgroups, improving downstream phylogenetic analysis.

## Prerequisites:
Run [ipyrad](https://ipyrad.readthedocs.io/en/latest/) to get the .loci file and .phy file as the input for this pipeline.


## python Dependencies

This pipeline is on [python3](https://www.python.org/downloads/)

* [Biopython](https://biopython.org/wiki/Packages). Easy installation from [conda](https://biopython.org/wiki/Packages) 
* [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html). Easy installation from [conda](https://anaconda.org/anaconda/pandas)
* [argparse](https://pypi.org/project/argparse/). Easy installation from [conda](https://anaconda.org/conda-forge/argparse)

## Other Software Prerequisites
1. [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi). Easy installation from [conda](https://anaconda.org/bioconda/blast)

```
check if BLAST is installed successfully by typing "blastn -h" in terminal.
```

2. [MAFFT](https://mafft.cbrc.jp/alignment/software/). Easy installation from [conda](https://anaconda.org/bioconda/mafft)

```
check if MAFFT is installed successfully by typing "mafft -h" in terminal.
```

## Environment
Examples can be run on Mac or Linux.


## Details
It includes six steps as follows:

1) the function “Loci2partition_nex” transfers the loci output file (from ipyrad) into partition nexus file. 

2) according to the partition file, the concatenated gene phylip output file (from ipyrad) were divided into different genes alignments by the “Concatenated2gene_phylip” function. 

3) combined all gene sequences from all individual into one master fasta file using the “combRADseq” function. 

4) use transcriptomic Trinity contigs result as the reference and BLAST the RAD-seq master fasta file from step 3 with the reference via the “Blast_py” function. 

5) according to the blast result, the matching transcriptomic sequences were obtained to each corresponding locus via the “addRNA2RAD” function. 

6) realign the genes with new outgroup sequences using “mafft_genes” function.

## Usage

  This script is used to recapture loci in RAD-seq outgroup from RNA-seq or Genome data. It requires .loci file from ipyrad, .phy file from ipyrad, .fasta file from RNA-seq (Trinity) or Genomic data. You also need to define one outgroup name and output partition file name. '-i', '-o', '-iph', '-itr', '-og' are required arguments. The default output file will be generated at current working dirctory.
  
  Make sure your working dirctory contain all the RADADOR python scripts. You can copy all files to RAD_Allele_Dropout_Remedy folder.
  
  ``` 
  cd RAD_Allele_Dropout_Remedy/
  ```
 
  To check all parameters in RADADOR.py using:

  ```python
  python RADADOR.py -h
  ```
  
```python
usage: RADADOR.py [-h] [-i INPUT_DIR] [-o OUTPUT_NAME] [-iph INPUT_PHYLIP_DIR]
                [-itr INPUT_TRANS_DIR] [-og OG_NAME]


optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --inputlocifile INPUT_DIR
                        type in the path of loci file
  -o OUTPUT_NAME, --outputpartition OUTPUT_NAME
                        name the output partition file (.nexus)
  -iph INPUT_PHYLIP_DIR, --inputphy INPUT_PHYLIP_DIR
                        type in the path of phylip file.
  -itr INPUT_TRANS_DIR, --inputranscriptome INPUT_TRANS_DIR
                        type in the path of reference file, generated by Trinity (RNA-seq).
  -og OG_NAME, --outgroupname OG_NAME
                        define your outgroup name.
```

example:
  ```
  cd ./example/
  ```
  
  ```python
  python3 ../RADADOR.py -i nr50.loci -o partition.nex -iph nr50.phy -itr trinity_Acer_rubrum.Trinity.fasta -og Acer
  ```

## Output
* partition.nex
  
  partition file result for your M50 data.
  
* split_genes/

  Contains gene alignments without adding any new outgroup sequences.
  
* BLAST/

  Deposit your BLAST reference and output.
  
* added_outgroup_genes/
  
  Contains gene seqeunces with new outgroup sequences added, but not aligned.

* aligned_loci/
  
  Contains gene alignments with new outgroup sequences added.

Finally you can concatenate aligned_loci/ and split_genes/ as the final matrix for phylogenetic analyses.


## Citation

* Zhou et al. in prep.

## Acknowledgements
 The example data is partially from Du, Zhi-Yuan, A. J. Harris, and Qiu-Yun Jenny Xiang. "Phylogenomics, co-evolution of ecological niche and morphology, and historical biogeography of buckeyes, horsechestnuts, and their relatives (Hippocastaneae, Sapindaceae) and the value of RAD-Seq for deep evolutionary inferences back to the Late Cretaceous." Molecular Phylogenetics and Evolution 145 (2020): 106726.
