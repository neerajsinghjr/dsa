'''
-------------------------------------------------------------------------------------
-> Problem Title: 303. Range Sum Query - Immutable
-> Problem Status: Completed
-> Problem Attempted: 06/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/range-sum-query-immutable/description/

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
class NumArray:

    def __init__(self, nums: List[int]):
        """--- Entry Point ---"""
        self.nums = nums
        # moved below line to _ansv3() as per use;;
        # self.all_sum = self.get_prefix_sum()

    def sumRange(self, left: int, right: int) -> int:
        """
        _stdin:
            arg1: int
            arg2: int
        _stdout: int
        """
        # return self._ansv1(left, right)
        return self._ansv2(left, right)
        # return self._ansv3(left, right)
    
    def get_prefix_sum(self):
        """--- generating prefix sum array ---"""
        cur_sum, all_sum = 0, []
        for idx, num in enumerate(self.nums):
            cur_sum += num
            all_sum.append(cur_sum) 
        return all_sum
    
    def _ansv3(self, left: int, right: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 3676 ms
        _choke:
        _brief: --- prefix sum algorithms used ---
        - approach demonstrate calculating the prefix sum for the given array. we 
        iterate over the loop and store the sequential sum in run time.
        - at the time of getting the index we are only calculating the differential
        sum by subtracting the sum present at right_idx and left_idx in our prefix 
        sum array and that's itft].
        """
        all_sum = self.get_prefix_sum()
        rt_sum = all_sum[right]
        lt_sum = all_sum[left-1] if left > 0 else 0
        return rt_sum - lt_sum

    def _ansv2(self, left: int, right: int) -> int:
        """
        _run: accepted (BEST!!!)
        _code: tc: o(n), sc: o(1), rt: 2345 ms
        _choke:
        _brief:
        - simple for loop again but this time we are iterating specifically between 
        (left <= idx >= right) index and calculating returning the sum.
        """
        cur_sum = 0
        for idx in range(left, right+1):
            cur_sum += self.nums[idx]
        return cur_sum

    def _ansv1(self, left: int, right: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: (1), rt: 693 ms
        _choke: none
        _brief:
        - simple calling sum method but specifically pulling nums between 
        (left <= nums >= right) first.
        """
        return sum(self.nums[left: right+1])    




##---Main Execution;;
def main(res=None):
    try:
        # Your NumArray object will be instantiated and called as such:
        obj = NumArray(nums)
        res = obj.sumRange(left,right)
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
