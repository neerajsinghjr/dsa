'''
-------------------------------------------------------------------------------------
-> Problem Title: Parition list
-> Problem Status: Completed
-> Problem Attempted: 19/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://leetcode.com/problems/partition-list/

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
        self.value = value
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

    # traversal of node;;
    def show(self, head=None):
        node = head if head else self.head
        while(node):
            print(node.value, end=" ")
            node = node.next
        print() # for new line;;

    # parition list
    def partition(self, target):
        """
        run: accepted
        time: o(n)
        space: o(1)
        brief: simple parition the list in two
        1) node lesser than target
        2) node not lesser than targe
        then attache list_1 -> list_2
        """
        s_node = Node()
        l_node = Node()
        s_ptr = s_node
        l_ptr = l_node
        node = self.head

        while(node):
            if node.value < target:
                s_node.next = node
                s_node = s_node.next
            else:
                l_node.next = node
                l_node = l_node.next
            node = node.next
        
        s_node.next = l_ptr.next
        l_node.next = None
    
        return s_ptr.next


##---Main Execution;;
def main(res=None):
    try:
        i = 0

        # Case 0: Basic Linked List;;
        ll = LinkedList(1)
        items = [4,3,2,5,2]
        for item in items:
            ll.append(item)
        print("Total Record :: ", ll.len)
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Partition list;;
        new_head = ll.partition(3)
        ll.show(new_head)
        
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
    
    