'''
-------------------------------------------------------------------------------------
-> Title: Pandas Python Library
-> Attempted: 2024-03-09
-> Description:
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
'''
from time import time
from csv import DictReader, DictWriter
import pandas as pd


##---Main Execution;;
def main():
    file = '/Users/neeraj/Downloads/investments.csv'
    with open(file, 'rb') as obj:
        print()


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")