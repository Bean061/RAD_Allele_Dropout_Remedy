#### s4 function: use transcriptomic Trinity contigs result as the reference and BLAST the RAD-seq combined
#### fasta file from step 3 with the reference via the “Blast_py” function.

#### Any questions, please contact Wenbin Zhou. wzhou10@ncsu.edu

import os
import argparse


def blast_py(transcriptome):
    ### reference path ###
    ref = os.path.dirname(transcriptome) + "/BLAST/reference"

    ### the combined fasta file containing all RAD-seq from s3
    combined_RAD = os.path.dirname(transcriptome) + "/BLAST/combined.fasta"

    ### the path of blast output
    blast_result_txt = os.path.dirname(transcriptome) + "/BLAST/result.txt"

    blastdb_cmd = "makeblastdb -in " + transcriptome + " -dbtype nucl -out "+ ref
    os.system(blastdb_cmd)

    blastn_cmd = "blastn -query " + combined_RAD + " -db " + ref + " -out " + blast_result_txt + " -perc_identity 85 -outfmt 6"
    os.system(blastn_cmd)
    # print cmd



def main():
    parser = argparse.ArgumentParser(
        description="BLAST the RAD-seq with RNA-seq data. Make sure there is a combined.fasta and reference file in the BLAST folder",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-itr", "--inputranscriptome", dest='input_trans_dir', type=str,
                        help='put the full directory of loci file')

    args = parser.parse_args()
    if args.input_trans_dir:
        input_RNA_seq = os.path.realpath(args.input_trans_dir)

        blast_py(input_RNA_seq)

if __name__ == '__main__':
    main()
