"""
Array Sorting Algorithms :
Merge Sort, Quick Sort, Counting Sort, Selection Sort, Insertion Sort, 
"""

## HELPERS FUNCTION USED FOR ARRAY
def showList(arr,start=None,end=None):
    if(start and end):
        print(f"Array from {start} to {end}")
        for i in range(len(arr[start:end])):
            print(nums[i], end=" ")
    else:
        for num in nums:
            print(num,end=" ")


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
    return temp

def mergeSort(nums):
    size = len(nums)
    if(size <= 1):
        return nums
    else:
        mid = size // 2
        left = mergeSort(nums[:mid])                                      
        right = mergeSort(nums[mid:])
        return merge(left, right)


## IMPLEMENTATION OF MergeSortV2() ALGORITHMS...
def mergeV2(nums, start, mid, end):
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


def mergeSortV2(num,):
    if(size <= 1):
        showList(arr)
        return nums
    else:
        start = 0
        end = size
        mid = size//2
        print("mid:",mid)
        mergeSortV2(nums,start,mid)                                      
        showList(arr,start,mid)
        mergeSortV2(nums,mid,end)
        showList(arr,mid,end)

        return mergeV2(nums,start,mid,end)
        

## IMPLEMENTATION OF QuickSort() ALGORITHMS...
def parition(nums):
    pass

def quickSort(nums):
    pass
