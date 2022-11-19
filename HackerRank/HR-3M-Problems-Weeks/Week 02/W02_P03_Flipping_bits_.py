'''
Problem Description:
You will be given a list of 32 bit unsigned integers. 
Flip all the bits (0->1) and (1->0) and return the result as an unsigned integer.

Eg,
num = 9 (base 10)
9 (base 10) = 1001 (base 2)
0000 0000 0000 0000 0000 0000 0000 0000 0000 1001 (base 2) = 9 (base 10)
1111 1111 1111 1111 1111 1111 1111 1111 1111 0110 (base 2) = 4294967286 (base 10)
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def flippingBits(num):
    # Write your code here
    return (2**32-1)^num

def main():
    try:
        res = flippingBits(9)
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
    