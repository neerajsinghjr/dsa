'''
-------------------------------------------------------------------------------------
-> Problem Title: 92. Reverse Linked List II
-> Problem Status: Completed
-> Problem Attempted:
-> Problem Description: 
-------------------------------------------------------------------------------------

https://leetcode.com/problems/reverse-linked-list-ii/submissions/1102234708/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Node:

    # single node
    def __init__(self, value=0):
        self.val = value
        self.next = None


class LinkedList:
    
    # Constructor;;
    def __init__(self, value=0):
        node = Node(value)
        self.head = node
        self.tail = node
        self.len = 1

    # Append to list;;
    def append(self, value):
        if not self.head:
            # create new linked list;
            node = Node(value)
            self.head = node
            self.tail = node
            self.len = 1
        else:
            # append to the end of list;
            node = Node(value)
            self.tail.next = node
            self.tail = node
            self.len += 1

    # Traversal of node;;
    def show(self):
        node = self.head
        if not node:
            print("[]", end=" ")
        while(node):
            print(node.val, end=" ")
            node = node.next
        print() # for new line;;
        
    # Return length of linked list
    def length(self, head=None):
        ll_len, ptr = 0, head
        ptr = self.head if not head else None
        while(ptr):
            ll_len += 1
            ptr = ptr.next

        return ll_len
    
    # Reverse linked list among left and right;;
    def reverseBetween(self, left, right):
        head = self.head
        if head and not head.next:
            return head
        
        return self.ansv1(head, left, right)

    def ansv1(self, head, left, right):
        dummy = Node(0)
        dummy.next = head
        
        pre = dummy
        
        # iterate till left - 1 location;;
        for _ in range(left-1):
            pre = pre.next
        
        start = pre.next
        then = start.next
        
        for _ in range(right-left):
            # reversal link update;;
            start.next = then.next
            then.next = pre.next
            pre.next = then 
            # update then node ;;
            then = start.next
        
        return dummy.next


##---Main Execution;;
def main(res=None):
    try:
        i = 0

        # Case 0: Basic Linked List;;
        ll = LinkedList(1)
        # head = [1,2,3,4,5], left = 2, right = 4
        items, left, right = [2,3,4,5,6], 2, 5
        for item in items:
            ll.append(item)
        print("Total Record :: ", ll.len)
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Delete Duplicates;;
        ll.head = ll.reverseBetween(left, right)
        print(f"Reverse nodes between left: {left} and right: {right}", end=" :: ")
        ll.show()
        
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
    