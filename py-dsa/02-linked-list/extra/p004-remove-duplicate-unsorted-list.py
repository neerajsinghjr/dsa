'''
-------------------------------------------------------------------------------------
-> Problem Title: Remove Duplicates from Unsorted Linked List
-> Problem Status: Completed
-> Problem Attempted: 11/11.2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

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

# Node Class
# class Node:
#     def __init__(self, data):   # data -> value stored in node
#         self.data = data
#         self.next = None
    
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        if not(head and head.next):
            return head
        
        self.head = head 
        return self.ansv1()
    
    def ansv1(self):
        # needs to track the duplicates;;
        num_set = set()
        
        # linked list iteration pointers;;        
        pre_node = self.head 
        cur_node = self.head.next
        
        # default value added for pre_node;;
        num_set.add(pre_node.data)
        
        while(cur_node):
            
            if(cur_node.data in num_set):
                # remove the cur_node if its duplicate;;
                pre_node.next = cur_node.next
            else:
                # else add the genuine node to our dataset;;
                num_set.add(cur_node.data)
                pre_node = cur_node
            
            # iterate next node;;
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
    