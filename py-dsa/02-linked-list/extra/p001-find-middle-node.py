'''
-------------------------------------------------------------------------------------
-> Problem Title: 876. Middle of the Linked List
-> Problem Status: Completed
-> Problem Attempted: 06/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Refer: https://leetcode.com/problems/middle-of-the-linked-list/description/

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

##---Main Solution
class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        if self.head.next == None:
            return self.head 

        # return self.ansv1()
        return self.ansv2()
    
    def ansv2(self):
        turtle = self.head
        rabbit = self.head

        while(rabbit and rabbit.next):
            rabbit = rabbit.next.next
            turtle = turtle.next
        
        return turtle

    def ansv1(self):
        count = self._count()
        count = count//2
        ptr = self.head
        while(count):
            count -= 1
            ptr = ptr.next

        return ptr
    
    def _count(self):
        count = 0
        ptr = self.head
        while(ptr):
            ptr = ptr.next
            count += 1
        return count
        

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
    