'''
-------------------------------------------------------------------------------------
-> Problem Title: 520. Detect Capital
-> Problem Status: Completed
-> Problem Attempted: 02-01-2023
-> Problem Description: 
-------------------------------------------------------------------------------------

We define the usage of capitals in a word to be right when one of the
following cases holds:

All letters in this word are capitals, like "USA". All letters in this word
are not capitals, like "leetcode". Only the first letter in this word is
capital, like "Google". Given a string word, return true if the usage of
capitals in it is right.

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

-> 1 <= word.length <= 100
-> word consists of lowercase and uppercase English letters.

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Solution:

    def detectCapitalUse(self, word: str) -> bool:
        """
        atype: str (~word)
        rtype: bool 
        """
        n = len(word)
        if not word:
            return False
        if(n == 1):
            return True
        
        # return self.ansv1(word, n)
        # return self.ansv2(word, n)
        return self.ansv3(word, n)


    def ansv3(self, word, n):
        """
        _run: accepted
        _code: optimise, time: o(n) and space: o(1)
        _choke:
        _study:
        simple approach counting uppercase and lowercase inside 
        uppper alphabets
        """
        uc,lc = 0,0
        letters = ("QWERTYUIOPASDFGHJKLZXCVBNM")
        for ch in word:
            if ch in letters:
                uc += 1
            else:
                lc += 1
        return (uc == n or lc == n) or (lc+1 == n and word[0].isupper())
 

    def ansv2(self, word, n):
        """
        _run: accepted
        _code: optimised, time: o(n), space: o(1)
        _choke: none
        _study:
        simply counted the uppercase count and lowercase count
        and check for equality at the end.
        """
        uc,lc = 0,0
        for ch in word:
            if ch.isupper():
                uc += 1
            else:
                lc += 1
        
        return (uc == n or lc == n) or (lc+1 == n and word[0].isupper())

    
    def ansv1(self, word, n):
        """
        _run: accepted
        _code: brute force, time:o(n) and space: o(1)
        _choke: none 
        _study: simply check for each scenario for uppercase
        and lowercase + titlecase
        """
        res = True
        flag = word[0].isupper()
        is_uc, is_lc = False, False 
        # check for smallcase only
        for char in word[1:]:
            # case 1: uppercase check;
            if(char.isupper() and flag):
                continue
            # case 2: lowercase check;
            if(char.islower()):
                continue
            else:
                res = False
                break
        return True if res else False


##---Main Execution;;
def main(res=None):
    try:
    	data = []				
        obj = Solution()	
        res = None
        print(f"Result: {res}") if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced : {e}")
    
    else:
        print("Program Completed : Success")

    finally:    
        print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    