'''
Problem Description:
You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: 
skeeG
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...
def reverseWord(s):
    rev = ""
    size = len(s)-1
    while(size >= 0):
        rev += s[size]
        size -= 1
    return rev


def main():
    try:
        data = "GeeksForGeeks"
        res = reverseWord(data)
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    