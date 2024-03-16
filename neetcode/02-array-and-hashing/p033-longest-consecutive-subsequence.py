'''
-------------------------------------------------------------------------------------
-> Problem Title: 128. Longest Consecutive Sequence
-> Problem Status: Completed
-> Problem Attempted: 2024-03-12
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/longest-consecutive-sequence/description/

Reference:-
https://youtu.be/P6RZZMu_maU

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
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 1 if nums else 0
        # return self.ansv1(nums, n)
        return self.ansv2(nums, n)

    def ansv2(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- optimization ---
        to optimize the solution from o(nlogn) to o(n). we use numset where
        search happens in o(1) time.
        [+] it automatically handles our choked solution of duplicate in ansv1()
        [+] our reduces our time from o(nlogn) to o(n)
        --- explaination ---
        objective is to find the start of the sequence.
        for eg, nums = [100, 4, 200, 1, 3, 2]
        ------ 1, 2, 3, 4 --------- 100, 200 -------
        now i need to check start of the sequenc only, here in tnis example num(1)
        can be a start of sequence because it doesnt have any left value which is
        0 in the case of 1.
        """

        max_count = 1
        numset = set(nums)
        print("numset: ", numset)
        for num in nums:
            if num - 1 not in numset:
                cur_count = 1
                while (num + cur_count) in numset:
                    cur_count += 1
                max_count = max(max_count, cur_count)

        return max_count

    def ansv1(self, nums, n):
        """
        _run: accepted (brute-force)
        _code: time: o(nlogn), space: (1)
        _study:
        ---- choke ----
        keep in mind that two duplicate can be there which can easily hamper
        the result count.
        ---- approach ----
        approach is pretty simple sort the array so that the all nums appears
        in the single line, then linearly iterate over the loop and sequentially
        count the longest sequence.
        """
        max_count = 1
        cur_count = 1
        nums = sorted(nums)
        for i in range(1, n):
            if nums[i] - 1 == nums[i - 1]:
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                if not nums[i] == nums[i - 1]:
                    cur_count = 1

        return max_count


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
