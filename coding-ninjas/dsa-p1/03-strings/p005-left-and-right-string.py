'''
-------------------------------------------------------------------------------------
-> Problem Title: Left and Right Rotation of A String
-> Problem Status: Completed
-> Problem Attempted: 30/09/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118626/offering/1377979?leftPanelTab=0

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
def leftRotate(ch, d):
    # Write your code here.
    d = d % len(ch) if d > len(ch) else d
    return ch[d:] + ch[:d]


def rightRotate(ch, d):
    # Write your code here.
    d = d % len(ch) if d > len(ch) else d
    mid = len(ch) - d
    return ch[mid:] + ch[:mid]


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
    