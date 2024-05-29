'''
-------------------------------------------------------------------------------------
-> Problem Title: 33. Search in Rotated Sorted Array
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Reference:-
https://youtu.be/U8XENwh8Oy8?si=KmKs0f-8gk-6X0NZ

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
        _stdin:
            arg1: nums : __list__
            arg2: target : __int__
        _stdout: __int__
        """
        return self.ansv1(nums, target)

    def ansv2(self, arr, target):
        """
        _run: accepted
        _code: ts: o(logn), sc: o(n)
        _study:
        --- explanation ---
        [+] we have to find the left or the right side at which the target element will be find.
        [+] we can only do that by find the short subarray which is rotated only
        [+] then on the basis of binary search we can check whether the target is in there or not.
        --- explanation ---
        [+] first calculate the $mid_value and if the target value falls in between the $mid_value
        and $left_value then you are target value can be in this range otherwise your target value
        is in another space.
        [+] do the same process everytime until unless we got the final our result or list burnout.
        """
        lo, hi = 0, len(arr) - 1

        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            if arr[mid] == target:
                return mid

            if arr[lo] <= arr[mid]:
                # Left Side is sorted;;
                if target >= arr[lo] and target <= arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # Right Side is sorted;;
                if target >= arr[mid] and target <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1

        return

    def ansv1(self, nums, target):
        """
        _run: accepted (brute-force)
        _code: ts: o(n), sc: o(1)
        _study:
        --- explanation ---
        [+] linear search approach to look for target value if exist then index else -1
        """
        for idx, num in enumerate(nums):
            if num == target:
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
