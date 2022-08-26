'''
Problem Description:

'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def countingSort(arr):
    count = [0]*100             ## Change 1: Working Fine
    for x in arr:
        count[x] += 1
    return count


# NOT WORKING FOR SOME CASE ~HR
def countingSort(arr):
    count = [0]*len(arr)       ## Change 2  : Some Test Case Stuck
    for x in arr:
        count[x] += 1
    return count


def main():
    try:
        data = [
            [1,22,4],
            [22,3,4],
            [4,5,66],
        ]
        res = countingSort(data)
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
    