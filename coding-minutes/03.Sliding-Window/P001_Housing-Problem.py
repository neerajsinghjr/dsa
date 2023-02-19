'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Housing Problem
-> Problem Status: Completed
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

        res1 = self.ansv1(areas,k,n)
        res2 = self.ansv2(areas,k,n)
        res3 = self.ansv3(areas,k,n)

        return (res1,res2,res3)


    """
    Run: Success
    Code: Sliding Window (Optimised) | T:O(N) | S:O(1)
    Study:
    Sliding Window protocol works well on those problem which require a fixed length of items.
    Just like this problem, a fixed window is maintained between the start => cur pointer index.
    and then the gross sum is maintained between these pointer $start => $cur, then Sliding Window 
    is updated on the basis of gross sum lesser than required k.
    """
    def ansv3(self,areas,k,n):
        res = []
        gross = 0
        start,cur = 0,0

        while(cur < n and start < cur):
            if(gross == k):
                res.append([start,cur])
                print(f"v3:start:cur => {areas[start]}:{areas[cur]}")
                gross += areas[cur]
                cur += 1
            elif(gross > k):
                gross -= areas[start]
                start += 1
            else:
                gross += areas[cur]
                cur += 1

        return res 


    """
    Run: Failed
    Code: Prefix Sum (Optimised) | T:O(N) | S:(1)
    Study:
    
    """
    def ansv2(self,areas,k,n):
        res = []
        prefix = [0]*n
        prefix[0] = areas[0]

        # S1: Calculate Prefix Sum;
        for i in range(1,n):
            prefix[i] += areas[i] + prefix[i-1]

        # S2: Tracing K Segments Areas;
        start,cur = 0,1

        if(prefix[0] == k): 
            res.append([0,0])
        print(f"{areas}")
        print(f"{prefix}")

        while(cur < n):
            cursum = prefix[cur]-prefix[start]
            if(cursum == k):
                res.append([start,cur])
                # print(f"v2:areas:start:cur => {areas[start]}:{areas[cur]}")
                # print(f"v2:prefix:start:cur => {prefix[start]}:{prefix[cur]}")
                cur += 1
            elif(cursum > k):
                start += 1
            else:
                cur += 1

        return res             


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
            if(sum == k):
                res.append([i,i])

            for j in range(i+1,n):
                sum += areas[j]
                if(sum == k):
                    res.append([i,j])
                    print(f"v1:start:cur => {areas[i]}:{areas[j]}")

        return res


##---Main Execution;;
def main():
    # try:
    areas,k = [4,5,6,4,2,1,3,4,5,6,7,8,9,10,11,12,3,4],8
    print(f"areas: {areas} and K:{k}")
    obj = Solution()
    res = obj.findHousing(areas,k)

    if(type(res) == int):
        print(f"Res: {res}") if res else print("Empty!")

    elif(type(res) == list or type(res) == tuple):
        for k,r in enumerate(res):
            print(f"Res{k+1}: {r}")

    else:
        print(f"Res: {res}") if res else print("Empty!")

        
    # except(Exception) as e:
    #     print(f"Exception Traced : {e}")
    
    # else:
    #     print("Program Completed : Success")

    # finally:    
    #     print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    