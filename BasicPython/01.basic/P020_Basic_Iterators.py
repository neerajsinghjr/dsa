#!/bin/python3

import os
import re
import sys
import time
import math
import random


#-------------------------- Example 1: Basic example of iterators
class FirstHundredNumber:

    def __init__(self):
        self.number = 0

    ### iterators are those which have next() function; 
    def __next__(self):
        if(self.number < 100):
            pre = self.number
            self.number += 1
            return pre
        else:
            raise StopIteration()


    ### Iterables are used to return iterator obj
    def __iter__(self):
        return self


class EvenOddNumber:

    def __init__(self,Flag=True):
        self.cur = 0

    def __next__(self):
        if(self.cur < 100):
            if(self.flag):
                if(self.cur % 2 == 0):
                    pre = self.cur
                    self.cur += 2
                    return pre
            else:
                if(x%2 != 0):
                    pre = self.cur
                    self.cur += 1
                    return pre
        else:
            raise StopIteration()

def example1():
   num = FirstHundredNumber()
   print(list(num))
   # print(num.__name__)
   # print(next(num))
   # print(next(num))    

#-------------------------- /Example 1;;

##---Main Execution;;
def main():
    example1()



if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    