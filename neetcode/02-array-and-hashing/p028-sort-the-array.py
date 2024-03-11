'''
-------------------------------------------------------------------------------------
-> Problem Title: 912. Sort an Array
-> Problem Status: Completed
-> Problem Attempted: 2024-03-10
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/sort-an-array/description/

Reference:-
https://youtu.be/MsYZSinhuFo

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

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        _stdin: list[int]
        _stdout: list[int]
        """
        if len(nums) == 1:
            return nums

        return self.ansv1(nums)

    def ansv1(self, nums):
        """
        _run: accepted
        _choke: time: o(n), space: o(n)
        _code: remember to take extra case for the mid and index values.
        _study: --- merge sort algorithm ----
        steps to be taken
        s1: first we recursively divide the array using mid index till the time length of
        nums becomes equals to 1
        s2: when the length of nums equals to 1, then we start merging the array from bottom
        to top.
        s3: process of merging is also straight forward
            1) initialize temp array and i,j indices with 0,0 value
            2) start iterating the left and right array with i < len(left) and j < len(right)
            and append the small values inside the temp array.
            3) loop will run till the one of index among ith and jth reaches its respective
            left or right nums length
            4) at the end simple merge the leftover values among the left or right array to
            the temp nums list.
            5) return the temp list
        s4: at s3 return temp list will be used the recursive call for further merging.

        for eg,
        nums [3, 2, 1]
        ---- Level 1: finding mid using merge_sort() ----
        mid = len(nums)//2 ~ 3//2 ~ 1
        left_list, right_list = [3], [2,1]
        ----- Level 1: for left_list ----
        left_list = [3] # will be returned because size of left_list == 1
        ----- Level 1: for right_list ----
        right_list = [2,1] # will go on ahead of futher mid dividation;;
            ---- Level 2: finding mid using merge_sort() ----
            left_list = [2]
            right_list = [1]
            ---- Level 2: at this time both call will return its 0th index vlaue
            left_list = [2]
            right_list = [1]
            ---- Level 2: now the merge function will be called ----
            merge function will merge left_list and right_list
            merge() ~ [1,2]
            ---- Level 2: now the Level 2 execution is completed ----
            final sorted array [1,2] will be given back to the Level 1 recursive
            call to the right_list.
            so now right_list holds the sorted array [1, 2]
        ---- Level 1: Call comes back to Level 1 from Level 2----
        left_list = [3]
        right_list = [1, 2]
        ---- Level 1: now merge function will be called again ----
        merge() function will now merge the again the new left_list and right_list.
        merge() ~ [1,2,3]
        ---- Level 1 : no more nums recursive call found ----
        final response is returned with sorted list
        final [1, 2, 3]

        NOTE: That's unsorted array from top to teardown to bottom till its reach length == 1
        and then sorting and merginhg begins from bottom to top again.
        """
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        else:
            # S1: Finding mid of the array;;
            mid = n // 2
            # S2: Dividing the left array;;
            left = self.merge_sort(nums[:mid])
            # S3: Dividing the right array;;
            right = self.merge_sort(nums[mid:])
            # final merge the merge array;;
            return self._merge(left, right)

    def _merge(self, left, right):
        # run time: 1100ms
        temp = []
        i, j = 0, 0
        # merge as per the number weightage;;
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
        # merging leftover among left and right;;
        temp += left[i:] if left[i:] else right[j:]

        return temp


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
