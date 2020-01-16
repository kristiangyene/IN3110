import sys
import os
import re


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
        colored_text = color_text(sourcefile, color_print(sourcefile, syntax_dict, theme_dict))
        print(colored_text)


def color_text(sourcefile, matched_colors):
    """Loops through the dict and colors the matched places simultaneously as it
    prevents the new match to overlap with the previous. Color where the dict 
    tells that the regex matches with the sourcefile.

        Args:
            sourcefile (String): a string to be colored. Representing the data 
            from the file.
            matched_colors (list): a list containing color code, match start and
            match end.

        return:
            sourcefile (String): A colored version of the sourcefile.

    """

    for start, end, color in matched_colors:
        start_code = f'\033[{color}m'

        color_positions = set() #All index positions in sourcefile occupied by color coding
        #Populate color_position with all indexes in sourcefile now occupied by color code
        for match in re.finditer(r"\033.+?m", sourcefile, flags=re.MULTILINE):
            for index in range(match.start(), match.end()):
                color_positions.add(index)
        # Find the new splits, ignoring positions occupied by color codes
        before, after , text = "","",""
        lim = 0
        counting = 0
        for i in range(len(sourcefile)):
            if counting == start:
                before = ""+sourcefile[:i]
                lim = i
            if counting == end:
                text = ""+sourcefile[lim:i]
                after = ""+sourcefile[i:]
            if i not in color_positions:
                counting += 1



        prev_defs = re.findall(r"\033.+?m", before+text) # FInd tha last coloring code inside match
        end_code = "\033[0m" if len(prev_defs) == 0 else prev_defs[-1] # Apply previous color code again, if any.


        text = re.sub(r"\033.+?m","",text) # Text to colorize cleaned from color codes
        color_string = start_code + text + end_code
        sourcefile = before\
            + color_string + after

 

    return sourcefile


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
    matched_colors = []
    #Puts all start/end matches in a list with the correct color code
    for name, regex in syntax_dict.items(): 
        for match in re.finditer(eval(regex), sourcefile, flags=re.MULTILINE):
            matched_colors.append([match.start(), match.end(),theme_dict[name]])
    return matched_colors
    

    


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
    syntax_dict = {}
    try:
        syntax_file = open(file, "r")
        for line in syntax_file.readlines():
            if ":" in line and line[0] is not "#":
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


