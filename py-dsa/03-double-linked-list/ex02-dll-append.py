'''
-------------------------------------------------------------------------------------
-> Problem Title: DLL Append
-> Problem Status: Completed
-> Problem Attempted: 28/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

Appending Functionality in DoubleLinkedList;;
Operation : O(1)

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


##---Main Execution;;
def main(res=None):
    try:
        ddl = DoubleLinkedList(1)
        items = [2,3,4,5,6]
        for item in items:
            ddl.append(item)
        print("Forward DLL List", end=' :: ')
        ddl.show()
        print("Reverse DLL List", end=' :: ')
        ddl.show(forward=False)


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
    print("Run Time:", endTime - startTime, "ms")
    print("#------------ Code Stop ----------------#")
