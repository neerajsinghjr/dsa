'''
-------------------------------------------------------------------------------------
-> Problem Title: 645. Set Mismatch
-> Problem Status: Completed
-> Problem Attempted: 05/08/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/set-mismatch/description/

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

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        _stdin:
            arg: list[int]
        _stdout: list[int]
        """
        return self._ansv1(nums)
    
    def _ansv1(self, nums: List[int]) -> List[int]:
        """
        """
        n = len(nums)
        n_sum = n*(n+1)//2  # sum of n natural number;;
        dup_sum = sum(nums)
        uniq_sum = sum(set(nums))
        return [dup_sum-uniq_sum, n_sum-uniq_sum]


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
