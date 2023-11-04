'''
-------------------------------------------------------------------------------------
-> Problem Title: 
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description: 
-------------------------------------------------------------------------------------

Popping item 

Popping item means removing item from the linkedlist.

Popping from the anywhere: O(n)

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
    def pop(self, index=None):
        # check of null head;;
        if not self.head:
            return None

        # check for single element only;;
        if not (self.head and self.head.next):
            return None

        # check for index upper bound;;
        if index and index > self.len:
            raise ValueError("List index out of range")

        i = 0
        ptr = self.head
        index = index if index != None else self.len-1
        is_tail = True if index == self.len-1 else False
        
        if index == 0 and index == self.len-1:
            # 0th index removal directly
            temp = self.head
            self.head = ptr.next
        else:
            while(i < index-1):
                ptr = ptr.next
                i += 1
            # node removal;;
            temp = ptr.next
            ptr.next = ptr.next.next

        if is_tail:
            # Tail will update only if the 
            # index is the end of the list;;
            self.tail = ptr

        del temp        # delete node;
        self.len -= 1   # update length;


##---Main Execution;;
def main(res=None):
    try:
        i = 0

        # Basic Linked List Operation;;
        ll = LinkedList(1)
        items = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        for item in items:
            ll.append(item)
        print("Total Record :: ", ll.len)
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Popping from end x 2;;
        ll.pop()
        print("Popping From Last", end=" :: ")
        ll.show()
        ll.pop()
        print("Popping From Last", end=" :: ")
        ll.show()

        # Case 2: Popping with specifc index;
        ll.pop(4)
        print("4th Index Poppin: ", end=" :: ")
        ll.show()
        ll.pop(0)
        print("0th Index Popping", end=" :: ")
        ll.show()

        # ll.pop(10)
        # print("Popping", end=" :: ")
        # ll.show()
        
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
    