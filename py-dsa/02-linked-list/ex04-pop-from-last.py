'''
-------------------------------------------------------------------------------------
-> Problem Title: Pop From Last
-> Problem Status: Completed
-> Problem Attempted: 04/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

#-------------- INSTRUCTOR VERSION ---------------------#

Pop from Last or Right 

Popping item means removing item from the linkedlist.

Popping from Right: O(n)

NOTE: Poppping from the end will O(1) only in the case of double ended queue
because in that case deque will have a reverse pointer as well.

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
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    
    # Constructor;;
    def __init__(self, value):
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

    # traversal of node;;
    def show(self):
        node = self.head
        while(node):
            print(node.value, end=" ")
            node = node.next
        print() # for new line;;

    # Popping from list;;
    def pop_right(self, index=None):
        if self.len == 0:
            return

        # Popv2: Using two variable to map the pre_node 
        temp = self.head
        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.len -= 1
        
        # Reset the pointer if the list is null;;
        if self.len == 0:
            self.head = None
            self.tail = None

        return temp


##---Main Execution;;
def main(res=None):
    try:
        i = 0

        # Case 0: Basic Linked List;;
        ll = LinkedList(1)
        items = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        for item in items:
            ll.append(item)
        print("Total Record :: ", ll.len)
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Popping from the right;;
        ll.pop_right()
        print("Pop Right", end=" :: ")
        ll.show()
        ll.pop_right()
        print("Pop Right", end=" :: ")
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
    