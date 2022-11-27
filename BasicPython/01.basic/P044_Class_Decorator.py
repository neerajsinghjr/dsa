'''
-------------------------------------------------------------------------------------
-> Title: Decorator in Class
-> Attempted: 26/11/2022
-> Description: 
-------------------------------------------------------------------------------------
Class in Decorator:
-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


def printUppercase(_class):
    # Main Code;
    def wrapper(self): 
        # Main Code Body;

    _class.show = wrapper       # Overriding old show function with wrapper
    return wrapper


@printUppercase
class Dictionary:

    def __init__(self):
        self.word = "halloween"

    def show(self):
        return f"Word of the day is {self.word}"


##---Main Execution;;
def main(res=None):
    try:
        obj = Dictionary()
        print(obj.show())

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
    
