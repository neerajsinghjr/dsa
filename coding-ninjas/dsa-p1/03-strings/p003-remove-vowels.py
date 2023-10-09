'''
-------------------------------------------------------------------------------------
-> Problem Title: Remove Vowels
-> Problem Status: Completed
-> Problem Attempted: 24/09/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118626/offering/1377977?leftPanelTab=0

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
def removeVowels(stmt):
    if not stmt:
        return 
    # return removeVowels_v1(stmt)
    return removeVowels_v2(stmt)


def removeVowels_v2(stmt):
    """
    time: o(n)
    space: o(1)
    run: success
    choke: none
    brief: traversing single character and check
    for the respective vowels in it;;
    """
    result = ''
    vowels = 'aeiouAEIOU'
    for s in stmt:
        if not(s in vowels):
            result += s

    return result


def removeVowels_v1(stmt):
    """
    time: o(k)
    space: o(1)
    run: success
    choke: none
    brief: replacing vowels directly from the 
    inputted string.
    """
    vowels = "aeiouAEIOU"
    for v in vowels:
        stmt = stmt.replace(v,'')
    return stmt


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