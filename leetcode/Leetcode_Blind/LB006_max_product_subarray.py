'''
-------------------------------------------------------------------------------------
-> Problem Title: 152. Maximum Product Subarray
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/maximum-product-subarray/description/

Reference:-
https://youtu.be/lXVy6YWFcRM?si=vtyDMMLuvtxriMEi

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

    def maxProduct(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: nums : __list__
        _stdout: __int__
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # return self.ansv1(nums, n)
        return self.ansv2(nums, n)

    def ansv2(self, nums, n):
        """
        _run: accepted
        _code: ts: o(n), sc: o(1)
        _study:
        --- constraints ---
        [+] The challenge lies in handling negative numbers, as a negative number can turn
        a minimum product into a maximum product and vice versa.
        --- explanation ---
        [+] To tackle this, we can use a dynamic programming approach where we keep track of
        both the maximum and minimum products up to the current position
        [+] Initialize two variables to keep track of the maximum and minimum products up to
        the current position (max_so_far and min_so_far).
        [+] Iterate through the array and update these variables based on the current number.
        If the current number is negative, it can swap the maximum and minimum when multiplied.
        [+] Keep track of the global maximum product seen so far.
        """
        if not nums:
            return 0

        cur_max = cur_min = res = nums[0]

        for i in range(1, n):
            # find max of current iteration by multiplying num with cur_max, cur_min;;
            new_max = max(nums[i], cur_max * nums[i], cur_min * nums[i])

            # find min of current iteration by multiplying num with cur_max, cur_min;;
            cur_min = min(nums[i], cur_max * nums[i], cur_min * nums[i])

            # update the cur_max with pre_max;;
            cur_max = new_max

            # update the result;;
            res = max(res, cur_max)

        return res

    def ansv1(self, nums, n):
        """
        _run: TLE [166/190]
        _code: ts: o(n^2), sc: o(1)
        _study:
        --- explanation ---
        [+] two nested loop and keep tracking the maximum product while running both loop
        """
        res = nums[0]

        for i in range(n):
            cur_prod = nums[i]
            for j in range(i + 1, n):
                cur_prod *= nums[j]
                res = max(res, cur_prod)

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
