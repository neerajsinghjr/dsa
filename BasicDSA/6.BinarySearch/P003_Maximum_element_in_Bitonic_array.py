"""
Problem Description:
return max element in bitonic element in array
"""

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
def maxBitonicArray(arr,n):
    low,high = 0,n-1
    while(low<=high):
        mid = low+(high-low)//2
        if(mid == 0 or arr[mid-1] < arr[mid]) and (mid == n-1 or arr[mid] > arr[mid+1]):
            return arr[mid]
        else:
            if(mid > 0 and arr[mid-1] >= arr[mid]):
                high = mid-1
            else:
                low = mid+1

    return 0    


def main():
    try:
        data = [1,2,3,4,5,6,9,10,11,4,3,2,1,0]               # ~ data
        res = maxBitonicArray(data,len(data))
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
    