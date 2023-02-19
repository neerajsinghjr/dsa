'''
-------------------------------------------------------------------------------------
-> Title: Decorator in Class
-> Attempted: 27/11/2022
-> Description: 
-------------------------------------------------------------------------------------
Class in Decorator:
-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- EXAMPLE 1 : DECORATOR FUNCTION ON CLASSES 

def printUppercase(_class):
    
    # Main Wrapper Starts Here
    def wrapper(self): 
        print(self.word.upper())

    
    # _class.show = wrapper 
    # here, we are overriding the memory reference of show method 
    # from the class to the wrapper function of the decorator.
    # So that we can modify or extends the functional requirement
    # of that function.
    
    _class.show = wrapper   # Overriding old show function with wrapper 

    return _class


@printUppercase
class Dictionary:

    def __init__(self):
        self.word = "Word of the day is Halloween"

    def show(self):
        print("Dictionary show...")
        return self.word


def example1():
    obj = Dictionary()
    obj.show()

###--- /EXAMPLE 1

###--- EXAMPLE 2 : DECORATOR CLASS ON REGULAR FUNCTION

class StoreResults:
    """
    @classname
    Here, you've defined the class as a decorator on a regular function.
    In class, you have to received the function name inside the __init__
    method using any keyword.
    Like this,
        def __init__(self, function): ...

    and the given functional arguments from external function (~add())
    will be received by the __call__() magic methods.
    """
    def __init__(self, func):
        self.func = func            # <-- accepts function as arguments;
        self.result = []            # <-- lists to store result;

    def __call__(self, *args, **kwargs):
        print("LOG : args:", args)            # debugger 1
        print("LOG kwargs:", kwargs)        # debugger 2
        res = self.func(*args, **kwargs)
        self.result.append(res)
        return self.result


@StoreResults
def add(a,b, y,z): 
    return a+b 


def example2():
    print(add(10,10, y=10, z=20))
    print(add(11,11, y=22, z=33))

###--- /EXAMPLE 2

###--- EXAMPLE 3 : PASSING ARGUMENTS TO THE CLASS DECORATOR;

# Given Abbreviation inside the system;
abbr = {
  "ttyl": "Talk to you later",
  "omg": "Oh my God!",
  "gtg": "got to go"
}

class Abbreviation:

    """
    Catch here is that, one layer added for top abstraction for 
    receiving the class decorator argument;
    __init__() : It will receive the argument from the decorator
    calling.

    dargs : decorator arguments received;
    """
    def __init__(self, decorator_args): 
        self.dargs = decorator_args


    def __call__(self, func):   # here, func : name of the external function;

        # Nested Wrapper for main functionality;
        # args : refers to external argument of function;
        def wrapper(args):   
            
            # string, *_ = args             # Doesn't effect the code ;
            # print("string : ", string)    # Doesn't effect the code ;
            # print("undescore : ", _)      # Doesn't effect the code ;

            for key,value in self.dargs.items():
                if(key in args):
                    args = args.replace(key,value)

            return func(args)

        return wrapper


@Abbreviation(abbr)
def message(msg):
    print(msg)


def example3():
    message("omg that's so funny. Anyways I gtg. ttyl okay.")


###---/EXAMPLE 3

##---Main Execution;;
def main(res=None):    
    example3()
    # example2()
    # example1()

   
if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")