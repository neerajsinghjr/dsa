'''
-------------------------------------------------------------------------------------
-> Problem Title: 1189. Maximum Number of Balloons
-> Problem Status: Completed
-> Problem Attempted: 09/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/maximum-number-of-balloons/description/

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

    WORD = "balloon"
    WORD_LEN = len(WORD)

    def maxNumberOfBalloons(self, text: str) -> int:
        """
        _stdin:
            arg1: str
            arg2: str
        _stdout: int
        """
        n = len(text)
        if n < self.WORD_LEN:
            return 0
        # return self._ansv1(text, n)
        return self._ansv2(text, n)
    
    def _ansv2(self, text: str, n: int) -> int:
        """
        _run: accepted (code-level-optimization)
        _code: tc: o(n), sc: o(n), rt: 3 ms, tcz: 28/28
        _choke: none
        _brief:
        - simple hashmap under the hood. mapped text string into a hashmap and then count
        the occurence with out pre-mapped occurence; return the count;
        """
        count = 0
        hashmap = collections.Counter(ch for ch in text if ch in self.WORD)
        while True:
            for char in self.WORD:
                if hashmap.get(char, 0) == 0:
                    return count
                hashmap[char] = hashmap.get(char) - 1
            count += 1
        return count

    def _ansv1(self, text: str, n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 4 ms, tcz: 28/28
        _choke: none
        _brief:
        - simple hashmap under the hood. mapped text string into a hashmap and then count
        the occurence with out pre-mapped occurence; return the count;
        """
        count = 0
        hashmap = collections.Counter(text)
        while True:
            for char in self.WORD:
                if hashmap.get(char, 0) == 0:
                    return count
                hashmap[char] = hashmap.get(char) - 1
            count += 1
        return count


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
