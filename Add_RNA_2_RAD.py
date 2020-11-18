import pandas as pd
from Bio import SeqIO
import argparse
import os


def addRNA2RAD(outgroup_name, transcriptome, blast_result_txt, split_genes):
    added_genes = os.path.dirname(split_genes) + "/added_outgroup_genes/"
    if os.path.isdir(added_genes) == False:
        os.makedirs(added_genes)
    ### transcriptome data
    fasta_name = transcriptome

    data = pd.read_csv(blast_result_txt, sep= '\t', header=None)
    print(data)
    #
    # #create dataframe
    df=pd.DataFrame(data, index=None, columns=None)
    type(df)
    # #print(df)
    #
    #name column to target it for split
    df = df.rename(columns={0:"gene_name"})
    print(df)
    gene_name = ""

    for i in range(len(df)):
        ind_name_value = df.values[i][0]
        trinity_name_value = df.values[i][1]

        starting_pos = df.values[i][8]
        ending_pos = df.values[i][9]
        print(ind_name_value, trinity_name_value,gene_name)

### because it has duplicate, therefore, we run a loop to choose on value of the duplicates.
        if gene_name != df.values[i][0].split("_g")[1]:
            file_name = split_genes + "/g" + str(df.values[i][0].split("_g")[1]) + "_aligned.fas"

            for test in SeqIO.parse(fasta_name, 'fasta'):
                if test.name == trinity_name_value:
                    print(test.name)
                    print(test.seq)
                    print(starting_pos)
                    print(ending_pos)
                    if starting_pos < ending_pos:
                            # print(test.seq[0:3])
                        sequence_og = test.seq[(starting_pos-1):ending_pos]

                    else:
                            # print(test.seq[0:3])
                        sequence_og = test.seq[(ending_pos-1):starting_pos]
                    print(sequence_og)

                    sum1 = ">" + str(outgroup_name) + "\n" + str(sequence_og) + "\n"
                    print(sum1)

                    f1 = open(file_name, "a")
                    f1.write(sum1)
                    f1.close()
                    # return file_name

            cmd = "mv " + file_name + " " + added_genes
            print(cmd)
            os.system(cmd)

            gene_name = df.values[i][0].split("_g")[1]


def main():
    parser = argparse.ArgumentParser(
        description="Extract shared loci from outgroup based on the blast result between RAD-seq and RNA-seq data.",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-og", "--outgroupname", dest='og_name', type=str,
                        help='type in outgroup name.')

    parser.add_argument("-itr", "--inputranscriptome", dest='input_trans_dir', type=str,
                        help='type in the full directory of loci file')

    parser.add_argument("-ibl", "--inpublastresult", dest='input_blast_result_dir', type=str,
                        help='type in the full directory of blast result file')

    parser.add_argument("-iogf", "--outputgenesfile", dest='output_genes_dir', type=str,
                        help='type in the full directory of split gene file')


    args = parser.parse_args()
    if args.input_trans_dir and args.og_name and args.input_blast_result_dir and args.output_genes_dir:

        input_RNA_seq = os.path.realpath(args.input_trans_dir)
        blast_result = os.path.realpath(args.input_blast_result_dir)
        split_genes_folder = os.path.realpath(args.output_genes_dir)

        addRNA2RAD(args.og_name, input_RNA_seq, blast_result, split_genes_folder)

if __name__ == '__main__':
    main()
