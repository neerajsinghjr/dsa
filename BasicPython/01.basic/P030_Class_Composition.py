#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Bookshelf:

   def __init__(self, *books):
      print(books)
      self.books = books

   def __str__(self):
      return f"Bookshelf with {len(self.books)} books"

   def getBooks(self):
      for book in self.books:
         print(f"book: {book.name}")


class Book:

   def __init__(self, name):
      self.name = name

   def __str__(self):
      return f"Book {self.name}"



##---Main Execution;;
def main():
   book1 = Book("Harry Potter The Philosopher Stone")
   book2 = Book("Harry Potter The Prisioner of Akzaban")
   shelf = Bookshelf(book1, book2)

   print(shelf)
   print(shelf.getBooks())

   print(sys.path)


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    