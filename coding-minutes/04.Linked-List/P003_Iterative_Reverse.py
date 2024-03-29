'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Reverse of Linked List
-> Problem Status: Ongoing...
-> Problem Attempted: 26.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Reverse a Linked List...

Example 1:
Input: 1 -> 2 -> 3
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



###--- Main Solution;;
def itrReverse(head):

    if(head == None):
        return head

    if(head.next == None):
        return head

    pre,cur = None,head

    while(cur != None):
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex

    return pre


##---Main Execution;;
def main():

    try:
        head = ll.createLinkedList(start=False)
        
        print("Before...")
        ll.printList(head)

        print("After...")
        head = itrReverse(head)
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
    
