'''
-------------------------------------------------------------------------------------
-> Problem Title: 82. Remove Duplicates from Sorted List II
-> Problem Status: Completed
-> Problem Attempted: 19/11/2023
-> Problem Description:
-------------------------------------------------------------------------------------

Problem
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

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

    # traversal of node;;
    def show(self):
        node = self.head
        if not node:
            print("[]", end=" ")
        while(node):
            print(node.val, end=" ")
            node = node.next
        print() # for new line;;

    # delete duplicates from linked list;;
    def deleteDuplicates(self):
        head = self.head

        if not head:
            return head

        return self.ansv1(head)
        # return self.ansv2(head)

    def ansv2(self, head):
        """
        run: accepted;;
        """
        dummy = Node(0)
        dummy.next = head

        # default, we will start from dummy node;;
        pre_node = dummy

        while(head):
            if head.next != None and head.val == head.next.val:
                # skipped the duplicated values;;
                while(head.next != None and head.val == head.next.val):
                    head = head.next
                # we are only updating the link of pre_node here with cur_node here
                # then in the else block we will modify the pre_node actual value;;
                pre_node.next = head.next
            else:
                # we are updating the previous node here only;;
                pre_node = pre_node.next

            # traversing to the next head node;;
            head = head.next

        return dummy.next

    def ansv1(self, head):
        """
        run: rejected;;
        """
        dummy = Node(0)  # -101 to avoid node value discrepancy;;

        pre_node = dummy
        cur_node = head
        nex_node = head.next

        while(cur_node and nex_node):
            if cur_node and nex_node and cur_node.val == nex_node.val:
                if not nex_node:
                    cur_node = None
                    nex_node = None
                else:
                    cur_node = nex_node.next
                    nex_node = nex_node.next.next
            else:
                # update the link;;
                pre_node.next = cur_node
                cur_node = cur_node.next
                nex_node = nex_node.next
                pre_node = pre_node.next

        return dummy.next


##---Main Execution;;
def main(res=None):
    try:
        i = 0

        # Case 0: Basic Linked List;;
        ll = LinkedList(1)
        # solution: 1,2,5 // 1,2,3,5
        items = [2,3,3,4,4,5]
        # solution: 2 // []
        # items = [1,2,3,3,4,4,5,5]
        # solution: [] // []
        # items = [1,2,2,3,3,4,4,5,5]
        for item in items:
            ll.append(item)
        print("Total Record :: ", ll.len)
        print("Linked List", end=" :: ")
        ll.show()

        # Case 1: Delete Duplicates;;
        ll.head = ll.deleteDuplicates()
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
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
