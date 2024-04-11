'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Reverse of Linked List using recursion
-> Problem Status: Completed
-> Problem Attempted: 27.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Reverse a Linked List, using the recursion approach only

Exmaple 1:
Input : 1 -> 2 -> 3
Output : 3 -> 2 -> 1

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import P000_Helpers as ll


###---Main Solution;;
def recReverse(head):
    if(head.next == None):
        return head

    revHead = recReverse(head.next)         # Reverse Head;;
    head.next.next = head
    head.next = None

    return revHead

 
###---ReverseV2 using Recursion;;
def recReverseV2(head,pre=None):
    if(head == None):
        return pre

    nex = head.next
    head.next = pre
    pre = head

    return recReverseV2(nex,pre)


##---Main Execution;;
def main():
    try:
        
        head = ll.createLinkedList(nodes=5, start=False)
        print("Before Reversing...")
        ll.printList(head)

        print("After Reversing...")
        # head = recReverse(head)               # Version 1;;
        head = recReverseV2(head)             # Version 2;;
        ll.printList(head)

        
    except(Exception) as e:
        print(f"Exception Traced : {e}")
    
    else:
        print("Program Completed : Success")

    finally:    
        print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    