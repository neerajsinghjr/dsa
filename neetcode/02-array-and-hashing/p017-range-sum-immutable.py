'''
-------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

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


"""
NOTE: 
refer ansv1() and ansv2(), run time different on 2024-03-04
because the test case are of 10^4 items. Then optimizing can be 
done using giving space.
Refer ansv3() once with o(n) space complexity.
"""

class NumArray:

    def __anv1(self, nums):
        self.nums = nums

    def __anv2(self, nums):
        self.nums = nums

    def __ansv3(self, nums):
        cur = 0
        for num in nums:
            cur += num
            self.nums.append(cur)

    def __init__(self, nums):
        self.nums = []
        # self.__ansv1(nums)  # ref: ansv1()
        # self.__ansv2(nums)  # ref: ansv2()
        self.__ansv3(nums)  # ref: ansv3()

    def sumRange(self, left: int, right: int) -> int:
        # return self._ansv1(left, right)
        # return self._ansv2(left, right)
        return self._ansv3(left, right)

    def _ansv3(self, left, right):
        """
        run: accepted (optimized)
        time: o(n)
        space: o(n)
        choke: none
        breif: --- prefix sum algorithms used ---
        approach demonstrate calculating the prefix sum for the given array before hand.
        we iterate over the loop and store the sequential sum in run time.
        so when give right and left index. We can directly fetch the sum for the respective
        nums[right] and nums[left]. Instead of Calculating again and again.
        """
        right_sum = self.nums[right]
        left_sum = self.nums[left - 1] if left > 0 else 0

        return right_sum - left_sum

    def _ansv2(self, left, right):
        """
        run: accepted
        time: o(n) ~ 2199ms
        space: o(1)
        choke: check run-time
        breif: calculating sum by iteration.
        """
        cur_sum = 0
        for i in range(left, right + 1):
            cur_sum += self.nums[i]
        return cur_sum

    def _ansv1(self, left, right):
        """
        run: accepted
        time: o(n) ~ 819ms
        space: o(1)
        choke: none
        brief: calculate sum between the range left to right.
        """
        return sum(self.nums[left:right + 1])


##---Main Execution;;
def main(res=None):
    try:
        # Your NumArray object will be instantiated and called as such:
        limit = 10000000
        nums = [i for i in range(limit)]
        obj = NumArray(nums)
        res = obj.sumRange(left=1000,right=10000)
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
