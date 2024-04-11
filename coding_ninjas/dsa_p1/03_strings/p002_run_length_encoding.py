'''
-------------------------------------------------------------------------------------
-> Problem Title: Encode the message
-> Problem Status: Completed
-> Problem Attempted: 24/09/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118626/offering/1377976?leftPanelTab=0

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
def encode(message):
    """
    time: o(n)
    space: o(1)
    run: success
    choke: none 
    brief: verifying the current index and index+1 is the same 
    if same then count++ otherwise move to next character;;
    """
    res, count = '', 1
    for i in range(len(message)):
        if i < len(message)-1 and message[i] == message[i+1]:
            count += 1
        else:
            res += "{}{}".format(message[i], count)
            count = 1
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