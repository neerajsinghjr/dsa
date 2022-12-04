'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Reverse Linked List in K Group
-> Problem Status: Completed
-> Problem Attempted: 27.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given a linked list, write a function to reverse every 'K' nodes (where k is an input to the 
function)

Example 1:
Input : 1->2->3->4->5->6->7->8->9->10->11 and k = 3
Ouput: 3->2->1->6->5->4->9->8->7->10->11
Explanation: Every K number of nodes gets reversed and when total number of nodes < K, nodes left
untouched.

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import P000_Helpers as ll


###--- Main Solution;;
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
        


##---Main Execution;;
def main():
    # try:
    head = ll.createLinkedList(nodes=5,start=False)
    ll.printList(head)

    head = reverseGroupByK(head, 3)
    ll.printList(head)
        
        
    # except(Exception) as e:
    #     print(f"Exception Traced : {e}")
    
    # else:
    #     print("Program Completed : Success")

    # finally:    
    #     print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    