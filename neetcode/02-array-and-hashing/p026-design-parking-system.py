'''
-------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

...

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
class ParkingSystem:
    """
    _run: accepted (optimized)
    _code: time: o(n), space: o(n)
    _choke: none
    _study: use hashmap to map car_type with availability and track
    if every car_type is exist or not.
    """

    def __init__(self, lg: int, mid: int, sm: int):
        self.car_parking = [lg, mid, sm]

    def addCar(self, car_type: int) -> bool:
        if self.car_parking[car_type - 1] > 0:
            self.car_parking[car_type - 1] -= 1
            return True
        return False


class ParkingSystemV1:
    """
    _run: accepted (brute-force)
    _code: time: o(n), space:p o(n)
    _choke: none
    _study: use hashmap to map car_type with availability and track
    if every car_type is exist or not.
    """

    def __init__(self, lg: int, mid: int, sm: int):
        self.car_parking = {1: lg, 2: mid, 3: sm}

    def addCar(self, car_type: int) -> bool:
        if self.car_parking.get(car_type, 0) > 0:
            self.car_parking[car_type] -= 1
            return True
        return False


##---Main Execution;;
def main(res=None):
    try:
        # Your ParkingSystem object will be instantiated and called as such:
        # obj = ParkingSystem(big, medium, small)
        # param_1 = obj.addCar(carType)
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
