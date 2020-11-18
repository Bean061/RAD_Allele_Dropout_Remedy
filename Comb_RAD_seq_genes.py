from Bio import SeqIO
import os
import argparse

def combRADseq(genes_file):
    # path = Path(os.path.dirname(genes_file))
    # parent_path = path.parent

    output_BLAST = os.path.dirname(genes_file) + "/BLAST/"
    if os.path.isdir(output_BLAST) == False:
        os.makedirs(output_BLAST)

    for file in os.listdir(genes_file):
        fname = genes_file + "/" + file
        gene_name = file.split("_")[0]
        print(file)
        if file != ".DS_Store":

            for test in SeqIO.parse(fname,'fasta'):
                if test.seq != len(test.seq) * "N" and test.seq != len(test.seq) * "n":
                    # print("test")
                    test.id = test.id + "_" + gene_name
                    print(test.id)
                    test.description = test.id
                    test.name = test.id

                    file = output_BLAST + "/combined.fasta"
                    f1 = open(file, 'a')
                    SeqIO.write(test, f1, "fasta")
                    f1.close()


def main():
    parser = argparse.ArgumentParser(
        description="Combine RAD-seq genes in one file which will be used for BLAST.",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-ig", "--inputgenes", dest='input_gene_dir', type=str,
                        help='put the directory of separate gene files')

    args = parser.parse_args()
    if args.input_gene_dir:
        input_gene_file = os.path.realpath(args.input_gene_dir)

        combRADseq(input_gene_file)

if __name__ == '__main__':
    main()