'''
-------------------------------------------------------------------------------------
-> Problem Title: 83. Remove Duplicates from Sorted List
-> Problem Status: Ongoing...
-> Problem Attempted: 25/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        return self.ansv1(head)

    def ansv1(self, head):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: match previous node and current node.
        if found same then skipped.
        """
        pre, cur = head, head.next
        while (cur):
            if cur and pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return head


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
