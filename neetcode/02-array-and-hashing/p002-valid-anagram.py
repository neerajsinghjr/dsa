'''
-------------------------------------------------------------------------------------
-> Problem Title: 242. Valid Anagram
-> Problem Status: Completed
-> Problem Attempted: 2024/02/28
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/valid-anagram/

Reference:-
https://youtu.be/9UtInBqnCgA

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
from collections import defaultdict


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


##---Main Execution;;
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return self.ansv1(s, t)
        # return self.ansv2(s, t)
        # return self.ansv3(s, t)
        return self.ansv4(s, t)

    def ansv4(self, s, t):
        """
        run: accepted
        time: o(nlogn)
        space: o(1)
        choke: none
        brief: anagram is just jumble words of the first string.
        so sorting both the string and checking equality works.
        """
        return sorted(s) == sorted(t)

    def ansv3(self, s, t):
        """
        run: accepted
        time: o(n+m)
        space: o(n+m)
        choke: length of both string should same.
        brief: optimized version for ansv1()
        """
        s_map, t_map = {}, {}

        # map the character occurrences;;
        for idx in range(len(s)):
            s_map[s[idx]] = s_map.get(s[idx], 0) + 1
            t_map[t[idx]] = t_map.get(t[idx], 0) + 1

        # verify the character occurrences;;
        for key in s_map:
            if s_map[key] != t_map.get(key, 0):
                return False

        return True

    def ansv2(self, s, t):
        """
        run: accepted
        time: o(nlogn)
        space: o(1)
        choke: none
        brief: anagram is just jumble words of the first string.
        so sorting both the string and checking equality works.
        """
        a = "".join(sorted(s))
        b = "".join(sorted(t))
        return a == b

    def ansv1(self, s, t):
        """
        run: accepted
        time: o(n+m)
        space: o(n+m)
        choke: none
        brief: anagram are simple jumble words only
        1) first count the occurrence of characters
        2) we have to verify the number of keys - exactly same
        3) we have to verify the values of mapped to that keys -- exactly same.
        """
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        # mapping first string;;
        for char in s:
            s_map[char] += 1

        # mapping second string;;
        for char in t:
            t_map[char] += 1

        # C1: check for number of keys;;
        if sorted(s_map.keys()) != sorted(t_map.keys()):
            return False

        # C2 : check for values of keys;;
        for sc in s_map.keys():
            if s_map.get(sc) != t_map.get(sc):
                return False

        return True


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
