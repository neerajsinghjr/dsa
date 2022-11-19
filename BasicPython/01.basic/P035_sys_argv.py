#!/bin/python3

import sys
import dis


def fib(n):
   if n <= 2: 
      return 1
   return fib(n-1) + fib(n-2)


if __name__ == '__main__':

   """
   dis called disassember used to show the byte code of the function;
   """
   print("#1 :-", dis.dis(fib))

   """
   """
   print("#2 :-", dis(fib.__code__))

   """
   """
   print("#3 :-", dill.)

   """
   sys.argv attribute is used to list the arguments given by the command
   line argument;
   """
   args = sys.argv
   if(len(args) > 1):
      for arg in args:
         print(f"arg: {arg}")
   else:
      print(f"No argument found!")

   print("end...")
    
    