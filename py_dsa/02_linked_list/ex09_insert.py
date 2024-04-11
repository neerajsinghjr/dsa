'''
-------------------------------------------------------------------------------------
-> Problem Title: Insert
-> Problem Status: Completed
-> Problem Attempted: 05/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Insert Item in linked list

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

    # Traversal of node;;
    def show(self):
        node = self.head
        while(node):
            print(node.value, end=" ")
            node = node.next
        print() # for new line;;

    # Get from list;;
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

    # Set value in list;;
    def set(self, index, value):
        try:
            node = self.get(index=index)
            if node:
                node.value = value
            return 
        except Exception as ex:
            return ex

    # Insert value in list;;
    def insert(self, index, value):
        if self.len == 0:
            return 

        # Index Lower and Upper Bound Validation;;
        if not (index >= 0 and  index < self.len):
            raise ValueError("Incorrect Index Provided")
        
        if index == 0:
            return self.prepend(value)
        elif index == self.len-1:
            return self.append(value)
        else:
            cur_node = self.head
            pre_node = self.head

            # Iterating list;;
            while(index):
                pre_node = cur_node
                cur_node = cur_node.next
                index -= 1

            # Update the node;;
            new_node = Node(value)
            pre_node.next = new_node
            new_node.next = cur_node
            self.len = self.len + 1    
        
        return True


##---Main Execution;;
def main(res=None):
    try:
        i = 0

        # Case 0: Basic Linked List;;
        ll = LinkedList(10)
        items = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        for item in items:
            ll.append(item)
        print(f"Total Record: {ll.len}, Indices: {ll.len-1}")
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Set Node;;
        ll.insert(index=8, value=28)
        print("Node(index=8, Inserted=21)", end=" :: ")
        ll.show()
        ll.insert(index=0, value=21)
        print("Node(index=0, Inserted=22)", end=" :: ")
        ll.show()
        last_idx = ll.len-1 
        ll.insert(index=last_idx, value=30)
        print(f"Node(index={last_idx}, Inserted=30)", end=" :: ")
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
    