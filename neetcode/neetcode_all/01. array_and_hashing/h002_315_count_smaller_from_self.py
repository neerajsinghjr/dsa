'''

-------------------------------------------------------------------------------------
-> Problem Title: 84. Largest Rectangle in Histogram
-> Problem Status: Completed
-> Problem Attempted: 15/06/2025
-> Problem Description:

Problem Statement:
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

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

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        _stdin:
            args: list[int]
        _stdout: int
        """
        n = len(heights)
        if n == 1:
            return heights[0]
        # return self._ansv1(heights, n)
        return self._ansv2(heights, n)
    
    def _ansv2(self, heights: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 141 ms, tcz: 99/99
        _choke: none
        _brief: --- monotonic increasing stack optimization ---
        - we use a monotonic increasing stack to keep track of bar indices.
        - whenever the current bar is smaller than the top of the stack, we pop the stack 
        and calculate the area for the popped height.
        - we keep track of the maximum area seen so far.
        - a 0 is appended at the end to ensure all bars are processed.
        """
        stack = []  # Stack will store indices
        max_area = 0
        heights.append(0)  # Sentinel to flush out remaining bars

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area


    def _ansv1(self, heights: list[int], n: int) -> int:
        """
        _run: tle (brute-force)
        _code: tc: o(n^2), sc: o(1), rt: nan, tcz: 87/99
        _choke: none
        _brief:
        - here we are using 2 for_loops making the solution go o(n^2) straight.
        - for_loop_1: iterate from 0th index to nth index and for each iteration.
            - we iterate from cur_idx to left and check if there is any bar which is greater
            than the current bar; then we increase the $lt_ht 
            - similarly we do from cur_idx to right and check if there is any abar which is 
            greater than the current bar; then we increase the $rt_ht
            - we capture ans from max(ans, lt_ht+rt_ht+heights[cur_idx])
        """
        ans = float("-inf")
        for idx in range(n):
            # lt_idx and rt_idx pointer to iterate left and right from the current index;;
            lt_idx, rt_idx = idx-1, idx+1

            # lt_ht and rt_ht will hold left and right heights when we traverse left and right;;
            lt_ht, rt_ht = 0, 0
            
            # left iterating loop will check if there is any bar on left side which is greater 
            # than the exiting bar; if yes then include it else break the while loop;;
            while lt_idx >= 0 and heights[lt_idx] >= heights[idx]:
                lt_ht += heights[idx]
                lt_idx -= 1

            # right iterating bar will check if there is any bar on right side which is greater 
            # than the existing bar; if yes then include it else break the while loop;;
            while rt_idx < n and heights[idx] <= heights[rt_idx]:
                rt_ht += heights[idx]
                rt_idx += 1

            ans = max(ans, lt_ht+rt_ht+heights[idx])

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
