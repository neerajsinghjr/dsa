'''
Problem Description:
Given two integer arrays arr1 and arr2, and the integer d, 
return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i],
such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example: 
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
    For arr1[0]=4 we have: 
    |4-10|=6 > d=2 
    |4-9|=5 > d=2 
    |4-1|=3 > d=2 
    |4-8|=4 > d=2 
    For arr1[1]=5 we have: 
    |5-10|=5 > d=2 
    |5-9|=4 > d=2 
    |5-1|=4 > d=2 
    |5-8|=3 > d=2
    For arr1[2]=8 we have:
    |8-10|=2 <= d=2
    |8-9|=1 <= d=2
    |8-1|=7 > d=2
    |8-8|=0 <= d=2
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time
from bisect import bisect_left


## Main Working Function, here
def findTheDistanceValue(arr1, arr2, d) -> int:
    arr2.sort()
    ret = len(arr1)
    for v in arr1:
        i = bisect_left(arr2, v)
        if i==0:
            if arr2[0]-v<=d:
                ret-=1
        elif i==len(arr2):
            if v-arr2[i-1]<=d:
                ret-=1
        else:
            if arr2[i]-v<=d or v-arr2[i-1]<=d:
                ret-=1
    return ret


def main():
    try:
        arr1 = [123,12,3123,34,34,22,45,45345,345,36,56,456,4]
        arr2 = [10,9,12,3123,121,24124,14,124,1,8]
        res = findTheDistanceValue(arr1, arr2, d=2)
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Program Stopped: {e}")
    
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