'''
Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''


# class Solution:
#     # Constructor Structured;
#     def __init__(self):
#         print("Constructor Initialized")

# Divide the given list into Key Sub-Arryays;
def splitArrayIntoSubArray(nums, key) -> int:
    result = 0
    maxValue = 0
    sumValue
    low = 0
    high = 0
    print(type(nums))
    # for x in range(len(nums)):
    #     sumValue += nums[x]
    #     maxValue = max(maxValue, nums[x])
    # low = maxValue
    # high = sumValue
    # while (low <= high):
    #     mid = (low + high) // 2
    #     if self.isSubArrayPossible(nums, mid, key):
    #         result = mid
    #         mid = high - 1
    #     else:
    #         low = mid + 1

    return result

# Check if Sub-Array Possible at Particular Key;
def isSubArrayPossible(self, nums, mid, key) -> bool:
    subArray = 1
    sum = 0
    for num in nums:
        sum += num
        if sum > mid:
            sum = num
            subArray += 1
    if subArray == key:
        return True
    else:
        return False


def main():
    nums = [7, 2, 5, 10, 8]
    # key = int(input("Key: "))
    # obj = Solution()
    # result = obj.splitArrayIntoSubArray(nums, 2)
    result = splitArrayIntoSubArray(nums, 2)
    print(result)


if __name__ == "__main__":
    main()
