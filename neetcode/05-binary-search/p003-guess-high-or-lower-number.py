'''
-------------------------------------------------------------------------------------
-> Problem Title: 374. Guess Number Higher or Lower
-> Problem Status: Completed
-> Problem Attempted: 2024-03-25
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/guess-number-higher-or-lower/description/

Reference:-
https://youtu.be/xW4QsTtaCa4

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
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def guessNumber(self, n: int) -> int:
        """
        _run: accepted
        _code: time:o(logn), space: o(1)
        _study:
        --- constraints ---
        -> -1: Your guess is higher than the number I picked (i.e. num > pick)
        -> 1: Your guess is lower than the number I picked (i.e. num < pick)
        -> 0: your guess is equal to the number I picked (i.e. num == pick)
        --- explanation ---
        simple binary search implementation as per the question requirements
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            my_guess = guess(mid)
            if my_guess == -1:
                hi = mid - 1
            elif my_guess == 1:
                lo = mid + 1
            else:
                return mid


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
