'''
-------------------------------------------------------------------------------------
-> Problem Title: 18. 4Sum
-> Problem Status: Completed
-> Problem Attempted: 2024-04-05
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/4sum/description/

Reference:-
https://youtu.be/EYeR-_1NRlQ

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

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        _stdin:
            arg1: list[int],
            arg2: int
        _stdout: list[int]
        """
        n = len(nums)

        if n <= 4:
            if n <= 3:
                return []
            return [nums] if sum(nums) == target else []

        # return self.ansv1(nums, n, target)
        return self.ansv2(nums, n, target)


    def ansv2(self, nums, n, target):
        """
        _run: (optimal)
        _code: time: o(n*n*logn), space: o(1)
        _study:
        --- choke ---
        [+] iterated over 2 x for loop
        [+] inner nested loop we are using the two pointer search
        """
        res = []
        nums.sort()

        for i in range(n):
            # s1: checkpoint for duplicate orders;;
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                # s2: checkpoint for duplicate order;;
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k, l = j + 1, n - 1
                base_sum = nums[i] + nums[j]

                # s3: two pointer approach from here;;
                while (k < l):
                    cur_sum = base_sum + nums[k] + nums[l]
                    if cur_sum < target:
                        k += 1
                    elif cur_sum > target:
                        l -= 1
                    else:
                        s4 = [nums[i], nums[j], nums[k], nums[l]]
                        res.append(s4)

                        k += 1

                        # s4: remove the duplicate value from left pointer;;
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1

                        # s5: remove the duplicate values from right pointer;;
                        while nums[l] == nums[l - 1] and k < l:
                            l -= 1

        return res


    def ansv1(self, nums, n, target):
        """
        _run: TLE (brute-force)
        _code: time: o(n^4), space: o(1)
        _study:
        --- explanation ---
        [+] iterate over the 4 x for loop and check for sum at every nested loop
        iteration.
        [+] if sum equals to target then append to the result.
        """
        res = []
        nums.sort()  # o(nlogn)

        for i in range(n):
            # s1: check for duplicate elements inside list;;
            if i > 0 and nums[i] != nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # s2: check for duplicate elements inside list;;
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, n):
                    # s3: check for duplicate elements inside list;;
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    base_sum = nums[i] + nums[j] + nums[k]
                    for l in range(k + 1, n):
                        cur_sum = base_sum + nums[l]
                        s4 = [nums[i], nums[j], nums[k], nums[l]]
                        if cur_sum == target and not s4 in res:
                            res.append(s4)

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
