'''
-------------------------------------------------------------------------------------
-> Problem Title: 290. Word Pattern
-> Problem Status: Completed
-> Problem Attempted: 13/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/word-pattern/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import collections


##---Main Solution
class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        _stdin: 
            arg1: str
            arg2: str
        _stdout: bool
        """
        p_len = len(pattern)
        n_len = len(s.split(" "))
        if n_len != p_len:
            return False
        # return self._ansv1(pattern, s)
        return self._ansv2(pattern, s, n_len, p_len)
    
    def _ansv2(self, pattern: str, s: str, n_len: int, p_len: int) -> bool:
        """
        _run: accepted (BEST!!!)
        _code: tc: o(n), sc: o(n), rt: 0 ms, tcz: 44/44
        _choke:
        _brief:
        -  this approach says hashmap cross mapping, which means first we map p_char with 
        s_char.
        - simnultaneously we check if there is any difference in our existing mapping 
        then we return False; else return True at the end;
        - for eg,
            pattern = "abba"
            s = "dog cat cat dog"
            # p_map and n_map built over loop
            p_map={'a': 'dog', 'b': 'cat'}
            s_map={'dog': 'a', 'cat': 'b'}
        """
        p_map, s_map = {}, {}
        s_list = s.split(" ")
        for p_ch, s_ch in zip(pattern, s_list):
            if (
                p_ch in p_map and p_map[p_ch] != s_ch or
                s_ch in s_map and s_map[s_ch] != p_ch
            ):
                return False
            p_map[p_ch] = s_ch
            s_map[s_ch] = p_ch

        return True
    
    def _ansv1(self, pattern: str, s: str) -> bool:
        """
        _run: accepted
        _code: tc:o(n), sc: o(1), rt: 0 ms, tcz: 44/44
        _choke: none
        _study: --- python oriented solution ----
        - first we check length of pattern with length of string in set datastructure.
        - then we map every string to pattern then convert to set remove duplicacy.
        """
        s_list = s.split(" ")
        p_set_len = len(set(pattern))
        s_set_len = len(set(s_list))
        zip_set_len = len(set(zip(pattern, s_list)))
        return p_set_len == s_set_len == zip_set_len


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
