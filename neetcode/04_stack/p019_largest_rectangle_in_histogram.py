'''
-------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

reference:
https://www.youtube.com/watch?v=J2X70jj_I1o

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
class Solution:

    # Constructor;
        def __init__(self):
            pass


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
