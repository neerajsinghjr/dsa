'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Merge Two Sorted List
-> Problem Status: Completed
-> Problem Attempted: 28.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Merge two sorted linked list together, as one

Example 1:
Ipnut : list 1=[2,4,6] list2 = [1,3,5]
Output: [1,2,3,4,5,6]

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


## Merge With Extra Space;
def mergeList(list1,list2):

    dummy = ll.Node()
    head = dummy

    while(list1 and list2):
        if(list1.val < list2.val):
            dummy.next = list1
            list1,dummy = list1.next,dummy.next
        else:
            dummy.next = list2
            list2,dummy = list2.next,dummy.next

    if(list2 != None):
        dummy.next = list2
    if(list1 != None):
        dummy.next = list1

    return head.next


## Merge With only Stack Space;
def mergeListV2(list1,list2):
    if(list1 == None): return list2

    if(list2 == None): return list1

    dummy = ll.Node()

    if(list1.val < list2.val):
        dummy  = list1
        dummy.next = mergeListV2(list1.next, list2)
    else:
        dummy = list2
        dummy.next = mergeListV2(list1,list2.next)

    return dummy


### Merge Without Extra Space
def mergeListV3(list1,list2):
    head = ll.Node()
    dummy = head        
    
    while(list1 and list2):
        print(f"list1: {list1.val} | list2: {list2.val}")
        if(list1.val <= list2.val):
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next
        else:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next

    if(list1 or list2):
        dummy.next = list1 if(list1) else list2

    return head.next


###---Main Execution;;;
def main():
    try:
        list1 = ll.createList(start=1,end=7,fromLeft=False,even=True)
        ll.printList(list1)

        list2 = ll.createList(start=3,end=10,fromLeft=False,even=False)
        ll.printList(list2)

        # head = mergeList(list1, list2)
        # ll.printList(head)
        
        # head = mergeListV2(list1, list2)
        # ll.printList(head)

        head = mergeListV3(list1, list2)
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
    