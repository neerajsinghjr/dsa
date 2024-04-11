'''
-------------------------------------------------------------------------------------
-> Problem Title: Pop From Start
-> Problem Status: Completed
-> Problem Attempted: 04/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Pop Item From Left or Start

Popping from Left: O(1)

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

    # Prepend to linked list;;
    def prepend(self, value):
        node = Node(value)
        if self.len == 0 or not self.head:
            self.head = node
            self.tail = node
            self.len += 1
        else:
            node.next = self.head
            self.head = node
            self.len += 1

    # Popping from left;;
    def pop_left(self):
        if self.len == 0 or not self.head:
            return 

        temp = self.head 
        self.head = self.head.next
        self.len -= 1

        # NOTE: Remove the next pointer 
        # if you're not deleting this node. 
        temp.next = None

        # Reset Head & Tail if required;;
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

        # Case 1: Popping from end x 2;;
        ll.pop_left()
        print("Pop Left", end=" :: ")
        ll.show()
        ll.pop_left()
        print("Pop Left", end=" :: ")
        ll.show()
        ll.pop_left()
        print("Pop Left", end=" :: ")
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
    