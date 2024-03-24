'''
-------------------------------------------------------------------------------------
-> Problem Title: 1984. Minimum Difference Between Highest and Lowest of K Scores
-> Problem Status: Completed
-> Problem Attempted: 2024-03-19
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

Reference:-
https://youtu.be/JU5XdBZZtlk

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

    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        _stdin: list[int]
        _stdout: int
        """
        if k == 1:
            return 0
        return self.ansv1(nums, k)

    def ansv1(self, nums, k):
        """
        _run: accepted
        _code: time: o(nlogn), space: o(1)
        _study:
        --- intuition ---
        [+] as per the problem, we have to find the minimum difference of
        high and low values of k group.
        [+] here we are asked to work in group or a fixed window and to
        determine the min different of high and low of a given group.
        --- approach ---
        [+] that's why approach core step is to sort the array. so that we
        can predict the order of every kth group.
        [+] and when you've applied the sorting then inside the kth group
        first index element would be lowest and similary (k-1)th index element
        would be maximum in that kth group.
        [+] after using sliding window increasing the sliding window by unit
        scale and calculate the difference of highest and lowest value.
        """
        # sorting the array will make kth group left end element
        # as minimum and right end element as maximum;;
        nums.sort()
        res = float("inf")  # positive inifinity;;
        left, right = 0, k - 1

        # iterating over the kth gap window from 0 to k-1 where
        # k is always lesser than the length of nums;;
        while (right < len(nums)):
            res = min(res, nums[right] - nums[left])
            left += 1
            right += 1

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
