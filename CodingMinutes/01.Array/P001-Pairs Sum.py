"""
#Problem Title: Pair Sum 
#Problem Attempted: 24/07/2022
#Problem Description:

You need to return the pair sum which is equals to the target value of the given array.
eg,
array = [1,2,3,4,5]
"""


from copy import deepcopy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        if len(nums) == 2:
            if sum(nums) == target:
                return [0,1]
            else:
                return []
        
        return self.ansv1(nums, target)
        # return self.ansv2(nums, target)
    
    
    # APPORACH: USING SET
    def ansv2(self,nums,target):
        dataset = set()
        start,end = 0,len(nums)
        while(start < end):
            reqSum = target - nums[start]
            if(reqSum in dataset):
                return [nums.index(reqSum),start]
            else:
                dataset.add(nums[start])
                start += 1
                
        return []
    

    """
    APPROACH: TWO POINTER WITH SORTING... FAILED !!!
    becoz output should be pair indexes. So if you sorted the array then the index will long gone.
    So to overcome such thing. you will using temporay datastructure to map number with original index.
    Here, analysis...
    TIME: T(NXLOGN) || SPACE: T(N)
    """
    def ansv1(self,nums,target):
        tmp = deepcopy(nums)
        nums.sort()                     # O(nlogn)
        print(tmp)
        print(nums)
        start,end = 0,len(nums)-1
        while(start <= end):
            curSum = nums[start] + nums[end]
            if curSum == target:
                return [tmp.index(nums[start]),tmp.index(nums[end])]
            elif(curSum > target):
                end -= 1
            elif(curSum < target):
                start += 1
                
        return []
	
