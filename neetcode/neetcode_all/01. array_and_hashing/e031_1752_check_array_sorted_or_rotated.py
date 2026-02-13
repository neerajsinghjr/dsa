'''
-------------------------------------------------------------------------------------
-> Problem Title: 1752. Check if Array Is Sorted and Rotated
-> Problem Status: Completed
-> Problem Attempted: 19/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import collections


##---Main Solution
class Solution:

    def check(self, nums: List[int]) -> bool:
        """
        _stdin:
            arg: list[int]
        _stdout: bool
        """
        n = len(nums)
        if n == 1:
            return True
        # return self._ansv1(nums, n)
        return self._ansv2(nums, n)

    def _ansv2(self, nums: List[int], n: int) -> bool:
        """
        _run: accepted (!!! BEST)
        _code: tc: o(n), sc: o(1), tc: 0 ms, tcz: 112/112
        _choke:
        _brief: --- fixed circularity issue using mod operator ---
        - this approach tells us about the mismatch counts; 0 states non-decreasing array, 
        1 states this is rotated one time, >1 states rotated more than one time.
        - inside a for_loop we are checking negative scenario where prev_idx num is greater 
        than cur_idx num then we are increamenting our mismatch flag
        - everytime when we increament our mismatch count states that we have observed a 
        rotated group of numbers
        - final status would be True if mistach is 0 or 1 else False
        """
        disorder_count = 0
        for idx in range(n):
            if nums[idx] > nums[(idx+1)%n]:
                disorder_count += 1
        return False if disorder_count > 1 else True 

    def _ansv1(self, nums: List[int], n: int) -> bool:
        """
        _run: rejected
        _code: tc: o(n), sc: o(1), tc: nan, tcz: ???
        _choke:
        - due to deficiency of circular check, mismatch count is showing different.
        _brief:
        - this approach tells us about the mismatch counts; 0 states non-decreasing array, 
        1 states this is rotated one time, >1 states rotated more than one time.
        - inside a for_loop we are checking negative scenario where prev_idx num is greater 
        than cur_idx num then we are increamenting our mismatch flag
        - everytime when we increament our mismatch count states that we have observed a 
        rotated group of numbers
        - final status would be True if mistach is 0 or 1 else False 
        """
        mismatch = 0
        for idx in range(1, n):
            if nums[idx-1] > nums[idx]:
                mismatch += 1
        return False if mismatch > 1 else True 


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
