'''
-------------------------------------------------------------------------------------
-> Problem Title: Insert
-> Problem Status: Completed
-> Problem Attempted: 05/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Remove Item in linked list

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

    # Insert value in list;;
    def remove(self, index):
        if self.len == 0:
            return 

        # Index Lower and Upper Bound Validation;;
        if not (index >= 0 and  index < self.len):
            raise ValueError("Incorrect Index Provided")

        if index == 0:
            self.pop_left()
        elif index == self.len-1:
            self.pop_right()
        else:
            cur_node = self.head
            pre_node = self.head

            while(index):
                pre_node = cur_node
                cur_node = cur_node.next
                index -= 1

            pre_node.next = cur_node.next
            cur_node.next = None

            self.len -= 1
            del cur_node

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
        print("Total Record :: ", ll.len)
        print("New Linked List", end=" :: ")
        ll.show()

        # Case 1: Remove Node;;
        ll.remove(index=8)
        print("Removed, Node(index=8)", end=" :: ")
        ll.show()
        ll.remove(index=0)
        print("Removed, Node(index=0)", end=" :: ")
        ll.show()
        last_idx = ll.len-1 
        ll.remove(index=last_idx)
        print(f"Removed, Node(index={last_idx})", end=" :: ")
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
    