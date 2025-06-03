'''
-------------------------------------------------------------------------------------
-> Problem Title: 217. Contains Duplicate
-> Problem Status: Completed
-> Problem Attempted: 03/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/contains-duplicate/description/

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
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        _stdin: 
            arg1: nums: __list__
        _stdout: __bool__
        """
        n = len(nums)
        if n <= 2:
            if n == 1:
                return False
            return nums[0] == nums[1]

        # return self.ansv1(nums, n)
        return self.ansv2(nums, n)
    
    def ansv2(self, nums, n):
        """
        _run: accepted
        _code: time: o(nlogn), space: o(n)
        _study:
        --- explanation ---
        [+] as per problem there is only one duplicate of any existing values. That also means
        we have to find our duplicate.
        [+] first we sorted our the nums, because will make every nums in sequence and duplicate
        also lined up one after another.
        [+] then we run simple loop and check if both consecutive duplicate exists or not.
        """
        nums.sort()
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True
        return False

    
    def ansv1(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- explanation ---
        [+] using hashset or hashmap to check if the current value is already being parsed
        or not.
        [+] if parsed then true else false
        """
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


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
