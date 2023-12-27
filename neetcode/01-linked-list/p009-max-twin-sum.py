'''
-------------------------------------------------------------------------------------
-> Problem Title: 2130. Maximum Twin Sum of a Linked List
-> Problem Status: Completed
-> Problem Attempted: 27/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

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
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


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
        while (node):
            print(node.value, end=" ")
            node = node.next

    def pair_sum(self, head) -> int:
        if not (head.next and head.next.next):
            return head.val + head.next.val

        return self.ansv1(head)
        # return self.ansv2(head)

    def ansv2(self, head):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief:
            - simplification of ansv1()
            - in this apporach, we have combined the S1 and S2 of
            solution referred in ansv1() together.
        """
        max_sum = 0
        slow, fast = head, head
        pre = None

        # S1: Finding mid and reversing the first half;;
        while (fast and fast.next):
            fast = fast.next.next
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp

        # S2: Traversing both list to find max sum;;
        while (slow and pre):
            cur_sum = slow.value + pre.value
            max_sum = max(max_sum, cur_sum)
            slow = slow.next
            pre = pre.next

        return max_sum

    def ansv1(self, head):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke:
            - there was issue in finding mid of the list which is
            one element shifted from first half to another half.
            - added one extra node before head.
        brief:
            - derivative of reorder list problem.
            - twin is represented by, ith & [(n-1)-i]
            - S1: Finding the mid of the list
            - S2: Reverse the second half of list
            - S3: Traverse together simultaneously and grep max sum
        """
        max_sum = 0
        # S1: Finding the mid of the list;;
        dummy = Node(next=head)
        slow, fast = dummy, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        # S2: Reverse the second half of list;;
        pre, cur = None, slow.next
        # break the first list to avoid loop
        slow.next = pre
        while (cur):
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        # S3: Traverse together simultaneously and grep max sum;;
        # list1, list2 = head, pre
        while(list1 and list2):
            cur_sum = list1.value + list2.value
            max_sum = max(max_sum, cur_sum)
            list1 = list1.next
            list2 = list2.next

        return max_sum


##---Main Execution;;
def main(res=None):
    try:
        ll = LinkedList(7)
        # max twin sum: 130
        items = [
            57,13,31,17,65,32,3,97,22,7,20,69,35,69,75,13,33,50,
            80,64,71,15,28,2,27,39,48,13,22,84,5,51,46,26,78,56,63
        ]
        for item in items:
            ll.append(item)
        max_sum = ll.pair_sum(ll.head)
        print("Max Twin Sum: ", max_sum)

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
