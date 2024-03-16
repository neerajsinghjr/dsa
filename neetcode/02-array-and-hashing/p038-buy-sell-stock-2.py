'''
-------------------------------------------------------------------------------------
-> Problem Title: 122. Best Time to Buy and Sell Stock II
-> Problem Status: Completed
-> Problem Attempted: 2024-03-16
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Reference:-
https://youtu.be/3SJ3pUkPQMc

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
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        _stdin: list[int]
        _stdout: int
        """
        n = len(prices)
        if n <= 2:
            if n == 1:
                return 0
            profit = prices[1] - prices[0]
            return profit if profit > 0 else 0

        return self.ansv1(prices, n)

    def ansv1(self, prices, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        solution is pretty simple. if the current day price is greater than
        price of last day then we are buying it and adding the differential
        profit in the profit variable.
        """
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


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
