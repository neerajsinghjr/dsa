	'''
-------------------------------------------------------------------------------------
-> Problem Title: 328. Odd Even Linked List
-> Problem Status: Ongoing...
-> Problem Attempted: 09-12-2022
-> Problem Description: 
-------------------------------------------------------------------------------------
Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered
list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain
as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time
complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 
Constraints:
The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106

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

    ###---Main Execution;;
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return head
        if(head.next == None or head.next.next == None):
            return head

        return self.ansv1(head)
        # return self.ansv2(head)
              
    def ansv1(self, head):
        """
        _run: accepted
        _code: optimised | time: o(n) | space: o(1)
        _study:
        simple apporach, keep traversing the list remove even index and append to the 
        end of the list.
        """
        i, count = 1, 1
        start, end = head, head
        #1 Traversing till the end of the node;
        while(end.next):
            count += 1
            end = end.next
        hop_count = count//2
        #2 Inserting the even index node to list end;
        while(hop_count):
            #2.1
            temp = start.next 
            end.next = temp

            start.next = start.next.next  # hop twice start node;
            end.next = temp           # end node points to even node;
            start = start.next          
            end = end.next
            hop_count -= 1          # reducing hop_count;

        end.next = None             # reset last index to null to avoid cycle
        return head



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
    