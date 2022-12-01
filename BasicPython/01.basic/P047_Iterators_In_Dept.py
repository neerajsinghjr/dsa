'''
-------------------------------------------------------------------------------------
-> Title: Iterator Python
-> Attempted: 28/11/2022
-> Description: 
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


#-------------------------- Example 1: Basic example of iterators
def example1():
    cartoons = ['Tom and Jerry', 'Shin Chan', 'Doraemon', 'Ninja Hatodi', 'Hage Maru']

    cartoon = iter(cartoons)

    print("Generator Object :", cartoon)
    print("next cartoon :", next(cartoon))
    print("next cartoon :", next(cartoon))
    print("next cartoon :", next(cartoon))
    print("next cartoon :", next(cartoon))
    print("next cartoon :", next(cartoon))

#-------------------------- /Example 1;;

#-------------------------- Example 2: Iterators;
class IDGenerator:

    def __init__(self, ECODE):
        self.id = 0
        self.ECODE = ECODE

    def __iter__(self):
        return self                 # return the self instance of the object;

    def __next__(self):
        self.id += 1
        return f"{self.ECODE}{self.id:03d}"


def example2():
    idObject = IDGenerator('EAC')       # IdGenerator Object;;
    iterObject = iter(idObject)         # Iterator Object;;

    print("GENERATING EMPLOYEE CODE ...")
    for _ in range(5):
        print("ID: ", next(iterObject))

#-------------------------- /Example 2;;


##---Main Execution;;
def main():
    example2()
    # example1()


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    