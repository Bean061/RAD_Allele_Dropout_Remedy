# -*- coding:utf-8 -*-
import argparse
import os

def Loci2partition(ipyrad_locifile, output_partition):

    f1=open(ipyrad_locifile,'r') # open the the .tre file.
    s = len(f1.readlines())
    f1.close()  #print how many lines are there in the file, which will be used for the loop.
    sum = "#nexus\nbegin sets;\n"
    a = 0
    start_num = 1

    f1 = open(ipyrad_locifile, 'r')
    for n in range(s):
        text = f1.readline()
        print(text)
        if text[0] != "/":
            a = len(text.rstrip().split(" ")[-1])
            # print(text.split(" "))
            print(a)
            # sum = sum + text

        else:
            end_num = int(start_num) + int(a) - 1

            number = text.find("|")
            number2 = text.rfind("|")
            loci_number = text[number + 1:number2]

            sum = sum + "\tcharset gene" + str(loci_number) + " = " + str(start_num) + "-" + str(end_num) + ";\n"
            start_num = int(start_num) + int(a)

            fw = open(output_partition, 'a')  # you can change your output file name here.
            fw.write(sum)
            fw.close()
            # print sum
            sum = ""
    f1.close()

    fw = open(output_partition, 'a')  # you can change your output file name here.
    fw.write("end;\n")
    fw.close()
    print("yes")


def main():
    parser = argparse.ArgumentParser(
        description="Format transition from loci file (ipyrad output) to partition nexus file.",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-i", "--inputlocifile", dest='input_dir', type=str,
                        help='put the full directory of loci file')

    parser.add_argument("-o", "--outputpartition", dest='output_name', type=str,
                        help='put the full directory of output partition file')
    args = parser.parse_args()
    if args.input_dir and args.output_name:
        input_filename = os.path.realpath(args.input_dir)
        output_filename = os.path.realpath(args.output_name)
        Loci2partition(input_filename, output_filename)

if __name__ == '__main__':
    main()
