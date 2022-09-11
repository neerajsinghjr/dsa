'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 188. Best Time to Buy and Sell Stock IV
-> Problem Status: Completed
-> Problem Attempted: 10.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

You are given an integer array prices where prices[i] is the price of a given
stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k
transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2

Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit =
3-0 = 3.
 

Constraints:
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000

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
    