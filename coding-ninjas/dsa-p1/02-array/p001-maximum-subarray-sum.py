'''
-------------------------------------------------------------------------------------
-> Problem Title: Maximum Subarray Sum
-> Problem Status: Completed
-> Problem Attempted: 02/02/2023
-> Problem Description:
-> Problem Link: https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381870?leftPanelTab=0
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
def maxSubarraySum(arr, n) :
    """
    time: o(n)
    space: o(n)
    run: success
    explanantion: simple kadane's algorithms
    choke: Remember to check sum < 0. In both cases
    cur_sum and max_sum, not only in the case of
    cur_sum 
    """
    max_sum = max(arr)
    if n == 0 or max_sum < 0:
        return 0
    if n == 1:
        return 0 if max_sum < 0 else max_sum
    cur_sum = 0
    for a in arr:
        if cur_sum < 0:
            cur_sum = 0
        if max_sum < 0:
            max_sum = 0
        cur_sum += a
        max_sum = max(max_sum, cur_sum)

    return max_sum


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