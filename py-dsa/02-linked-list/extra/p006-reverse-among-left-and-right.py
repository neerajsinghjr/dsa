'''
-------------------------------------------------------------------------------------
-> Problem Title: 92. Reverse Linked List II
-> Problem Status: Completed
-> Problem Attempted: 25/12/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Problem:
https://leetcode.com/problems/reverse-linked-list-ii/

Reference:
https://www.youtube.com/watch?v=RF_M9tX4Eag

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
        self.val = value
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

    # Traversal of node;;
    def show(self):
        node = self.head
        if not node:
            print("[]", end=" ")
        while(node):
            print(node.val, end=" ")
            node = node.next
        print() # for new line;;
        
    # Return length of linked list
    def length(self, head=None):
        ll_len, ptr = 0, head
        ptr = self.head if not head else None
        while(ptr):
            ll_len += 1
            ptr = ptr.next

        return ll_len
    
    # Reverse linked list among left and right;;
    def reverseBetween(self, left, right):
        head = self.head
        if head and not head.next:
            return head
        
        return self.ansv1(head, left, right)

    def ansv1(self, head, left, right):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief:
        s1: find the start node pointing to the left of the linked list;
        s2: then reverse the list in-between the left and right;
        s3:
            - eg, 1 => [ 2 -> 3 -> 4 ] => 5
                ~ 1 => [ 4 -> 3 -> 2 ] => 5
            - attach the left-1 node to the end node of in-between reverse linked list
            - attach end node of reversed linked list to end of original list
        """
        # S1: We will find the node pointing to left index of the linked list;;
        dummy = Node(0, head)
        left_pre, cur = dummy, head
        for _ in range(left - 1):
            left_pre, cur = left_pre.next, cur.next

        # print(f"pre: {left_pre.val} // cur: {cur.val}")

        # S2: We will reverse the linked list between the left <= right;;
        pre_node = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = pre_node
            pre_node = cur
            cur = temp

        # print(f"s2: cur: {cur.val} // pre_node: {pre_node.val}")

        # S3: Reset the Parent links of linked list in-between left and right;;
        left_pre.next.next = cur
        left_pre.next = pre_node

        return dummy.next


##---Main Execution;;
def main(res=None):
    try:
        i = 0

        # Case 0: Basic Linked List;;
        ll = LinkedList(1)
        # head = [1,2,3,4,5], left = 2, right = 4
        items, left, right = [2,3,4,5,6], 2, 5
        for item in items:
            ll.append(item)
        print("Total Record :: ", ll.len)
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Delete Duplicates;;
        ll.head = ll.reverseBetween(left, right)
        print(f"Reverse nodes between left: {left} and right: {right}", end=" :: ")
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
    