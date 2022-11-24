'''
-------------------------------------------------------------------------------------
-> Title: Decorator
-> Attempted: 23/11/2022
-> Description: 
-------------------------------------------------------------------------------------
Decorator are extended functionality on the basic function. 

# decorator accepts a functions return a wrapper;

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
 
# ---------------------------EXAMPLE 1;
## Decorator accepts a functions return a wrapper;
## Simple Decorator;
def decorator(abc, "Sdfsdf"):
    # Wrapper can take argument directly from decorator;
    # Explcit : External function argument 
    # Decorator maker :
    def wrapper(xyz):
        return abc(xyz).upper()
    return wrapper


@decorator
def func(name):
    return "hello " + name

#-------------------------/EXAMPLE 1;

#-------------------------/EXAMPLE 2 : DECORATOR MAKER;
## General purpose Decorator with Decorator itself accepting arbitary arguments;;
## 1st Level Decorator;;
def decorator_maker(*args):  # decorator_kwargs: kwargs are coming from decorator main (@decorator_maker);
    ## Decorator works likes the main;
    def decorator_main(func):   # func : 
        ## Wrapper receives functional arguments from the main external function (employee_details);
        def wrapper(**kwargs):            
            print("-----------------------------------")
            print("****|Decorator Maker Arguments|****")
            print("-----------------------------------")
            for key,value in kwargs.items():
                print(f"{key} : {value}")
            print("-----------------------------------")
            for key,value in enumerate(args, start=1):
                print(f"Hobbies {key} : {value}")
            else:
                print("-----------------------------------")
                data = func(**kwargs)
                print(f"data : {data}")

        return wrapper          ## 2nd-level-decorator > wrapper;

    return decorator_main       ## /1st-level-decorator;


@decorator_maker("Crickets", "Badminton", "Football", "Volleyball")
def employee_details(**kwargs):
    return kwargs

#-------------------------/EXAMPLE 2 : DECORATOR MAKER;

#-------------------------/EXAMPLE 3 : SIMPLE DECORATOR;
def measure_time(function):
    #Measures time for execution
    print("func2")
    print(f"function-name: {function}")
    def wrapper(name):
        start = time.time()
        result = function(name)
        result = "Mr." + result
        print(f"result : {result}")
        end = time.time()
        print(f"Time taken : {end - start}")
        return result

    print(f"@return function 2")
    return wrapper

def do_twice(function):
    #Executes the function twice
    print("func1 : do_twice")
    def wrapper(name):
        print(f">>> name: {name}")
        return function(name).upper()

    print("@return function 1")
    return wrapper

@measure_time # <-- Decorator 1;
@do_twice # <-- Decorator 2 :--- do_twice(print_name)
def print_name(name):
  # print(f"My name is {name}")
  return f"My name is {name}"

#-------------------------/EXAMPLE 3 : SIMPLE DECORATOR;

##---Main Execution;;
def main(res=None):
    # print_name("Eleven")              # decorator 3 calling
    employee_details(                   # decorator 2 calling
        firstname="Neeraj", 
        middlename="Singh", 
        lastname="Junior", 
        std='XII'
    )
    # print(func("Neeraj", "url"))      # decorator 1 calling


###---Main Entry Point;
if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
