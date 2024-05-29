'''
-------------------------------------------------------------------------------------
-> Problem Title: 268. Missing Number
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/missing-number/description/

Reference:-
https://youtu.be/WnPLSRLSANE?si=0I1deap5xE_wqesg

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

    def missingNumber(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: nums: __int__
        _stdout: __int__
        """
        # return self.ansv1(nums)
        return self.ansv2(nums)
        # return self.ansv3(nums)

    def ansv3(self, nums):
        """
        _run: accepted
        _code: ts: o(n), sc: o(1)
        _study:
        --- explanation ---
        [+] we do two sum calculation in which one is the expected_sum which is running
        sum from 0 to n.
        [+] and another one is current_sum which is sum of our existing nums.
        [+] at the end we just subtract the expected_sum - cur_sum.
        """
        expected_sum = sum([
            i for i in range(len(nums) + 1)
        ])
        cur_sum = sum(nums)

        return expected_sum - cur_sum

    def ansv2(self, nums):
        """
        _run: accepted
        _code:
        _study:
        --- explanation ---
        [+] this is nother but the sum of nth natural numbers only which is our whole
        sum from 0 => n and our current sum which is sum(nums)
        [+] formula based approach
        sum_of_nth_number = n * (n + 1) // 2
        current_sum = sum(nums)
        """
        n = len(nums)
        sum_of_nth_number = n * (n + 1) // 2
        current_sum = sum(nums)

        return sum_of_nth_number - current_sum

    def ansv1(self, nums):
        """
        _run: accepted (brute-force)
        _code: ts: o(nlogn), sc: o(n)
        _study:
        --- explanation ---
        [+] problem statement is saying missing number can be found in between 0 => n
        [+] we sorted out the array now we can go ahead with sequential search by
        checking the nums with the idx of the variable.
        """
        nums.sort()

        for idx, num in enumerate(nums):
            if idx != num:
                return idx

        return nums[-1] + 1


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
