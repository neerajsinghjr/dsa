'''
Problem:
Given five positive integers, find the minimum and maximum values 
that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line 
of two space-separated long integers.

Example
arr = [1,3,5,7,9]

The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24. 
The function prints 16,24

Constraints:
1. array can have 5 integers 
2. 1<= arr[i] <= 10^9

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minMaxSum' function below.
#

## Main Working Function

def miniMaxSum(arr):
    # base cases;
    if not arr:
        print(0,0)
    elif len(arr) == 4:
        minMax = sum(arr)
        print(minMax,minMax)
    else:
        # main cases;
        sumArr = 0
        nMin, nMax = arr[0], arr[0]
        for num in arr:
            sumArr += num
            if nMin > num:
                nMin = num
            elif nMax < num:
                nMax = num
        print(sumArr-nMax,sumArr-nMin)


def main():
    res = ""
    print(res) if res else print("Empty!")
        

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    