'''
-------------------------------------------------------------------------------------
-> Problem Title: 53. Maximum Subarray
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/maximum-subarray/description/

Reference:-
https://youtu.be/5WZl3MMT0Eg?si=wEJVH1NWh4Kd33Yp

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

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if (len(nums) == 1):
            return nums[0]

        # return self.ansv1(nums,0,len(nums)-1)
        return self.ansv2(nums)
        # return self.ansv3(nums)

    def ansv3(self, nums):
        """
        _run: accepted
        _code: tc: o(n), sc: o(1)
        _study:
        --- explanation ---
        [+] by default cur_sum and max_sum is set to default nums[0] because as per constraints
        [+] here what we are doing different is the way we are finding the cur_sum and which
        is we are looking for finding the cur_sum by max of nums[i] and cur_sum + nums[i]
        [+] then checking if the max_sum is equals to max of max_sum and cur_sum.
        """
        cur_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)

        return max_sum

    # Kadane : O(n)
    def ansv2(self, nums):
        """
        _run: accepted
        _code: tc: o(n), sc: o(1)
        _study:
        --- algorithm ---
        [+] kadane algorithm to calculate the running sum.
        --- explanation ---
        [+] here we are calculating the running sum of the nums arrays and checking if the
        cursum is greater than maxsum.
        [+] if somehow the cursum is lesser than 0 then we are resettingt he cursum to 0,
        again and start over from zero.
        """
        maxsum = nums[0]
        cursum = nums[0]

        for i in range(1, len(nums)):
            if (cursum < 0):
                cursum = 0
            cursum += nums[i]
            if (maxsum < cursum):
                maxsum = cursum

        return maxsum

    # Noob : O(n^2)
    def ansv1(self, nums, lo, hi):
        """
        _run: TLE
        _code: tc: o(n^2), sc: o(1)
        _study:
        --- explanation ---
        [+] used two nested loop to calculate the max subarray sum.
        """
        maxsum = 0
        for i in range(0, hi):
            cursum = nums[i]
            for j in range(i, hi):
                cursum += nums[j]
                if (cursum > maxsum):
                    maxsum = cursum

        return maxsum


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
