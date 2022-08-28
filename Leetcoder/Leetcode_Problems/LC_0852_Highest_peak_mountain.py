"""
852. Peak Index in a Mountain Array
Problem Description:
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array arr that is guaranteed to be a mountain, 
return any i such that 
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

"""


"""
Approach 1: Binary Search
"""
def binarySearch(arr) -> int:
    start, end = 0, len(arr)
    while(start < end):
        mid = (start + (end-start))//2
        if(arr[mid] < arr[mid+1]):
            start = mid + 1
        else:
            end = mid
    return start

def peakIndexInMountainArray(arr) -> int:
    # base case;
    if not arr: return 0
    # general case;
    return binarySearch(arr)


# """
# Approach 2: Python Based Solution
# """
# ## Python Based Solution;
# def peakIndexInMountainArray(self, arr) -> int:
#     # base case
#     if not arr:
#         return 0
    
#     # general
#     return arr.index(max(arr))


def main():
    # Input Here
    res = peakIndexInMountainArray(arr=[0,1,0])
    print(res)

if __name__ == "__main__":
    print("#------------------------- Code Starts ----------------------#")
    main()
    print("#------------------------- Code Ends ---------------------#")