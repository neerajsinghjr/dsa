'''
-------------------------------------------------------------------------------------
-> Problem Title: DLL Constructor
-> Problem Status: Completed
-> Problem Attempted: 28/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

DoubleLinkedList constructor initialization;;

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

    def show(self):
        node = self.head
        while(node):
            print(node.val, end=" ")
            node = node.next
        print()


##---Main Execution;;
def main(res=None):
    try:
        ddl = DoubleLinkedList(1)
        ddl.show()


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
