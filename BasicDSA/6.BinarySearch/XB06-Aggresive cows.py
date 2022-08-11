'''
Problem Description:
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random



def aggressiveCows(stalls,k):
    n=len(stalls)

    if(n == 1 and k == 1):
        return 1

    if(n < k):
        return -1

    stalls.sort()
    res = None
    low, high = 1,stalls[n-1]-stalls[0]

    while(low <= high):
        mid = low+(high-low)//2
        if(isPossbile(stalls,mid,n,k) == True):
            print(f"mid//high : {mid}//{high}")
            res = mid
            low = mid-1 	
        else:
            high = mid+1

    return res


def isPossbile(stalls,mdist,n,k):

    cowPlaced = 1	# Default number of cow placed is 1 at location a[0];
    lastCowPlaced = stalls[0]	# Last Location of cow placed, arr[0];

    for i in range(1,n):
        print(f"cowPlaced//lastCowPlaced:{cowPlaced}//{lastCowPlaced}")
        if(stalls[i]-lastCowPlaced >= mdist):
            cowPlaced += 1
            lastCowPlaced = stalls[i]	# Last Cow Location Updated;
        if(cowPlaced > k):
            return False
        
    return True


def main():
    try:
        stalls = [4, 2, 1, 3, 6]            # ~ data
        k = 3
        res = aggressiveCows(stalls,k)
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
    