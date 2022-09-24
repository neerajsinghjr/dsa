#!/bin/python3

import os
import re
import sys
import time
import math
import random



##---Main Execution;;
def main():
   
   # 1: float precision;
   x = 890989.8998008
   # print(x:.2f)          # not working;

   print(round(x, 20))

   # 2: list comprehensions;
   names = ['anna', 'alex', 'jenny', 'chloe']
   ans = [name for name in names if(name.startswith('a'))]
   print(ans)

   # 3: destructing looping 
   head, *tail = [1,2,3,4,5,6]
   print(head)       # 1
   print(tail)       # [2,3,4,5,6]

   *head, tail = [1,2,3,4,5,6]
   print(head)       # [1,2,3,4,5]
   print(tail)       # 6


   # 4: function;
   def addfriend():
      friends.append("anna")
      print(2, id(friends))

   friends = []
   print(1, id(friends))
   addfriend()
   print(3, friends, id(friends))


   # 5 lambda;
   def double(x): return x*2

   nums = [1,2,3,4]

   print('comp:', [x*2 for x in nums])

   print('func:', [double(x) for x in nums])

   print('lambda:', list(map(lambda x: x*2, nums)))

   print('lambda-comp:', [(lambda x: x*2)(x) for x in nums])

   # 6 Destructing variables;

   def add(*nums):   # *args: send or receive tuples;
      print(nums, type(nums))
      return nums[0]+nums[1]

   print(add(13,14))


   def add2(x,y):    # var-args-rev: destructured at func call;
      return x + y

   nums = [10,20]
   print(add2(*nums))

   def sub(**nums):     # **kargs: send or receive dictionary'      
      return nums['x']+nums['y']

   print(sub(x=50,y=50))       # variable arguments;

   dic = {'x': 100, 'y':100}
   print(sub(**dic))             # both end keyword arguments;


   # end;;


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    