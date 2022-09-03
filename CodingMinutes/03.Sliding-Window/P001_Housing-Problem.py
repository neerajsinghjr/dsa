'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Housing Problem
-> Problem Status: Ongoing...
-> Problem Attempted: 03.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Along one side of the road there is a sequence of vancant plots has a difference area of non zero, 
So the areas forms a sequence A[1], A[2], A[3], A[4] ... A[N]

You want to buy K acres of land to build a house. You want to find all segments of contains of 
continguous plots (i.e, a subsection in the sequence) of whose sum is exactly equals to K


Example 1:
Input: areas = [1,2,3,4,5,6,4,2,1,3,4,5,6,7,8,9,10,11,12,3,4] and k = 12
Output: [[2, 5], [5, 8], [9, 12], [18, 19]]

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

    def findHousing(self,areas,k):
        n = len(areas)

        if(n == 1): 
            return areas

        if(k == 0):
            return areas

        # return self.ansv1(areas,k,n)
        return self.ansv2(areas,k,n)
        # return self.ansv3(areas,k,n)

    """
    Run:
    Code: Optimised Prefix Sum 
    Study:
    """
    def ansv2(self,areas,k,n):
        prefix = [0]*n
        prefix[0] = areas[0]
        # S1: Calculate Prefix Sum;
        for i in range(1,n):
            prefix[i] += areas[i] + prefix[i-1]

        print(f"prefix: {prefix}")

        # S2: Tracing K Segments Areas;
        for j in range(n):
            pass






    """
    Run: Success
    Code: Brute Force | T:(N^2) | S:O(1)
    Study:
    Simply iterating over the all the areas, and fetch all the sum over n times
    then match for the running sum with the k areas requirement.
    """
    def ansv1(self,areas,k,n):
        sum,res = 0,[]
        for i in range(n):
            sum = areas[i]
            for j in range(i+1,n):
                if(sum == k):
                    res.append([i,j])
                sum += areas[j]

        return res


##---Main Execution;;
def main():
    try:
        areas,k = [1,2,3,4,5,6,4,2,1,3,4,5,6,7,8,9,10,11,12,3,4],20
        obj = Solution()
        res = obj.findHousing(areas,k)
        if(type(res) == int):
            print(f"Result: {res}") if res else print("Empty!")
        elif(type(res) == list):
            for r in res:
                print(f"Result: {r}")
        else:
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
    