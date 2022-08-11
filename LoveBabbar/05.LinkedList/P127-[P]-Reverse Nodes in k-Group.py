'''
Problem Description:
Given a linked list of N nodes. The task is to reverse this list.

# Example 1:
Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.


# Example 2:
Input:
LinkedList: 2->7->8->9->10
Output: 10 9 8 7 2
Explanation: After reversing the list,
elements are 10->9->8->7->2.

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
    
    def reverseList(self, head):
        # Base case
        if not (head or head.next): return head
            
        # return self.reverse(head, None)               # Iterative;
        return self.recursion(head, None)               # Recursion;
        
    
    # Reverse Helper    
    def reverse(self, head, prevNode):
        while(head):
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
            
        return prevNode
        
    
    # Recursion Helper
    def recursion(self, head, prevNode):
        # Base case
        if not head: return
        
        nextNode = head.next        # next node;
        head.next = prevNode
        prevNode = head
        head = nextNode
        return self.reverse(head, prevNode)


def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = obj.reverseList(data)
        print(res) if res else print("Empty!")
        
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
    