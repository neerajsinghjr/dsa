'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Shuffle Arrya without helper
-> Problem Status: Completed
-> Problem Attempted: 02.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Shuffle the element of the array

Example 1:
Input: ["Abhi", "Badal", "Chetan", "Dharmesh", "Ekdant", "Farooq"]
Output: ['Dharmesh', 'Farooq', 'Farooq', 'Dharmesh', 'Farooq', 'Farooq']
Everytime output should be different

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math

from random import randint


###--- Main Solution;;
def shuffle(sample):
    if(len(sample) <= 1):
        return sample

    idxSet = set()          # To avoid same index again;;
    start,end = 0,len(sample)
    for i in range(start,end):
        randIndex = randint(start,(end-1)//2)
        if not(randIndex in idxSet):
            sample[randIndex],sample[i] = sample[i],sample[randIndex]
        else:
            while(True):
                randIndex = randint(start,end)
                if(randIndex in range(end) and randIndex not in idxSet):
                    break
            sample[randIndex],sample[i] = sample[i],sample[randIndex]

        idxSet.add(randIndex)           # Updating Idx Set;;

    return sample   


##---Main Execution;;
def main():
    # try:
    x = ["Abhi", "Badal", "Chetan", "Dharmesh", "Ekdant", "Farooq"]
    shuffle(x)
    print(f"res: {x}")
        
    # except(Exception) as e:
    #     print(f"Exception Traced : {e}")
    
    # else:
    #     print("Program Completed : Success")

    # finally:    
    #     print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    