import sys
import re

def main():
    """takes two files as input, and outputs a file containing all changes which
    have to be made to the first file to make it into the second file. It goes 
    through the files line by line, prints 0 in front of the line if not 
    modified, prints + if its added, and prints - if its deleted. Not sure if
    we are supposed to use regex here, but i could'nt find a way. The method 
    does not always take into account the correct order of the lines.

    """
    orig_file = list(open(sys.argv[1], 'r').readlines())
    mod_file = list(open(sys.argv[2], 'r').readlines())
    output_file = open("diff_output.txt", "w")

    orig_lines = [re.sub("\n", "", line) for line in orig_file]
    mod_lines = [re.sub("\n", "", line) for line in mod_file]

    for line in orig_lines:
        #if its in orig but not in mod then it must be deleted
        if not line in mod_lines:
             output_file.write("- " + line + "\n")
        #if its in orig and in mod then it must be neutral
        elif line in mod_lines:
            output_file.write("0 " + line + "\n")
            mod_lines.remove(line)
    for line in mod_lines:
        #if its in mod but not in orig then it must be added
        if not line in orig_lines:
             output_file.write("+ " + line + "\n")


if __name__ == '__main__':
    main()