'''
-------------------------------------------------------------------------------------
-> Problem Title: Convert String
-> Problem Status: Completed
-> Problem Attempted: 23/09/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118626/offering/1377975

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
def convertString(str):
	"""
    time: o(n)
    space: o(1)
    run: success
    choke: none 
    brief: simple iterate over the loop and check for
    space and then upper the next character.
    """
    res, space_traced = '', True
    for idx in range(len(str)):
        if str[idx].isalpha() and space_traced:
            space_traced = False
            res += str[idx].upper()
        elif str[idx] == ' ':
            space_traced = True
            res += str[idx]
        else:
            space_traced = False
            res += str[idx]
            
    return res


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