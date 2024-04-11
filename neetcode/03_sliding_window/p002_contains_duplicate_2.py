'''
-------------------------------------------------------------------------------------
-> Problem Title: 219. Contains Duplicate II
-> Problem Status: Completed
-> Problem Attempted: 2024-03-23
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/contains-duplicate-ii/description/

Reference:-
https://youtu.be/ypn0aZ0nrL4

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

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        _stdin: list[int]
        _stdout: bool
        """
        n = len(nums)
        if n == 1:
            return False
        if n == 2:
            if nums[0] == nums[1]:
                return True and 1 <= k
            return False

        # return self.ansv1(nums, k, n)
        return self.ansv2(nums, k, n)

    def ansv2(self, nums, k, n):
        """
        _run: accepted (optimal-solution)
        _code: time: o(n), space: o(n)
        _study:
        --- tricky part ---
        this question is asking you to check for duplicate in the group of k number
        and in the group of k number you've to find the those state true or false
        on the basis of below constraints...
        1) num[i] == num[j] should be equal
        2) abs(i-j) <= k
        --- explanation ---
        we iteratively use a hashmap to map the num value with its respective index
        value and then we check if we have already stored the existing number in our
        map then we are fetching the index and checking the respective constraints.
        """
        hashmap = {}
        for idx, val in enumerate(nums):
            if val not in hashmap:
                hashmap[val] = idx
            else:
                pre_idx = hashmap[val]
                if abs(idx - pre_idx) <= k:
                    return True
                hashmap[val] = idx

        return False

    def ansv1(self, nums, k, n):
        """
        _run: TLE (brute-force)
        _code: time:o(n^2), space: o(1)
        _study:
        --- explanation ---
        we are nested loop to check for respective nums[i] == nums[j] and abs(i-j) <=k
        """
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (nums[i] == nums[j] and abs(j - i) <= k):
                    return True

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
