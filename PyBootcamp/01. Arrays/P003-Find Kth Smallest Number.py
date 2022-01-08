'''
Problem Description: Find Kth Smallest Number
Given an array arr[] and an integer K where K is smaller than size of array, 
the task is to find the Kth smallest element in the given array. It is given 
that all array elements are distinct.

Example 1:

Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
'''
arr : given array
l : starting index of the array i.e 0
r : ending index of the array i.e size-1
k : find kth smallest element and return using this function
'''
class Solution:
    def kthSmallest(self,arr,k):     
        if arr:
            arr = sorted(arr)           # nlog(n)
            return arr[k-1]
        return 0

def main():
    try:
        data = [12,14,1589,234,34534,23225,6,456,467432,3424,534,5,3453,535,3]               # ~ data
        obj = Solution()
        res = obj.kthSmallest(data,k=9)               # ~ func
        # res = obj.kthSmallestV2(data,l=0,r=len(data),k=9)               # ~ func
        print(res) if res else print("Empty!")
        
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
    