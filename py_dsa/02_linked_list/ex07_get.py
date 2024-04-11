'''
-------------------------------------------------------------------------------------
-> Problem Title: Get
-> Problem Status: Completed
-> Problem Attempted: 05/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Get IteM from linked list

TIME COMPLEXITY : O(n)

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

    # Get from list;
    def get(self, index):
        if self.len == 0:
            return 

        # Index Lower and Upper Bound Validation;;
        if not (index >= 0 and  index < self.len):
            raise ValueError("Incorrect Index Provided")

        ptr = self.head
        while(index):
            ptr = ptr.next
            index -= 1

        return ptr


##---Main Execution;;
def main(res=None):
    try:
        i = 0

        # Case 0: Basic Linked List;;
        ll = LinkedList(10)
        items = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        for item in items:
            ll.append(item)
        print("Total Record :: ", ll.len)
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Get Node;;
        node = ll.get(index=8)
        value = node.value if node else None
        print(f"Node(index=8): {value}")
        node = ll.get(index=0)
        value = node.value if node else None
        print(f"Node(index=0): {value}")


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
    