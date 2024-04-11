'''
-------------------------------------------------------------------------------------
-> Problem Title: 88. Merge Sorted Array
-> Problem Status: Completed
-> Problem Attempted: 2024-03-22
-> Problem Description:
-------------------------------------------------------------------------------------

NOTE: Problem re-attempted on 2024-03-23 with optimal approach refer ansv2()
Reference:-
https://leetcode.com/problems/merge-sorted-array/description/

Solution :-
https://youtu.be/P1Ic85RarKY

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

    def merge(self, n1: List[int], m: int, n2: List[int], n: int) -> None:
        # Do not return anything, modify nums1 in-place instead.
        if not n1 or not n2:
            return n1 or n2

        # return self.ansv1(n1, m, n2, n)
        return self.ansv2(n1, m, n2, n)

    def ansv2(self, n1, m, n2, n):
        """
        _run: accepted
        _code: time: o(n), space:o (1)
        _study:
        ___ tricky part ---
        don't try to merge or swipe from start of the sorted listS because there is no
        benefit from that (refer ansv1()), as soon as you've swipe one number from one
        sorted array to another sorted array. then the resultent array will be not sorted
        and to make the array sorted, you might have to waste nlogn cost.
        NOTE : to fix try to merge from the end of both the list. because from
        you can the upper bound number of the both the list in one go.
        --- explanation ---
        This function takes nums1, m, nums2, and n as input parameters, where nums1 is
        the array that contains enough space to hold additional elements from nums2 at
        the end. m is the number of elements initialized in nums1, and n is the number
        of elements in nums2.

        [+] The function merges nums2 into nums1 in place. It starts from the end of
        both arrays and compares elements using two pointers p1 and p2.
        [+] The larger element between nums1[p1] and nums2[p2] is placed at the end of
        nums1, and the corresponding pointer (p1 or p2) is decremented.
        [+] This process continues until one of the arrays is fully merged. Then, any
        remaining elements from nums2 are copied to the beginning of nums1.
        """

        last_index = m + n - 1  # total length of num1 with m + n

        m = m - 1  # array index for num1 (~n1)
        n = n - 1  # array index for num2 (~n2)

        print(f"last_index: {last_index}, n: {n}, m: {m}")

        while (m >= 0 and n >= 0):
            if n1[m] > n2[n]:
                n1[last_index] = n1[m]
                m = m - 1
            else:
                n1[last_index] = n2[n]
                n = n - 1
            # iterating from the end of total length of num1;;
            last_index -= 1

        print(f"n1: {n1}")

        # copy the remaining from num2 to num1;
        while (n >= 0):
            n1[last_index] = n2[n]
            last_index -= 1
            n = n - 1

        print(f"n1: {n1}")

        return

    def ansv1(self, n1, m, n2, n):
        """
        _run: accepted (brute-force)
        _code: time: o(m * nlogn), space: o(1)
        _study:
        --- constraints ---
        nums1 list length is equal to m + n
        --- explanation ---
        [+] iteratively taking the small number among the list n1 and n2 and
        storing it at the ith index inside the n1.
        [+] in every iteration you will find one value which is smaller in n1
        and n2. So smaller value should be stored in n1 and the larger value
        should be stored in n2.
        [+] make sure to again sort the n2 list when you swipe values among n1
        and n2
        """
        i, j = 0, 0
        n1_len = len(n1)
        # s1: iterative placing the small value in n1 list among n1 and n2;;
        while i < m:
            if n1[i] > n2[j]:
                n1[i], n2[j] = n2[j], n1[i]
                n2.sort()
            i += 1

        # s2: adding the leftover value to the nums1 list;;
        while (i < n1_len and j < n):
            n1[i] = n2[j]
            i, j = i + 1, j + 1

        return


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
