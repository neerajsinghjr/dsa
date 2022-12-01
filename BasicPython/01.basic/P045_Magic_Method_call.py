'''
-------------------------------------------------------------------------------------
-> Title: Magic Method __call__
-> Attempted: 27/11/2022
-> Description: 
-------------------------------------------------------------------------------------
Python has a set of built-in methods and __call__ is one of them. The __call__
method enables Python programmers to write classes where the instances behave
like functions and can be called like a function. When the instance is called
as a function;

If this method is defined, x(arg1, arg2, ...) is a shorthand
for x.__call__(arg1, arg2, ...).

	object() is shorthand for object.__call__()

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Student:

	_record = {}

	def __init__(self, name):
		self._record['name'] = name
		print(f"NEW STUDENT CREATED : {name}")

	def __call__(self, *args, **kwargs):
		flag = False
		if (args):
			flag = True
			self._record['extra'] = args

		if(kwargs):
			flag = True
			for key,value in kwargs.items(): 
				self._record[key] = value

		if(flag):
			print(f"PROFILE UPDATED")


	def showDetails(self):
		print(f"Student Profile : {self._record['name']}")
		for k,v in self._record.items():
			if not(k == 'name'):
				print(f"{k} : {v}")


##---Main Execution;;
def main(res=None):    
    neeraj = Student("Neeraj Singh")
    neeraj('Crickets', 'Volleyball', 'Badminton', 
    	school='DUCS Sr. Sec. School',
    	std='XII',
    	teacher='Shristi Sharma',
    	Subjects=('Physics', 'Chemisty', 'Computer Cpp', 'Maths', 'English')
    )
    neeraj.showDetails()

   
if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")