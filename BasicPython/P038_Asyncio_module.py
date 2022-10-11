#!/bin/python3

import os
import re
import sys
import time
import math
import random
import asyncio


# example 1
async def cor1():
   print("cor1 start...")
   for x in range(10):
      await asyncio.sleep(2)
      cor2()
      print(f"cor1: {x}")
   print("cor1 -> end")


async def cor2():
   print("cor2 start ...")
   for y in range(5):
      await asyncio.sleep(1)
      print(f"cor2: {y}")
   print("cor2 -> end")
   
   
# example 2



async def main():
   pass
   


##---Main Execution;;
def main():
   
   
   # example 1 
   loop = asyncio.get_event_loop()
   loop.run_until_complete(cor1())
   # loop.run_until_complete(cor2())
   

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    