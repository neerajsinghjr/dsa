'''
-------------------------------------------------------------------------------------
-> Problem Title: 1929. Concatenation of Array
-> Problem Status: Completed
-> Problem Attempted: 2024/02/28
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/concatenation-of-array/

Reference:-
https://youtu.be/68isPRHgcFQ

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
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        # return self.ansv1(nums)
        # return self.ansv2(nums)
        # return self.ansv3(nums)
        return self.ansv4(nums)

    def ansv4(self, nums, iteration=2):
        """
        run: accepted
        time: o(n)
        space: o(2xn) ~ o(n)
        choke: none
        brief: scalable approach not iteration can be extended to any
        number of times.
        """
        ans = []
        for _ in range(iteration):
            for num in nums:
                ans.append(num)
        return ans

    def ansv3(self, nums):
        """
        run: accepted
        time: o(n)
        space: o(2xn) ~ o(n)
        choke: this solution will work for 1 iteration only due to
            using indexing approach. (refer ansv4())
        brief: simple traversing from start the end and appending
            to the same nums list.
        """
        for idx in range(len(nums)):
            nums.append(nums[idx])
        return nums

    def ansv2(self, nums):
        """
        run: accepted
        time: o(n)
        space: o(2n) ~ o(n)
        choke: none
        breif: python list can added or multiply
        """
        return nums + nums

    def ansv1(self, nums):
        """
        run: accepted
        time: o(n)
        space: o(2n) ~ o(n)
        choke: none
        breif: python list can added or multiply
        """
        return nums * 2


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
