"""
Implementation of Binary Tree;
"""

class Node:

    """
    init() : constructor
    """
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

    """
    getNode() : get node data;
    """
    def getData(self):
        return self.data

    """
    setData() : set node data;
    """
    def setData(self,data):
        self.data = data


class Tree:

    """
    init() : constructor;
    """    
    def __init__(self):
        self.root = None

    """
    len() : len of the tree;
    """
    def __len__(self):
        pass    

    """
    getRoot() : get root node;
    """
    def getRoot(self):
        return self.root

    """
    add() : build tree;
    """
    def add(self,data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self._add(self.root,data)

    """
    _add() : add node to the tree
    """
    def _add(self,root,data):
        if(data < root.data):            # Left Sub Tree
            if(root.left is not None):
                self._add(root.left,data)
            else:
                root.left = Node(data)
        else:                           # Right Sub Tree
            if(root.right is not None):
                self._add(root.right,data)
            else:
                root.right = Node(data)

    """
    show() : show tree nodes;
    """    
    def show(self,key=None):       # key: pre,in,post-order;
        if(self.root is not None):
            if(key == "preorder"):
                self.preorder(self.root)
            elif(key == "inorder"):
                self.inorder(self.root)
            elif(key == "postorder"):
                self.postorder(self.root)
            else:
                self._show(self.root)
        else:
            return None

    """
    _show() : show the tree in default style;
    """
    def _show(self,root):
        if(root is not None):
            print(root.data,end=", ")            # print;
            self._show(root.left)              # go left;
            self._show(root.right)             # go right;
        return

    """
    preorder() : pre-order tree traversal;
    """
    def preorder(self,root=None):
        if(root is not None):
            print(root.data,end=", ")            # print;
            self.preorder(root.left)       # go left;
            self.preorder(root.right)      # go right;
        return

    """
    inorder() : in-order tree traversal;
    """
    def inorder(self,root=None):
        if(root is not None):
            self.inorder(root.left)            # go left;
            print(root.data,end=", ")            # print;
            self.inorder(root.right)           # go right;
        return 

    """
    postporder() : post-order tree traversal;
    """
    def postorder(self,root=None):
        if(root is not None):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=", ")            # print;
        return

    """
    find() : find note inside tree;
    """
    def find(self,data):
        pass

    """
    delete() : delete a not from tree;
    """
    def delete(self,data):
        pass
    
