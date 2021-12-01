'''
Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3

# Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

# Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
Input: s = ""
Output: 0

# Example 5:
Input: "dvdf"
Ouput: 2
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...

# FAILED TO PASS: EXAMPLE 3
def lengthOfLongestSubstringV1(s):
    i = maxCount = 0
    size,temp, = len(s),set()
    while(i<size):
        if(s[i] in temp):
            temp.remove(s[i])
        temp.add(s[i])
        maxCount= max(maxCount, len(temp))
        i += 1
    return maxCount

# FAILED TO PASS EXAMPLE: 5
def lengthOfLongestSubstringV2(s):
    i = maxCount = 0
    size,temp, = len(s),set()
    while(i<size):
        if(s[i] in temp):
            temp.remove(s[i])
        temp.add(s[i])
        maxCount= max(maxCount, len(temp))
        i += 1
    return maxCount

# PASSED: Used two pointer for insertion and Deletion;
def lengthOfLongestSubstringV3(s):
    i = d =maxCount = 0                     ## i: insertion, d: deletion;
    size,temp, = len(s),set()
    while(i<size):
        if(s[i] not in temp):
            temp.add(s[i])
            maxCount= max(maxCount, len(temp))
            i += 1
        else:
            temp.remove(s[d])               ## Removing from Beginning of Set;
            d += 1
            
    return maxCount
        
    


def main():
    try:
        string = "abcabcbc"
        # res = lengthOfLongestSubstringV1(string)                ## V1
        # res = lengthOfLongestSubstringV2(string)                ## V2
        res = lengthOfLongestSubstringV3(string)                ## V3
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
    