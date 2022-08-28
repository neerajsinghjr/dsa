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

    """
    Code: Optimised Recursive ~v1 | T:O(N) | S:O(1) + Stack Space
    Study: 
    Simply reversing the first node then recursion magic followd;
    """
    def ansv2(self,head,pre=None):
        if(head.next == None):
            return pre

        nex = head.next
        head.next = pre
        pre = head

        return self.ansv2(nex,pre)


    """
    Code: Optimized Recursive ~v2 | T:O(N) | S:O(1) + Stack Space
    Study:
    In this recursion apporach, we are gonna reverse the list frome end point...
    1) Iterate till the end node and return the end node as $NewHEAD
    2) At function call previous to end node, then make the next node of current node points to current node
        $next-of-current-node->next = $current-node
    3) After changing link, return the current node as NEW HEAD

    For eg, In real life suppose students are lined up the queue and when they about turn, 
    First guy in the line turn himself
    Fecond guy turn himself after seeing the first one turn 
    Third one do the same and so on ...
    till the whole queue get reversed !
    """
    def ansv3(self,head):
        if(head.next == None):          # Till reach end node, only;;
            return head

        newHEAD = self.ansv3(head.next)
        head.next.next = head

        return newHEAD



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
    