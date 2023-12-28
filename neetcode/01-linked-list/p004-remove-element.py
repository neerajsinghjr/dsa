'''
-------------------------------------------------------------------------------------
-> Problem Title: 203. Remove Linked List Elements
-> Problem Status: Completed
-> Problem Attempted: 25/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/remove-linked-list-elements/description/

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

    def removeElements(self, head, val):
        if not (head and head.next):
            if head and head.val == val:
                return None
            return head

        # return self.ansv1(head, val)
        return self.ansv2(head, val)

    def ansv1(self, head, val):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: linear approach
        """
        dummy = ListNode(next=head)
        pre, cur = dummy, head

        while (cur):
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

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
