'''
Problem Description:
Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way.

Example 1:

Input:
LinkedList: 2->2->4->5
Output: 2 4 5
Explanation: In the given linked list 
2 ->2 -> 4-> 5, only 2 occurs more 
than 1 time.

Example 2:

Input:
LinkedList: 2->2->2->2->2
Output: 2
Explanation: In the given linked list 
2 ->2 ->2 ->2 ->2, 2 is the only element
and is repeated 5 times.
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
def removeDuplicates(head):
    # base case
    if not (head and head.next):
        return head

    # main case
    temp = None
    hashset = set()
    pNode = head                # pNode : previous node;
    cNode = head.next           # cNode : current node;
    while(cNode):
        if(pNode.data == cNode.data):
            temp = cNode
            pNode.next = cNode.next
        else:
            pNode = cNode
            
        cNode = cNode.next              # increment node;
        if temp != None: 
            del temp               # Delete temp
    
    return head


def main():
    try:
        res = ""
        print(res) if res else print("Empty!")
        
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
    