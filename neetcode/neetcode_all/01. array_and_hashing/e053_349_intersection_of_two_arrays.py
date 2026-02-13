'''
-------------------------------------------------------------------------------------
-> Problem Title: 349. Intersection of Two Arrays
-> Problem Status: Completed
-> Problem Attempted: 10/08/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/intersection-of-two-arrays/description/

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
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        _stdin:
            arg1: list[int]
            arg2: list[int]
        _stdout: list[int]
        """
        # return self._ansv1(nums1, nums2)
        # return self._ansv2(nums1, nums2)
        return self._ansv3(nums1, nums2)

    def _ansv3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 0 ms, tcz: 57/57
        _choke: none
        _brief: --- pythonic-way ---
        - This Pythonic solution converts both input lists into sets to remove duplicates 
        and enable efficient O(1) average time complexity for lookups. 
        - It then iterates through the first set, checking for the membership of each 
        element in the second set, and appends the common elements to a result list.

        """
        res = []
        ns1, ns2 = set(nums1), set(nums2)
        for n1 in ns1:
            if n1 in ns2:
                res.append(n1)
        return res

    def _ansv2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 0 ms, tcz: 57/57
        _choke: none
        _brief: --- pythonic-way ---
        - This highly optimized Pythonic solution leverages the set intersection operator (&) 
        to find all common elements between the two input lists. 
        - The lists are first converted to sets, and the intersection operation efficiently 
        returns a new set containing only the elements present in both. 
        - The result is then cast back to a list.

        """
        return list(set(nums1) & set(nums2))
    
    def _ansv1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        _run: accepted
        _code: tc: o(n^2), sc: o(1), rt: 11 ms, tcz: 57/57
        _choke: none
        _brief: --- brute-force ---
        - This brute-force approach uses nested loops to find common elements. 
        - It iterates through each number in the first list and checks if it exists in the 
        second list. 
        - To avoid duplicates in the result, it also checks if the number is already in the 
        result list before appending it.
        """
        res = []
        for num in nums1:
            if num in nums2 and num not in res:
                res.append(num)
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
