'''
Problem Description:
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are

Example:
n = 7
arr = [1,2,3,1,3,3,3,2]

Result: 4

Explanation:
pair ~ (1,1) (2,2) (3,3) (3,3)

There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description
Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):
int n: the number of socks in the pile
int ar[n]: the colors of each sock

# Returns
int: the number of pairs
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time

from collections import defaultdict


# Main Working Function, here...
def sockMerchantV1(n, arr):
    count = 0
    temp,pairs = [], defaultdict(int)
    # mark pairs;
    for a in arr:
        if a not in temp:
            temp.append(a)
        else:
            pairs[a] += 1
            temp.remove(a)

    # count pairs;
    for (k,v) in pairs.items():
        count += v
    
    return count


def sockMerchantV2(n, arr):
    if arr is None:
        return 0
    count,pairs = 0,defaultdict(int)
    # mark pairs;
    for a in arr:
        pairs[a] += 1
    # count pairs;
    for (k,v) in pairs.items():
        count += pairs[k]//2
    return count
        

def main():
    # try:
    n,arr = 7,[1,2,3,1,3,3,3,2]
    res = sockMerchantV1(n,arr)
    # res = sockMerchantV2(n,arr)
    print(res) if res else print("Empty!")
        
    # except(Exception) as e:
    #     print(f"Exception Traced: {e}")
    
    # else:
    #     print("Program Executed: Success")

    # finally:
    #     print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    