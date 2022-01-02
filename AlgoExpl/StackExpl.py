#!/bin/python3

import math
import os
import random
import re
import sys
import time
from Helpers.mStack import *
from collections import deque

## Deque Pre-Installed Library
def dequeExpl():
    pass


## Main Working Function Call
def main():
    try:
        # dequeExpl()                           # Deque init

        stack = Stack()

        stack.append("Adam")
        stack.append("Branda")
        stack.append("Camelio")
        # stack.append("Dominoz")
        # stack.append("Erenster")
        # stack.append("Ferero")
        # stack.append("Gosepho")
        # stack.append("Hercules")
        # stack.append("Iglesius")
        
        stack.show()

        # print(len(stack))

    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

        
## Main Working Here...
if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    