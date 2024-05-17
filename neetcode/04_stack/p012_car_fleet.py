'''
-------------------------------------------------------------------------------------
-> Problem Title: 853. Car Fleet
-> Problem Status: Completed
-> Problem Attempted: 2024-05-11
-> Problem Description:
-------------------------------------------------------------------------------------

Reference:-
https://youtu.be/Pr6T-3yB9RM

Problem:-
https://leetcode.com/problems/car-fleet/description/

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
class Solution:

    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        """
        _stdin:
            arg1: target : __int__
            arg2: position : __list__
            arg3: speed : __list__
        _stdout: __int__
        """
        # return self.ansv1(target, pos, speed)
        return self.ansv2(target, pos, speed)

    def ansv2(self, target, pos, speed):
        """
        _run: accepted
        _code: time: o(nlogn), space: o()
        _study: refer ansv1()
        """
        arrival_time = []
        pair = [(p, s) for p, s in zip(pos, speed)]
        pair_sorted = sorted(pair, reverse=True)

        for pos, spd in pair_sorted:
            cur_time = (target - pos) / spd
            arrival_time.append(cur_time)
            if len(arrival_time) >= 2 and arrival_time[-2] >= arrival_time[-1]:
                arrival_time.pop()

        return len(arrival_time)

    def ansv1(self, target, pos, speed):
        """
        _run: accepted
        _code: time: o(nlogn), space: o(1)
        _study:
        --- constraints ---
        [+] car fleet means when two or more car joined their bumber to bumber and
        continue their run on the road, in this case they are counted as 1.
        --- explanation ---
        [+] we sort the cars by their initial position in descending order because
        we want to start from the car closest to the target.
        [+] we iterate through the sorted cars and calculate the arrival time for
        each car using the formula (target - position) / speed.
        [+] if the current car's arrival time is greater than the previous car's
        arrival time, it means the current car forms a new fleet, so we increment
        the fleet count.
        """
        fleet = 0
        last_arrival_time = None
        pair = sorted(zip(pos, speed), reverse=True)

        for pos, spd in pair:
            cur_time = (target - pos) / spd
            # check if cur_time is smaller than the last arrival_time;;
            if not last_arrival_time or cur_time > last_arrival_time:
                last_arrival_time = cur_time
                fleet += 1

        return fleet


##---Main Execution;;
def main(res=None):
    try:
        data = []
        obj = Solution()
        res = None
        print(f"Result: {res}") if res else print("Empty!")

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
