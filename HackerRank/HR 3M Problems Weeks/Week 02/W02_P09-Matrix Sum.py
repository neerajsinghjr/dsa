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


## Main Working Function, here...
def matrixSum(matrix):
    # Initial Variable;
    size = len(matrix)
    i = j = sum = 0
    row, col = 0, 
    # Change Column;
    for mat in matrix:
    
    # Change Row;

    return sum



def main():
    try:
        matrix = [
            [119,42,83,119],
            [56,125,56,49],
            [15,78,101,43],
            [62,98,114,108],
        ]
        res = matrixSum(matrix)
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
    