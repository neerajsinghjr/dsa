#!/bin/python3

import os
import re
import sys
import time
import math
import random

def checkImport():
	print(f"filename: {__name__}")
	print('checkImport func')


##---Main Execution;;
def main():
	res = 0
	data = [1,2,2,1]
	l,r = 0,len(data)-1
	while(l <= r):
		if not(data[l] == data[r]):
		    break

		l,r = l+1,r-1

	else:
		res += 1

	print(f"res -> {res}")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    