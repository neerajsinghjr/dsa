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
# import Helpers.mHelpers.mTrie as Trie

# """
# Trie() : Create Trie Structure;
# """
# def Trie(words):
#     _end = "end"                # Delimiter
#     root = dict()               # Default dict()
#     for word in words:          # Words = ["bar","baz"] 
#         current = root
#         for letter in word:     # Word = ["b","a","r"]
#             current = current.setdefault(letter,{})
#         current[_end] = _end    # Terminator;
#     return root


# """
# find() : find inside Trie structure;
# """
# def find(root,word):
#     _end = "end"
#     for letter in word:
#         if(letter not in root[letter]):
#             return False
#         root = root[letter]
#     return _end in root[_end]


## Main Working Fun
def main():
    # try:
    data = ["apple","mango","banana","organge","grapes","guava"] 
    query = ["appy","apple,","mango","mangoes","organges"]

    trie = Trie(data)
    # trie = Trie.Trie(data)
    print(trie)

    print("Querying...")
    for q in query:
        # print(f"{q}:",Trie.find(trie,q))
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
    