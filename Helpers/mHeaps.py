"""
Implementation of Heaps Datastructure in python;
# Heap Pre-Requisite : 
    1) Binary Tree
    2) Complete Binary Tree
    3) Heaps - MinHeap, MaxHeap
"""

class Heap:

    """
    init() : constructor
    """
    def __init__(self,capacity=20,maxHeap = True):
        self.maxHeap = True             # maxHeap : True 
        self.heap = [-1]*capacity
        self.capacity = capacity
    

    """
    len() : length of the constructor;
    """
    def __len__(self):
        if(self.heap is not None):
            len(self.heap)
        return 0


    """
    push() : push node to heap;
    """
    def push(self,data):
        size = len(self.heap)
        if(size == 0):  # base case
            self.heap[1] = data
        else:
            if(self.maxHeap == True):
                for i in range(1,size+1):
                    pass                    
            else:
                # min heap code here
                pass


    """
    pop() : pop node from heap;
    """
    def pop(self):
        pass


    """
    remove() : remove node from particular key
    """
    def remove(self,index):
        pass 


    """
    find() : find node inside the heap;
    """
    def find(self,data):
        pass

