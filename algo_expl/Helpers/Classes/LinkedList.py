"""
Implementation of LinkedList Datastructure in Python
"""

class Node:

    """
    init() : constructor
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


    """
    getData() : get the data of node;
    """
    def getData(self):
        return self.data


    """
    setData() : set the data to the required node;
    """
    def setData(self,data):
        self.data = data


class LinkedList:

    """
    init() : constructor;
    """
    def __init__(self, head = None):
        self.head = None


    """
    len() : return the length of the nodes;
    """
    def __len__(self):
        if(self.head == None):
            return 0
        else:
            count = 0
            node = self.head
            while(node != None):
                node = node.next
                count += 1
            return count


    """
    getItem() : return the specific index node from linked list;
    """
    def __getitem__(self, index):
        return self.head[index]


    """
    print() : list all nodes of linked list
    """
    def show(self):
        node = self.head
        while(node.next != None):
            print(node.data, end=" -> ")
            node = node.next
        print(node.data)


    """
    pushFront() : push elements from front;
    eg, A <- B <- C <- D <- E
    """
    def pushFront(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            prevHead = self.head
            self.head = newNode
            newNode.next = prevHead


    """
    pushBack() : push elements from the end;
    eg, A -> B -> C -> D -> E
    """
    def pushBack(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode


    """
    remove() : remove node for specific index;
    eg, 
    Input : HEAD -> A -> B -> C -> None, index : 2
    Output : HEAD -> A -> C -> None
    """        
    def remove(self, index):
        if(self.head == None):
            return None
        else:
            i, size = 1, len(self)
            # Index > Size;
            if(index > size):
                index = index % size
            # Base Case;
            if(index == 1):
                self.head = self.head.next
                return 
            # Main Case;
            # Step 1 : Go to one node before end;
            while(i < index-1):
                node = node.next
                i += 1
            # Step 2 : Removal of Specific node
            if(node.next and node.next.next):
                temp = node.next 
                node.next = node.next.next
                del temp            # Free-Up Memory
            else:
                node.next = None
            

    """
    pop() : remove node from end;
    eg, 
    Input : A -> B -> C 
    Output  :A -> B -> None  
    """
    def pop(self):
        if(self.head == None):
            return
        else:
            node = self.head
            prevNode = None
            # Step 1 : Go to one node before end;
            while(node.next != None):
                prevNode = node
                node = node.next
            # Step 2 : Reset the last node;
            prevNode.next = None
            del node                # Delete last node;


    """
    reverse() : reverse the linked list;
    eg, 
    Input : HEAD -> A -> B -> C -> None 
    Output : A <- B <- C <- HEAD
    """
    def reverse(self):
        if(self.head == None):
            return 
        else:
            node = self.head
            prevNode = None
            # Step 1 : Reverse Links;
            while(node != None):
                temp = node.next 
                node.next = prevNode
                prevNode = node
                node = temp
                # Step 2 : Change Head;
                if(temp == None):
                    self.head = prevNode
            return self.head

    """
    ReverseByPivot: 
    LinkedList: 1->2->3->4->5
    K = 3
    Output: 3 2 1 5 4 
    """
    def reverseByKthIndex(self, k):
        # print(self.next)
        totalSize = len(self)
        group = totalSize/4
        prevNode,node = None,self.head
        i = limit = 0
        while(group > 0):
            limit += k
            while(i < limit and i < totalSize):
                if not node:
                    break
                nextNode = node.next
                node.next = prevNode
                prevNode = node
                node = nextNode
                if nextNode:
                    print("p/c:", prevNode.data,"/",node.data)
                else:
                    print("None")
                i += 1
            group = group - 1      # main loop counter;
        return 