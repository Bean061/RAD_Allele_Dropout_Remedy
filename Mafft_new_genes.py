### s6: realign the genes with new outgroup sequences using “mafft_genes” function.

#### Any questions, please contact Wenbin Zhou. wzhou10@ncsu.edu

from Bio import SeqIO
from Bio.Seq import Seq
import os
from Bio import AlignIO
import argparse


def mafft_genes(added_genes_output):
    aln_output = os.path.dirname(added_genes_output) + "/aligned_loci/"
    if os.path.isdir(aln_output) == False:
        os.makedirs(aln_output)

    # realign all loci using mafft
    for file in os.listdir(added_genes_output):
        fname = added_genes_output + "/" + file
        output_name = aln_output + file
        if file != ".DS_Store":
            cmd = "mafft --adjustdirection --maxiterate 1000 --globalpair " + fname + " > " + output_name
            print(cmd)
            os.system(cmd)


    ### replace all n to -, otherwise trimal can not run successfully.

    cmd_replace_name = '''FILES=''' + aln_output + '''\nfor f in $FILES*\ndo\nsed -i '' -e 's/_R_//g' $f\ndone\n'''

    print(cmd_replace_name)

    os.system(cmd_replace_name)

def main():
    parser = argparse.ArgumentParser(
        description="Extract shared loci from outgroup based on the blast result between RAD-seq and RNA-seq data.",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-iago", "--addedgenes", dest='added_gene_output', type=str,
                        help='type in outgroup name.')


    args = parser.parse_args()
    if args.added_gene_output:
        add_gene_folder = os.path.realpath(args.added_gene_output)

        mafft_genes(add_gene_folder)

if __name__ == '__main__':
    main()
