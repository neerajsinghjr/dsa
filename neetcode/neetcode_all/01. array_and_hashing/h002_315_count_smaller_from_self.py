'''
-------------------------------------------------------------------------------------
-> Problem Title: 315. Count of Smaller Numbers After Self
-> Problem Status: Completed
-> Problem Attempted: 12/07/2025
-> Problem Description:

Problem Statement:
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

Refer Explanation: 
https://www.youtube.com/watch?v=AseUmwVNaoY&ab_channel=takeUforward

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

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        _stdin:
            arg1: list[int]
        _stdout: list[int]    
        """
        n = len(nums)
        if n == 1:
            return [0]
        # return self._ansv1(nums, n)
        return self._ansv2(nums, n)
    
    def _ansv2(self, nums, n):
        """
        _run: accepted
        _code: tc: o(nlogn), sc: o(n), rt: 1130 ms, tcz: 66/66
        _choke: None
        _brief: --- optimized with merge sort algorithm ---
        - this method calculates, for each number in the input array `nums`, the count of 
        smaller numbers that appear strictly to its right.
        - it leverages a modified Merge Sort algorithm, which is augmented to perform the 
        counting during its efficient merging phase.
            - Algorithm Breakdown:
                - An auxiliary `result` list of size `n` (initialized to zeros) is created to 
                store the final counts for each original index.
                - Each number from `nums` is paired with its original index `(og_index, value)` 
                using `enumerate` to preserve its position through sorting.
            - Recursive Sorting:
                - The `merge_sort` function recursively divides the list of `(index, value)` 
                pairs into smaller sub-arrays until they are trivially sorted.
            - Augmented Merging (Core Logic):
                - when merging two sorted sub-arrays (left and right halves):
                - if an element `(idx_L, val_L)` from the `left` sub-array is chosen (because 
                `val_L <= val_R`):
                    - Its `result[idx_L]` entry is incremented by `j`, where `j` is the count 
                    of elements already moved from the `right` sub-array. These `j` elements 
                    are guaranteed to be smaller than `val_L` and were originally located to 
                    its right.
                - If an element from the `right` sub-array is chosen (because `val_R < val_L`):-
                    - It is simply appended to the merged list, and `j` is incremented. No count 
                    is added to `result` for `val_R` at this step, as it's not being compared 
                    against elements from its original left side.
                    - After processing one of the sub-arrays, any remaining elements from the `left`
                    sub-array are appended to the merged list, and their `result` count is updated 
                    by the total number of elements successfully merged from the `right` sub-array 
                    (which is the final value of `j`).
        - Example:
            - Input: nums = [5, 2, 6, 1]
            - Initial: result = [0, 0, 0, 0]
            - Initial: enum = [(0, 5), (1, 2), (2, 6), (3, 1)]`
            - During Merge Operations
                - When `5` (original index 0) is processed, numbers `2` and `1` 
                (which were originally to its right) are found to be smaller. result[0] becomes 2
                - When `2` (original index 1) is processed, number `1` 
                (originally to its right) is found to be smaller. result[1] becomes 1
                - When `6` (original index 2) is processed, number `1` 
                (originally to its right) is found to be smaller. result[2] becomes 1
                - Number `1` (original index 3) has no elements to its right. result[3] is 0
            - Output: result = [2, 1, 1, 0]
        """
        result = [0] * n
        enum = list(enumerate(nums))  # [(index, value)]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            # --- merge sort algo --- #
            i, j, merged = 0, 0, []
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    result[left[i][0]] += j  # j elements in right are smaller than current left
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            # Remaining items in left — all right elements are smaller than them
            while i < len(left):
                result[left[i][0]] += j
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged

        merge_sort(enum)
        return result

    def _ansv1(self, nums: list[int], n: int) -> list[int]:
        """
        _run: tle
        _code: tc: o(n^2), sc: o(n), rt: nan, tcz: 49/66
        _choke: none
        _brief: --- brute-force-solution ---
        - simple counting based solution using nested loops using o(n^2)
        - we are standing on cur_idx and then iterate from cur_idx+1 and look for smaller values
        inside rest of the list; if found then append it the ans variable. 
        """
        ans = []
        for idx, num in enumerate(nums):
            count = 0
            for nex in range(idx+1,n):
                if nums[idx] > nums[nex]:
                    count += 1
            ans.append(count)
        return ans


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
