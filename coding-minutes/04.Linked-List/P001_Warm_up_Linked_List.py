'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Create/Read/Update/Delete Operation in Linked List
-> Problem Status: Completed
-> Problem Attempted: 15.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You asked for creating a linked list for CRUD operation,
    1 -> 2 -> 3 -> 4 -> NONE
Every node points to the next node of the list. 

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###---Node Class;;
class Node:
    
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


###---Insert node at Start Of Linked List;;
def intsertAtStart(head,val=None) -> None:
    if(val != None):
        node = Node(val)        
        node.next = head
        head.next = node

    return


###---Insert node at the end of Linked List;;
def insertAtEnd(head,val=None):
    if(val != None):
        if(head == None):
            head.next = Node(val)
        else:
            while(head.next != None):
                head = head.next
            head.next = Node(val)
    return 


###---Print Linked List;;
def printList(head):
    while(head != None):
        marker = "->" if(head.next != None) else ""
        print(head.val,marker,end=" ")
        head = head.next
    print("-> NULL")
    return 


##---Main Execution;;
def main():
    try:
        head = Node(1)
        
        for i in range(2,10):
            insertAtEnd(head,val=i)

        printList(head)

        print("End")
        
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
    