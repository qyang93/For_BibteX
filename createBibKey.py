#####################################################################################
#####                   date: 30 of December 2020                               #####
#####       Written by Qun Yang (Qun.Yang@cpfs.mpg.de) in MPI-CPFS              #####
#####################################################################################

import sys
import getopt
import numpy as np
import re

def usage():
    print("Readme:")
    print("This script is used to atomatically create the BibTex key in the format of \n[first_author_name + year + journal_name + first_word_of_title]")
    print("For running the script, it needs your own file.bib as input_file_name.")
    print("Usage:")
    print("-h,--help\t\tprint usage;")
    print("-o,--output-file\toutput file.")
    print("python createBibKey.py -o output_file_name input_file_name")
    return

def main():
    try:
        # Short option syntax: "hv:"
        # Long option syntax: "help" or "verbose="
        opts, args = getopt.getopt(sys.argv[1:], "ho:", ['help', 'output-file='])
    except getopt.GetoptError as err:
        # Print debug info
        print(str(err))
        usage()
        sys.exit(2)
    for option, argument in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit(1)
        elif option in ("-o", "--output-file"):
            output_file_name = argument
    input_file_name = args[0]

    bibkey=[]
    with open(input_file_name, "r") as fr:
        line_list = fr.readlines()
    with open(output_file_name,"w") as fw:
        num = 0
        for cnt, line in enumerate(line_list):
            if line.split("{")[0] == "@article" or line.split("{")[0] == "@book":
                num += 1
                bibkey = [line_list[cnt+1].split("{")[1].split(",")[0],line_list[cnt+3].split("{")[1].split("}")[0].replace(" ","").replace(".",""),line_list[cnt+2].split("{")[1].split()[0]] 
                fw.write(line.replace(line.split("{")[1].split(",")[0],"%s" % ("".join(bibkey))))
                fw.write("\n")
            else:
                fw.write(line)
        #print(num)
    return 0
                
if __name__ == "__main__":
    main()
            
