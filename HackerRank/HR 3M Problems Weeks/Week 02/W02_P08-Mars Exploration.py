'''
Problem Description:
A pangram is a string that contains every letter of the alphabet. 
Given a sentence determine whether it is a pangram in the English alphabet. 
Ignore case. Return either pangram or not pangram as appropriate

# Example: 
s = The quick brown fox jumps over the lazy fox

# Function Description
Complete the function pangrams in the editor below. 
It should return the string pangram if the input string is a pangram. 
Otherwise, it should return not pangram.

pangrams has the following parameter(s):

1) string s: a string to test

# Returns
string: either pangram or not pangram
'''

#!/bin/python3

import string
import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def pangramsV1(s):
    # Write your code here
    aStr = 'qwertyuiopasdfghjklzxcvbnm'            ## alphabet;
    aDict = {}                                     ## alphabet dict;
    
    for ch in aStr:
        aDict[ch] = 0                               ## Frequency counts;
        
    for ch in s.lower():
        if ch in aStr:
            aDict[ch] += 1
            
    if 0 in list(aDict.values()):
        return "not pangram"        
        
    return "pangram"


## Python Based Solution;
def pangramsV2(s):
    if set(s.lower()) >= set(string.ascii_lowercase):
        return "pangram"
    return "not pangram"


def main():
    try:
        myStr = [
            "The quick brown fox jumps over the lazy fox",                      ## Not Pangram;
            "We promptly judged antique ivory buckles for the next prize",      ## Pangram;
            "We promptly judged antique ivory buckles for the prize"            ## Not Pangram;
        ]
        for string in myStr:
            # res = pangramsV1(string)                                          ## Version 1
            res = pangramsV2(string)                                          ## Version 2
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
    