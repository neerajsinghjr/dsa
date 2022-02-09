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
from math import ceil


## Main Working Function, here...
class Solution:
    
    def merge(self, arr1, arr2, n, m):
        total = n+m
        arr1 = arr1+arr2
        print(arr1)
        i = 0
        gap = n+m//2
        while(gap > 0):
            x, y = 0,gap
            if(x < total and y < total):
                if(arr1[x] > arr1[y]):
                    arr1[x], arr1[y] = arr1[y], arr1[x]
                else:
                    x += 1
                    y += 1
            else:
                gap = gap//2
                




def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = ""
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
    