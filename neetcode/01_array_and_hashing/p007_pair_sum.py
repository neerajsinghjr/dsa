'''
-------------------------------------------------------------------------------------
-> Problem Title: 1. Two Sum
-> Problem Status: Completed
-> Problem Attempted: 2024-03-01
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/two-sum/description/

Reference:-
https://youtu.be/KLlXCFG5TnA

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
    def twoSum(self, nums: List[int], x: int) -> List[int]:
        n = len(nums)
        if n == 2:
            return [0, 1] if sum(nums) == x else []
        return self.ansv1(nums, x, n)

    def ansv1(self, nums, x, n):
        """
        run: accepted
        time: o(n)
        space: o(n)
        choke: Don't use abs() to calculate leftover sum.
        brief: Iteratively calculating the leftover sum by subtracting target value
        with the current iterative value.
        if leftover is the one we needed then ok
        else store the value in hashmap so that we can use it later;;
        """
        existing_sum = {}
        for i in range(n):
            leftover_sum = x - nums[i]
            if leftover_sum in existing_sum:
                return [i, existing_sum[leftover_sum]]
            else:
                existing_sum[nums[i]] = i
        return []


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
