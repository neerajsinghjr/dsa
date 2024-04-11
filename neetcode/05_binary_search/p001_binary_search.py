'''
-------------------------------------------------------------------------------------
-> Problem Title: 704. Binary Search
-> Problem Status: Completed
-> Problem Attempted: 2024-03-25
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/binary-search/description/

Reference:-
https://youtu.be/s4DPM8ct1pI

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

    def search(self, nums: List[int], target: int) -> int:
        """
        _stdin: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            return -1

        # return self.ansv1(nums, target, n)
        return self.ansv2(nums, target, n)

    def ansv2(self, nums, x, n):
        """
        _run: accepted
        _code: time: o(logn), space: o(1)
        _study:
        --- constraints ---
        [+] list should be in sorted order, asc or desc.
        --- explanation ---
        [+] binary search algorithm implementation.
        """
        debug = 0
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == x:
                return mid
            elif nums[mid] < x:
                lo = mid + 1
            elif nums[mid] > x:
                hi = mid - 1
            debug += 1
            if debug == n:
                break

        return -1

    def ansv1(self, nums, x, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- explanation ---
        linear search algorithm to trace the target element inside the list.
        """
        for idx, val in enumerate(nums):
            if val == x:
                return idx
        return -1


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
