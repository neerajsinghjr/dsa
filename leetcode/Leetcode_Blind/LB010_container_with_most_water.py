'''
-------------------------------------------------------------------------------------
-> Problem Title: 11. Container With Most Water
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/container-with-most-water/description/

Reference:-
https://youtu.be/RyBM56RIWrM?si=_7RNYXUhTzGLyCC9

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

    def maxArea(self, poles: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        n = len(poles)

        if n == 2:
            if n < 2:
                return 0
            min_hp = min(poles)  # pole with minimum height;;
            return min_hp * min_hp

        # return self._ansv1(poles, n)
        return self._ansv2(poles, n)

    def _ansv2(self, poles, n):
        """
        _run: accepted (optimal)
        _code: time: o(n), space: o(1)
        _study:
        --- approach ---
        [+] main intuition based on two pointer approach with the area of rectangle formula;
        --- explanation ---
        [+] logic to calculate water level among two pole depends on the short poles height
        among the pole mapped to $lo and $hi pointer. that would be our length then breadth
        can be calculate using the difference of index $hi and $lo.
        [+] logic to slide among the left and right pole depends on the height of the pole
        mapped to $lo and $hi again. whoever have the smaller height will be shift by 1 unit
        in the hope of getting the bigger pole next time.
        """
        max_water = 0
        lo, hi = 0, n - 1

        while (lo < hi):

            # S1: logic to calculate water among poles;;
            min_hp = min(poles[lo], poles[hi])  # pole with minimum height;;
            cur_water = (hi - lo) * min_hp
            max_water = max(max_water, cur_water)

            # S2: whoever among the $lo, $hi contains small height will be +1 only;;
            if poles[lo] < poles[hi]:
                lo = lo + 1
            else:
                hi = hi - 1

        return max_water

    def _ansv1(self, poles, n):
        """
        _run: TLE (brute-force)
        _code: time: o(n^2), space: o(1)
        _study:
        --- main crux of problem ---
        [+] level of water can be stored between two poles, till its cover the height
        of the shorter poles only.
        [+] after calculating the pole height, calculate the breadth of subtracing right
        side index with the left side index.
        [+] iterate 2 x nested loop for above step and filter the max_water in every
        iteration.
        """
        max_water = 0

        for l in range(n):
            cur_water = 0
            for r in range(l + 1, n):
                common_height = min(poles[l], poles[r])
                cur_water = (r - l) * common_height  # area of rectangle;;
                max_water = max(max_water, cur_water)

        return max_water


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
