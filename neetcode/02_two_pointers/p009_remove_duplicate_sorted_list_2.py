'''
-------------------------------------------------------------------------------------
-> Problem Title: 80. Remove Duplicates from Sorted Array II
-> Problem Status: Completed
-> Problem Attempted: 2024-04-14
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

Reference:-
https://youtu.be/ycAq8iqh0TI

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

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        n = len(nums)
        if n <= 2:
            if n == 1:
                return 1
            return 2

        return self.ansv1(nums, n)

    def ansv1(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- explanation ---
        [+] simple explanation to approach is that we are using the two pointer $left and $right.
        $right pointer will traverse normally but $left pointer will trace unique record with
        max 2 occurrence's count.
        [+] loop_1 : we are using a nested while_loop that will use $right pointer to traverse
        the list in a sequentially manner to trace the count of duplicate numbers. after counting
        the occcurrence of duplicate number, we have to consider the min(2, duplicate_number_count)
        [+] loop_2 : we are using another for_loop that will use the $left pointer to fill up the
        occurrence of ith number inside the $nums using min(2, duplicate_number_count)
        [+] finally return the $left pointer
        """
        l, r = 0, 0

        while r < n:
            count = 1

            # l1: check duplicate from the next index;;
            while r + 1 < n and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            # l2: replacing the ith index with value 2 time;;
            for _ in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            # increament r for the next iteration;;
            r += 1

        return l


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
