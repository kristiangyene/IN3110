import sys
import os
import re
from collections import OrderedDict


def main():
    """Main fuction to start the program. Calls on the filereader methods to get 
    dictionarys containing data. Calls on color_print and send with the dicts.
    
    """
    if len(sys.argv) == 4:
        for i in sys.argv:
            if not os.path.isfile(i):
                print("Argument: '" + str(i) + "' is not a file")
                sys.exit(0)
        syntax_dict = read_syntaxfile(sys.argv[1])
        theme_dict = read_themefile(sys.argv[2])
        sourcefile = open(sys.argv[3], "r").read()
        colored_text = color_print(sourcefile, syntax_dict, theme_dict)
        print(colored_text)


def color_text(matchobject, code):
    """Recieves a match object and a code to apply to that match

        Args:
            matchobject
            code: color code 

        return:
             (String): A colored version of the match to use in substituton

    """

    prev_defs = re.findall(r"\033.+?m", matchobject.string[:matchobject.start()]) # FInd tha last coloring code inside match
    end_code = "\033[0m" if len(prev_defs) == 0 else prev_defs[-1] # Apply previous color code again, if any.
    text = re.sub(r"\033.+?m","",matchobject.group()) # Text to colorize cleaned from color codes
    start_code = "\033[{}m".format(code) # New color code for text

    return start_code+ text+ end_code


def color_print(sourcefile, syntax_dict, theme_dict):
    """Loops through the syntax dict to find matches in the sourcefile. Puts
    all matches(match start and match end) in a list with the associated color
    codes as tuples. 

        Args:
            sourcefile (String): a string to be colored. Representing the data 
            from the file.
            syntax_dict (dict): a dict containing name(key) and regex(value).
            theme_dict (dict): a dict containing name(key) color code(value).
           

        return:
            matched_colors (list): a list containing where matches start and end,
            and the color to be applied to each match. This list is sorted after
            the match start.

    """
    #Puts all match objects in a list with the correct color code
    for name, regex in syntax_dict.items(): 
        print(name, regex, re.findall(eval(regex), sourcefile))
        sourcefile = re.sub(eval(regex), lambda t, code = theme_dict[name]: color_text(t,code), sourcefile) 
        #https://stackoverflow.com/questions/26496119/passing-two-arguments-to-replace-function-for-re-sub

    return sourcefile
    

    


#Read syntaxfile
def read_syntaxfile(file):
    """Reads the syntaxfile sent as an cmd-argument, and makes a dictionary out
    of the data. 

        Args:
            file (file): .syntax file containing regular expressions and names.
            
        Return:
            syntax_dict (dict): dictionary with name of area to color as key, 
            and regex as value.

    """
    syntax_dict = OrderedDict()
    try:
        syntax_file = open(file, "r")
        for line in syntax_file.readlines():
            regex, name = line.rsplit(":", 1)
            syntax_dict[name.strip()] = regex.strip()
        syntax_file.close()
        return syntax_dict

    except IOError as error:
        print("error: " + str(error))
        


#read themefile
def read_themefile(file):
    """Reads the themefile sent as an cmd-argument, and makes a dictionary out
    of the data. 

        Args:
            file (file): .theme file containing names and color codes
            
        Return:
            theme_dict (dict): dictionary with name of area to color as key, 
            and color code as value.

    """
    theme_dict = {}
    try:
        theme_file = open(file, "r") 
        for line in theme_file.readlines():
            name, seq = line.split(":", 1)
            theme_dict[name.strip()] = seq.strip()
        theme_file.close()
        return theme_dict

    except IOError as error:
        print("error: " + str(error))



if __name__ == '__main__':    
    main()


