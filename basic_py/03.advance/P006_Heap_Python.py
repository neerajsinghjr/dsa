'''
-------------------------------------------------------------------------------------
-> Problem Title: Python Heap
-> Problem Attempted: 25-01-2025
-> Problem Description:
-------------------------------------------------------------------------------------

Covering the aspect of Python Heap !!!

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import heapq
import random


##---Main Execution;;
def main(res=None):
    try:
        nums = [10, 1, 4, 2, 7, 3, 9, 5, 1000]

        # Min Heap
        min_heap = []

        # initailize the min_heap
        heapq.heapify(min_heap)

        # To push an element onto the min heap
        for num in nums:
            heapq.heappush(min_heap, num)

        # Traversing min_heap
        print("Min Heap: ", end=" ")
        while(min_heap):
            val = heapq.heappop(min_heap)
            print(val, end=" ")
        print()

        # Max Heap
        max_heap = [ -1 * num for num in nums]

        # To pop the smallest element from the min heap
        heapq.heapify(max_heap)  # Convert the list into a min heap (with negated values)

        print("Max Heap: ", end=" ")
        while max_heap:
            val = heapq.heappop(max_heap)
            print(-1 * val, end=" ")
        print()

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
