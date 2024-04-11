'''
-------------------------------------------------------------------------------------
-> Problem Title: 217. Contains Duplicate
-> Problem Status: Completed
-> Problem Attempted: 28/02/2024
-> Problem Description: 28/02/2024
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/contains-duplicate/description/

Reference:-
https://youtu.be/3OamzN90kPg

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
        n = len(nums)
        if not nums or n == 1:
            return False

        # return self.ansv1(nums, n)
        return self.ansv2(nums, n)

    def ansv2(self, nums, n):
        """
        run: accepted
        time: o(nlogn)
        space: o(1)
        choke: keep in mind for lower and upper bound
        brief: first sort the array then check if i index
        is equals to i+1 index.
        """
        if n == 2:
            return nums[0] == nums[1]

        nums = sorted(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

    def ansv1(self, nums, n):
        """
        run: accepted
        time: o(n)
        space: o(n)
        choke: none
        breif: To check duplicacy we are storing every element in a set.
        """
        numset = set()
        for num in nums:
            if num in numset:
                return True
            numset.add(num)

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
