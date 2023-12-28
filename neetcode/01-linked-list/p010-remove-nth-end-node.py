'''
-------------------------------------------------------------------------------------
-> Problem Title: 19. Remove Nth Node From End of List
-> Problem Status: Completed
-> Problem Attempted: 26/12/2023
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

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
    def removeNthFromEnd(self, head, n) -> Optional[ListNode]:
        if not (head and head.next):
            return None

        # return self.ansv1(head, n)
        return self.ansv2(head, n)

    def ansv2(self, head, n):
        """
        """
        dummy = ListNode(next=head)
        # S1: Maintain the initial gap between nth range;;
        fast = head
        while(n - 1):
            fast = fast.next
            n = n - 1

        # S2: Traverse the fast pointer to the end;;
        slow = dummy
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next

    def ansv1(self, head, n):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke:
            - edge case found when ll_total_length == index to remove.
            - used dummy node to remove that choked scenario.
            - for eg, head = [1,2], n = 2
        brief:
            - S1: Fetch the total length of linked list
            - S2: Find the target element's index
            - S3: Traverse the list the remove the target node.
        """
        # S1: Fetch the total length of linked list
        ll_len = self.get_count(head)
        # S2: Find the target element's index
        index = ll_len - n
        # NOTE : To avoid lower and upper bound cases, use dummy node;
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        # S3: Traverse the list the remove the target node.
        while (index):
            pre, cur = cur, cur.next
            index = index - 1
        pre.next = cur.next

        return dummy.next

    def get_count(self, head):
        count, ptr = 0, head
        while (ptr):
            count += 1
            ptr = ptr.next
        return count


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
