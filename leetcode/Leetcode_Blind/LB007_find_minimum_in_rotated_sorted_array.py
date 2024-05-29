'''
-------------------------------------------------------------------------------------
-> Problem Title: 153. Find Minimum in Rotated Sorted Array
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Reference:-
https://youtu.be/nIVW4P8b1VA?si=jRNXlYBeVIRdMSwp

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
    def findMin(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: nums : __list__
        _stdout: __int__
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        return self.ansv1(nums, n)

    def ansv1(self, nums, n):
        """
        _run: accepted
        _code: ts: o(logn), sc: o(1)
        _study:
        --- explanation ---
        [+] as per constraints the array is sorted once but its not rotated in a cycle
        with some pivot.
        [+] core of this problem revolves around the binary search algorithms because
        array is sorted and runtime should be (logn) as per question
        [+] so, we can expect at least one time the array will be rotated;
        [+] for eg,
        org_list = [1,2,3,4,5,6], rotated 1 time
        rot_list = [4,5,6,1,2,3]
        s0: there can be any stage where your subarray is completely sorted
        then in that case nums[lo] <= nums[hi] then nums[lo] would be lowest
        s1: find mid of the solution
        s2: if nums[mid] >= nums[lo], then lo = mid + 1
        s3: else hi = mid - 1
        s4: return res variable
        """
        lo, hi = 0, n - 1
        res = nums[0]

        while lo <= hi:
            # base check because anytime in the array we can reach to a point where the
            # current subarray is sorted perfectly in that case
            if nums[lo] <= nums[hi]:
                res = min(res, nums[lo])
                break

            mid = lo + (hi - lo) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1

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
