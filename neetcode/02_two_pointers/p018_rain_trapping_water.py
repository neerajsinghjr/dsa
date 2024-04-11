'''
-------------------------------------------------------------------------------------
-> Problem Title: 42. Trapping Rain Water
-> Problem Status: Completed
-> Problem Attempted: 2024-04-07
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/trapping-rain-water/description/

Reference:-
https://youtu.be/ZI2z5pq0TqA

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

    def trap(self, height: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        n = len(height)
        if n == 1:
            return 0
        return self.ansv1(height, n)

    def ansv1(self, height, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- constraint ---
        [+] this problem is similar to (11. Container With Most Water) where we iterate
        over the loop using two pointer left and right.
        [+] and left pointer find max poles height from left and right pointer fetch max
        height from right side. here we are also doing the same kind of stuffs.
        --- explanation ---
        [+] crux here is also remains the same. find the max building height from the
        left to right and right to left side of the building.
        [+] here we are using two array - $max_left_level, $max_right_level to trace
        max height of building using for loop.
        [+] then after finding the $max_left_level and $max_right_level of the building
        [+] now we are iterating over the loop and for every ith index we have to find
        the min(max_left_level, max_right_level) and subtract it with the height[i] of
        the building to find the amount of rain water trappin units.
        """
        res = 0
        # max_left_level will trace max height from left side;;
        max_left_level = [0] * n
        # max_right_level will trace max height from right side;;
        max_right_level = [0] * n

        max_left_level[0] = height[0]  # default value from max_left_level
        max_right_level[n - 1] = height[n - 1]  # default value from max_right_level

        # Here we are finding max of max_left_level and max_right_level for
        # particularly ith index only;;
        for i in range(1, n):
            max_left_level[i] = max(max_left_level[i - 1], height[i])
            max_right_level[n - i - 1] = max(max_right_level[n - i], height[n - i - 1])

        # this is final logic for calculating water trapping.
        # for particular ith index you've to pick max of max_left_level and max_right_level
        # and subtract it with the height of ith building and result would be empty
        # space where the rain water can be trapped;
        for i in range(1, n):
            res += min(max_left_level[i], max_right_level[i]) - height[i]

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
