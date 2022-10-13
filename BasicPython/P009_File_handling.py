#!/bin/python3

import os
import re
import sys
import time
import math
import json
import random


# example 1:
def mainEx1():
    ## Code Here...
    student = { "id": 1, "grade":"primary", "name": "neeraj"}
    print(type(student),student)
    studentJson = json.dump()
    print()

    file = open("abc.txt","r")
    print(file.read)


# example 2:
def mainEx2():
    # read or write but file close when block ends;
    with open('resources/file.txt', 'r+') as fileobj:
        ## read all the lines as it is in file;
        # line = fileobj.read()
        # print(line)
        
        ## read line by line using looping;
        # for (key,line) in enumerate(fileobj):
        #   print(f"{key} : {line}")

        ## readlines(): method returns the list of all lines inside the file;;
        # print(fileobj.readlines().strip())
        print(fileobj.tell())
        fileobj.read()
        print(fileobj.tell())
        fileobj.seek(4000)
        print(fileobj.readline())
        
        
        ## readline(): Read single line only at one time;;
        # for line in fileobj.readlines():
        #     lines = fileobj.readline()
        #     print(lines)


##---Main Execution;;
def main():
    mainEx2()
    
   # mainEx1()
   


if __name__ == '__main__':
    print("#------------ Code Start ---------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")