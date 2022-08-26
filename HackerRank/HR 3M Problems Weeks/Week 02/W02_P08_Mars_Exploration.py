'''
Problem Description:
A space explorer's ship crashed on Mars! They send a series of 
SOS messages to Earth for help.

Letters in some of the SOS messages are altered by cosmic 
radiation during transmission. 

Given the signal received by Earth as a string, 'sos' , 
determine how many letters of the SOS message have been 
changed by radiation

#Example
sos = SOSTOT
The original message was SOSSOS. 
Two of the message's characters were changed in transit.

#Return
1) int: the number of letters changed during transmission
'''

#!/bin/python3

import string
import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def marsExplorationV2(sos):
    sos = sos.lower()
    size = len(sos)
    count,sosLen = 0,math.ceil(size//3)
    print("sosLen:",sosLen)
    for x in range(0,size,3):
        lo,hi = x, x+3              # iterator;
        split = sos[lo:hi]
        print("split:",split,"lo:hi:x",lo,":",hi,":",x)
        if "sos" != split:
            print("split neq:",split)
            for y in split:
                if y not in "sos":
                    count += 1
                    print("str:",y,"count:",count)
    print(count)              
    return count
    
    
def marsExploration(sos):
    count = 0
    for x in range(0,len(sos),3):
        if(sos[x] != "S"):   count += 1
        if(sos[x+1] != "O"): count += 1
        if(sos[x+2] != "S"): count += 1
    return count


def main():
    try:
        myStr = [
            "SOSTOTSOSTOT",                      
            "QWERTYUIOPLKJHGFDSAZXCVBNMQWERTYUIOPASDFGHJKL;POIUYTREWAZSXDFGHJKLMNBVCXZ",      
            "SOSQWENJKJSDJSOSSJDKFJSDKFSDSOSSDKFKSJDFKSDPSP"           
        ]
        for string in myStr:
            # res = marsExplorationV2(string)                                  ## Version 1
            res = marsExploration(string)                                    ## Version 2
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
    