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


def prefixSum(nums):
    map = {}
    
    for (key,value) in enumerate(nums):

        if(value in map):
            pass


def main():
    try:
        # data = [1,-2,-3,4,-7,5,1,1,3,4,5,-6]
        data = [-1,2,1,-4,2,3,-1,2]                  
        res = prefixSum(data, target=0)
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
    