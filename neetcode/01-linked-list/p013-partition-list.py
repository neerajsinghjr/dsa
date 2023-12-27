'''
-------------------------------------------------------------------------------------
-> Problem Title: 86. Partition List
-> Problem Status: Completed...
-> Problem Attempted: 26/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/partition-list/description/

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
    def partition(self, head, x):
        if not (head and head.next):
            return head

        return self.ansv1(head, x)

    def ansv1(self, head, x):
        list1 = ListNode()
        list2 = ListNode()
        ll1, ll2 = list1, list2
        ptr = head
        while (ptr):
            if ptr.val < x:
                list1.next = ptr
                list1 = list1.next
            else:
                list2.next = ptr
                list2 = list2.next
            ptr = ptr.next

        list1.next = ll2.next
        list2.next = None

        return ll1.next

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
