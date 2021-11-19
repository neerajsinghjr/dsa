"""
Array Sorting Algorithms :
Merge Sort, Quick Sort, Counting Sort, Selection Sort, Insertion Sort, 
"""

## IMPLEMENTATION OF MergeSort() ALGORITHMS...
def merge(left, right):
    temp = []
    x = y = z = 0
    leftSize, rightSize = len(left), len(right)
    while(x < leftSize and y < rightSize):
        if(left[x] < right[y]):
            temp.append(left[x])
            x += 1
        else:
            temp.append(right[y])
            y += 1
    while(x < leftSize):
        temp.append(left[x])
        x += 1
    while(y < rightSize):
        temp.append(right[y])
        y += 1
    for x in range(len(temp)):
        nums[x] = temp[x]
    print("before return:",temp)
    # return temp


def mergeSort(nums):
    size = len(nums)
    if(size <= 1):
        print("breakpoint:", nums)
        return nums
    else:
        mid = size // 2
        print("mid:",mid)
        left = mergeSort(nums[:mid])                                      
        print("to mid:",nums)
        right = mergeSort(nums[mid:])
        print("from mid:",nums[mid:])                             
        # nums = merge(left, right)
        # print("before return:", nums)
        return merge(left, right)
        

## IMPLEMENTATION OF QuickSort() ALGORITHMS...
def parition(nums):
    pass

def quickSort(nums):
    pass
