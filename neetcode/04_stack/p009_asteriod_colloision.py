'''
-------------------------------------------------------------------------------------
-> Problem Title: 735. Asteroid Collision
-> Problem Status: Completed
-> Problem Attempted: 2024-04-13
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/asteroid-collision/description/

Reference:-
https://youtu.be/LN7KjRszjk4

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

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        _stdin:
            arg1: list[int]
        _stdout: list[int]
        """

        return self.ansv1(asteroids)
        # return self.ansv2(asteroids)

    def ansv2(self, asteroids):
        """
        _run: accepted
        _code: time: (n), space: o(n)
        _study:
        --- explanation ---
        [+] explanation is pretty much same like in the ansv1(), only the coding
        style have been changed.
        """
        space = []

        for a in asteroids:

            while space and a < 0 and space[-1] > 0:
                # using addition logic to finalize stronger magnitude among the current
                # asteroid and last asteroid.
                diff = a + space[-1]
                if diff < 0:
                    space.pop()  # last asteroid will be destroyed by incoming asteroid;;
                elif diff > 0:
                    a = 0  # current asteroid will be destroyed by last asteroid;;
                else:
                    a = 0  # both asteroid will destroy one another;;
                    space.pop()

            if a:
                space.append(a)  # add current asteroid to the space;;

        return space

    def ansv1(self, asteroids):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- ds picked ---
        [+] to solve this problem, we can use a stack data structure.
        --- problem ---
        [+] you are given an array asteroids representing asteroids in a row.
        [+] for each asteroid, the absolute value represents its size, and the sign
        represents its direction (positive indicating right, negative indicating left).
        [+] each asteroid moves at the same speed.
        [+] when two asteroids collide, the smaller asteroid may explode.
        [+] if both asteroids are the same size, they both explode.
        [+] two asteroids moving in the same direction will never meet.
        [+] After the collision, the larger asteroid may continue moving to the right,
        and the smaller asteroid may continue moving to the left.
        --- explanation ---
        [+] we iterate through the asteroids and maintain a stack to track the asteroids
        moving to the right.
        [+] if the current asteroid is moving to the right or the stack is empty, we simply
        push it onto the stack.
        [+] if the current asteroid is moving to the left, we handle collisions with the
        asteroids on the stack.
        [+] if a collision occurs, we update the stack accordingly. Finally, the stack contains
        the surviving asteroids after all collisions.
        """
        space = []

        for asteroid in asteroids:
            if not space or asteroid > 0:
                space.append(asteroid)
            else:
                while space and space[-1] > 0:
                    # if incoming asteroid magnitude is larger than our last stored asteroid;;
                    if space[-1] < abs(asteroid):
                        space.pop()

                    # if both the asteroid have equal magnitude than both will destroy;;
                    elif space[-1] == abs(asteroid):
                        space.pop()
                        break

                    # if our last asteroid have bigger magnitude than our incoming asteroid;;
                    else:
                        break
                else:
                    space.append(asteroid)

        return space


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
