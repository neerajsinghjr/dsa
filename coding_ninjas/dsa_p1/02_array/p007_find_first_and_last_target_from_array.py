'''
-------------------------------------------------------------------------------------
-> Problem Title: Find First & Last Position Of Element in Sorted Array.
-> Problem Status: Completed
-> Problem Attempted: 05/06/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118820/offering/1381880

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
def searchRange(arr: [int], x: int) -> [int]:
    n = len(arr)-1
    first_idx = binary_search(arr, 0, n-1)
    firs
        
def binary_search(arr, lo, hi):
    while


def searchRange_v2(arr: [int], x: int) -> [int]:
    """
    run: success
    time: o(n)
    space: o(k)
    choke: none
    study: simple storing the index of all target from the list, 
    then return first and last index from stored area.
    """
    n = len(arr)
    ans = [ i for i in range(n) if arr[i] == x]
    if not ans:
        return -1,-1

    return ans[0], ans[-1]


def searchRange_v1(arr: [int], x: int) -> [int]:
    """
    run: success
    time: o(n)
    space: o(1)
    choke: none
    study: first value index from the left to right search,
    and for second value index it is vice-versa.
    """
    n = len(arr)-1
    first_idx, second_idx = -1, -1
    if x in arr:
        first_idx = arr.index(x)
    if x in arr:
        second_idx = arr[::-1].index(x)
        second_idx = n-second_idx
    return first_idx, second_idx
    


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