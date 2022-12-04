'''
Recursion Exploration
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


# increase function;
def increaseFunc(num):
    # base case
    if num == 0:
        return 
    # main case
    increaseFunc(num-1)
    print(num)

# decrease function;
def decreaseFunc(num):
    # base case
    if(num == 0):
        return 
    # main case
    print(num)      
    decreaseFunc(num-1)

# down to up function;
def downAndUpFunc(num):
    # base case
    if(num == 0):
        return 
    # main case
    print(num)          
    downAndUpFunc(num-1)
    print(num)

# power function;
def power(num,exp):
    # base case
    if(exp == 0):
        return 1
    # main case
    return num * power(num,exp-1)

# power fast function;
def powerFast(num, exp):
    # base case
    if(exp == 0):
        return 1
    # main case
    res = num * power(num,exp//2)
    return (res*num if exp%2 == 0 else res)

# main function;
def main():
    try:
        num,exp = 2,12
        # res = increaseFunc(num)               # 1,2,3,4,5
        # res = decreaseFunc(num)               # 5,4,3,2,1
        # res = upAndDownFunc(num)              # 1,2,3,4,5,5,4,3,2,1
        # res = downAndUpFunc(num)              # 5,4,3,2,1,1,2,3,4,5
        # res = power(num,exp)                  # 2 ^ 2 ~ 4
        # res = powerFast(num,exp)              # 2 ^ 2 ~ 4
        print(res) if res else print("main: None")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

# init
if __name__ == '__main__':
    print("#------------ Code Start ---------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    