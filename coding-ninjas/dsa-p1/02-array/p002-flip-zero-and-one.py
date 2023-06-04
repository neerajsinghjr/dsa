'''
-------------------------------------------------------------------------------------
-> Problem Title: Flip Bits Zero and One.
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
def flipBits(arr, n): 
    """
    run: success
    time: o(n)
    space: o(1)
    choke: none
    study: simple approach, just count the max contiguous 
    count of zero then add total ones in list.
    """
    cur_zero = 0
    max_zero = 0
    max_one = 0
    for a in arr:
        if a == 0:
            cur_zero += 1
        else:
            cur_zero -= 1
            max_one += 1
        if cur_zero < 0:
            cur_zero = 0
        max_zero = max(max_zero, cur_zero)
        
    return max_zero + max_one


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