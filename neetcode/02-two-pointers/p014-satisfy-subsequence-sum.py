'''
-------------------------------------------------------------------------------------
-> Problem Title: 1498. Number of Subsequences That Satisfy the Given Sum Condition
-> Problem Status: Completed
-> Problem Attempted: 2024-04-07
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

Reference:-
https://youtu.be/xCsIkPLS4Ls

External Reference:-
Refer read under neetcode directory for subsequence understanding

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
MOD = 10 ** 9 + 7


class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        _stdin:
            arg1: list[int]
            arg2: int
        _stdout: int
        """
        return self.ansv1(nums, target)

    def ansv1(self, nums, target):
        """
        _run: accepted
        _code: time: o(nlogn), space: o(1)
        _study:
        --- choke ---
        [+] you've to MOD not only your iterative results but also the final result.
        --- external references ---
        [+] `2**(right-left)` for this refer your github file, readme: dsa/neetcode repo
        --- explanation ---
        [+] logic to check index of the state where sum of (left and right) index > target
        because as we have already sorted the entire array that means we can automcally
        assume that values before the right index when loop breaks satify below condition
        nums[left] + nums[right] <= target
        [+] `2**(right-left)`: Let's say you have a string "abc". If left = 0 and right = 2,
        then you have substrings "a", "ab", "abc", "b", "bc", and "c".
        The count of substrings is `2^(2-0)=4`, which includes all combinations of including
        or excluding characters between the left and right pointers.
        [+] MOD constraints is defined in the problem only
        """
        res = 0
        nums.sort()  # nlogn to make sequence in the nums;;

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                res += (2 ** (right - left)) % MOD  # store the result;;
                left = left + 1
            else:
                right = right - 1

        return res % MOD


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
