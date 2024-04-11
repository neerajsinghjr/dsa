'''
-------------------------------------------------------------------------------------
-> Problem Title: 69. Sqrt(x)
-> Problem Status: Completed
-> Problem Attempted: 2024-03-28
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/sqrtx/description/

Reference:-
https://youtu.be/zdMhGxRWutQ

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

    def mySqrt(self, num: int) -> int:
        """
        _stdin: int
        _stdout: int
        """
        if num in (0, 1, 2):
            return 0 if not num else 1

        # return self.ansv1(num)
        return self.ansv2(num)

    def ansv2(self, num):
        """
        _run: rejected
        _code: time: o(logn), space: o(1)
        _study:
        --- explanation ---
        [+] uses binary search approach, to find the mid of the high and the low on
        every iteration.
        [+] on every iteration we square the mid value and check of equality with the
        `num` if current square match given the number x.
        [+] other we reduce the slider range again check for the mid value if current
        mid not found then at the end of while loop then return mid - 1.
        """
        lo, hi = 0, num
        while lo <= hi:
            mid = (lo + hi) >> 1
            sqr = mid * mid
            if sqr > num:
                hi = mid - 1
            elif sqr < num:
                lo = mid + 1
            else:
                return mid

        return hi

    def ansv1(self, num):
        """
        _run: accepted
        _code: time: o(k), space: o(1)
        _study:
        --- explanation ---
        [+] iterative over a loop from 3 to target, checking if square(i) == num,
        otherwise square(i) > num then return i-1 value would be the nearest square
        root value of the give number.
        """
        for i in range(3, num):
            if i * i == num:
                return i
            if i * i > num:
                return i - 1


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
