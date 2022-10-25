#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Book:
    
    def __init__(self, name=None, author=None):
        self.name = name
        self.author = author

    @property
    def author(self):
        return self.author if(self.author) else "NA"

    @author.setter
    def author(self, author):
        if not(author):
            return
        self.author = author 
        
        
##---Main Execution;;
def main():
   book = Book("Murder on Orient Express", "Agatha Christie")
   print(book.author)
#   book2 = Book("Harry Potter")



if __name__ == '__main__':
    print("#------------ Code Start ---------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    