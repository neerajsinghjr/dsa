'''
Problem Description:
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated into ascending order.
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
    # Method 1 : Dict() Solution
    def sort012_V1(self,arr):
        if arr:
            # temp = dict()                                           # Method 1
            # temp[0] = temp[1] = temp[2] = 0
            
            # temp = {0:0, 1:0, 2:0}                                  # Method 2

            temp = dict.fromkeys([1,2,3], 0)                        # Method 3

            # Step 1: Using Dict;
            for num in arr:
                if(temp[num] is None):
                    temp[num] = 1
                else:
                    temp[num] += 1
            # Step 2: Updating the List;
            arrIndex = 0                       # Array Index Default 0;
            for i in [0,1,2]:
                if(temp[i] != 0):
                    x = temp[i]
                    while(x > 0):
                        if(x > 0):
                            arr[arrIndex] = i  
                            arrIndex += 1       
                            x = x - 1           
                else:
                    break
        
        return arr if arr else []


    # Method 2 : DNF(Dutch National Flag) Solution
    def sort012_V2(self, nums):
        if nums:
            low,mid,high = 0,0,len(nums)-1
            for i in range(0,len(nums)):

                # Mid : For 1's Value
                if(nums[mid] == 0):
                    nums[low],nums[mid] = nums[mid],nums[low]           # Swapped
                    low += 1
                    mid += 1
                
                # Low : For O's Value
                elif(nums[mid] == 1):
                    mid += 1
                    
                # High : For 2's Value
                elif(nums[mid] == 2):
                    nums[mid],nums[high] = nums[high],nums[mid]         # Swapped
                    mid += 1
                    high -= 1
                
        return nums
    
    def sort012_V3(self, arr):
        t = {0:0, 1:0, 2:0}
        
        for num in arr:
            t[num] += 1
        
        idx = 0
        for key,value in t.items():
            while(value > 0):
                arr[idx] = key
                idx += 1
                value -= 1
                
        return arr


def main():
    try:
        # arr = [2,0,1,2,2,2,2,2,1,0,1,0,0,0,1,0,2,1,0,0,1,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,1,1,1,1,0,0,2,2,2,1,1,0]
        arr = [2,0,1,2,2,1,0]
        obj = Solution()
        # obj.sort012_V1(arr)     # V1
        obj.sort012_V2(arr)     # V2
        # obj.sort012_V1(arr)     # V3
        print(arr) if arr else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    