'''
-------------------------------------------------------------------------------------
-> Problem Title: 15. 3Sum
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/3sum/description/

Reference:-
https://youtu.be/jzZsG8n2R9A?si=HSea0B36oNrkk_ql

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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        _stdin:
            arg1: list[int]
        _stdout: list[list[int]]
        """
        n = len(nums)
        if n == 3:
            if sum(nums) == 0:
                return [nums]
            return []

        # return self.ansv1(nums, n)
        # return self.ansv2(nums, n)
        return self.ansv3(nums, n)

    def ansv3(self, nums, n, target=0):
        """
        _run: accepted
        _code: time: o(nlogn), space: o(1)
        _study:
        --- choked for solution v2() ---
        refer the optimization point
        --- explanation ---
        [+] Sorting the Array:
        [+] Iterating Through the Array:
        [+] Avoiding Duplicate Triplets: Inside the loop, there is a check to
        skip duplicate elements. If the current element nums[i] is the same as
        the previous element nums[i - 1], it means that we have already processed
        triplets with the same starting element, so we skip to the next iteration
        [+] Two-Pointer Approach
        [+] Finding Triplets
        [+] Adjusting Pointers
        [+] Skipping Duplicate Elements: After finding a triplet, the code skips
        duplicate elements by incrementing the left pointer while the next element
        is the same as the previous one, and decrementing the right pointer while
        the previous element is the same as the next one.
        """
        res = []
        nums.sort()

        for i in range(n):
            # optimize 1: To avoid duplicate number from ith side;;
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while (j < k):
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum < 0:
                    j += 1
                elif cur_sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    j, k = j + 1, k - 1

                    # optimize 2: avoid duplicate values from left side till reach kth;;
                    while (nums[j] == nums[j - 1] and j < k):
                        j += 1

                    # optimize 3: avoid duplicate value from right side till reach jth;;
                    while (nums[k] == nums[k + 1] and j < k):
                        k -= 1

        return res

    def ansv2(self, nums, n, target=0):
        """
        _run: TLE (311/313) (optmized)
        _code: time: o(n*nlogn), space: o(1)
        _study:
        --- formula ---
        target = 0
        a + b + c = target
        b + c = target - a
        --- constraints ---
        [+] nums should be in sorted order because to implement binary search array
        should be in sorted order to function.
        --- explanation ---
        [+] approach is typically based on the formulla described.
        """
        res = []
        nums.sort()

        for i in range(n):
            j, k = i + 1, n - 1
            needed = target - nums[i]  # b + c = target - a

            while (j < k):
                cur_sum = nums[j] + nums[k]
                if cur_sum == needed:
                    s3 = [nums[i], nums[j], nums[k]]
                    if not s3 in res:
                        res.append(s3)
                    j += 1
                elif cur_sum < needed:
                    j += 1
                elif cur_sum > needed:
                    k -= 1

        return res

    def ansv1(self, nums, n, target=0):
        """
        _run: TLE (brute-force)
        _code: time:o(n^3) + o(nlogn) ~ o(n^3), space: o(1)
        _study:
        --- constraints ---
        [+] approach can only be implemented when array is sorted only.
        --- explanation ---
        [+] Duplicacy is meant to be ignored
        [+] approach comprises of for three nested loop with i, j, k pointer and
        for the end for loop just sum of for loop instances
        [+] for eg, nums[i] + nums[j] + nums[k] == 0
        then add to result else ignore
        """
        res = []
        nums.sort()  # o(nlogn)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s3 = [nums[i], nums[j], nums[k]]
                    if sum(s3) == target and not s3 in res:
                        res.append(s3)

        return res


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
