'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Middle of the Linked List
-> Problem Status: Completed
-> Problem Attempted: 22.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
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
1) The number of nodes in the list is in the range [1, 100].
2) 1 <= Node.val <= 100

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
    
    #---Return Length of LinkedList;;
    def getLength(self,head):
        node = head
        count = 0
        while(node != None):
            node = node.next
            count += 1
        return count
    
    
    #---Main Execution;;
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        # return self.ansv1(head)
        return self.ansv2(head)
    
    
    """
    Code: Optimised Approach | T:O(N) | S:O(1)
    Study: Slow and Fast Pointer
    Simple apporach works on slow and fast pointer;
     1) Slow pointer jumps one at a time;;
     2) Fast Pointer jumps twice at a time;;
    Finally, when fast pointer reached at end,
    then return slow pointer node;
    """
    def ansv2(self,head):
        slow,fast = head,head
        
        while(fast != None):
            if not(fast.next): 
                break
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    
    """
    Code: Optimised | T:O(N) | S:O(1)
    Study:
    Simple easy approach with following steps...
     1) Count number of nodes in LinkedList;;
     2) Integer divide by 2;;
     3) Iterate from 0 to the limit;;
    return the node at the index = limit;;
    """
    def ansv1(self,head):
        cur = head
        n = self.getLength(head)
        
        i,limit = 0,n//2
        while(i < limit):
            cur = cur.next
            i += 1
            
        return cur


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
    