'''
-------------------------------------------------------------------------------------
-> Problem Title: 367. Valid Perfect Square
-> Problem Status: Completed
-> Problem Attempted: 2024-03-28
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/valid-perfect-square/description/

Reference:-


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

    def isPerfectSquare(self, num: int) -> bool:
        """
        _stdin: int
        _stdout: bool
        """
        if num == 1:
            return True
        return self.ansv1(num)
        # return self.ansv2(num)

    def ansv2(self, num):
        """
        _run: accepted
        _code: time: o(logn), space: o(1)
        _study:
        --- explanation ---
        [+] race here is to find the mid value among a high is the square value
        and low is 0 by default and we are aiming the find the square of mid variable
        [+] if square(mid) is equal to square(num) then return True
        [+] if square(mid) > square(num) then high should point to mid - 1
        [+] if square(mid) < square(num) then low should point to mid + 1
        """
        lo, hi = 0, num
        while lo <= hi:
            mid = (lo + hi) >> 1
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr > num:
                hi = mid - 1
            elif sqr < num:
                lo = mid + 1
        return False

    def ansv1(self, num):
        """
        _run: accepted (brute-force)
        _code: time: o(k), space: o(1)
        _study:
        --- explanation ---
        [+] iterative over a loop from 2 to target, checking if square(i) == num or not
        """
        for i in range(2, num):
            if i * i == num:
                return True
            elif i * i > num:
                return False
        return False


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
