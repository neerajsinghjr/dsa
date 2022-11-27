'''
-------------------------------------------------------------------------------------
-> Title: Operator Overloading
-> Attempted: 24/11/2022
-> Description: 
-------------------------------------------------------------------------------------
Operator Overloading is implemented in the class using the __add__() magic method
by overriding the core object class.
-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


"""
OPERATOR OVERLOADING USING THE __add__(self), USING THE (+) OPERATOR;
"""
class Basket:

   def __init__(self):
      self.basket = []

   def __add__(self, fruit):
      self.basket.append(fruit)
      return self.basket

   def __repr__(self):
      return f"Bucket have {len(self.basket)} including {self.basket}"

   def show(self):
      for item in self.basket:
         print(item.showProps())


class Fruit:

   def __init__(self, name, props=None):
      self.name = name
      self.props = props 

   def __repr__(self):
      return f"Fruits : {self.name} with Properties : {self.props} "

   def showProps(self):
      print(f"Fruit : {self.name}")
      print(f"Props : {self.props}")

"""
UNARY OPERATOR CAN BE TURNED OFF AND ON USING THE __invert__(self), METHOD;
"""
class Bulb:

   def __init__(self):
      self.switch = "OFF"

   def __invert__(self):
      self.switch = 'ON' if self.switch == 'OFF' else 'OFF'

   def __repr__(self):
      return f"Bulb : {self.switch}"


##---Main Execution;;
def main(res=None):
   # # EXAMPLE 2: UNARY OPERATOR USING THE __invert__(self)
   # bulb = Bulb()
   # print(bulb)
   # ~(bulb)
   # print(bulb)
   # ~(bulb)
   # print(bulb)

   # EXAMPLE 1: OPERATOR OVERLAODING USING THE __ADD__(SELF);
   basket = Basket()
   apple = Fruit  ('apple', props = {
      'taste' :'sweat',
      'colour' : 'red',
      'qty' : 12
   })

   basket += apple
   basket.show()

   banana = Fruit  ('banana', props = {
   'taste' :'sweat',
   'colour' : 'yellow',
   'qty' : 24
   })

   basket = basket + apple
   basket.show()


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    
