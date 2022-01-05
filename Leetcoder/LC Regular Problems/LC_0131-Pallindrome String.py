'''
Problem Description:
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
class Solution:
    # @cache  
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            print(f"s[:{i}]::",s[:i][::-1])
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                print(f"=====>")
                for suf in self.partition(s[i:]):  # process suffix recursively
                    print("[s[:i]]", [s[:i]]+suf)
                    ans.append([s[:i]] + suf)
        return ans


def main():
    try:
        s="abacddcfghj"
        obj = Solution()
        print("string:",s)
        res = obj.partition(s)
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

        

if __name__ == '__main__':
    print("#-------------------- Code Start -------------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#-------------------- Code Stop --------------------#")
    