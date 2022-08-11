'''
#Problem Title: Rain Water Trapping
#Problem Attempted: 11-08-2022
#Problem Description:
Given 'N' non negative interger representing an elevation map where the width of 
each bar is 1, 
Compute how much water it can trap after raining.

for eg,

eg,
Inputs = [0,1,0,2,1,0,1,3,2,1,2,1]   (Levels of Water)
Output = 6
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
class Solution:
    
    def rainWaterTrapping(self,levels):
        n=len(levels)
 
        if n == 0:
            return 0

        if n == 2:
            return 0


        return self.ansv1(levels,n)


    def ansv1(self,levels,n):
        
        maxFromLeft = [0]*n
        maxFromRight = [0]*n

        # S1: Counting max from left of array;
        maxFromLeft[0],maxFromRight[n-1] = levels[0],levels[n-1]
        temp,maxFromLeft[0] = levels[0],levels[0]

        for i in range(1,n):
            maxFromLeft[i] = max(maxFromLeft[i-1], levels[i])
            maxFromRight[n-i-1] = max(maxFromRight[n-i], levels[n-i-1])
 
        # print(f"MaxFromLeft: {maxFromLeft}")
        # print(f"MaxFromRight: {maxFromRight}")


        # S3: Summing up the Trapped Rain Water; 
        totalWaterTrapped = 0
        for i in range(n):
            totalWaterTrapped += min(maxFromLeft[i], maxFromRight[i]) - levels[i]

        return totalWaterTrapped


def main():
    try:
        # levels = [0,1,0,2,1,0,1,3,2,1,2,1]                # ~ data;
        levels = [4,3,2,1,4,1,1,1]                # ~ data;
        obj = Solution()
        res = obj.rainWaterTrapping(levels)
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
    