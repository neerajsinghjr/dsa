'''
-------------------------------------------------------------------------------------
-> Problem Title: 92. Reverse Linked List II
-> Problem Status: Completed
-> Problem Attempted: 26/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/reverse-linked-list-ii/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not (head and head.next):
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
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        for _ in range(left - 1):
            pre, cur = cur, cur.next

        # S2: reverse the in-between list;;
        pre_node = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = pre_node
            pre_node = cur
            cur = temp

        # S3: Re-link the first and last node;;
        pre.next.next = cur
        pre.next = pre_node

        return dummy.next


##---Main Execution;;
def main(res=None):
    try:
        data = []
        obj = Solution()
        res = None
        print(f"Result: {res}") if res else print("Empty!")

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
