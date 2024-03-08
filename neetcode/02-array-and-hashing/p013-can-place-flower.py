'''
-------------------------------------------------------------------------------------
-> Problem Title: 605. Can Place Flowers
-> Problem Status: Completed
-> Problem Attempted: 2024-03-08
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/can-place-flowers/description/

Reference:-
https://youtu.be/ZGxqqjljpUI

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        return self.ansv1(flowerbed, n)

    def ansv1(self, bed, n):
        """
        _run: accepted
        _code: o(n)
        _choke: make sure to fill the bed with 1 if its left and right space is empty
        _study: Just iterative over the bed and check if i-1th and i+1th index is 0
        then its good for placing flower.
        Make sure to check for lower bound i.e i = 0 and upper bound i.e, i = n-1 index
        of flowerbed.
        """
        for i in range(len(bed)):
            if bed[i] == 0:
                # left of ith index or i is at first index;;
                left_empty = (i == 0 or bed[i - 1] == 0)
                # right of ith index or i is at last index;;
                right_empty = (i == len(bed) - 1 or bed[i + 1] == 0)
                if left_empty and right_empty:
                    n, bed[i] = n - 1, 1

            if n == 0:
                return True

        return False


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
