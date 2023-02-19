'''
-------------------------------------------------------------------------------------
-> Problem Title: 876. Middle of the Linked List
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description: 
-------------------------------------------------------------------------------------

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 


Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

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
    
    # Helper : @return count of linked list;;
    def length(self, head):
        count = 0
        cur = head
        while(cur):
            count += 1
            cur = cur.next
        return count
    
    ##---Main Exection;;
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
    
        # return self.ansv1(head)
        return self.ansv2(head)
    
    def ansv2(self, head):
        """
        Run: Accepted
        Code: Optimised | T: O(N) | S:O(1)
        Study:
        Implemented using slow and fast pointer, where slow takes one steps
        and fast pointer hope 2 steps at a time.
        Crux : When fast pointer reached at end of the list then slow pointer
        would be at its middle
        """
        slow, fast = head, head
        while(fast and fast.next):
            slow, fast = slow.next, fast.next.next        
        return slow
    
    def ansv1(self, head):
        """
        Run: Accepted
        Code: Brute Force | T: O(N + N) ~ O(N) | S: O(1)
        Study:
        Simple approach, get the length of total items inside linked list.
        Then iterate over loop exactly half of it.
        """
        cur, n = head, self.length(head)
        for i in range(n//2):
            cur = cur.next
        return cur


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
    