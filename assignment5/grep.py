import argparse
import re
from highlighter import color_text
from highlighter import color_print


def main():
    """
    A small user interface using argument parser. The program takes a filename, 
    along with a regular expression from the command line.

    A grep-like utility. Prints all lines where the regex matches on one part of 
    the line. It's possible to color the matching parts of the lines by using 
    --highlight flag.
    """
    parser = argparse.ArgumentParser(description="Usage of grep utility")
    parser.add_argument("sourcefile",
                        type=str,
                        help="Sourcefile to be matched with the regex.")
    parser.add_argument("regex",
                        type=str,
                        help="A regular expression to match with the lines in t\
                            he sourcefile.\n")
    parser.add_argument("--highlighter",
                        action="store_true",
                        help="Use to highlight matches")

    args = parser.parse_args()
    try:
        sourcefile = list(open(args.sourcefile, 'r').readlines())
        syntax_dict = {"example": "'"+args.regex+"'"} # Added extra quotes because of the eval() in highlighter
        theme_dict = {"example": 31}
        for line in sourcefile:
            #Need to remove newline and string literals on the regex
            line = re.sub("\n", "", line)
            matcher = re.compile(args.regex.strip('\"'))
            #Ignore lines without matches
            if matcher.search(line):
                if args.highlighter:
                    #Call on color_print from highlighter    
                    print(color_print(line, syntax_dict, theme_dict))

                else: print(line)

    except OSError as error:
        print("error: " + str(error))


if __name__ == '__main__':
    main()