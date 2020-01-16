# Mandatory Assignment 5 - Regular expressions

All files are tested on a ifi computer.

## General notice
I assume that the user have already installed everything needed for running these scripts.

## 5.1: Syntax highlighting

highlighter.py requires three cmd-arguments: syntaxfile themefile sourcefile_to_color

Example of how to run highlighter.py:
```
$ python3 highlighter.py nython.syntax nython.theme hello.ny
```
Highlighter then prints a text from a file with appropriate colors to standard out to the terminal.


## 5.2: Python syntax

Run the same way as in 5.1 but with python.syntax, a python.theme file and a python_sourcefile instead.

Example of how to run with python syntax:

```
$ python3 highlighter.py python.syntax python.theme demo.py
```

Highlighter then prints a text from a file with appropriate colors to standard out to the terminal.

### notice
Had to completely change my method for highlighting when I moved on to this task. First one did not work for every regex.

## 5.3: Syntax for your favorite language

Run the same way as in 5.1 but with favorite_language.syntax, favorite_language.theme and a java_sourcefile instead.

How to run:
```
$ python3 highlighter.py favorite_language.syntax favorite_language.theme favorite_demo.java
```

Highlighter then prints a text from a file with appropriate colors to standard out to the terminal.

## 5.4 Grep

grep.py has two required, and one optional cmd-arguments: [--highlighter] sourcefile regex

To get the instructions:
```
$ python3 blur.py --help
> usage: grep.py [-h] [--highlighter] sourcefile regex
```
Example of how to run grep.py:
```
$ python3 grep.py grep_demo.txt aaab
```
or
```
$ python3 grep.py --highlighter grep_demo.txt aaab
```

Grep them prints a text from a file with just the lines where it matches with the regex from the cmd-argument. If the optional
argument --highlighter is on, the matches will be highlighted with a red color. 




## 5.5 superdiff

takes two files as input: original_file and modified_file, and writes a file as output: result_file


Example of how to run diff.py:
```
$ python3 diff.py diff_original.txt diff_modified.txt
```
Diff will then write a file, diff_modified.txt, with all changes which have to be made to the first file to make it into the second file.

### notice

I had ALOT of difficulties of figuring out how to do this task in a good way. I know its not the best implementation but it works for
most cases, its just not always the right order. It doesnt say directly in the task that I need to use regex but I suppose its expected.

## 5.6 Coloring diff

Even though task 5.5 did not go as planned, I still managed to get the coloring right anyway.

Run the same way as in 5.1 but with diff.syntax diff.theme diff_output.txt instead.

How to run:
```
$ python3 highlighter.py diff.syntax diff.theme diff_output.txt
```

