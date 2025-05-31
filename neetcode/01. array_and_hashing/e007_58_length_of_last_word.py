'''
-------------------------------------------------------------------------------------
-> Problem Title: 58. Length of Last Word
-> Problem Status: Completed
-> Problem Attempted: 13/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/length-of-last-word/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        stdout:
            arg1: str
        stdout: int
        """
        # return self._ansv1(s)
        # return self._ansv2(s)
        # return self._ansv3(s)
        return self._ansv4(s)
    
    def _ansv4(self, s):
        """
        _run: accepted
        _code: time: o(n), space: o(1), rt: 1ms
        _choke: 
        - alway keep and mind to check the current idx. i.e, idx >= 0
        _brief:
        - loop1 will help us skip the while spaces
        - loop2 help us counting the length of the final word
        """
        strlen = 0
        idx = len(s)-1
        # loop 1: help us skip the white character from the end;;
        while(s[idx] == " " and idx >= 0):
            idx -= 1
        # loop 2: help us counting the length of final length of word;; 
        while(s[idx] != " " and idx >= 0):
            idx -= 1
            strlen += 1
        return strlen

    def _ansv3(self, s):
        """
        _run: accepted
        _code: time: o(n), space: o(1), rt: 0ms
        _choke: none
        _brief:
        - in this we are traced the first character from the end and start counting 
        the character length.
        - this approach obsolete the requirement for calling the strip() method and 
        simple iterative over the loop and return the length of string.
        """
        strlen = 0
        is_char_traced = False
        for idx in range(len(s)-1, -1, -1):
            if s[idx] == " " and not is_char_traced:
                continue
            if s[idx] != " ":
                strlen += 1
                is_char_traced = True
            if s[idx] == " " and is_char_traced:
                break
        return strlen
    
    def _ansv2(self, s):
        """
        _run: accepted
        _code: time: o(n), space: o(1), rt: 0ms
        _choke: none
        _brief:
        - main component here is also the python strip() method to trunc 
        extra white space from start and the end.
        - secondly a for loop and for every iteration we are counting the 
        character and will terminate as soon as white space traced. 
        """
        s, strlen = s.strip(), 0
        for idx in range(len(s)-1,-1,-1):
            if s[idx] == " ":
                break
            strlen += 1
        return strlen
    
    def _ansv1(self, s):
        """
        _run: accepted
        _code: time: o(n), space: o(k), rt: 0ms
        _choke: none
        _breif:
        - used stip() method to remove extra blank space from start and end.
        - converting to list and return length of last index word list.
        """
        s = s.strip()
        s_list = s.split(" ")
        return len(s_list[-1])


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
