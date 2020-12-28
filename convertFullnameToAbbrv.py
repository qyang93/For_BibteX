#####################################################################################
#####                   date: 28 of December 2020                               #####
#####       Written by Qun Yang (Qun.Yang@cpfs.mpg.de) in MPI-CPFS              #####
#####################################################################################

import sys
import getopt
import numpy as np
import re

def usage():
    print("This script is used to interconvert the journal's full name and abbreviation.")
    print("For running the script, it needs journal_fullname_abbrv.txt and your own ref.bib.")
    print("Usage:")
    print("-h,--help\t\tprint usage;")
    print("-o,--output-file\toutput file.")
    print("python convert_fullname_abbrv.py -o output_file_name input_file_name")
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

    data = np.genfromtxt("journal_fullname_abbrv.txt",delimiter=";", dtype = str,skip_header=0, skip_footer=0)
    all_journal_fullname = []
    all_journal_abbrv = []
    for i,j in zip(data[:,0], data[:,1]):
        all_journal_fullname.append(i.strip())
        all_journal_abbrv.append(j.strip())

    journal_line = re.compile(r"\s*(j|J)ournal\s+\=")
    line_of_journal_line = 0
    with open(input_file_name, "r") as fr:
        line_list = fr.readlines()
    with open(output_file_name,"w") as fw:
        for i, line in enumerate(line_list):
            if journal_line.match(line.split("{")[0]):
                line_of_journal_line = i+1
                line_of_RN_num = line_of_journal_line - 3
                ref_RN_num = line_list[line_of_RN_num-1].split("{")[1].split(",")[0]
                journal_name = line_list[line_of_journal_line-1].split("{")[1].split("}")[0]
                if run == 0 :
                    if journal_name in all_journal_fullname:
                        #print(line_of_journal_line)
                        #print(journal_name)
                        #print(all_journal_fullname.index(journal_name))
                        #print(all_journal_abbrv[all_journal_fullname.index(journal_name)])
                        #print("\n")
                        fw.write(line_list[line_of_journal_line-1].replace(journal_name,all_journal_abbrv[all_journal_fullname.index(journal_name)]))
                    else:
                        fw.write(line)
                if run == 1:
                    if journal_name in all_journal_abbrv:
                        fw.write(line_list[line_of_journal_line-1].replace(journal_name,all_journal_fullname[all_journal_abbrv.index(journal_name)]))
                    else:
                        fw.write(line)
            else:
                fw.write(line)
    return 0
                
if __name__ == "__main__":
    print("run=0: convert journal's full name to abbreviation'")
    print("run=1: convert journal's abbreviation to full name")
    run = int(raw_input("run=: "))
    main()
            
