'''
-------------------------------------------------------------------------------------
-> Problem Title: 1768. Merge Strings Alternately
-> Problem Status: Completed
-> Problem Attempted: 2024-03-19
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/merge-strings-alternately/description/

Reference:-
https://youtu.be/LECWOvTo-Sc

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

    def mergeAlternately(self, w1: str, w2: str) -> str:
        """
        _stdin: str, str
        _stdout: str
        """
        if not w1 or not w2:
            return w1 if not w1 else w2

        # return self.ansv1(w1, w2)
        # return self.ansv2(w1, w2)
        return self.ansv3(w1, w2)

    def ansv3(self, w1, w2):
        """
        _run: accepted
        _code: time: o(n), space: o()
        _study:
        --- intution ---
        [+] below solution depends on sliding window approach, where we have concatenate
        both the string into one first.
        [+] then run the loop over the combined string where start = 0, mid = len(word1)
        [+] where one pointer in loop will run from start 0 to len(word1) and then next
        pointer will run from len(word1) to len(combined string)
        [+] rest for fallback contcatenate the leftover string for complete solution.
        """
        res = ""
        start = 0
        mid = len(w1)
        w = w1 + w2
        w_len = len(w)

        while (start < len(w1) and mid < w_len):
            res += w[start] + w[mid]
            start += 1
            mid += 1

        if w[mid:]:
            res += w[mid:]

        if w[start: len(w1)]:
            res += w[start: len(w1)]

        return res

    def ansv2(self, w1, w2):
        """
        _run: accepted
        _code: time: o(m+n), time: o(m+n)
        _study:
        --- intuition ---
        intuition is pretty much the same but here i 've optimized
        a code a bit level.
        """
        i = 0
        res = ""
        w1_len = len(w1)
        w2_len = len(w2)
        w_len = max(w1_len, w2_len)

        while (i < w_len):
            if i < w1_len:
                res += w1[i]
            if i < w2_len:
                res += w2[i]
            i += 1

        return res

    def ansv1(self, w1, w2):
        """
        _run: accepted
        _code: time: o(m+n), space: (m+n)
        _study:
        --- intuition ---
        iterating over a loop and creating the new string.
        --- observation ---
        style of coding is not efficient here addition and checking if
        and else is not optimized.
        """
        i = 0
        res = ""
        w1_len = len(w1)
        w2_len = len(w2)
        w_len = max(w1_len, w2_len)

        while (i < w_len):
            w1_char = w1[i] if i < w1_len else ""
            w2_char = w2[i] if i < w2_len else ""
            res += w1_char + w2_char
            i += 1

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
