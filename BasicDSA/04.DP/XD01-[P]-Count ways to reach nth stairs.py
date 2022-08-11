'''
Problem Description:
Count ways to reach the nth stair using step 1, 2 or 3
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

Example 1
Input : 4
Output : 7
Explanation:
Below are the seven ways
    1 step + 1 step + 1 step + 1 step
    1 step + 2 step + 1 step
    2 step + 1 step + 1 step 
    1 step + 1 step + 2 step
    2 step + 2 step
    3 step + 1 step
    1 step + 3 step

Example 2
Input : 3
Output : 4
Explanation:
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step
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
    
    def waysToReachTop(self, n):                # n : totalStairs
        if(n == None or n == 0):return n
        return self.bruteForce(n)


    # Iterative Brute Force
    def bruteForceV1(self, n):
        # base case
        if n == 0:  return 0
        if n == 1:  return 1
        return self.bruteForceV1(n-1) + self.bruteForceV1(n-2) + self.bruteForceV1(n-3)


def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = ""
        print(res) if res else print("Empty!")
        
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
    