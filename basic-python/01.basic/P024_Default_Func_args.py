#!/bin/python3

import os
import re
import sys
import time
import math
import random

from typing import List 


# Its a bad idea to create empty list as a default variable. 
# because nums is gonna behave like global list. 
# and all the elements are gonna inside the nums
# on each call as per example;;
# Instead of assigning common empty list at the time of initialization
# You can define variable as None and pass the empty list from the
# callable;;
def number(x: int, nums: List = []):
    nums.append(x)
    return { 'x': x+1, 'nums': nums }


"""
nums: List: 
"""
def main():
	x1 = number(10)	

	print(x1)		# {'x': 11, 'nums': [10]}

	x2 = number(12)	

	print(x2)		# {'x': 13, 'nums': [10, 12]}


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    