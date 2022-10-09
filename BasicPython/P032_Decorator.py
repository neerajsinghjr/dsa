#!/bin/python3

import os
import re
import sys
import time
import math
import random



def lowercase(func):
   def wrapper():
      return func().lower()

   return wrapper


def uppercase(func):
   def wrapper():
      return func().upper()

   return wrapper


def titlecase(func):
   def wrapper(arg):
      return arg.title()

   return wrapper


@titlecase
def greetingV2(name):
   return f"Welcome Back, {name} !!!"



@lowercase
def greeting(name):
   return "Welcome, {name} !!!"


##---Main Execution;;
def main():
   # res = greeting()
   res = greetingV2("neeraj singh jr.")

   print(res)


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    