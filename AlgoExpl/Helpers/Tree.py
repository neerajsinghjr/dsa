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
        return self.height()


    """
    getRoot() : get root node;
    """
    def getRoot(self):
        return self.root


    """
    add() : add nodes;
    """
    def add(self,data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self._add(self.root,data)


    """
    _add() : add method init;
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
    _show() : show method init;
    """
    def _show(self,root):
        if(root is not None):
            print(root.data,end=", ")          # print;
            self._show(root.left)              # go left;
            self._show(root.right)             # go right;
        return


    """
    preorder() : pre-order tree traversal;
    """
    def preorder(self,root=None):
        if(root is not None):
            print(root.data,end=", ")      # print;
            self.preorder(root.left)       # go left;
            self.preorder(root.right)      # go right;
        return


    """
    inorder() : in-order tree traversal;
    """
    def inorder(self,root=None):
        if(root is not None):
            self.inorder(root.left)            # go left;
            print(root.data,end=", ")          # print;
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
    find() : find nodes inside tree;
    """
    def find(self, data):
        if self.root is not None:
            return self._find(self.root,data)
        else:
            return None


    """
    _find() : find method init;
    """
    def _find(self,root,data):
        if(root is not None):
            if data == root.data:
                return f"Node {data}: Found"
            elif (data < root.data):
                return self._find(root.left,data)
            elif (data > root.data):
                return self._find(root.right,data)
        else:
            return f"Node {data}: Not Found"


    """
    height() : height of a tree
    """
    def height(self):
        if(self.root is None):
            return 0
        else:
            return self._height(self.root)


    """
    _height() : height method init;
    """
    def _height(self,root):
        if(root == None):
            return 0
        else:
            lenOne = self._height(root.left)
            lenTwo = self._height(root.right)
            return 1+max(lenOne,lenTwo)


    """
    deleteTree() : delete all the tree
    """
    def deleteTree(self):
        if(self.root == None):
            return None


    """
    delete() : delete node from tree;
    """
    def delete(self,data):
        if(self.root == None):
            return None
        else:
            self._delete(self.root,data)
    

    """
    _delete() : _delete node init;
    """
    def _delete(self,root,data):
        if(root == None):
            return 
        elif(data < root.data):
            self._delete(root.left,data)
        elif(data > root.data):
            self._delete(root.right,data)
        else:
            # Case 1 : Remove Tree Leaf Node
            if(root.left and root.right):
                return None
            # Case 2 : Remove Skew Tree Node;
            elif(root.left):        # Left Leaf
                return root.left
            elif(root.right):       # Right Leaf
                return root.right
            # Case 3 : Remove In-Between Tree Node;
            else:
                temp = self.findMinNode(root.right)
                root.data = temp.data
                root.right = self._delete(root.right,temp.data)

        return root
    

    """
    findMinNode() : find min node in-order style;
    """
    def findMinNode(self,root):
        if(root):
            while(root.left is not None):
                root = root.left
        return root
        