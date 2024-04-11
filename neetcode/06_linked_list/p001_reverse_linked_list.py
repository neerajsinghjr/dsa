'''
-------------------------------------------------------------------------------------
-> Problem Title: 206. Reverse Linked List
-> Problem Status: Completed
-> Problem Attempted: 20/11/2023
-> Problem Description:
-------------------------------------------------------------------------------------

Refer: https://leetcode.com/problems/reverse-linked-list/description/

-------------------------------------------------------------------------------------
'''

# !/bin/python3

import os
import re
import sys
import time
import math
import random


class ListNode:

    # single node
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedList:

    # Constructor;;
    def __init__(self, val=0):
        node = ListNode(val)
        self.head = node
        self.tail = node
        self.len = 1

    # Append to list;;
    def append(self, value):
        if not self.head:
            # create new linked list;
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.len = 1
        else:
            # append to the end of list;
            node = ListNode(value)
            self.tail.next = node
            self.tail = node
            self.len += 1

    # traversal of node;;
    def show(self):
        node = self.head
        if not node:
            print("[]", end=" ")
        while (node):
            print(node.val, end=" ")
            node = node.next
        print()  # for new line;;

    # reverse linked list;;
    def reverseList(self, head=None):
        head = self.head
        if not (head and head.next):
            return head

        return self.ansv1(head)

    def ansv1(self, head):
        """
        run: accepted
        time: o(n)
        space: o(1)
        brief: set the current node link backwards one by one.
        """
        pre_node = None

        while(head):
            nex_node = head.next
            head.next = pre_node
            pre_node = head
            head = nex_node

        return pre_node



##---Main Execution;;
def main(res=None):
    try:
        # Case 0: Basic Linked List;;
        ll = LinkedList(1)
        items = [2, 3, 3, 4, 4, 5]
        for item in items:
            ll.append(item)
        print("Total Record :: ", ll.len)
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Delete Duplicates;;
        ll.head = ll.reverseList()
        print("Non-Duplicated Linked List", end=" :: ")
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
    print("Run Time:", endTime - startTime, "ms")
    print("#------------ Code Stop ----------------#")
