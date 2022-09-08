'''
----------------------------------------------------------------------------------------------------
-> Problem Title: First negative integer in every window of size k
-> Problem Status: Ongoing...
-> Problem Attempted: 
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given an array A[] of size N and a positive integer K, find the first negative integer for each and 
every window(contiguous subarray) of size K.

 

Example 1:

Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
 
Example 2:
Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0 
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function 
printFirstNegativeInteger() which takes the array A[], its size N and an integer K as i
nputs and returns the first negative number in every window of size K starting from the
first till the end. If a window does not contain a negative integer , then return 0 for
that window.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)

Constraints:
1 <= N <= 105
-105 <= A[i] <= 105
1 <= K <= N

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
def printFirstNegativeInteger(nums,k):
    n = len(nums)

    if(n == 1):
        if(nums[0] < 0):
            return nums[0]
        return 0
    
    i,j = 0,0
    res,data = [],[]
    
    while(i < n):
        print(f"num[i]: {nums[i]}")
        if(i-j+1) < k:
            # P1: find the initial window;    
            if(nums[i] < 0): 
                data.append(nums[i])
            print(f"if:z:num[i:j] -> {i}/{i-j+1}/{data}")
            i += 1
        elif((i-j)+1) == k:
            # P2: Calculate the initial result;
            print(f"el:z:num[i:j] -> {i}/{i-j+1}/{data}")
            if(len(data) == 0): 
                res.append(0)                    # print data;
            else:   
                res.append(data[0])              # print data;
                data.remove(data[0])        # remove data;
                
            # P3: Shift the window from left and right;
            i,j = i+1,j+1
    
    return res


##---Main Execution;;
def main():
    try:
        res = []

        data = [
            ([-8, 2, 3, -6, 10], 2),
            # ([12, -1, -7, 8, -15, 30, 16, 28], 3)
        ]

        for d in data:
            res.append(printFirstNegativeInteger(*d))

        for r in res:
            print(f"res: {r}")
        
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
    