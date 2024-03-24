'''
-------------------------------------------------------------------------------------
-> Problem Title: 290. Word Pattern
-> Problem Status: Completed
-> Problem Attempted: 2024-03-07
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/word-pattern/description/

Reference:-
https://youtu.be/W_akoecmCbM

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from itertools import zip_longest


##---Main Solution
class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        stdin: str
        stdout: bool
        """
        # both the pattern and string are equal;;
        if pattern == s and len(pattern) == len(s) == 1:
            return True

        # return self.ansv1(pattern, s)
        return self.ansv2(pattern, s)

    def ansv2(self, pattern, s):
        """
        _run: accepted
        _code: time: o(n) | space: o(n+m)
        _choke: length of pattern and word should be equal
        _study: we are mapping every single pattern to their respective word and vice-versa.
        if any pattern maps to different word vice-versa, then in that case pattern failed.
        """
        words = s.split(" ")

        # length of pattern and string should be equal;;
        if len(pattern) != len(words):
            return False

        pattern_to_word_map = {}
        word_to_pattern_map = {}

        for p, w in zip(pattern, words):
            # pattern_to_word_map map pattern to word;;
            if p in pattern_to_word_map and pattern_to_word_map[p] != w:
                return False
            # word_to_pattern_map map word to pattern;;
            if w in word_to_pattern_map and word_to_pattern_map[w] != p:
                return False

            pattern_to_word_map[p] = w
            word_to_pattern_map[w] = p

        return True

    def ansv1(self, pattern, s):
        """
        _run: accepted
        _code: time:o(n) | space: (1)
        _choke: none
        _study: --- python oriented solution ----
        - first we check length of pattern matched with length of string in set datastructure.
        - then we map every string to pattern then convert to set remove duplicacy
        """
        s = s.split(" ")
        res = (len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern, s))))
        return res


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
