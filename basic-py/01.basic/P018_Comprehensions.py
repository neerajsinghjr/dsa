#!/bin/python3

import os
import re
import sys
import time
import math
import random



class Solution:

    def __init__(self):
        pass


def sample():
    pass
        

##---Main Execution;;
def main():
   l1 = [x for x in range(10) if(x%2 == 0)]

   l2 = { x:x**2
    for x in range(10) 
    if(x%2 == 0)
   }

   print(f"l1: {l1}")

   print(f"l2: {l2}")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
