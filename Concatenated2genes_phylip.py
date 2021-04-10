### s2: according to the gene partition file, the concatenated gene phylip output file (from ipyrad) were divided 
### into different genes alignments by the “Concatenated2gene_phylip” function.

### This script is used for devide the nex file into different genes, based on the gene position.

#### Any questions, please contact Wenbin Zhou. wzhou10@ncsu.edu

import os
import argparse
from Bio import SeqIO

def con2genes(output_partition, input_phylip_file_name):
    dir_path = os.path.dirname(output_partition)
    print(dir_path)
    output_genes_file = dir_path + "/split_genes/"
    if os.path.isdir(output_genes_file) == False:
        os.makedirs(output_genes_file)

    charset=[]
    ### read nex partition file line by line to extract the information of each locus position, including
    ### the starting position and ending position.
    with open (output_partition, "rU") as f:
        for line in f:
            line=line.strip ()
            if "charset" in line:
                #line = line.split (" = ")
                charset.append (line)
        # print charset

    for c in charset:
        name = c.split(" ")[1]
        # print name
        with open(output_genes_file + name + "_aligned.fas", "w") as out:
            for record in SeqIO.parse (input_phylip_file_name, "phylip"):
                locus = c.split(" = ")[1]
                print(locus)
                start = int(locus.split("-")[0])
                end_1 = locus.split("-")[1]
                end = int(end_1.split(";")[0])
                print(start)
                print(end)

                print(">" + record.id, file=out)
                print(record.seq[start:end], file=out)
    return(output_genes_file)

def main():
    parser = argparse.ArgumentParser(
        description="Divide concatenated gene into individual genes. The result will be generated at the same folder with partition file",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-ipa", "--inputparti", dest='input_partition_dir', type=str,
                        help='put the full directory of loci file')

    parser.add_argument("-iph", "--inputphy", dest='input_phylip_dir', type=str,
                        help='put the full directory of output partition file')
    args = parser.parse_args()
    if args.input_partition_dir and args.input_phylip_dir:
        input_partition = os.path.realpath(args.input_partition_dir)
        input_phylip = os.path.realpath(args.input_phylip_dir)
        con2genes(input_partition, input_phylip)

if __name__ == '__main__':
    main()
