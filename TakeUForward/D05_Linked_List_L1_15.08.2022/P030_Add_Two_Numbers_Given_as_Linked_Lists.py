'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Add Two Numbers
-> Problem Status: Completed
-> Problem Attempted: 15.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You are given two non-empty linked lists representing two non-negative integers. The digits are 
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers 
and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: head = [4,5,1,9], node = 5
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
1) The number of nodes in each linked list is in the range [1, 100].
2) 0 <= Node.val <= 9
3) It is guaranteed that the list represents a number that does not have leading zeros.

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
    
    #---Main Execution;;
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(l1 == None and l2 == None):
            return l1
        
        if(l1 == None):
            return l2
        
        if(l2 == None):
            return l1
        
        return self.ansv1(l1,l2)
    
    
    """
    Code: Optimised Approach | T:O(N) | S:O(1)
    Study:
    - Adding the current node's value to `maxsum`;
    - After adding carry fetch out using maxsum//10;
    - create new dummy node then add values to it;
    - Bottleneck : Look out for carry variable even the linkedlist reached end;
    
    @return head
    """
    def ansv1(self,l1,l2):
        i = 0
        carry = 0
        head = ListNode()
        dummy = head
        
        while(l1 or l2 or carry):
            cursum = 0
            
            if(l1 != None):
                cursum += l1.val
                l1 = l1.next
                
            if(l2 != None):
                cursum += l2.val
                l2 = l2.next
            
            cursum += carry
            carry = cursum // 10                  # New Carry
            value = cursum % 10                 
            
            node = ListNode(value)
            
            dummy.next = node
            dummy = dummy.next
        
            # Choke Prevention;;
            if(i == 100):
                break
            i += 1
            
        return head.next


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
    