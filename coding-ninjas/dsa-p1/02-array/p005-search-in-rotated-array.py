'''
-------------------------------------------------------------------------------------
-> Problem Title: Search in Rotated Sorted Array
-> Problem Status: Completed
-> Problem Attempted: 05/05/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118820/offering/1381878

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
def search(arr, target):
    """
    run: ...
    time: o(logn)
    space: o(1)
    choke: none
    study: simply you need to find the sorted subarray in both
    left and right side. then check value in the required side.
    """
    lo, hi = 0, len(arr)-1
    while(lo <= hi):
        mid = lo + (hi-lo)//2
        if arr[mid] == target:
            return mid
        elif arr[lo] <= arr[mid]:
            # Left Side is sorted;;
            if target >= arr[lo] and target <= arr[mid]:
                hi = mid-1
            else:
                lo = mid+1
        else:
            # Right Side is sorted;;
            if target >= arr[mid] and target <= arr[hi]:
                lo = mid+1
            else:
                hi = mid-1

    return -1


def search_v3(arr, target):
    """
    run: failure
    time: o(logn)
    space: o(1)
    choke: not working properly.
    study: binary search algorithms
    """
    lo, hi = 0, len(arr)-1
    while(lo <= hi):
        mid = lo + (hi-lo)//2
        if arr[mid] == target:
            return mid
        else:
            if arr[lo] > target and arr[mid] > arr[mid-1]:
                print("shift to right side : ", mid,'->',mid+1)
                lo = mid+1
            else:
                print("shift to left side : ", mid,'->',mid-1)
                hi = mid

    return -1


def search_v2(arr, target):
    """
    run: TLE:
    time: o(n)
    space: o(1)
    choke: TLE
    study: used simple linear search algorithms
    """
    for i, a in enumerate(arr):
        if target == a:
            return i
    return -1


def search_v1(arr, target):
    """
    run: TLE
    time: o(n)+ o(logn) ~ o(n)
    space: o(n)+o(n)+o(1) ~ o(n)
    choke: TLE
    study: tried to fix the rotated array like it was before
    and then use binary search on new sorted array.
    """
    new_arr = arr
    n, idx = len(arr), None
    if n == 1:
        return 0 if arr[0] == target else -1
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            idx = i
            break
    if idx:
        new_arr = arr[idx:n] + arr[0:idx]
    
    return get_target_index(arr, new_arr, target, n) 


def get_target_index(arr, new_arr, target, n):
    low, high = 0, n-1
    mid = (low + high)//2
    flag = False
    while(low <= high):
        mid = (low+high)//2
        if new_arr[mid] == target:
            flag = True
            break
        elif target < new_arr[mid]:
            high = mid-1
        elif target > new_arr[mid]:
            low = mid+1
    
    if flag: 
        return arr.index(new_arr[mid])
    else:
        return -1


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