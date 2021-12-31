'''
Problem Description:
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time
from Helpers.mBinaryTree import *


## Main Working Function, here...
def main():
    try:
        tree = Tree()       # Init Tree
        # tree.add(1)
        # tree.add(2)
        # tree.add(3)
        # tree.add(4)
        # tree.add(5)
        # tree.add(6)
        # tree.add(7)
        # tree.add(8)

        tree.add(45)
        tree.add(10)
        tree.add(7)
        tree.add(90)
        tree.add(12)
        tree.add(50)
        tree.add(13)
        tree.add(39)
        tree.add(57)        

        # print("Height: ",tree.height())
        # print("Length:",len(tree))
        
        # print("Finding...:",tree.find(51))

        # tree.show()

        # print("\nPre-Order...")
        # tree.show("preorder")
        # print("\nIn-Order...")
        # tree.show("inorder")
        # print("\nPost-Order...")
        # tree.show("postorder")
        
        print("Program End Reached...")
            
    except(Exception) as e:
        print(f"Exception Traced : {e}")
    
    else:
        print(f"Program Executed: Success")

    finally:
        print(f"Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    