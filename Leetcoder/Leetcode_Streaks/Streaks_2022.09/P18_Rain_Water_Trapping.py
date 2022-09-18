'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 42. Trapping Rain Water
-> Problem Status: Completed
-> Problem Attempted: 18.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
 
Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- Main Solution;;
class Solution:
    
    ###---Main Execution;;
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        if(n == 1):
            return 0
        
        return self.ansv1(heights,n)
    
    
    """
    Run: Accepted
    Code: Optimized | T:O(N) | S:O(N)
    Study:
    This approach defines, tracing the max level heights from left and similarly
    max level heights from the right.
    Then after calculating this result is calculated by traversing both the 
    difference of max arrays of left and right with the current heights.
    """
    def ansv1(self,heights,n):
        # MaxLevelLeft tracing max level heights from the left iteration;
        # MaxLevelRight tracing max level heights from the right iteration;
        maxLeftLevel, maxRightLevel = [0]*n, [0]*n
        
        # Default Values for MaxLeftLevel and MaxRightLevel;
        maxLeftLevel[0], maxRightLevel[n-1] = heights[0], heights[n-1]
        
        # Trace max heights from left and right by iteration;
        for i in range(1,n):
            maxLeftLevel[i] = max(maxLeftLevel[i-1], heights[i])
            maxRightLevel[n-i-1] = max(maxRightLevel[n-i], heights[n-i-1])
        
        # Total Water Trapping;
        res = 0
        for i in range(n):
            res += min(maxLeftLevel[i], maxRightLevel[i]) - heights[i]
        
        return res
            

##---Main Execution;;
def main():
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
    