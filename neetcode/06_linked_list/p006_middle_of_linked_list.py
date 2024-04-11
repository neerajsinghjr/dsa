'''
-------------------------------------------------------------------------------------
-> Problem Title: 876. Middle of the Linked List
-> Problem Status: Completed
-> Problem Attempted: 25/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/middle-of-the-linked-list/description/

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
    def get_count(self, head):
        count = 0
        ptr = head
        while (ptr):
            ptr = ptr.next
            count += 1
        return count

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        # return self.ansv1(head)
        return self.ansv2(head)

    def ansv2(self, head):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: Two pointer apporach, slow pointer hops one time
        and fast pointer hop two times.
        So, When fast pointer reached at end of the linked list
        slow pointer would be at the mid of linked list.
        """
        slow, fast = head, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        return slow

    def ansv1(self, head):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief:
            - calculating the length of linked list
            - finding mid of the linked list
            - traversing to the mid node.
        """
        ll_len = self.get_count(head)
        mid = ll_len // 2
        ptr = head
        while (mid):
            ptr = ptr.next
            mid = mid - 1
        return ptr


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
