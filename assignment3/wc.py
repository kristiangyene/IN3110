#!/usr/bin/env python3
import os
import sys

def wc():
    """Main-function. Starts the wc program.

    Args:
        Files: as many type(files) the user wants.

    """
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            print_file_info(arg)


def print_file_info(fileName):
    """Reads the file and counts lines, words and chars in it. 

    The function opens the file, tripple for-loop through it to count and closes
    the file. Finally it prints a nice list of all argument files.

    Args:
        fileName (str): name of the file to be read.

    """
    lines = 0
    words = 0
    chars = 0
    fn = open(fileName, "r")
   

    for line in fn:
        lines += 1
        for word in line.split():
            words += 1
            for char in word:
                chars += 1
    fn.close()
    print (lines, words, chars, " " + fileName)

wc()