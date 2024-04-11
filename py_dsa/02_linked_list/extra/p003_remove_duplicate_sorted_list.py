'''
-------------------------------------------------------------------------------------
-> Problem Title: Remove Duplicate From Sorted Linked List
-> Problem Status: Completed
-> Problem Attempted: 11/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        if not(head and head.next):
            return head

        return self.ansv1()
    
    def ansv1(self):
        pre_node = self.head 
        cur_node = self.head.next 

        while(cur_node):
            if pre_node.val == cur_node.val:
                pre_node.next = cur_node.next
                cur_node = cur_node.next
            else:
                pre_node = cur_node
                cur_node = cur_node.next

        return self.head
        


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
    