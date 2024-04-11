'''
-------------------------------------------------------------------------------------
-> Problem Title: Minimum Parenthesis
-> Problem Status: Completed
-> Problem Attempted: 24/09/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118626/offering/1377978?leftPanelTab=0

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
def minimumParentheses(pattern):
    # Write your code here
    # Return the minimum number of parentheses required.
    if not pattern:
        return 0
    # return ans_v1(pattern)
    return ans_v2(pattern)


def ans_v1(pattern):
    """
    - time : o(n)
    - space: o(n)
    - run : failed
    - choke : some calculation is not correct, because of mismatch bracket. 
    - brief: solution tells, iterate over the loop and find the current index
      opening and next index closing bracket. If match then pass else count it.
    """
    count = 0
    for idx in range(len(pattern)):
        if (pattern[idx] == '(' and pattern[idx+1] == ')'):
        # or (pattern[idx] == ')' and pattern[idx+1] == '('):
            pass
            print("match found: ", pattern[idx],'->', pattern[idx+1])
        else:
            count += 1
            print("match not found: ", pattern[idx],'->', pattern[idx+1])
            
    return count


def ans_v2(pattern):
    """
    - time: o(n)
    - space: o(n)
    - run: success
    - choke: none
    - brief: we are iterating over the pattern and storing all the open
      bracket inside the stack and as soon as we found any closing bracket
      then we are popping the open bracket from stack only. if there is any
      unmatched closing bracket then simply increase the occurence;;
    """
    stack = []
    cb_count = 0
    ob, cb = '(', ')'
    for br in pattern:
        if br == ob:
            # Store the open bracket in the stack;;
            stack.append(ob)
        else:
            if len(stack) > 0:
                # if a couple open and close bracket found 
                # then pop it from stack, then pass it;;
                ob_last = stack.pop()
                
            else:
                # if there is any unmatched closing bracket then 
                # increase the count directly;;
                cb_count += 1
                
    return cb_count + len(stack)


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