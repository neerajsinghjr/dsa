'''
-------------------------------------------------------------------------------------
-> Problem Title: 1624. Largest Substring Between Two Equal Characters
-> Problem Status: 04/08/2025
-> Problem Attempted: 04/08/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

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

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        _stdin: 
            arg1: str
        _stdout: int
        """
        # return self._ansv1(s)
        return self._ansv2(s)

    def _ansv2(self, s):
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 0 ms; tcz: 59/59
        _choke: none
        _brief: --- optimized sol ---
        - optimized solution using a hash map to track the first occurrence of each character.
        - iterates through the string once, calculating the distance between the current index
        and the character's first appearance to find the maximum length.
        """
        freq_map = {}
        max_len = -1
        for i, char in enumerate(s):
            if char in freq_map:
                cur_len = i - freq_map[char] - 1
                max_len = max(max_len, cur_len)
            else:
                freq_map[char] = i
        return max_len 

    def _ansv1(self, s):
        """
        _run: accepted
        _code: tc: o(n^2), sc: o(1), rt: 27 ms; tcz: 59/59
        _choke: none
        _brief: --- brute force ---
        - it iterates through all possible pairs of characters to find matching ones 
        and calculates the substring length between them.
        """
        n = len(s)
        max_len = -1
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    max_len = max(max_len, len(s[i+1:j]))
                    continue
        return max_len


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
