'''
Problem Description:
In this challenge, the task is to debug the existing code to successfully 
execute all provided test files.

Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.

Debug the given function strings_xor to find the XOR of the two given strings appropriately.

Note: 
You can modify at most three lines in the given code and you cannot add or remove lines to the code.

To restore the original code, click on the icon to the right of the language selector.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


"""
## Error Prone Function,
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] = t[i]:
            res = '0';
        else:
            res = '1';
"""
## Main Working Function, here...
## Change this Function only,
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';


def main():
    try:
        res = ""
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
    