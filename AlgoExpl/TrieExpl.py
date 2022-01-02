'''
Problem Description:
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from Helpers.mHelpers.mTrie import *


## Main Working Fun
def main():
    # try:
    data = ["apple","mango","banana","organge","grapes","guava"] 
    query = ["appy","apple,","mango","mangoes","organges"]

    trie = Trie(data)
    print(trie)

    print("Querying...")
    for q in query:
        print(f"{q}:",find(trie,q))

    print("End Reached...")
    
    # except(Exception) as e:
    #     print(f"Exception Traced: {e}")
    
    # else:
    #     print("Program Executed: Success")

    # finally:
    #     print("Program Terminated!")

        
if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    