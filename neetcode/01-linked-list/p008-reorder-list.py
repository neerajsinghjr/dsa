'''
-------------------------------------------------------------------------------------
-> Problem Title: 143. Reorder List
-> Problem Status: Ongoing...
-> Problem Attempted: 26/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/reorder-list/description/

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

    def reorderList(self, head) -> None:
        # Do not return anything, modify head in-place instead.
        if not (head and head.next):
            return

        return self.ansv1(head)
        # return self.ansv2(head)

    def ansv2(self, head):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief:
            - find the middle of the node
            - reverse the second half
            - join the corresponding element together
        """
        # find the middle of the node;;
        slow, fast = head, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half list;;
        pre, cur = None, slow.next
        slow.next = pre  # avoid cycle loop;;
        while (cur):
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        # reordering the list;;
        l1, l2 = head, pre
        while (l1 and l2):
            nex_l1 = l1.next
            nex_l2 = l2.next
            l1.next = l2
            l2.next = nex_l1
            l1 = nex_l1
            l2 = nex_l2

        return

    def ansv1(self, head):
        """
        run: rejected (TLE)
        time: o(m+n)
        space: o(m)
        choke: none
        brief:
            - store linked list inside the list
            - reorder the list item.
        """
        ll, ptr = [], head
        while (ptr):
            ll.append(ptr)
            ptr = ptr.next

        start, end = 0, len(ll) - 1
        while (start <= end):
            if start == end:
                # set the mid link to none to avoid cycle
                ll[start].next = None
            else:
                # next element backup
                nex_element = ll[start + 1] if start + 1 < len(ll) // 2 else None
                ll[start].next = ll[end]
                ll[end].next = nex_element

        return


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
