'''
Problem Description:
Write a function findFirstLoopNode() that checks whether a given Linked List contains a loop. If the loop is present then it returns point to the first node of the loop. Else it returns NULL.

Example 1:

Input: LinkedList: 2->2->4->5
                      |_____|            
Output: 2
Explanation: Loop is visible from 5 to 2 so starting point should be 2
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
    
    # Main Function;
    def detectCycle(self, head):
        # base case
        if not(head and head.next): 
            return None
        
        # main case;
        node = None
        slow = fast = head
        while(fast and fast.next):
            # slow pointer reached end;
            if not(slow.next): return None
            slow = slow.next
            
            # fast pointer reached end;
            if not(fast and fast.next and fast.next.next): return None
            fast = fast.next.next
            
            # cycle detected True
            if(slow == fast):
                node = self.getLoopIndex(head, slow)
                return node
        
        return node
    
    
    # Helper: Return Loop Index inside Linked List;
    def getLoopIndex(self, head, meetup): 
        start = head
        while(start != meetup):
            start = start.next
            meetup = meetup.next
        return start


def main():
    try:
        res = ""
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
    