'''
Problem Description:
There are two 'n'-element arrays of integers, A and B. 
Permute them into some A' and B' such, that the relation, 
A'[i] + B'[i] >= k. holds for all i where 0 <= i <= n.

There will be q queries consisting of A,B,C and . 
For each query, return YES if some permutation A',B' 
satisfying the relation exists. Otherwise, return NO.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...
def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for (key,value) in enumerate(A):
        if((B[key]+value) < k):
            return "NO"
    return "YES"


def main():
    try:
        res = twoArrays(2,A=[1,0],B=[0,2])
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
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
    