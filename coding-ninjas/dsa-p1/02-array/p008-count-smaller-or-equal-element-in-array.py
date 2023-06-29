'''
-------------------------------------------------------------------------------------
-> Problem Title: Count Smaller or Equal Elements in Array
-> Problem Status: Completed
-> Problem Attempted: 05/06/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118820/offering/1381881
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
def countSmallerOrEqual(nums1, nums2, n, m):
    """
    run: success
    time: o(nlogn) + o(nlogn) ~ o(nlogn)
    space: o(n)+o(n)+o(1) ~ o(n)
    choke: none
    study: implement using binary search, track only the first number 
    to which target element is smaller and then just increase the 
    slider in the forward direction to check any duplicate as well.
    """
    res = []
    nums2.sort()
    for num in nums1:
        count = count_element(nums2, num)
        res.append(count)
    return res
    
def count_element(nums, target):
    res = None #  Storing the count;;
    lo, hi = 0, len(nums)-1
    while(lo <= hi):
        mid = lo + (hi-lo)//2
        if target >= nums[mid]:
            res, lo = mid, mid+1
        else:
            hi = mid-1
    
    return res+1 if res != None else 0
    
def countSmallerOrEqual_v1(nums1, nums2, n, m):
    """
    run: TLE
    time: o(n*m) ~ o(n^2)
    space: o(n)
    choke: TLE
    study: brute force, counting individually smaller element from 
    A into B, then store it inside list and then return result.
    """
    res = []
    nums2.sort()
    for a1 in nums1:
        count = 0
        for a2 in nums2:
            if a1 < a2:
                break
            count += 1
        res.append(count)

    return res    


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