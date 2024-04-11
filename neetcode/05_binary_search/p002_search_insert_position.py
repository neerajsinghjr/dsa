'''
-------------------------------------------------------------------------------------
-> Problem Title: 35. Search Insert Position
-> Problem Status: Completed
-> Problem Attempted: 2024-03-25
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/search-insert-position/description/

Reference:-
https://youtu.be/K-RYzDZkzCI

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

    def searchInsert(self, nums: List[int], x: int) -> int:
        """
        _stdin: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            if nums[0] == x or x < nums[0]:
                return 0
            return 1
        if x > nums[-1]:
            return n
        return self.ansv1(nums, x, n)

    def ansv1(self, nums, x, n):
        """
        _run: accepted
        _code: time: o(logn), space: o(1)
        _study:
        --- constraints ---
        [+] in this binary search derivative, i've used `lo` and `hi` pointer
        where `lo` pointer should be lesser than `hi` pointer only.
        [+] But that doesn't mean we are not including the `hi` pointer. `hi`
        pointer is included directly inside the `mid` variable.
        --- explanation ---
        [+] problem statement is to look for target element inside the nums list
        [+] if target element is found then return the mid index directly
        [+] we can use this index as the reference index on which target element
        can be adjusted.
        """
        debug = 0
        lo, hi = 0, n - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == x:
                return mid
            elif nums[mid] < x:
                lo = mid + 1
            elif nums[mid] > x:
                hi = mid

        return hi


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
