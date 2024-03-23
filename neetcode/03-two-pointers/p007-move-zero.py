'''
-------------------------------------------------------------------------------------
-> Problem Title: 283. Move Zeroes
-> Problem Status: Completed
-> Problem Attempted: 2024-03-19
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/move-zeroes/description/

Reference:-

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
    def moveZeroes(self, nums: List[int]) -> None:
        """
        """
        # Do not return anything, modify nums in-place instead.
        n = len(nums)
        if n == 1:
            return nums
        if 0 not in nums:
            return nums

        # return self.ansv1(nums, n)
        return self.ansv2(nums, n)

    def ansv3(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- approach ---
        two pointer approach in which one right pointer successively
        iterate over the loop. till it found any non-zero value.
        if it found any non-zero then it replace with left pointer value.
        """
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return

    def ansv2(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- optimial ---
        optimize the code first level zero counting loop.
        """
        # s1: overlapping the zeroth value with non-zero value;;
        i, nz_idx = 0, 0  # tracking non-zero index;;
        while (i < len(nums)):
            if nums[i] != 0:
                nums[nz_idx] = nums[i]
                nz_idx += 1
            i += 1

        # s2: add the zero at the end of the loop;;
        while (nz_idx < len(nums)):
            nums[nz_idx] = 0
            nz_idx += 1

        return

    def ansv1(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- intution ---
        problem is straigth forward move the zeros to the end of the array.
        --- solution ---
        [+] first iteration count the number of zero
        [+] second iteration replace the non-zero with the respective zero index place.
        [+] third iteration is just append the respective zero count at the end.
        """
        zeros = 0
        # s1: count the occurrence of zero
        for n in nums:
            if n == 0:
                zeros += 1

        # s2: overlap the new values in the nums array;;
        i, nz_idx = 0, 0  # tracking non-zero index;;
        while (i < len(nums)):
            if nums[i] != 0:
                nums[nz_idx] = nums[i]
                nz_idx += 1
            i += 1

        # s3: add the zero at the end of the loop;;
        while (zeros):
            nums[nz_idx] = 0
            nz_idx += 1
            zeros -= 1

        return


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
