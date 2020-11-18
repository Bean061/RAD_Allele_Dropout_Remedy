from Bio import SeqIO
from Bio.Seq import Seq
import os
from Bio import AlignIO
import argparse


#copy files into one folder.
#path = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus"
#os.mkdir(path)


# mafft

def mafft_genes(added_genes_output):
    aln_output = os.path.dirname(added_genes_output) + "/aligned_loci/"
    if os.path.isdir(aln_output) == False:
        os.makedirs(aln_output)
# transfer the file format
    for file in os.listdir(added_genes_output):
        fname = added_genes_output + "/" + file
        output_name = aln_output + file
        if file != ".DS_Store":
            cmd = "mafft --adjustdirection " + fname + " > " + output_name
            print(cmd)
            os.system(cmd)

    #for aln_file in os.listdir(aln_output):
        ### replace all n to -, otherwise trimal can not run successfully.
        # aln_name = aln_output + "/"
    cmd_replace_name = '''FILES=''' + aln_output + ''' && for f in $FILES*\n do\n sed -i '' -e 's/_R_//g' $f\n done\n'''
    os.system(cmd_replace_name)

        ###  --maxiterate 1000 --globalpair

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
