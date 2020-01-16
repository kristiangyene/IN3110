# Mandatory Assignment 3 - Basic Python programming

Most files are tested on a ifi computer.


## 3.1: wc

How to make file executable and to run wc:
```
$ chmod a+x wc.py
$ alias wc='./wc.py'
# Then you can use it:
$ wc *.py
> 27 61 302  wc.py
# or
$ wc *
```

NB: make sure you are in the right directory when executing.

A list of the number of lines, words, and chars of the argument file will be shown.

## 3.2: Unit tests for complex numbers

The first unit tests are implemented.


## 3.3: Implement complex numbers

I assume that pytest is already installed.

How to run pytest:

```
$ pytest -v
```
NB: make sure you are in the right directory when executing.

Then you will get something like this if all the tests passes:

test_complex.py::test_add PASSED &nbsp;&nbsp; [ 16%]

test_complex.py::test_sub PASSED &nbsp;&nbsp; [ 33%]

test_complex.py::test_multi PASSED  &nbsp;&nbsp; [ 50%]

test_complex.py::test_conj PASSED  &nbsp;&nbsp;  [ 66%]

test_complex.py::test_mod PASSED    &nbsp;&nbsp;  [ 83%]

test_complex.py::test_equal PASSED  &nbsp;&nbsp;   [100%]

=========================== 6 passed in 0.02 seconds ==========================

### Difficulities

Had a problem with running pytest at a IFI computer. I dont think its installed and i dont have
permission to download it. However i think it should work either way.

## 3.4 Make your implementation work with Python’s complex numbers

Run pytest the same way as 3.3

Functions now work with python complex numbers and integers. I made a decision to not implement the two last methods
because of other assignments in other classes. But i will take a look at it later.

