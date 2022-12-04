'''
Problem Description:
Given a linked list of N nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X. If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present.  

Example 1:

Input:
N = 3
value[] = {1,3,4}
X = 2
Output: 1
Explanation: The link list looks like
1 -> 3 -> 4
     ^    |
     |____|    
A loop is present. If you remove it 
successfully, the answer will be 1. 

Example 2:
Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output: 1
Explanation: The Linked list does not 
contains any loop. 
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from AlgoExpl.Helpers.Classes.LinkedList import LinkedList


## Main Working Function, here...
class Solution:
    
    # helper : remove loop from linked list;
    def removeLoop(self, head):
        if not(head and head.next): return head
            
        return self.removeNode(head)
        
        
    # helper : remove node from linked list;
    def removeNode(self, head):
        # base case;
        meetup = self.detectLoop(head)
        if(meetup == False or meetup == None): 
            return head
        else:
            start = head
            temp = None
            while(start != meetup):
                temp = meetup               # backup to remove loop node;
                start = start.next
                meetup = meetup.next
                
            # remove looping node;
            if temp:    
                temp.next = None
            return head
            
    
    # helper : detect loop method;
    def detectLoop(self, head):
        slow = fast = head
        while(fast and fast.next):
            # check for slow pointer;
            if not(slow.next): return False
            slow = slow.next
        
            # check for fast pointer;
            if not(fast and fast.next.next): return False
            fast = fast.next.next
            
            # detect loop;
            if(slow == fast): return slow
            
        return False 



def main():
    try:
        i = 1
        list = LinkedList()
        while(i <= 10):
            list.pushFront(i)
            i += 1
        list.show()


        # obj = Solution()
        # res = ""
        # print(res) if res else print("Empty!")
        
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
    