'''
-------------------------------------------------------------------------------------
-> Problem Title: 1800. Maximum Ascending Subarray Sum
-> Problem Status: Ongoing ...
-> Problem Attempted: 03/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/maximum-ascending-subarray-sum/description/

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
    
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        return self._ansv1(nums, n)
    
    def _ansv1(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 0 ms
        _choke: 
        - make sure to set the max_sum variable to the 0th index num value at the start
        - when prev_val > cur_val then reset the cur_sum to currently iterating num value.
        _brief:
        - singularly interating over a loop and check 
        - if prev_val < cur_val then we are adding num to our cur_sum; 
        - else we are setitng our cur_sum variable again to the existing loop num value.
        - at the enw we are returning the max of cur_sum and max_sum value.
        """
        max_sum = cur_sum = nums[0]
        for idx in range(1, n):
            if nums[idx-1] < nums[idx]:
                cur_sum = cur_sum + nums[idx] 
            else:
                cur_sum = nums[idx]
            max_sum = max(cur_sum, max_sum)
        return max_sum
        

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
