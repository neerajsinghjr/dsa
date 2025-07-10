'''
-------------------------------------------------------------------------------------
-> Problem Title: 1422. Maximum Score After Splitting a String
-> Problem Status: Completed
-> Problem Attempted: 10/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

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

    def maxScore(self, s: str) -> int:
        """
        _stdin
            arg: str
        _stdout: int
        """
        return self._ansv1(s, len(s))
        # return self._ansv2(s, len(s))
    
    def _ansv2(self, s, n):
        """
        _run: accepted (BEST!!!)
        _code: tc: o(n), sc: o(1), rt:0 ms, tcz: 104/104
        _choke: none
        _brief:
        - solves the problem by maximizing the score from splitting the binary string `s`into 
        two non-empty parts.
        - the score is calculated as the number of '0's in the left part plus the number of '1's 
        in the right part.
        - we first count all '1's in the string (to represent the initial right side). Then, as 
        we iterate through the string (excluding the last index),
        - we increment a counter for '0's on the left and decrement the '1's from the right as 
        we pass them.
        - at each step, we compute the current score and track the maximum encountered.
        """
        left_0s = 0
        right_1s = s.count("1")
        max_score = -math.inf
        for i in range(n-1):
            if s[i] == '0':
                left_0s += 1
            else:
                right_1s -= 1
            max_score = max(max_score, left_0s + right_1s)
        return max_score

    def _ansv1(self, s: str, n: int) -> int:
        """
        _run: accepted
        _code: tc: (n^2), sc: o(1), rt: 7 ms, tcz: 104/104
        _choke: none
        _brief:
        - brute-force solution for finding the maximum score by splitting the binary string `s`
        into two non-empty parts. 
        - the score is defined as the number of '0's in the left part plus the number of '1's 
        in the right part. 
        - the method handles small edge cases first, such as when the string has length 2 or 
        consists entirely of one character ('0' or '1'), where the maximum score is always `n-1`. 
        - for the general case, it iteratively considers every valid split position, explicitly
        counting '0's on the left and '1's on the right at each index, and 
        - tracks the maximum score found. This results in O(n²) time due to repeated substring scans 
        and character counting.
        """
        if n == 2:
            return n if s in "01" else (0 if s in "10" else n-1)
        if "0" not in s:
            return n-1
        if "1" not in s:
            return n-1
        max_score = -math.inf
        for i in range(n):
            if i == 0:
                lt_cnt = s[:i].count("0")
                rt_cnt = s[i+1:].count("1")
            else:
                lt_cnt = s[:i].count("0")
                rt_cnt = s[i:].count("1")
            cur_score = lt_cnt + rt_cnt
            max_score = max(max_score, cur_score)
        return max_score


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
