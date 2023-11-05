'''
-------------------------------------------------------------------------------------
-> Problem Title: Set
-> Problem Status: Completed
-> Problem Attempted: 05/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Set Item in linked list

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

    # Set value in list;;
    # def set(self, index, value):
    #     """
    #     Writing the whole code snippet again is bad approach. 
    #     I have killed the purpose of Re-Usability in this approach.
    #
    #     Instead what i should do is, 
    #     1) Main set() function call
    #     2) Inside the set(), get() function called which fetch node
    #     3) Then set(), function only update the value if everythink ok.
    #     """
    #     if self.len == 0:
    #         return 
    #
    #     # Index Lower and Upper Bound Validation;;
    #     if not(index >= 0 and index < self.len):
    #         raise ValueError("ValueError: Index not correct")
    #
    #     ptr = self.head
    #     while(index):
    #         ptr = ptr.next
    #         index -= 1
    #     ptr.value = value


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

        # Case 1: Set Node;;
        node = ll.set(index=8, value=21)
        print("Node(index=8,Updated=21)", end=" :: ")
        ll.show()
        node = ll.set(index=0, value=22)
        print("Node(index=0, Updated=22)", end=" :: ")
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
    