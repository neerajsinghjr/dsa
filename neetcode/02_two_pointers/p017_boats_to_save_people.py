'''
-------------------------------------------------------------------------------------
-> Problem Title: 881. Boats to Save People
-> Problem Status: Completed
-> Problem Attempted: 2024-04-07
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/boats-to-save-people/description/

Reference:-
https://youtu.be/XbaxWuHIWUs

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

    def numRescueBoats(self, peoples: List[int], limit: int) -> int:
        """
        _stdin:
            arg1: list[int]
            arg2: int
        _stdout: int
        """
        return self.ansv1(peoples, limit)

    def ansv1(self, peoples, limit):
        """
        _run: accepted
        _code: time: o(nlogn), space: o(1)
        _study:
        --- constraints ---
        [+] two people atmost travel in a boat when total weight lesser than boat limit
        [+] possible for a single guy to travel in a boat if weight is under boat limit
        --- explanation ---
        [+] problem: peoples = [3,5,3,4], limit = 5
        [+] output: 4 boats (3), (3), (4), (5)
        [+] we need to sort the peoples weight first, in order to find the total weight
        of two people whose weight is lesser than the boat capacity.
        [+] if group two people's weight is not lesser than the boat's capacity then that
        means we can still reduce the one peolpe from the end but result can add by 1.
        """
        lo = res = 0
        hi = len(peoples) - 1
        peoples.sort()  # o(nlogn)

        while (lo <= hi):
            # contraints to check for 2 pople together in the boat;;
            if peoples[lo] + peoples[hi] <= limit:
                lo += 1

            # here we are directly reducing the weight of people from end directly
            # without checking because as per the question constraints people weight
            # can't be greater than that the limit of boat capacity;;
            # otherwise you've to pick whether the candidate can be assigned to the
            # result or not on the basis of weight of people[high] < limit only;;
            hi -= 1

            res += 1

        return res


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
