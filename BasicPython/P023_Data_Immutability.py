#!/bin/python3

import os
import re
import sys
import time
import math
import random


# ## Global Variablep;;
# friendsLastSeen = {
#     'Rolf': 31,
#     'Jenna': 1,
#     'Anne': 7
# }   

x = 10

def checkInteger(x):
    print(f"func:x: {id(x)}")


def seeFriend(friends, friend):
    print(f"func:friends : {id(friends)}")
    print(f"func:Jenna : {id(friends['Jenna'])}")


def increament (xy):
    print(f"func:xy: {id(xy)}")
    xy += 1
    print(f"func:xy: {id(xy)}")



"""
integer, stirng, float, number, tuple - immutable 

list, dict, set - mutable
"""
def main():

    ages = [14,10,12,15]

    print(f"bf:ages: {id(ages)}")

    # In background, uses list.__iadd__(self) and this only modifies exisintng array that's why memory location not changed.
    # ages += [20,20]     

    # In background, uses list.__add__(self) and this one change the memory location because return a new list even if new values already exist.        
    # ages = ages + [20,20]

    # this also returned the new list
    ages = [14,10,12,15] + [20,20]

    print(f"af:ages: {id(ages)}")


    # print(f"id: {id(x)}")           # global;

    # increament(x)                   # global

    # print(f"id: {id(x)}")           # global;


    # friendsLastSeen = {
    #     'Rolf': 31,
    #     'Jenna': 1,
    #     'Anne': 7
    # }

    # print(f"main:friends : {id(friendsLastSeen)}")

    # print(f"bf:main:Jenna : {id(friendsLastSeen['Jenna'])}")

    # seeFriend(friendsLastSeen, "Jenna")

    # print(f"af:main:Jenna -> {id(friendsLastSeen['Jenna'])}")

    # print(f"main:x: {id(x)}")

    # checkInteger(x=10)               # Same Id;

    # checkInteger(x=11)               # Not Same Id;



if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    