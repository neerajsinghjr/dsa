'''
-------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
...

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
    
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        _stdin:
            arg1: list[int]
        _stdout: bool
        """
        n = len(nums)
        if n == 1:
            return True
        # return self._ansv1(nums, n)
        return self._ansv2(nums, n)
    
    def _ansv2(self, nums: int, n: int):
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 57 ms, tcz: 371/371
        _choke: none
        _brief: 
        - simple approach with two variable - is_increasing, is_decreasing with the default
        value is set True
        - for_loop is checking pattern for is_increasing and is_decreasing ...
            - is_increase : ~(cur_idx's num is smaller than nex_idx's num)
            - is_decrease : ~(cur_idx's num is greater than cur_idx's num)
        - everytime when we mismatch the pattern we set the flag to false in both the case
        """
        is_increasing, is_decreasing = True, True
        for idx in range(1, n):
            # increasing sequence 
            if not(nums[idx-1] <= nums[idx]):
                is_increasing = False
            if not(nums[idx-1] >= nums[idx]):
                is_decreasing = False
        return is_increasing or is_decreasing
    
    def _ansv1(self, nums: int, n: int):
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 16 ms, tcz: 371/371
        _choke: none
        _brief:
        - Using adjacent for_loops approach to check increasing/decreasing number patterns
        - for trace monotonic decreasing pattern - we are checking negation of nature like 
            - cur_idx nums should be greater than the nex_idx nums
        - for trace monotonic increasing pattern - we are checking negation of nature like 
            - cur_idx nums should be greater than the  nex_idx nums
        """    
        def check_monotonic_pattern(flag=True):
            ans = True
            for idx in range(1, n):
                if flag: 
                    # NOTE: for monotonic increasing pattern: we will check for decreasing pattern
                    if not(nums[idx-1] <= nums[idx]):
                        return False
                else: 
                    # NOTE: for monotonic decreasing pattern: we will check for increasing pattern
                    if not(nums[idx-1] >= nums[idx]):
                        return False
            return ans
        
        # --- main execution --- #
        ans = check_monotonic_pattern()
        if not ans:
            ans = check_monotonic_pattern(flag=False)
        return ans


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
