import os
import argparse


def blast_py(transcriptome):
    ref = os.path.dirname(transcriptome) + "/BLAST/reference"
    combined_RAD = os.path.dirname(transcriptome) + "/BLAST/combined.fasta"
    blast_result_txt = os.path.dirname(transcriptome) + "/BLAST/result.txt"
    # cmd = "cp " + transcriptome + " > " + output_BLAST + "ref"

    blastdb_cmd = "makeblastdb -in " + transcriptome + " -dbtype nucl -out "+ ref
    os.system(blastdb_cmd)

    blastn_cmd = "blastn -query " + combined_RAD + " -db " + ref + " -out " + blast_result_txt + " -outfmt 6"
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
