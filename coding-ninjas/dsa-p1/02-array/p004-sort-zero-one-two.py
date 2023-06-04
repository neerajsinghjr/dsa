'''
-------------------------------------------------------------------------------------
-> Problem Title: Flip Bits Zero and One.
-> Problem Status: Completed
-> Problem Attempted: 02/02/2023
-> Problem Description:
-> Problem Link: https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381875?leftPanelTab=1
-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


def sort012(arr, n):
    """
    run: success
    time: o(n)
    space: o(1)
    choke: none
    study: solved with DNF approach
    """
    low, mid, high = 0, 0, len(arr)-1
    while(mid <= high):
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


def sort012_v1(arr, n) :
    """
    run: succes
    time: o(n)
    space: o(n)
    choke: none
    study: At first simple mapping count of 0,1,2.
    Placing every 0,1,2 inside given reference array.
    """
    nums = {0:0, 1:0, 2:0}
    for a in arr:
        nums[a] += 1
    arr.clear()
    for i in [0,1,2]:
        arr += [i]*nums[i]
    
    
##---Main Execution;;
def main(res=None):
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