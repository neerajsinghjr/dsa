'''
-------------------------------------------------------------------------------------
-> Problem Title: 901. Online Stock Span
-> Problem Status: Completed
-> Problem Attempted: 2024-04-19
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/online-stock-span/description/

Reference:-
https://youtu.be/slYh0ZNEqSw

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import copy


##---Main Solution
class StockSpanner:
    """
    _run: accepted (optimal)
    _code: time: o(n), space: o(n)
    _study:
    --- problem crux ---
    [+] crux is to find the prices which are lesser than or equals to the ith price
    --- explanation ---
    [+] here we are using the approach in which everytime we are pushing the price
    with its minimum span which are lesser than or equals to the current price.
    [+] every time we push the price and we calculate the previous span by popping
    the previous prices adnd if its price is lesser than the current price then we
    are adding the span with current span.
    [+] when the loop breaks we return the calculated current span.
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][1] <= price:
            span += self.stack[-1][0]
            self.stack.pop()

        self.stack.append([span, price])
        return span


class StockSpannerV2:
    """
    _run: rejected (solution not completed)
    _code: ...
    _study: ....
    --- problem crux ---
    [+] crux is to find the prices which are lesser than or equals to the ith price
    --- explanation ---
    [+] here we missed out popping the span from the previous prices that we have
    covered in the latest version of solution
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cur_min = 1
        if self.stack:
            last_min, last_price = self.stack[-1]
            if last_price <= price:
                cur_min = last_min + 1

        self.stack.append([cur_min, price])
        return cur_min


class StockSpannerV1:
    """
    _run: TLE [85/99] (brute-force)
    _code: time: o(n^2), space: o(n)
    _study:
    --- problem crux ---
    [+] crux is to find the prices which are lesser than or equals to the ith price
    --- explanation ---
    [+] here we used the stack popping and stack pushing mechanism where i store the
    price inside the stack and evey time when there is a new price i create a copy
    and start poping the prices stack and count the occurence of all the price
    which are lesser than the current price and return the final count at the end.
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        index = 1
        if self.stack:
            stack = copy.deepcopy(self.stack)
            while stack:
                cur_price = stack.pop()
                if not cur_price <= price:
                    break
                index += 1

        self.stack.append(price)

        return index





##---Main Execution;;
def main(res=None):
    try:
        # Your StockSpanner object will be instantiated and called as such:
        stockSpanner = StockSpanner()
        stockSpanner.next(100)
        stockSpanner.next(80)
        stockSpanner.next(60)
        stockSpanner.next(70)
        stockSpanner.next(60)
        stockSpanner.next(75)
        stockSpanner.next(85)

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
