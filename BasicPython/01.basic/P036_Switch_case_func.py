#!/bin/python3

import os
import re
import sys
import time
import math
import random


def switch_v1(value):
   if(value == 1):
      return value*10
   elif(value == 2):
      return value*30
   elif(value == 3):
      return value*30
   else:
      return "Default: Exiting..."

class SwitchBase:
   def switch(self, case):
      m = getattr(self, 'case_{}'.format(case), None)
      if not m:
         return self.default
      return m

   __call__ = switch

class CustomSwitch:
   def case_1(self):
      return "case_1"

   def case_2(self):
      return "case_2"

   def case_3(self):
      return "case_3"

   def default(self):
      raise Exception("Default: Exiting...")


##---Main Execution;;
def main():
   """
   clase introspection: method overloading...
   """
   switch = CustomSwitch()
   print(switch(1))

   """
   switch_v1: Switch functionality implemented using the if-else;
   """
   # print(switch_v1(3))
   # print(switch_v1(4))

   """
   switch_v2: Switch functionality implemented using the dictionary;
   """
   switch_v2 = {
      1: lambda: 1*10,
      2: lambda: 2*20,
      3: lambda: 3*30,
   }

   def default():
      return "Default: Exiting..."

   print(switch_v2.get(1, default))       # return lambda function object; 
   print(switch_v2.get(4, default))       # return local default method object;

   print(switch_v2.get(1, default)())       # return lambda function object; 
   print(switch_v2.get(4, default)())      # return local default method object;


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    