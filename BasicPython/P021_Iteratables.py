#!/bin/python3

import os
import re
import sys
import time
import math
import random



class FirstEvenNumber:

    def __init__(self,start=0,limit=100):
        self.start,self.limit = start,limit

    def __next__(self):
        if(self.start < self.limit):
            print(f"self.start: {self.start}")
            pre = self.start
            if(pre % 2 == 0):
                # here yield wont work because you need to return the value to the __iter__() function 
                # and yield return generator object everytime iter() call __next__(self) method;
                # yield pre
                return pre

            self.start += 1

        else:
            raise StopIteration(f"Limit Reached {self.limit}")

    def __iter__(self):
        return self


class FirstEvenNumberV2:

    def __init__(self,start=0,limit=100):
        self.start = start
        self.limit = limit

    def __iter__(self):
        while(True):
             if(self.start < self.limit):
                if(self.start % 2 == 0):
                    # but 
                    yield self.start                
                self.start += 1


### Example of showing directly __iter__() iterable 
### Iterable direclty use the __iter__() method to carrout serialization of the data;
class Fib:
    def __init__(self):
        self.a, self.b = 0, 1


    def __iter__(self):
        while self.a < 20:
            # here yield work because now yield can return the value directly to the external function entity;
            yield self.a
            self.a, self.b = self.b, self.a+self.b



### Iterator: are those who have __next__(self) method.
### Example of this as follows.
### not __iter() object will return an iterator because __next__()
class FibV2:
    
    def __init__(self,a=0,b=1,limit=20):
        self.a,self.b = a,b
        self.limit = limit + a              # next series till limit;

    def __next__(self):
        if(self.a < self.limit):
            pre = self.a 
            self.a, self.b = self.b, self.a + self.b
            return pre
        else:
            raise StopIteration("Limit Reached 20")

    def __iter__(self):
        return self



##---Main Execution;;
def main():
   # even = FirstEvenNumber(start=1,limit=500)
   # print(even)
   # print(next(even))
   # print(next(even))
   # print(next(even))
   # print(next(even))


   # f = Fib()
   # print(list(f))

   f1 = FibV2(a=1,b=2,limit=10000)
   print(list(f1))

   # x1 = FirstEvenNumberV2()
   # print(f"iter: {list(x1)}")



if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    