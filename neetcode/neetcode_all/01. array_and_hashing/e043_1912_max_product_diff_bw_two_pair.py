'''
-------------------------------------------------------------------------------------
-> Problem Title: 1913. Maximum Product Difference Between Two Pairs
-> Problem Status: Completed
-> Problem Attempted: 07/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import collections


##---Main Solution
class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        # return self._ansv1(nums)
        # return self._ansv2(nums)
        # return self._ansv3(nums)
        return self._ansv4(nums)
    
    def _ansv4(self, nums: List[int]) -> int:
        """
        _run: accepted (BEST!!!)
        _code: tc: o(n), sc: o(1), rt: 141 ms, tcz: 96/96
        _choke: --- optimized version for ansv1() and fix for ansv3() ---
        _brief:
        - this solution efficiently calculates the maximum product difference between two 
        pairs of numbers in the array.
        - the core strategy is to identify the two largest values (mx1, mx2) and the two 
        smallest values (mn1, mn2) from the input array.
        - it achieves this by performing a single, linear pass through the 'nums' array.
        - during this pass, each number is independently evaluated to update the current 
        largest/second largest and smallest/second smallest variables.
        - this methodology ensures an optimal time complexity of O(N) and constant space 
        complexity of O(1).
        """
        n = len(nums)
        mx1, mx2 = -1, -1   # you can use -math.inf for negative infinity
        mn1, mn2 = 10**4+1, 10**4+1 # similarly math.inf for positive infinity
        
        for i in range(n):
            # if_block_1 will handle max1 and max2;
            if nums[i] > mx1:
                mx2 = mx1
                mx1 = nums[i]
            elif nums[i] > mx2:
                mx2 = nums[i]
            
            # if_block_2 will handle min1 and min2;
            if nums[i] < mn1:
                mn2 = mn1
                mn1 = nums[i]
            elif nums[i] < mn2:
                mn2 = nums[i]

        return (mx1*mx2)-(mn2*mn1)

    def _ansv3(self, nums: List[int]) -> int:
        """
        _run: rejected (brute-force)
        _code: tc: o(n), sc: o(1), rt: nan, tcz: 96/96
        _choke:
        - Logical Flaw in Conditional Structure: 
            - The primary oversight is the use of a single `if-elif` chain to update all 
            four variables (two maximums and two minimums).
        - Dependent Updates:
            - This structure causes a number to only be considered for *one* of the four 
            variables (`a`, `b`, `c`, or `d`) in a given iteration if it matches an earlier 
            `if`/`elif` condition.
        - Inaccurate Extremes: 
            - Consequently, numbers are not independently evaluated for both their potential 
            as one of the two largest and one of the two smallest, leading to `a, b, c, d` 
            often holding incorrect values for the true four extremes.
        - Rejection Reason: 
            - The method's rejection is due to this logical bug, as it fails to correctly 
            identify the required four numbers for all test cases, despite aiming for O(N) 
            time complexity.
        _brief:
        - This approach attempts to solve the problem of finding the maximum product difference
        by identifying the two largest and two smallest numbers in a single pass.
        - It initializes four variables to track the largest (`a`), second largest (`b`), 
        smallest (`c`), and second smallest (`d`) values encountered.
        - The goal is to calculate the product difference (a*b - c*d) after iterating through 
        all elements.
        """
        n = len(nums)
        a,b = -1, -1
        c,d = 10**4+1, 10**4+1
        for i in range(n):
            if nums[i] > a:
                a = nums[i]
            elif nums[i] < a and nums[i] > b:
                b = nums[i]
            elif nums[i] < c:
                c = nums[i]
            elif nums[i] < d and nums[i] > c:
                d = nums[i] 
        return (a*b)-(c*d)

    def _ansv2(self, nums: List[int]) -> int:
        """
        _run: accepted (brute-force)
        _code: tc: o(nlogn), sc: o(1), rt: 157 ms, tcz: 96/96
        _choke: none
        _brief:
        - problem says to look for 4 individual value whose differential pair product is larger
        - we find 2 max nums and 2 min number easily by sorting the nums list;
        - pull 2 num from start would be min and similarly pull 2 from last would be max nums
        - thats it, using formula ... (a*b) - (c*d)
        """
        n = len(nums)
        nums_lst = sorted(nums)
        max_prd = nums_lst[n-1] * nums_lst[n-2]
        min_prd = nums_lst[1] * nums_lst[0]
        return max_prd - min_prd

    def _ansv1(self, nums: List[int]) -> int:
        """
        _run: accepted (brute-force)
        _code: tc: o(n+k+m), sc: o(1), rt: 141 ms, tcz: 96/96
        _choke: none
        _brief:
        - problem says to look for 4 individual value whose differential pair product is larger
        - alternatively you can see problem from a different perspective; pick top two max nums
        from the nums lista and two small nums and return different pair product; thats it
        - pull out 2 max number from the nums list
        - similary, pick 2 minimum number from the nums list
        - thats it, using formula ... (a*b) - (c*d)
        """
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        nums.remove(b)
        c = min(nums)
        nums.remove(c)
        d = min(nums) # assuming d would be sligtly bigger than value $c
        return (a*b) - (d*c)


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
