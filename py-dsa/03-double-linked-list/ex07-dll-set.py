'''
-------------------------------------------------------------------------------------
-> Problem Title: DLL Set
-> Problem Status: Completed
-> Problem Attempted: 28/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

Set Functionality in DoubleLinkedList;;
Operation : O(N)

-------------------------------------------------------------------------------------
'''

# !/bin/python3

import os
import re
import sys
import time
import math
import random


class Node:
    """
    Node class represent single node
        - value represent the data
        - next represent next node
        - prev represent prev node
    """
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    """
    DoublyLinkedList class will manage a list of chain of
    nodes(which are independently created) with double
    pointer functionality.
        - head pointer points to start of list
        - tail pointer points to end of the list
        - total_length will manage number of nodes
    """
    def __init__(self, val=0):
        node = Node(val=val)
        self.head = node
        self.tail = node
        self.length = 1

    def show(self, forward=True):
        """ Show the elements of DLL """
        node = self.head \
            if forward else self.tail
        while(node):
            print(node.val, end=" ")
            node = node.next \
                if forward else node.prev
        print()
        return

    def append(self, val):
        """ Append elements of DLL """
        node = Node(val)
        if not self.head:
            # when list have nothing;;
            self.head = node
            self.tail = node
        else:
            #  setup next and prev
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return

    def pop(self):
        # Target node needs to delete;;
        node = self.tail

        # Base Case for single pointer only;;
        if not(self.head and self.head.next):
            self.head, self.tail = None, None
            self.length = 0
            return node

        # Update the previous node next pointer;;
        pre_node = self.tail.prev
        pre_node.next = None
        node.next = None
        node.prev = None
        self.tail = pre_node
        self.length -= 1
        return node

    def prepend(self, val):
        if not self.head:
            self.append(self, val)
        else:
            node = Node(val=val)
            node.next = self.head
            self.head = node
            self.length += 1
        return

    def popleft(self):
        node = self.head
        if not(node and node.next):
            self.head.next = None
            self.tail.next = None
            self.length = 0
        else:
            nex_node = node.next
            nex_node.prev = None
            self.head = nex_node
            self.length -= 1

        return node

    def get(self, index):
        if not(index < self.length):
            raise ValueError("List Index Out of Range")
        if index == 0:
            return self.head
        if index == self.length-1:
            return self.tail

        node = self.head
        while(index):
            node = node.next
            index = index - 1
        return node

    def set(self, index, val):
        if not(index < self.length):
            raise ValueError("List Index out of Range")
        if index == 0:
            self.head.val = index
        elif index == self.length-1:
            self.tail.val = index
        else:
            node = self.head
            while(index):
                node = node.next
                index = index - 1
            node.val = val
        return node


##---Main Execution;;
def main(res=None):
    try:
        # S01: Constructor Initialization DLL;;
        dll = DoubleLinkedList(0)
        # S02: Appending Items DLL;;
        items = [1,2,3,4,5,6]
        for item in items:
            dll.append(item)
        # S03: Displaying Items DLL;;
        print("DLL Length: ", dll.length)
        print("Forward DLL List", end=' :: ')
        dll.show()
        print("Reverse DLL List", end=' :: ')
        dll.show(forward=False)
        # S04: Set Index of DLL;;
        val, index = 10, 5 # Real Life index is index+1
        print(f"Modify: Index: {index} with {val}")
        print(f"Doubly Linked List", end=" :: ")
        dll.show()

    except(Exception) as e:
        import traceback
        print(f"Exception Traced : {traceback.format_exc()}")

    else:
        print("Program Completed : Success")

    finally:
        print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:", endTime - startTime, "ms")
    print("#------------ Code Stop ----------------#")
