#!/bin/python3

import os
import re
import sys
import math
import random

from time import time
from typing import List,Type


###---class 1;
class Test:

    def __init_(self, msg="Hi from TEST TEAM"):
        self.msg = msg


###---class 2;
class Solution:

    def __init__(self, msg="Hey From SOLUTION TEAM"):
        self.msg = msg


##---function sample;;
def evenSampleSet(n: int) -> List[int]:
    res = [x for x in range(n) if(x % 2 == 0)]
    return res


def sample(obj: Type[Test]) -> None:
    print(obj.msg)


##---Main Execution;;
def main() -> None:
    # n = int(input("Number: "))
    # x = evenSampleSet(n)
    # print(x)

    obj1 = Solution()
    obj2 = Test()
    sample(obj1)
    sample(obj2)


##--- Entry Point;;
if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print(f"Run Time: {endTime-startTime} ms " )
    print("#------------ Code Stop ----------------#")