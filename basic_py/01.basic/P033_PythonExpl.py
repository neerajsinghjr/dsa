#!/bin/python3

import os
import re
import sys
import time
import math
import random
from collections import defaultdict

# Generator in Python;
def fibo(n):
   """
   Generators:-

   Generators are functions that return an iterable collection of items, one
   at a time, in a set manner. Generators, in general, are used to create
   iterators with a different approach. They employ the use of yield keyword
   rather than return to return a generator object. Let's try and build a
   generator for fibonacci numbers -

   """
   a,b = 0,1
   count = 0
   if(count < n):
      while(a <= n):
         print(f"by:count: {count}")         # checkpoint 1
         yield a
         a,b = b, a+b
         print(f"ay:count: {count}")         # checkpoint 2
         count += 1
         print(f"++count: {count}")          # checkoint 3

   else:
      raise StopIteration()


# Inheritance: Accessing attribute of parent class;
class parent:

   def __init__(self, name):
      self.name = name


class child(parent):

   def __init__(self, name, child):
      # super().__init__(name)         # Correct 1 ;;
      parent.name = name               # Correct 2 ;;
      self.child = child

   def getDetails(self):
      print(f"Father: {self.child}")
      print(f"Child: {self.name}")


# Inheritance: Acccessor
class student:

   def __init__(self, regId, studId, name, phone):
      self.__regId = regId # private
      self.__studId = studId # private
      self._phone = phone  # protected
      self.name = name


   def getDetails(self):   
      print(f"Register ID: {self.__regId}")
      print(f"Student ID: {self.__studId}")
      print(f"Student Name: {self.name}")
      print(f"Phone: {self._phone}")



class test(student):

   def __init__(self, regId, studId, name, std, phone):
      super().__init__(regId, studId, name, phone)
      self.std = std


   def getDetails(self):
      print(f"Register ID: {self.__regId}")    # not acessible
      print(f"Student ID: {self.__studId}")    # not acessible
      print(f"Student Name: {self.name}")
      print(f"Standard: {self.std}")
      print(f"Phone: {self._phone}")             # not acessible


# Class: Empty class;
class employee:
   pass


# Add two number without plus;
def add_nums(num1, num2):
   while num2 != 0:
       data = num1 & num2
       num1 = num1 ^ num2
       num2 = data << 1
   return num1


# Iterator in Pythonn;



##---Main Execution;;
def main():
   print(add_nums(2, 10))

   # print("subclass: ", issubclass(child, parent))
   # print('subclass: ', issubclass(test, student))

   # p = Student("REG_176096879", 176096879, 'Neeraj Singh', 7703863166)
   # p.getDetails()

   # t = Test("REG_176096879", 176096879, 'Neeraj Singh', "MCA", 7703863166)
   # t.getDetails()

   # c = child("Neeraj Singh", "Himmat Singh")
   # c.getDetails()

   # obj = fibo(3)        # generator object;
   # print(obj.__next__())
   # print(obj.__next__())
   # print(obj.__next__())
   # print(obj.__next__())
   # print(obj.__next__())

   # print(help(list))       # interactive help system doctype
   # print(dir(set))         # return list of methods which can be used by that function;



if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    