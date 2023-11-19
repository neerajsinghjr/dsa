'''
-------------------------------------------------------------------------------------
-> Problem Title: 19. Remove Nth Node From End of List
-> Problem Status: Completed
-> Problem Attempted: 11/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
        count, ptr = 0, head
        while(ptr):
            ptr = ptr.next
            count += 1
        return count

    def removeNthFromEnd(self, head, k) -> Optional[ListNode]:
        n = self.get_count(head)
        if not head.next or n == k:
            return head.next

        # return self.ansv1(head, n, k)
        return self.ansv2(head, k)

    def ansv2(self, head, k):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: na
        brief: 
        1) Hopping till nth no. of times to get slider
        2) If fast pointer reach end, k == total_ll_len
        3) Traverse fast pointer to end node to get target node
        4) Repace the target node link with node + 1 link
        """
        slow, fast = head, head
        while(k):
            # hopping till nth no. of times to get slider;;
            fast = fast.next
            k = k - 1
        if not fast:
            # if fast pointer reach end, k == total_ll_len;;
            return slow.next
        while(fast.next):
            # traverse fast pointer to end node
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

    def ansv1(self, head, n, k):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: na
        brief: 
        1) Fetch the length of 
        2) If fast pointer reach end, k == total_ll_len
        3) Traverse fast pointer to end node to get target node
        4) Repace the target node link with node + 1 link
        """
        ptr = head
        # target node should be 1 index less than the target node
        target = n - (k + 1)
        while(target):
            ptr = ptr.next
            target -= 1
        # discard the node from linked list;;
        ptr.next = ptr.next.next \
            if ptr.next else None

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
    