'''
Problem Description:
Given an array move all the elements lesser than 4, to the left of if
and greater than 4 to the right of it and leaving equals to 4 at the
center of it 

Example 1:
Input : [3,2,4,1,6,3,7,5]
Output : [3,2,1,3,4,6,7,5]
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random



## Main Working Function, here...
def moveByPivot(nums):      # nums = [1,-2,3,-1,-33, 8,9,4,-4,10,0] 
    low,mid,high = 0,0,len(nums)-1
    while(mid <= high):
        if(nums[mid] < 4):
            nums[mid],nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif(nums[mid] > 4):
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1
        else:
            mid += 1
    return nums
    

def main():
    try:
        # data = [1,-2,3,-1,-33, 8,9,4,-4,10,0]               # ~ data
        # data = [11,-22,3,-1,-33, 8,-9,40,-4,10,0]           # ~ data
        data = [3,2,4,1,6,3,7,5]                              # ~ data
        res = moveByPivot(data)
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
    