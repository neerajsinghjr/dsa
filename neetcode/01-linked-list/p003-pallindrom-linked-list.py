'''
-------------------------------------------------------------------------------------
-> Problem Title: 234. Palindrome Linked List
-> Problem Status: Completed
-> Problem Attempted: 25/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Link:-
https://leetcode.com/problems/palindrome-linked-list/

-------------------------------------------------------------------------------------
'''

# !/bin/python3

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

    def isPalindrome(self, head) -> bool:
        if not (head and head.next):
            return True

        # return self.ansv1(head)
        # return self.ansv2(head)
        return self.ansv3(head)

    def ansv3(self, head):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief:
            - find the middle node.
            - reverse the node of second half.
            - simply check val equivalent for both list
        """
        # s1: find middle node;;
        slow, fast = head, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        # s2: reverse second list (from slow onwards);;
        pre, cur = None, slow
        while (cur):
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        # S3: looping both list to check pallindrom;;
        cur = head
        while (pre and cur):
            print(f"s3: pre: {pre.val} // cur: {cur.val}")
            if not (pre.val == cur.val):
                return False
            pre = pre.next
            cur = cur.next

        return True

    def ansv2(self, head):
        """
        refer ansv1()
        """
        ll, ptr = [], head
        while (ptr):
            ll.append(ptr.val)
            ptr = ptr.next
        left, right = 0, len(ll) - 1
        while (left <= right):
            if not (ll[left] == ll[right]):
                return False
            left += 1
            right -= 1

        return True

    def ansv1(self, head):
        """
        run: accepted
        time: o(n)
        space: o(n)
        choke: none
        brief: simply comparing two list together.
        """
        ll, ptr = [], head
        while (ptr):
            ll.append(ptr.val)
            ptr = ptr.next

        return (ll == ll[::-1])


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
    print("Run Time:", endTime - startTime, "ms")
    print("#------------ Code Stop ----------------#")
