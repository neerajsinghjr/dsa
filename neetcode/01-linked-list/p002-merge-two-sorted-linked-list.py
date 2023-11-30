'''
-------------------------------------------------------------------------------------
-> Problem Title: 21. Merge Two Sorted Lists
-> Problem Status: Completed
-> Problem Attempted: 20/11/2023
-> Problem Description:
-------------------------------------------------------------------------------------

Refer: https://leetcode.com/problems/merge-two-sorted-lists/description/

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

    # merge two sorted linked list;;
    def mergeTwoLists(self, list1, list2):
        if not (list1):
            return list2

        if not list2:
            return list1

        # return self.ansv2(list1, list2)
        return self.ansv1(list1, list2)
    
    def ansv1(self, list1, list2):
        """
        run: accepted
        time: o(n+m)
        space: o(1)
        brief: simply attaching nodes one after another on the basis of
        their weightage.
        """
        # finally a new list will return;;
        dummy = ListNode()
        head = dummy

        while (list1 and list2):
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        if list2:
            dummy.next = list2

        if list1:
            dummy.next = list1

        return head.next


##---Main Execution;;
def main(res=None):
    try:
        # Case 0: Basic Linked List;;
        list1 = LinkedList(1)
        items1 = [2, 3, 4, 7, 9, 10]
        list2 = LinkedList(1)
        items2 = [5, 6, 9, 10]

        for item1 in items1:
            list1.append(item1)
        for item2 in items2:
            list2.append(item2)

        print("Total Record List1 :: ", list1.len)
        print("Linked List List1", end=" :: ")
        list1.show()
        print("Total Record List2 :: ", list2.len)
        print("Linked List List2", end=" :: ")
        list2.show()

        # Case 1: Delete Duplicates;;
        list1.head = list1.mergeTwoLists(list1, list2)
        print("Non-Duplicated Linked List", end=" :: ")
        list1.show()

    except(Exception) as e:
        import  traceback
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
