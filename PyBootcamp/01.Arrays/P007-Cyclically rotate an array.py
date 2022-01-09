'''
Problem Description:
Given an array, rotate the array by one position in clock-wise direction.
 
Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4
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

    # Rotate Array One Time From End;
    def rotate(self, nums):
        if(nums):
            size = len(nums)-1
            last = nums[size]
            while(size > 0):
                nums[size] = nums[size-1]
                size -= 1
            nums[0] = last
                
        return nums

    # Rotate Array K Times From End;
    def rotateKTimes(self,nums,k):
        if(nums):
            size = len(nums)
            # Filter 'K' Rotate Calls;
            if(k > size):
                k = k % size
            while(k > 0):
                self.rotate(nums)
                k = k - 1
        return nums


def main():
    try:
        # data = [ 12, 23, 44, 50, 60, 77, 22, 12, 4, 6, 7, 2, 3, 56, 23, 2, 34, 23, 56, 34 ]
        data = [ 1, 2, 3, 4, 5 ]              
        obj = Solution()
        # obj.rotate(data)                          # O(n)
        obj.rotateKTimes(data,k=21)                  # O(k * n)  

        print(data) if data else print("Empty!")
        
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
    