'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Add Middle of the Linked List;;
-> Problem Status: Completed
-> Problem Attempted: 15.02.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Insert a new node in the mid of the linked list

Example 1:
Head : 1->2->3
Node : 4
Output : 1->4->2->3


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


##---Return length of the linked list;;
def getLength(head):
    count = 0
    while(head != None):
        head = head.next
        count += 1

    return count


###---Insert node the mid of the Linked List;;
def insertAtMid(head,val):
    n = getLength(head)

    if(n == 0):
        head.next = ll.Node(val)
    else:
        pre = None
        cur = head
        limit = n//2

        for _ in range(limit):
            pre,cur  = cur,cur.next

        node = ll.Node(val)
        pre.next = node
        node.next = cur

    return head


##---Main Execution;;
def main():
    try:
        head = ll.Node(1)       # ~ data

        for x in range(2,12):
            ll.insertAtEnd(head,x)
        
        ll.printList(head)

        newNode = int(input("New Node: "))

        print(f"Enter New Mid Node: {newNode}")

        insertAtMid(head,newNode)

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
    