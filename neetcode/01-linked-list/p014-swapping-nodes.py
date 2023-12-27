'''
-------------------------------------------------------------------------------------
-> Problem Title: 1721. Swapping Nodes in a Linked List
-> Problem Status: Completed
-> Problem Attempted: 27/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def get_count(self, head):
        count, ptr = 0, head
        while (ptr):
            ptr = ptr.next
            count += 1
        return count

    def swapNodes(self, head, k):
        if not (head and head.next):
            return head
            # return self.ansv1(head, k)
        return self.ansv2(head, k)

    def ansv2(self, head, k):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief:
            - S1: Finding left index node;;
            - S2: Finding right index node;;
            - S3: Swap the pointer;;
        """
        dummy = ListNode(next=head)
        slow, fast = head, head
        # S1: Finding left index node;;
        while (k - 1):
            fast = fast.next
            k = k - 1
        l_ptr = fast

        # S2: Finding right index node;;
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next
        r_ptr = slow

        # S3: Swap the pointer;;
        l_ptr.val, r_ptr.val = r_ptr.val, l_ptr.val

        return dummy.next

    def ansv1(self, head, left_index):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief:
            - S1: Find the right index node;;
            - S2: Finding left target node;;
            - S3: Finding right target node;;
            - S4: swap left and right node;;
        """
        # S1: Find the right index node;;
        ll_len = self.get_count(head)
        dummy = ListNode(next=head)
        right_index = ll_len - left_index

        # S2: Finding left target node;;
        l_ptr = head
        for _ in range(left_index - 1):
            l_ptr = l_ptr.next

        # S3: Finding right target node;;
        r_ptr = head
        for _ in range(right_index):
            r_ptr = r_ptr.next

        # S4: swap left and right node;;
        l_ptr.val, r_ptr.val = r_ptr.val, l_ptr.val

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
