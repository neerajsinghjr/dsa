'''
----------------------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified 
list.

k is a positive integer and is less than or equal to the length of the linked list. If the number 
of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5] 

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

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
    
    ###---Helpers
    def getLength(self,head):
        n,cur = 0,head
        while(cur != None):
            n  += 1
            cur = cur.next
            
        return n 
    
    
    ###---Main Execution;;
    def reverseKGroup(self, head, k):
        n = self.getLength(head)
        
        if(n == 0 or k == 0 or k > n):
            return head
        
        if(head == None or k == 1):
            return head
        
        return self.ansv1(head,k,n)
        
        
    """
    Run: Success
    Code: Optimised | T:O(N) | S:O(1)
    Study:
    Simply, reverse list node in the group of 'k' nodes recursively, 
    and then, finally make the current HEAD pointer points to the newHEAD.
    
    and then finally when all the recursive call reach to en
    return the $pre node of the linked list as the new HEAD node.
    """
    def ansv1(self,head,k,n):
        if(head == None or head.next == None or n < k):
            return head

        i = 0
        pre = None
        cur = head

        while(i < k and n >= k):
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
            i += 1

        newHead = self.ansv1(nex,k,n-k)

        if(head and newHead):
            head.next = newHead

        return pre


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
    
