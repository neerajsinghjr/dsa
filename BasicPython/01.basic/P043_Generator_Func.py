'''
-------------------------------------------------------------------------------------
-> Title: Generator Func
-> Attempted: 26/11/2022
-> Description: 
-------------------------------------------------------------------------------------
Generator Function in Python :- Generator are statefull function means they
maintain their states while executing itself. States are maintainted using
the yield keyword. 

Yield is like return keyword but the difference is that yield only pause the
current execution of the program whearease return keyword stop the execution
and return the function control back to function who called it.

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###---- Example 1 : Basic Example for the Generator object;
def orderFood():
    yield 'Red Wine'

    yield 'Fish and Rice'

    yield 'Ice Cream'

def example1():
    serving = orderFood()

    print("__main__ :", serving)
    print("Starters : ", next(serving))
    print("Main Course: ", next(serving))
    print("Desserts :", next(serving))

###---/Example 1;

###---Example 2: Fibonacci Series using the Generator Object;
def fibo(a=0, b=1, limit=10):
    a = 0
    yield(a)
    b = 1
    yield(b)
    for _ in range(limit):
        c = a+b 
        yield(c)
        a,b = b,c

def example2():
    a,b,limit = 0,1,10
    fib = fibo(a,b,limit)        
    print("Generator Initiated ")
    print("Object __main__ :", fib)
    for k in range(limit):
        print(next(fib), end="")
        if not(k == limit-1):
            print("->", end="")
    print('\nGenrator Terminated !')

###--- /Example2;

##--- Example 3: Calculate first N prime number default limit 10;
def checkPrimeNumber(num):
    for x in range(2, num//2):
        if(num % x == 0):
            return False
    return True


def primeGenerator(count):
    i = 2           # number 0 and 1 are not prime number;
    cur_count = 0
    while(i and cur_count<=count):
        if(checkPrimeNumber(i)):
            yield(i)
            cur_count += 1
        i += 1


def example3():
    count = 10
    nextPrimeNumber = primeGenerator(count)
    print("Generator Initialized...")
    print("Object __main__ : ", nextPrimeNumber)
    for _ in range(count):
        print("Next Prime Number : ", next(nextPrimeNumber))
    print("\nGenerator Terminated !")



##---Main Execution;;
def main(res=None):
    try:
        example3()
        # example2()
    	# example1()

        
    except(Exception) as e:
        print(f"Exception Traced : {e}")
    
    else:
        print("Program Completed : Success")

    finally:    
        print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
