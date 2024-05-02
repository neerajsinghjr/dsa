'''
-------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

...

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

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        _study:
            arg1: list[int]
            arg2: int
        _study: int
        """
        return self.ansv1(weights, days)

    def ansv1(self, weights, days) -> int:
        """
        _run:
        _code: time: o(n*logk), space: o(1)
        _study:
        --- tricky part ---
        [+] tricky part of this problem was to figureout like how this problem can be a
        binary search problem and what would be the left and right pointer for making
        binary search
        --- explanation ---
        [+] we are using here the binary search on the basis of the left and the right pointer
            [-] left pointer will point to the max wieght of the cargo
            [-] right pointer will point to the total sum of the cargo that would be default
        [+] every time we use left and right pointer to find the mid capacity of the ship
        and check whether all the ship will be able to be delievered all cargo in one go.
        [+] we check this by iterating over the a loop of cargo and each time we subtract
        the existing cargo from the given capacity if the difference > 0 then it can be shipped
        with the same ship
        [+] otherwise we increment the ship count and reset the capacity as well for calculting
        the cargo weight.
        [+] we do the same to find the min_capacity
        """

        def _verify_shipment(cap) -> bool:
            # module will check if all the cargo can be delievered in the given capacity;;
            ship, cur_cap = 1, cap
            for w in weights:
                if cur_cap - w < 0:
                    cur_cap = cap  # reset the current capacity;;
                    ship += 1
                cur_cap -= w

            return ship <= days

        lo, hi = max(weights), sum(weights)

        # for default min_capacity of ship would be total weight assigned to it;;
        min_capacity = hi

        while lo <= hi:
            cur_capacity = lo + (hi - lo) // 2
            if _verify_shipment(cur_capacity):
                min_capacity = min(min_capacity, cur_capacity)
                hi = cur_capacity - 1
            else:
                lo = cur_capacity + 1

        return min_capacity


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
