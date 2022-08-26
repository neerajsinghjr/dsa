'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Basic Methods of Linked List
-> Problem Status: Completed
-> Problem Attempted: 15.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
...

----------------------------------------------------------------------------------------------------
'''

###---Node Class;;
class Node:
    
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


###---Return length of the linked list;;
def getLength(head):
    count = 0
    while(head != None):
        head = head.next
        count += 1

    return count


###---Insert node at Start Of Linked List;;
def insertAtStart(head,val=None) -> None:
    if(val != None):
        node = Node(val)        
        node.next = head
        head = node

    return head


###---Insert node the mid of the Linked List;;
def insertAtMid(head,val):
    n = getLength(head)
    if(n == 0):
        head.next = Node(val)
    else:
        pre = None
        cur = head
        limit = n//2

        for _ in range(limit):
            pre,cur  = cur,cur.next

        node = Node(val)
        pre.next = node
        node.next = cur

    return head


###---Insert node at the end of Linked List;;
def insertAtEnd(head,val=None):
    if(val != None):
        if(head == None):
            head.next = Node(val)
        else:
            while(head.next != None):
                head = head.next
            head.next = Node(val)
    return 


###---Print Linked List;;
def printList(head):
    while(head != None):
        marker = "->" if(head.next != None) else ""
        print(head.val,marker,end=" ")
        head = head.next
    print("-> NULL")
    return 


###---Created Linked List;;
def createLinkedList(nodes=10,start=True):
    head = Node(1)
    for x in range(nodes):
        if start:
            insertAtStart(head,x)
        else:
            insertAtEnd(head,x)

    printList("main...",head)

    # return head
