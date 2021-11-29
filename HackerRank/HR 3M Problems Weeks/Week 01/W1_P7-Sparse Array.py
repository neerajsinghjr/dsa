'''
Problem:
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings.
Return an array of the results.
Example:
strings = ['ab','ba','abc']
queries = ['ab','abc','bc']
There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. 
For each query, add an element to the return array, 
'''

#!/bin/python3

import math
import os
import random
import re
import sys


## Main Working Function
def matchingStrings(strings, queries):
    # Write your code here
    res = []
    for q in queries:
        count = 0
        print("q: ",q)
        for s in strings:
            print("s: ",s)
            if s == q:
                count += 1
                print("s == q,count:",s,q,count)
        res.append(count)
    return res

def main():
    res = ""
    print(res) if res else print("Empty!")
        

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    