'''
-------------------------------------------------------------------------------------
-> Problem Title: 1299. Replace Elements with Greatest Element on Right Side
-> Problem Status: Completed
-> Problem Attempted: 2024-02-29
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Reference:-
https://youtu.be/ZHjKhUjcsaU

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

    def replaceElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [-1]
        if n == 2:
            return [nums[1], -1]

        # return self.ansv1(nums, n)
        return self.ansv2(nums, n)
        # return self.ansv3(nums, n)

    def ansv3(self, nums, n):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: We started looping from the end of the list to the start.
        - calculate right_max with default(-1)
        - every loop we check for max between right_max and cur index value
        - whoever is bigger we kept that at right_max and also at the array[ith] index.
        """
        right_max = -1
        for idx in range(n - 1, -1, -1):
            cur_max = max(right_max, nums[idx])
            nums[idx] = right_max
            right_max = cur_max

        return nums

    def ansv2(self, nums, n):
        """
        run: accepted
        time: o(n*k)
        space: o(n)
        choke: none
        brief: here we are not using max function on every iteration
        instead we've optimized it till we have any value greater than
        our current max.
        """
        ans, mx = [], -1
        for idx in range(n - 1):
            if not (mx > nums[idx]):
                mx = max(nums[idx + 1:])
            ans.append(mx)
        ans.append(-1)
        return ans

    def ansv1(self, nums, n):
        """
        run: TLE
        time: o(n^2)
        space: o(n)
        choke: none
        brief: iterating from 0th to n-1 and fetch max from i+1 index
        for ith index and append to array.
        """
        ans = []
        for idx in range(n - 1):
            ans.append(max(nums[idx + 1:]))
        ans.append(-1)
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
