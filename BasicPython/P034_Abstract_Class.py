#!/bin/python3

import os
import re
import sys
import time
import math
import random
from abc import ABCMeta

class Fruit:
   def checkRippness(self):
      raise NotImplementedError("Fruilt: checkRippness() method not defined")

class Apple(Fruit):
   def __init__(self):
      print("Apple obj is initialised!")


class Parent(object):
   __metaclass__ = ABCMeta

   @abstractmethod
   def virtualMethod(self):
      raise NotImplementedError("NA")


class Child(Parent):
   
   def __str__(self):
      return "Child <object>"
   
class MontyPython:
    def joke(self):
        raise NotImplementedError()

    def punchline(self):
        raise NotImplementedError()

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"


##---Main Execution;;
def main():
   # Case 3:
   sketch = ArgumentClinic() 
   sketch.joke() 
   sketch.punchline()

   # Case 2:
   # c = child()
   # print(f"child object : {c}")

   # case 1: 
   # obj = Apple() 
   print(f"Fruit object : {obj}")
   # obj.checkRippness()


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    