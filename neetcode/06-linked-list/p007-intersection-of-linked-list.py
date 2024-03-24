'''
-------------------------------------------------------------------------------------
-> Problem Title: 160. Intersection of Two Linked Lists
-> Problem Status: Completed
-> Problem Attempted: 26/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/intersection-of-two-linked-lists/description/

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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_count(self, head):
        count, ptr = 0, head
        while (ptr):
            ptr = ptr.next
            count += 1
        return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not (headA and headB):
            return None

        # return self.ansv1(headA, headB)
        # return self.ansv2(headA, headB)
        return self.ansv3(headA, headB)

    def ansv3(self, headA, headB):
        """
        run: accepted
        time: o(m+n)
        space: o(1)
        choke: None
        brief:
        - simple logic in which we only traverse the both the list
        inside the loop. If the list have common intersection then they
        will meet at the common point, else they will end in none
        - youtube: https://youtu.be/D0X0BONOQhI
        """
        ll_a, ll_b = headA, headB
        while (ll_a != ll_b):
            ll_a = ll_a.next if ll_a else headB
            ll_b = ll_b.next if ll_b else headA

        return ll_a

    def ansv2(self, headA, headB):
        """
        run: accepted
        time: o(m+n)
        space: o(1)
        choke: none
        brief:
            - Get length of list1 and list2.
            - Skipping the extra node from list have larger node.
            - Traverse both list for common intersection point.
        """
        # S1: Get length of list1 and list2
        len_a = self.get_count(headA)
        len_b = self.get_count(headB)
        jump = abs(len_a - len_b)

        # S2: Skipping the extra node from
        if len_a > len_b:
            for _ in range(jump):
                headA = headA.next
        else:
            for _ in range(jump):
                headB = headB.next

        # S3: Check for both the list intersection;;
        while (headA and headB):
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None

    def ansv1(self, headA, headB):
        """
        run: accepted
        time: o(m+n)
        space: o(m)
        choke: none
        brief:
            - map every node for headA inside hashmap
            - traverse headB and look for common node in hashmap.
        """
        # S1: Creating Hashmap for list1
        hashmap = {}
        ptr = headA
        while (ptr):
            hashmap[ptr] = ptr.val
            ptr = ptr.next

        # S2: Search node of list2 in hashmap
        ptr2 = headB
        while (ptr2):
            if ptr2 in hashmap:
                return ptr2
            ptr2 = ptr2.next

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
