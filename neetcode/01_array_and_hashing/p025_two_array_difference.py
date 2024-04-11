'''
-------------------------------------------------------------------------------------
-> Problem Title: 2215. Find the Difference of Two Arrays
-> Problem Status: Completed
-> Problem Attempted: 2024-03-08
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/find-the-difference-of-two-arrays/

Reference:-
https://youtu.be/a4wqKR-znBE

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

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # return self.ansv1(nums1, nums2)
        return self.ansv2(nums1, nums2)

    def ansv2(self, nums1, nums2):
        """
        _run: accepted
        _code: time: o(n+m), space: o(n+m)
        _choke: none
        _study: we have optimized our ansv1() solution from o(n^2) => o(n)
        by using set. Still we are iternating loop n time but searcing nth index
        value in the nums1 (~set) takes on o(1) time due to hashset.
        """
        res1, res2 = [], []
        nset1, nset2 = set(nums1), set(nums2)

        for n1 in nset1:
            if n1 not in nset2:
                res1.append(n1)

        for n2 in nset2:
            if n2 not in nset1:
                res2.append(n2)

        return [res1, res2]

    def ansv1(self, nums1, nums2):
        """
        _run: accepted (brute-force)
        _code: time: o(n^2), space: (n+m)
        _choke: none
        _study: simple apporach for checking for existence of one number in another list
        as we are using the list that means running loop n times and check if nth index value
        exist in nums1 list will take o(n x n) times and vice-versa
        also check for unique record only.
        """
        n1_list = []
        for n1 in nums1:
            if n1 not in nums2 and n1 not in n1_list:
                n1_list.append(n1)
        n2_list = []
        for n2 in nums2:
            if n2 not in nums1 and n2 not in n2_list:
                n2_list.append(n2)

        return [n1_list, n2_list]


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
