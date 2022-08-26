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



## Main Working Function, here...
def subArrayExists(arr):
    map = {}
    temp = 0
    for (key,value) in enumerate(arr):
        temp += arr[key]
        if (temp == 0):
            return 'Yes'
        elif(temp in map.keys()):
            return 'Yes'
        else:
            map[value] = key

    return 'No'
    
    
def main():
    try:
        arrays = [
            [1, 2, 3, 4, 5],
            [4, 2, 0, 1, 6],
            [4, 2, -3, 1, 6],
        ]
        for arr in arrays:
            res = subArrayExists(arr)
            print(f"{arr} : {res}") if res else print("Empty!")
        
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
    