'''
Problem Description: 
Find the pairs comprising of two elements, inside an array.

Input : array = [1,2,31,55,3,4,5,6,]
Output : [31,19]
'''

import time


## Method 1: Move Zeroes To Begins;
def moveZeroesToStart(nums):
    size = len(nums)
    lo = 0
    hi = 0
    while(lo < size and hi < size):
        if(nums[hi] == 0):
            nums[hi], nums[lo] = nums[lo], nums[hi]
            lo += 1
        hi += 1
    return nums

## Method 2: Move Zeroes To End;
def moveZeroesToEnd(nums):
    size = len(nums)-1
    lo = size
    hi = size
    while(lo >= 0 and hi >= 0):
        if(nums[hi] == 0):
            nums[hi], nums[lo] = nums[lo], nums[hi]
            lo -= 1
        hi -= 1
    return nums

def main():
    try:
        res1 = moveZeroesToStart(nums=[0, 2, 3, 0, 5, 0, 9, 0, 0, 0, 46])
        res = moveZeroesToEnd(nums=[0, 2, 3, 0, 5, 0, 9, 0, 0, 0, 46])
        print(res) if res else print("Empty!")

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
    