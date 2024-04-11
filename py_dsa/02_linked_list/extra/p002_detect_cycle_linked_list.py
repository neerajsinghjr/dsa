'''
-------------------------------------------------------------------------------------
-> Problem Title: 141. Linked List Cycle
-> Problem Status: Completed
-> Problem Attempted: 06/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Refer: https://leetcode.com/problems/linked-list-cycle/

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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

##---Main Solution
class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow, fast = head, head.next
        while(fast and fast.next):
            if slow == fast:
                return True 
            slow = slow.next
            fast = fast.next.next
        
        return False
        


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
    