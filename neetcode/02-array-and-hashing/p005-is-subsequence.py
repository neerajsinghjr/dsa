'''
-------------------------------------------------------------------------------------
-> Problem Title: 392. Is Subsequence
-> Problem Status: Completed
-> Problem Attempted: 2024-02-01
-> Problem Description:
-------------------------------------------------------------------------------------

problem:-
https://leetcode.com/problems/is-subsequence/description/

Subsequence:-
A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).

reference:-
https://youtu.be/99RVfqklbCE

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
        if not s:
            return True
        if not t:
            return False

        return self.ansv1(s, t)
        # return self.ansv2(s, t)

    def ansv2(self, s, t):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: simpe solution where every character of 's' string
        should be in 't' string.
        """
        s_idx, t_idx = 0, 0
        while (s_idx < len(s) and t_idx < len(t)):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1

        return True if s_idx == len(s) else False

    def ansv1(self, s, t):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: simpe solution where every character of 's' string
        should be in 't' string.
        """
        s_idx = 0
        is_subsequence = False
        for t_idx in range(len(t)):
            if s_idx < len(s) and s[s_idx] == t[t_idx]:
                s_idx += 1

        if s_idx == len(s):
            is_subsequence = True

        return is_subsequence


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
