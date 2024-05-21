'''
-------------------------------------------------------------------------------------
-> Problem Title: 895. Maximum Frequency Stack
-> Problem Status: Completed
-> Problem Attempted: 2024-05-18
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/maximum-frequency-stack/description/

Reference:-
https://youtu.be/Z6idIicFDOE

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
class FreqStack:

    """
    _run: accepted
    _code: time: o(n), space: o(n+n) ~ o(n)
    _study:
    --- constraints ---
    [+] problem is asking to implement most frequent stack that means stack works like
    normal in the case of pushing to the stack but popping mechanism will pop the most
    frequent element or it should return the value with most occurrence.
    [+] if two element is having the same occurrence then last value will be popped.
    --- datastructure ---
    [+] stack is used to keep the order of the value
    [+] dictionary is used to keep the count of the value
    [+] dictionary is also used to keep the group w.r.t  stack.
    --- explanation ---
    [+] approach of tackling the problem is bit different. We are not using the stack
    directly in this problem but we are using the 2 x hashmap and a variable that will
    hold the max_occurrence count.
        [1] count : __hashmap__
        [2] groups : __hashmap__
        [3] max_count : __int__
    [+] count(hashmap) is used to map the value with its related count in entire dataset.
    for eg, [1,5,5,6,5,4] => count = {1: 1, 5: 3 ... so on }
    [+] groups(hashmap) is used to map the occurence with its related stack values whose
    occcurrence is same in dataset.
    eg, [1,5,5,6,5,4] => groups = {1: [1, 6, 4], 3: [5]}
    [+] max_count(int) variable responsiblity is to hold the count of frequency which is
    coming in the dataset in the maximum times.
    for eg, [1,5,5,6,5,4], max_count = 3 which is corresponding to value 5.
    [+] using above count, groups, max_count, we pop element on the basis of max_count
    whenver we pop the max_count from the groups then we have to pop from the stack of the
    stack which is holding by the groups.
    [+] everytime when we execute pop() then relative max_count stack variable is popped and
    if the stack is empty then we reduce the max_countm,  otherwise we left it untouched.
    """

    def __init__(self):
        self.count = {}  # map value with their count;;
        self.groups = {} # this will hold group single count with all of values;;
        self.max_count = 0 # this count will hold the max frequency;;

    def push(self, val: int) -> None:
        # s1 : map the current count with the val;
        cur_count = self.count.get(val, 0) + 1
        self.count[val] = cur_count
        # s2: if the cur_count is greater then max_count;;
        if cur_count > self.max_count:
            self.max_count = cur_count
            self.groups[cur_count] = []
        # s3: update the val in the respective group;;
        self.groups[cur_count].append(val)

    def pop(self) -> int:
        # pop the last element from the groups with max_count key;;
        res = self.groups[self.max_count].pop()
        # update the count for particular value in count hashmap;;
        self.count[res] -= 1
        # reduce the max_count by one if group have empty array;;
        if not self.groups[self.max_count]:
            self.max_count -= 1
        return res


##---Main Execution;;
def main(res=None):
    try:
        # Your FreqStack object will be instantiated and called as such:
        obj = FreqStack()
        obj.push(val)
        param_2 = obj.pop()

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
