# Mandatory Assignment 2 - Bash scripting

All files are tested on a ifi computer.


## 2.1: Climbing the directory tree

How to make file executable and to source the file:

```
$ chmod a+x climb.sh
$ source climb.sh
#Then you can use it:
$ climb 2
```
* climb = climb 1 = cd ..
* climb 5 = cd ../../../../../

Remember to source the file whenever you open a new terminal, or put it in your .bashrc.


## 2.2: A simple time tracker

How to make file executable, export LOGFILE and to run the file:

```
$ chmod a+x track.sh
$ export LOGFILE > logfile.sh
#Then you can run it with: ./track {start [label]|stop|status}
```

### Example
```
$ ./track start task 1
$ ./track status
$ ./track stop
```

Output logfile.txt:
```
START Wed Sep  4 12:21:17 CEST 2019
LABEL task 1
END Wed Sep  4 12:21:39 CEST 2019
```

Output terminal:
```
Active task: task 1
```


## 2.3 Making the time tracker useful

Run log command the same way as the other commands in 2.2
```
$ ./track log
#Output terminal:
>task 1: 00:00:22
```
This also workes when multiple tasks are done, and when a task is still running.

### Difficulties
* I thought the function "date" on the Mac were the same as the one on linux, so i wasted a lot of time on that. Once i tested it on
a ifi computer, it worked.
