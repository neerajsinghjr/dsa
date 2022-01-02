'''
Problem Description:
A teacher asks the class to open their books to a page number. 
A student can either start turning pages from the front of the 
book or from the back of the book. They always turn pages one 
at a time. When they open the book, page 1 is always on the 
right side

When they flip page 1, they see pages 2 and 3. Each page except 
the last page will always be printed on both sides. The last page
may only be printed on the front, given the length of the book. 

If the book is  pages long, and a student wants to turn to page, 
what is the minimum number of pages to turn? They can start at 
the beginning or the end of the book.

Given 'n' and 'p', find and print the minimum number of pages that 
must be turned in order to arrive at page 'p'

Example:
n = 5
p = 3

Return: 1
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...
def pageCount(n,p):
    return min((n//2)-(p//2),(p//2))


def main():
    try:
        data = []                                   # ~ data
        res = ""                                    # ~ func
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    