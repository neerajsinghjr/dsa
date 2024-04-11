'''
-------------------------------------------------------------------------------------
-> Problem Title: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
-> Problem Status: Completed
-> Problem Attempted: 2024-03-23
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Refer:-
https://youtu.be/1pkOgXD63yU

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
        --- explanation ---
        We are maintaining two variable - (buy, profit). We will use below logic
        to calculate value of these...
        --- buy ---
        'buy' is default set to 0 index price by default, in our case buy = 7 stock.
        if current price of stock is smaller than last buy price of stock then we
        will update our buy pointer else ignore.
        --- profit ---
        profit variable is set to 0 by default. profit will update based on the logic
        profit = max(profit, prices[cur_buy_price] - prices[last_buy_price])
        """
        buy, profit = 0, 0
        for i in range(n):
            # if current price is lower than the buy prices
            # then buy again on current price else ignore;;
            if prices[buy] > prices[i]:
                buy = i
            # profit calculate again from current prices;;
            profit = max(profit, prices[i] - prices[buy])

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
