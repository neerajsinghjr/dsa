'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Remove Nth Node From End of List
-> Problem Status: Completed
-> Problem Attempted: 15.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1) 1 <= sz <= 30
2) 0 <= Node.val <= 100
3) 1 <= n <= sz

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
    
    #---Return length of list;;
    def getLen(self,head):
        count = 0
        while(head):
            head = head.next
            count += 1
        return count
    
    
    #---Main Execution;;
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.getLen(head)
        
        # Choke 1: If list == 1 and k == 1;;
        if(n == 1 and k == 1):
            return head.next
        
        return self.ansv1(head,n,k)
    
    
    """
    Code: Brute Force | T:O(N) | S:(1)
    Study:
    Simply, iterate till the node to be deleted...
    then,
    1) Calculate, 
        limit = n-k (n:total nodes; k:index to remove)
    2) Set the variable,
        pre,cur = None,head
    3) Iterate till the limit index from i=1
    4) At limit index, replace the 
        pre.next = cur.next
    
    ### Choke Scenario: 
    -> Before replacing $pre to cur.next node, Check for NONE case.
       Else, return head.next;;
    -> Before replacing $cur to $cur.next, Check for NONE case.
       Else, set it to NONE directly
    
    """
    def ansv1(self,head,n,k):
        pre,cur = None,head
        limit = n-k
        
        for _ in range(limit):
            pre,cur = cur,cur.next
        
        # Choke 2: If $pre not equal to None;
        if(pre == None):
            return head.next
        
        pre.next = cur.next if(cur.next) else None
        
        return head


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
    