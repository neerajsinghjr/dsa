'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Sort the list of tuples
-> Problem Status: Ongoing...
-> Problem Attempted: 28.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Consider the situation when you ae receiving the data in the list form and the nested tuple inside it
and you are asked to sort the given tuple.

Input: "[('English', 99), ('Math', 100), ('Science', 80)]"
Output:  [[('English', 99), ('Math', 100), ('Science', 80)]]

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- Main Solution;;
class Solution:
    
   def __init__(self):
    pass


##---Main Execution;;
def main():
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
    