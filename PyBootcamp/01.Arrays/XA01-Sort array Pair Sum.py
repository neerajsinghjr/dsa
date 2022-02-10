'''
Problem Description: 
Find the pairs comprising of two elements, inside an array.

Input : array = [1,2,31,55,3,4,5,6,19] / target = 50
Output : [31,19]
'''

import time


## Method 1: Brute Force Aproach
def pairSumV1(nums,target):
    res = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i],nums[j] == target):
                res.append([nums[i],nums[j]])
    return res


## Method 2: Sorted Only, Implemented using general Double Pointer Approach
def pairSumV2(nums, target):
    res = []
    start, end = 0, len(nums)-1
    while(start < end):
        _sum = nums[start] + nums[end]
        if(_sum == target):
            res.append([nums[start], nums[end]])
            start += 1
            end -= 1
        elif(_sum > target):
            end -= 1
        elif(_sum < target):
            start += 1
    return res if res else []


## Method 3: Pair Sum, Implemented on unsorted Array using Hashset;
def pairSumV3(nums, target):
    temp = {}
    res = []
    for (key,value) in enumerate(nums):                   # enumerate(nums) => key:value;
        needed = target-value
        if needed in temp:
            res.append([needed, value])
        else:
            temp[value]=key
    return res

def main():
    try:
        # res = pairSumV1(nums=[9,8,21,46,23,45,1,2,3,4,5], target=50)                # Unsorted
        res1 = pairSumV2(nums=[1, 2, 3, 4, 5, 8, 9, 21, 23, 45, 46], target=50)      # Sorted
        res2 = pairSumV3(nums=[9, 8, 21, 46, 23, 45, 1, 2, 3, 4, 5], target=50)                  # Unsorted
        print(res1) if res1 else print("Empty!")
        print(res2) if res2 else print("Empty!")
        
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
    