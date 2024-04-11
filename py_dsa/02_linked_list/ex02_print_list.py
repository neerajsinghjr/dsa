'''
-------------------------------------------------------------------------------------
-> Problem Title: Print Linked List
-> Problem Status: Completed
-> Problem Attempted: 04/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Traversing a linked list

-------------------------------------------------------------------------------------
'''

from time import time


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self, value):
        self.head = Node(value)

    def show(self):
        node = self.head
        while(node):
            print(node.value)
            # iterate for next node;
            node = node.next


##---Main Execution;;
def main():
    ll = LinkedList(5)
    ll.show() 

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")