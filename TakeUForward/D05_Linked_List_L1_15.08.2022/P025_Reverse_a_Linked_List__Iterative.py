'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Reverse a Linked List
-> Problem Status: Completed
-> Problem Attempted: 15.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Exmaple 2:
Input: head = [1,2]
Output: [2,1]
Example 3:

Example 3:
Input: head = []
Output: []

Constraints:
1) The number of nodes in the list is the range [0, 5000].
2) -5000 <= Node.val <= 5000
----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
class Solution:
    
    #--- Main Execution;;
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        return self.ansv1(head)
    
    
    """
    Code: Optimised Approach | Time: O(N) | Space: O(1)
    Study:
    This approach is basically just taking two pointer.
    - pre for previous node
    - cur for current node
    while traversing throughout each iteration we basically just
    changing the next pointer for $cur->next = $pre, and then 
    update $pre with $cur pointer.
    """
    def ansv1(self,head):
        dummy = ListNode()
        dummy.next = head
        
        pre = None            
        cur = dummy.next
        
        while(cur != None):
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        
        
        dummy.next = pre
        return dummy.next


def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = ""
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
    