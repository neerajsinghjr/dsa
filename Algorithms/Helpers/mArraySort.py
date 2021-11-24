"""
Array Sorting Algorithms :
Merge Sort, Quick Sort, Counting Sort, Selection Sort, Insertion Sort, 
"""

## HELPERS FUNCTION USED FOR ARRAY
def showList(arr,start=None,end=None):
    if(start and end):
        print(f"Array from {start} to {end}")
        for i in range(len(arr[start:end])):
            print(arr[i], end=" ")
    else:
        print(f"Array...")
        for data in arr:
            print(data,end=" ")


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


## IMPLEMENTATION OF QuickSort() ALGORITHMS...
def parition(nums):
    size = len(nums)
    pivot = size-1
    x = y = 0
    for x in range(size-1):
        if nums[x] < pivot:
            nums[x], nums[y] = nums[y], nums[x]
            y += 1
    nums[y+1],pivot = pivot, nums[y+1]
    return y+1
        

def quickSort(nums):
    size=len(nums)
    if(size<=1):
        return nums
    else:
        paritionIndex=parition(nums)
        left = quickSort(nums[:paritionIndex-1])
        print("left:", left)
        right = quickSort(nums[paritionIndex+1:])
        print("right:", right)
        return 