'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 234. Palindrome Linked List
-> Problem Status: Completed
-> Problem Attempted: 24.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 

Constraints:
1) The number of nodes in the list is in the range [1, 105].
2) 0 <= Node.val <= 9

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- Main Solution;;
class Solution:
    
    #--- Main Execution;;
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.head = head                #Using head as global Variable;;
        
        if(head == None):
            return False
        
        if(head.next == None):
            return True
        
        self.start = head       
        
        # return self.ansv1(head)
        return self.ansv2(head)
    
    
    """
    Run: Success 
    Code: Resursion | T:O(N) | S:O(1) + Stack Space
    Study:
    Simple approach one pointer at head and one at end(recursively reached), 
    then, both steps gets closer to each other and match initiated with 
    base case return True, when NODE pointer reached ends;
    Like below,
    1) Front HEAD pointer is global pointer;
    2) REAR NODE pointer is recusively reached till end;
    3) Compare both pointer values, HEAD == NODE
    4) Two variable is maintained, preMatch and curMatch. 
    $preMatch is the result of previous matching node cycle. 
    $curMatch is the current matching of node with the HEAD(~start) and NODE(-end)
    """
    def ansv2(self,node):
        if(node == None):
            return True
        
        preMatch = self.ansv2(node.next)             # preMatch: return match result till now;;
        curMatch = self.start.val == node.val
        self.start = self.start.next
        
        return (curMatch and preMatch)
    
     
    """
    Run: Success
    Code: Brute Force | T:O(N + N) | S:O(N)
    Study:
    Simple but extra sugary apporach...
    1) Store all the Linked List node's value inside a list
    2) Create reverse style of the stored list
    3) Return the comparision of both the list ;
    """
    def ansv1(self,head):
        items = []
        while(head != None):
            items.append(head.val)
            head = head.next
        return (items == items[::-1])
    


##---Main Execution;;
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
    