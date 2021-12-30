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
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        tree.add(5)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        print("\nPre-Order...")
        tree.show("preorder")
        print("\nIn-Order...")
        tree.show("inorder")
        print("\nPost-Order...")
        tree.show("postorder")
        
        print("end...")
            
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
    