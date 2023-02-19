#!/bin/python3

import os
import re
import sys
import time
import math
import random
from Helpers.Heaps import *
from Helpers.Other.Heap.heap_iterative import *
from Helpers.Other.Heap.heap_recursive import *


## Main Working Function, here...
def main():
    try:
        # heap = Heap()       # maxHeap = True;
        # heap = Heap()       # maxHeap = True;
        heap = MinHeap(10)      # maxHeap = True;

        # heap.insert(12)
        # heap.insert(10)
        # heap.insert(20)
        # heap.insert(80)
        # heap.insert(90)
        # heap.insert(92)
        # heap.insert(99)

        heap.insert(12)
        heap.insert(10)
        heap.insert(20)
        heap.insert(80)
        heap.insert(90)
        heap.insert(92)
        heap.insert(99)
        heap.insert(88)

        heap.show()

        print("\nEnd Reached...\n")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

    
if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    