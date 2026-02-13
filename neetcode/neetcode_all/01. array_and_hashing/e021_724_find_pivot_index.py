'''
-------------------------------------------------------------------------------------
-> Problem Title: 724. Find Pivot Index
-> Problem Status: Completed
-> Problem Attempted: 04/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/find-pivot-index/description/

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
    
    def pivotIndex(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return 0
        # return self._ansv1(nums, n)
        return self._ansv2(nums, n)
    
    def _ansv2(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 0ms
        _choke:
        _brief:
        - same approach of calculating left_sum and right_sum but here i optimized the storing 
        requirement of left_sum and right_sum. 
        - we calculate left_sum and right_sum; if they are equal then return idx; else go on
        adding it to left_sum
        """
        cur_lt_sum = 0
        all_sum = sum(nums)
        for idx in range(n):
            cur_rt_sum = all_sum - cur_lt_sum - nums[idx]
            if cur_lt_sum == cur_rt_sum:
                return idx
            cur_lt_sum += nums[idx]

        return -1

    def _ansv1(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 8 ms
        _choke:
        _brief:
        - this approach calculates left_sum and right_sum nad ignorign the current idx every time.
        - left_sum demonstrate sum from 0th index to idx index
        - right_sum demonstrate from idx+1 to $n wherer $n is the length of nums.
        - at the end when left_sum and right_sum meets that would be the pivot of our array.
        """
        all_sum = sum(nums)
        lt_sum, rt_sum = [], []
        cur_lt_sum, cur_rt_sum = 0, 0

        for idx in range(n):
            if idx == 0:
                lt_sum.append(0)
            else:
                cur_lt_sum += nums[idx-1]
                lt_sum.append(cur_lt_sum)

        for idx in range(n):
            if idx == n-1:
                rt_sum.append(0)
            else:
                cur_rt_sum += nums[idx]
                rt_sum.append(all_sum - cur_rt_sum)

        for idx in range(n):
            if lt_sum[idx] == rt_sum[idx]:
                return idx

        return -1   # not index exists;;


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
