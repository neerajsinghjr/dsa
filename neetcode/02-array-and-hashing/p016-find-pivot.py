'''
-------------------------------------------------------------------------------------
-> Problem Title: 727. Find Pivot Index
-> Problem Status: Completed
-> Problem Attempted: 2024-03-04
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/find-pivot-index/description/

Reference:-
https://youtu.be/u89i60lYx8U

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

    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        # return self.ansv1(nums, n)
        # return self.ansv2(nums, n)
        return self.ansv3(nums, n)

    def ansv3(self, nums, n):
        """
        run: accepted (optimized)
        time: o(n)
        space: o(1)
        choke: none
        brief:
        a) Calculate Total Sum:
            - iterate over the list and calculate total_sum of list.
        b) Iterate to Find Pivot Index:
            - Initialize a variable left_sum to 0. This variable will keep track
            of the sum of elements to the left of the current index.
            - Iterate through the array.
            - For each index i, check if left_sum is equal to total_sum - left_sum - nums[i].
            - If true, return i as the pivot index or else update left_sum by adding nums[i].
        c) No Pivot Found:
            - If the loop completes and no pivot index is found, return -1.
        """
        left_sum = 0
        right_sum = 0
        all_sum = sum(nums)
        for i in range(n):
            right_sum = all_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

    def ansv2(self, nums, n):
        """
        run: accepted (brute-force with 6677ms runtime as per LC)
        time: o(n^2)
        space: o(1)
        choke: cur_sum must be calculate after checking with right_sum.
        brief:
        - Adjusted the loop range to iterate through the entire array (range(n)).
        - Changed the condition to check if cur_sum is equal to the sum of elements
        to the right of the current index (sum(nums[i+1:])).
        - Updated the return statement to return the current index (i) as the pivot index.
        """
        cur_sum = 0
        for i in range(n):
            print(f"ith: {i}, cur_sum: {cur_sum}, sum: {sum(nums[i + 2:])}")
            if cur_sum == sum(nums[i + 1:]):
                return i
            cur_sum += nums[i]

        return -1

    def ansv1(self, nums, n):
        """
        run: rejected (tried on my own, Some Test Case Failed)
        time: o(n)
        space: o(1)
        choke: may be a lot.
        brief: applied two pointer sum approach.
        maintaing two slider left_sum and right on each time one pointer among
        left or right shifted towards each other in the chance of reducing the
        differential sum of gap.
        ---- chatgpt fixes ----
        (a) Increment Both Pointers when Sums are Equal:
            - In the original version, the function was only incrementing one pointer
            (left or right) when the sums were equal. However, in the case of finding
            the pivot index, both pointers should be moved to maintain the search space.
            - When the sums are equal, it means you have found a potential pivot, so
            it's necessary to move both pointers to explore more possibilities.
        (b)  Return Either left or right:
            - In the case where left_sum equals right_sum and left is equal to right,
            it indicates that you have found the pivot.
            - The choice of returning either left or right depends on your preference,
            as both pointers are pointing to the same index in this scenario.
        """
        left, right = 0, n - 1
        left_sum, right_sum = 0, 0
        while (left < right):
            if left_sum < right_sum:
                left_sum += nums[left]
                left += 1
                print(f"left: {left}, left_sum: {left_sum}")
            elif right_sum < left_sum:
                right_sum += nums[right]
                right -= 1
                print(f"right: {right}, right_sum: {right_sum}")
            else:
                # Increment both pointers if sums are equal
                left_sum += nums[left]
                right_sum += nums[right]
                left += 1
                right -= 1

        if left_sum == right_sum and left == right:
            print(f"left: {left}, left_sum: {left_sum}")
            print(f"right: {right}, right_sum: {right_sum}")
            return left_sum

        return -1


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
