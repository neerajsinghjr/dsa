'''
-------------------------------------------------------------------------------------
-> Problem Title: Sum of Inifinite Array
-> Problem Status: Ongoing...
-> Problem Attempted: 09/06/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

refer question here ...
https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381865

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


# SAMPLE OUTPU;
# 10 10 30 20 
# 22 33 22 33 110 
# 105 105 
# 205 
# 1090 8050 168 
# 112 112 
# 240 

def get_sum(arr_sum, n, idx):
    result = 0
    # Total repetition count of original array;;
    count = idx // n
    print("count: ", count)
    result = count * arr_sum[n-1]
    print("result1: ", result)
    # Calculate the residual sum of the array;;
    leftover_count = idx % n
    print("count: ", count, "residual:", residual)
    # Now, Total Sum = leftover + cur_result;;
    result = result + arr_sum[leftover_count]
    print("result2: ", result)
    return result


def sumInRanges(arr, n, queries, q):
    """
    run: ...
    time: ...
    space: ...
    choke: ...
    study : ...
    """
    mod = 10**9 + 7
    i, cur_sum = 0, 0
    res, arr_sum = [], [0]*n
    print("arr: ",arr)
    # S1: Mapping arr_sum at every index;
    while(i < n):
        cur_sum += arr[i]
        arr_sum[i] = cur_sum
        i += 1
    
    print("arr_sum: ", arr_sum)

    # S2: Map arr_sum with queries;;
    for l, r in queries:
        print("idx, l:",l,"r:",r)
        l, r = (l-1), (r-1)
        rsum = get_sum(arr_sum, n, r)
        print("rsum: ", rsum)
        lsum = get_sum(arr_sum, n, l)
        print("lsum: ", lsum)
        range_sum = rsum if l == r \
            else (rsum-lsum) % mod
        print("range_sum: ", range_sum)
        res.append(range_sum)
    
    print("finally result: ", res)
    return res


def sumInRanges_v1(arr, n, queries, q):
    """
    run: TLE
    time: o(n)
    space: o(q)
    choke: TLE
    study: simply adding sum from the left to right index.
    """
    # Base Case;;
    if not arr:
        return []
    # Main Case;;
    res = []
    for l,r in queries:
        l = l-1
        cur_sum = 0
        for i in range(l,r):
            # print("idx:", {i}, "val:", arr[i%n])
            cur_sum += arr[i%n]
        res.append(cur_sum)
    return res
    

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