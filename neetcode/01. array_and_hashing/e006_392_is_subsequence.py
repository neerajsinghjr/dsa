'''
-------------------------------------------------------------------------------------
-> Problem Title: 392. Is Subsequence
-> Problem Status: Completed
-> Problem Attempted: 11/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/is-subsequence/description/

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

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        stdout:
            arg1: str
            arg2: str
        stdout: bool
        """
        n = len(s)
        if n == 0:
            return True
        if n == 1:
            return s in t
        # return self._ansv1(s, t, n)
        # return self._ansv2(s, t, n)
        return self._ansv3(s, t, n)
    
    def _ansv3(self, s, t, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1), rt: 0ms
        _choke: none
        _brief: another way of writing the solution, 
        - here we are calculating answer one the basis of the idx. after loop ends if 
        s_idx reach end, indirectly $s is a subsequence of $t.
        """
        s_idx, t_idx = 0, 0
        while(s_idx < len(s) and t_idx < len(t)):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        return s_idx == len(s)

    
    def _ansv2(self, s, t, n):
        """
        _run: accepted
        _code: time:o(n), space: o(1), rt: 0ms
        _choke: 
        - problem for ansv1() is taken care in ansv2()
        _brief:
        - we traverse with a primary loop with idx and kept a $i for t_chars.
        - every iteration we check if the primary index $s_chars matches with the
        t_chars and if match then we manually increament the $t_counter.
        - if matching all character, we trace the end of the $t_chars then we return
        true.      
        """
        i = 0
        for idx in range(len(t)):
            if t[idx] == s[i] and i == (n-1):
                return True
            if t[idx] == s[i] and i < n:
                i += 1
        return False
        
    def _ansv1(self, s, t, n):
        """
        _run: rejected
        _code: time:o(n*2), space: o(1), rt: inf
        _choke: 
        - approach is brute force but character subsequence must be in sequential order. 
        for eg, s="acb", t="ahbgdc", my_output=true, exp_output=false
        _brief:
        - simple traversing from one string and searching inside another string
        if exist then true else false.
        - you wont be able to control or check the sequence of $s_char in $t_char.
        """
        for ch in s:
            if not ch in t:
                return False
        return True


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
