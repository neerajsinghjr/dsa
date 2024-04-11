'''
-------------------------------------------------------------------------------------
-> Problem Title: Insert
-> Problem Status: Completed
-> Problem Attempted: 05/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Reverse Item in linked list

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
    def __init__(self, value=None):
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

    # Insert value in list;;
    def reverse(self):
        # NOTE: Need to reverse the 
        # head and tail as well;;
        cur_node = self.head
        self.head = self.tail
        self.tail = cur_node

        pre_node = None
        nex_node = self.head

        while(cur_node):
            # s1: backup next node;;
            nex_node = cur_node.next
            # s2: link backward cur node;;
            cur_node.next = pre_node
            # s3: update previous node;
            pre_node = cur_node
            # s4: update cur_node with nex_node;;
            cur_node = nex_node

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
        print("Forward", end=" :: ")
        ll.show()

        # Case 1: Set Node;;
        node = ll.reverse()
        print("Backward", end=" :: ")
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
    