'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 967. Numbers With Same Consecutive Differences
-> Problem Status: Completed
-> Problem Attempted: 03.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Return all non-negative integers of length n such that the absolute difference between every two 
consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading 
zero and is invalid.

You may return the answer in any order.


Example 1:
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

 
Constraints:
2 <= n <= 9
0 <= k <= 9

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
from collections import deque
class Solution:
    
    ###---Main Execution;;;
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # base condition
        if(n <= 1): return []
        
        # return self.ansv1(n,k)
        return self.ansv2(n,k)
    
    
    """
    Run: Success
    Code: Optimised (BFS) | T:O(2^N) | S:O(2^N)
    Study:
    # The idea is to use BFS to try appending 0 - 9 to each number 
    # starting from a single digit 1 - 9 until the number has n digits
    # push all numbers with single digit to a deque
    # (1, d) : (current position, number), pop the first element from the deque
    # if the current position is n, then we can append num to ans
    # Otherwise, we can iterate 0 to 9
    # Then, num % 10 to get the last digit of num
    # then get the difference with j
    # since (num % 10) - j can be negative and positive,used abs()
    # if the difference is equal to k, then we can include digit j
    # so multiply the current number by 10 and add j
    """
    def ansv2(self,n,k):
        res = []
        q = deque((1,d) for d in range(1,10))
        while(q):
            pos,num = q.popleft()               
            if(pos == n):
                res.append(num)
            else:
                for j in range(10):
                    if(abs(num%10 - j) == k):
                        q.append((pos+1,num*10+j))
        
        return res
    
    
    """
    Run: Bug(Debugging REQ*) ~Working for many case
    Code: Brute Force | T:(10*10*5) | S:(1)
    Study:
    Simple, iterating loop for specific number of time. and match absolute 
    difference evertime, then store the result if match found equals to 7.
    """
    def ansv1(self,n,k):
        res = set()
        
        num,pre = "",None
        for _ in range(5):
            for i in range(1,10):
                for j in range(10):
                    if(len(num) <= n):                            
                        if not(num):
                            num += f"{i}{j}" if(abs(i-j) == k) else ""                            
                        else:
                            if(len(num) == n):
                                if(num): res.add(int(num))
                                num = ""
                                continue
                                
                            pre = int(num[-1])              # $num[-1]: last index value;
                            num += f"{j}" if(abs(pre-j) == k) else ""
                            
                    else:
                        if(num): 
                            res.append(int(num))             # $res: update;
                            num = ""                         # $num: reset;
        
        return list(res)


##---Main Execution;;
def main():
    try:
        # data = []               # ~ data
        # obj = Solution()
        # res = ""
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
    