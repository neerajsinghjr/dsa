'''
----------------------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description: 
----------------------------------------------------------------------------------------------------
...

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


# Code: Brute Force | T:(N) | S:(1)
def getMiddleNode(head):
    count = ll.getLength(head)
    if(count%2 == 0):
        limit = count//2-1
    else:
        limit = count//2

    for _ in range(limit):
        head = head.next

    return head


# Code: Slow & Fast | T:(N) | S:(1);
def getMiddleNodeV2(head):
    slow,fast = head,head

    while(fast != None):
        if(fast.next == None):
            break

        slow = slow.next
        fast = fast.next.next

    return slow


##---Main Execution;;
def main():
    # try:
    head = ll.createList(start=1,end=5)
    ll.printList(head)

    # node = getMiddleNode(head)
    # print(node.val) if(node) else print("Empty!!!")

    node = getMiddleNodeV2(head)
    print(node.val) if(node) else print("Empty!!!")  

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
    