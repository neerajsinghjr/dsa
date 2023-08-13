#!/bin/python3

import os
import re
import sys
import time
import math
import random
# from functools import singledispatch
from typing import overload


class Test:
    """
    Normal Method Overloading Failed because python consider everything
    as object. So when you create multiple function with the same
    name. Then Python Compiler will the function definition whose
    definition comes at the end of the whole code definition.

    Alternatively, you can use if-elif-else ladder but this will not
    trigger method overloading. It would be just like normal if-else ladder

    But, you can use multidispatch library to implement the method overloading
    upto its real extends. Refer Class Test2
    """
    def add(self):
        print("No values supplied")

    def add(self, x, y, z):
        print("Result: ", x+y+z)

    def add(self, x):
        if x and isinstance(x, (list, tuple)):
            print("Result: ", sum(x))
        else:
            print("Result:   ", x)


class Test2:
    @overload
    def add(self):
        print("No values supplied")

    @overload
    def add(self, x, y, z):
        print("Result: ", x+y+z)

    @overload
    def add(self, x):
        if x and isinstance(x, (list, tuple)):
            print("Result: ", sum(x))
        else:
            print("Result:   ", x)


##---Main Execution;;
def main():
    # Attempt 1: Failed Keep in mind;;
    # x = Test()
    # x.add()

    # Attempt 2: Using Multidispatch;;
    x = Test2()
    x.add()


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    