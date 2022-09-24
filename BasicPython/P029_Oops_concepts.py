#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Person:

   # constructor of init;
   def __init__(self, name, age):
        self.name = name
        self.age = age
 
   # a class method to create a Person object by birth year.
   @classmethod
   def fromBirthYear(cls, name, year):
     return cls(name, date.today().year - year)

   # a static method to check if a Person is adult or not.
   @staticmethod
   def isAdult(age):
     return age > 18

 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))


##---Main Execution;;
def main():
   obj = Sample()
   obj.get()      # 1
   Sample.get(obj)


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    