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

###--- Main Solution;;
def midpoint(head):
    slow,fast = head,head.next
    while(fast and fast.next):
        slow,fast = slow.next,fast.next.next
    return slow


def mergesort(head):
    # base case
    if(head == None or head.next == None):
        return head

    # Tracing mid node
    node = midpoint(head)

    # Break at mid
    start = head
    mid = node.next
    node.next = None

    # Recursive methodology;
    start = mergesort(start)
    mid = mergesort(mid)

    return ll.mergeList(start,mid)
    # return ll.mergeListV2(start,mid)
    # return ll.mergeListV3(start,mid)


##---Main Execution;;
def main():
    # try:        
    head = ll.createRandomList(n=8,start=1,end=10000)
    ll.printList(head)

    node = mergesort(head)
    ll.printList(node)
        
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
    