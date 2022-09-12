'''
----------------------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted: 
-> Problem Description: 
----------------------------------------------------------------------------------------------------

...

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
    
    ###---Main Execution;;;
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        if(n == 1):
            if(tokens[0] > power): 
                return 0
            return 1
        
        return self.ansv1(tokens,power,n)
    
    
    """
    Run: Accepted
    Code: Optimize (Two Pointer) | T:O(NLogN) | S:O(1)
    Study:
    Simple apporach states that, you have to find the maximum score by playing game.
    Includes this steps ...
    1) Make sure tokens should be sorted, left side should be min token 
    and right side should be max token, for easy traversal values
    2) Start FACE-UP game from left side and if current token <= power, 
    then score++
    3) Start FACE-DOWN, When  currenttoken greater than power, 
    then from right side score--
    4) result should be max of score;
    """
    def ansv1(self,tokens,power,n):
        tokens.sort()
        res,score = 0,0
        left,right = 0,n-1
        
        while(left <= right):
            # p1: face-up play (~ when current power is greater than tokens[i]);
            if(power >= tokens[left]):
                power -= tokens[left]
                score += 1
                left += 1           # left iter++
                res = max(res,score)            # max score;;
                
            # p2: face-down play (~ when score is greater than zero);
            elif(score > 0):
                power += tokens[right]
                score -= 1
                right -= 1              # right iter--
            
            # p3: no play (~ When power < tokens[i] & score == 0)
            else:
                break

        return res


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
    