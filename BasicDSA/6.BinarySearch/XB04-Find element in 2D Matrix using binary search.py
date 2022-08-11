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
def matSearch(grid,n,m,x):
    
    if not(len(grid)):
        return 0
    
    i,j = 0,m-1      # i:row j:column
    while(i<n and j>=0):
        if(grid[i][j] == x):
            return 1
        elif(grid[i][j] < x):
            i += 1          # row ++
        elif(grid[i][j] > x):
            j -= 1          # col --
    return 0


def main():
    try:
        data = [1,2,3,4,5,6,9,10,11,4,3,2,1,0]               # ~ data
        res = matSearch(data,len(data))
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
    