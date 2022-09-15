'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 2007. Find Original Array From Doubled Array
-> Problem Status: Completed
-> Problem Attempted: 15.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

An integer array original is transformed into a doubled array changed by
appending twice the value of every element in original, and then randomly
shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If
changed is not a doubled array, return an empty array. The elements in
original may be returned in any order.

 
Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]

Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []

Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
 

Constraints:

1 <= changed.length <= 105
0 <= changed[i] <= 105

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
from collections import Counter

class Solution:
    
    ###---Main Execution;;
    def findOriginalArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        if(n == 1): return []
        
        if(n % 2 != 0): return []
        
        return self.ansv1(nums, n)
    
    
    """
    Run: Accepted
    Code: Hashset Optimisation | T:O(N+NLogN) | S:O(N)
    Study:
    Simple approach but numbers needs to be sorted first for particular sequence...
    1) Count the number occurence using hashset
    2) Then, iteratively check for single number by number and verify if the double of 
    current number exist. 
    3.1) If so then include in result, reduce the count of current number and 2 * current number by 1 
    3.2) if not then set result to none    
    """
    def ansv1(self, nums, n):
        res = []
        nums.sort()
        data = Counter(nums)
        
        for i in nums:
            # p1:current num count is zero;
            if(data[i] == 0):
                continue
            else:
                # p2: check if double of current num exist;
                if(data.get(2*i,0) > 0):
                    res.append(i)
                    data[2*i] -= 1          # double num;
                    data[i] -= 1            # single num
                else:
                    return []
        
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
    