'''
-------------------------------------------------------------------------------------
-> Problem Title: 205. Isomorphic Strings
-> Problem Status: Completed
-> Problem Attempted: 24/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/isomorphic-strings/description/

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

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        _stdin:
            arg1: str
            arg2: str
        _stdout: bool
        """
        s_len, t_len = len(s), len(t)
        if s_len != t_len:
            return False

        # return self._ansv1(s, t, s_len, t_len)
        return self._ansv2(s, t, s_len, t_len)

    def _ansv2(self, s: str, t: str, s_len: int, t_len: int) -> bool:
        """
        run: accepted
        time: o(n)
        space: o(n+n) ~ o(n)
        choke: none
        brief: overcome the mapping problem in ansv1()
        - in this apporach we 've map the every 's' chars to respective 't' chars
        - if any duplicate character is coming again, then we are checking if its 
        the same previously mapped character then they are isomorphic otherwise 
        they are not isomorphic.
        """
        s_map, t_map = {}, {}
        for idx in range(len(s)):
            c1, c2 = s[idx], t[idx]
            # check if ith index 's' string already mapped to 
            # another string character in s_map;;
            if c1 in s_map and s_map[c1] != c2:
                return False
            # check if ith index 't' string already mapped to 
            # another string character in t_map;;
            if c2 in t_map and t_map[c2] != c1:
                return False
            s_map[c1], t_map[c2] = c2, c1

        return True
    
    def _ansv1(self, s: str, t: str, s_len: int, t_len: int) -> bool:
        """
        _run: rejected
        _code: tc: o(n), sc: o(n), rt: nan
        _choke:
        - approach is having choke situation, based on length of unqiue characters
        but failed to trace the unique character sequence...
        - input: s="bbbaaaba", t: "aaabbbba", my_output: true, exp_output: false
        _brief:
        - we are mapping the count of each character in hashmap.
        - if the lenth of unique character of both array is same then True else False.
        """
        s_map, t_map = {}, {}
        for idx in range(s_len):
            s_map[s[idx]] = s_map.get(s[idx], 0) + 1
            t_map[t[idx]] = t_map.get(t[idx], 0) + 1

        if len(s_map.keys()) != len(t_map.keys()):
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
