'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Merge Two Sorted Lists
-> Problem Status: Completed
-> Problem Attempted: 22.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of 
the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
1) The number of nodes in both lists is in the range [0, 50].
2) -100 <= Node.val <= 100
3) Both list1 and list2 are sorted in non-decreasing order

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
## Main Working Function, here...
class Solution:
    
    #---Return the length of LinkedList;;
    def getLen(self,head):
        count = 0
        while(head != None):
            head = head.next
            count += 1
            
        return count
        
        
    #---Main Execution;;
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(l1 == None):
            return l2
        
        if(l2 == None):
            return l1
        
        return self.ansv1(l1,l2)
    
    
    """
    Code: Brute Force | T:(n) | S:O(1) ~ [n:max node in any list]
    Study:
    Simply iterating both list at same time and making pointer $cur 
    points to the smallest node from each list. 
    Then change the smallest list node to next node, till one list gone none;
    
    finally, for leftover simply attach the residual to the end of the cur
    on the basis of null check;
    """
    def ansv1(self,l1,l2):
        len1 = self.getLen(l1)
        len2 = self.getLen(l2)
            
        dummy = ListNode()    
        cur = dummy
        
        while(l1 and l2):
            if(l1.val < l2.val):
                cur.next = l1               # Modify, $cur -> l1 node;;
                cur = cur.next              # Hop to L1's next node;;
                l1 = l1.next                # List1 next node;;
            else:
                cur.next = l2               # Modify, $cur -> l2 node;;
                cur = cur.next              # Hop to L2's next node
                l2 = l2.next                # List2 next node;;
        
        if(l1 or l2):
            cur.next = l1 if(l1) else l2
        
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
    