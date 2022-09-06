import bisect
print("-----------------------------------CODE BEGINS ---------------------------------------")

"""
bisect() => O(logn) works on binary search
insort()
"""

nums = [12, 1,3,45,56,342,33,45]
# nums = [1,2,3,3,3,4,5,6,6,7,8,10]
target = 102

nums = nums.sort()
index = bisect.bisect_left(nums, 123,0,len(nums))
bisect.insort_left(nums,123)

print("nums:",nums)
print(f"index for : {index}")


print("-----------------------------------CODE ENDS ---------------------------------------")