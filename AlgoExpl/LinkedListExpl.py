#!/bin/python3

import re
import os
import sys
import math
import time
import random
from Helpers.LinkedList import *

# Main Working Function, Here...
def main():
    try:

        list  = LinkedList()                

        # ## Pushing at Last eg, A -> B -> C -> D -> E
        # list.pushBack("Adam")
        # list.pushBack("Branda")
        # list.pushBack("Camelio")
        # list.pushBack("Dominoz")

        ## Pushing @ Front eg, A <- B <- C <- D <- E
        list.pushFront("Adam")
        list.pushFront("Branda")
        list.pushFront("Camelio")
        list.pushFront("Dominoz")
        list.pushFront("Erenster")
        list.pushFront("Ferero")
        list.pushFront("Gosepho")
        list.pushFront("Hercules")
        list.pushFront("Iglesius")

        # ## Before
        # print("Before Reverse :",end = " ")
        # list.show()
        # ## Reverse List
        # list.reverse()
        # ## After
        # print("After Reverse :",end = " ")
        # list.show()
        
        # print(len(list))

        # ## Before 
        # print("Before Popping :",end = " ")
        # list.show()
        # ## Pop Last Element;
        # list.pop()
        # ## After
        # print("After Popping :",end = " ")
        # list.show()

        ## Before
        print(f"List Before ({len(list)}) : ", end = " ")
        list.show()
        ## Remove Index Element
        index = 10
        print(f"Remove Index : {index}")
        list.remove(index)
        ## After
        print(f"List After ({len(list)}) :",end = " ")
        list.show()

    except(Exception) as e:
        print(f"\nException Traced: {e}")
    
    else:
        print(f"\nProgram Executed: Success")

    finally:
        print(f"Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    