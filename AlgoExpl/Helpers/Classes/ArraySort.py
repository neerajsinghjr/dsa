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


## IMPLEMENTATION OF QuickSortByLast() ALGORITHMS...
def partitionByEnd(arr,left,right):
    i,j,pivot = left, right-1,arr[right]
    while(i<j):
        # Checking, left values smaller than Pivot;
        while(i < right) and (arr[i] < pivot):
            i += 1

        # Checking, right values greater than Pivot;
        while(j > left) and (arr[j] > pivot):
            j -= 1

        # Safe Check for i crossover j;
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    
    # Final Pivot Swap 
    if(arr[i] > pivot):
        arr[i],arr[right] = arr[right],arr[i]

    return i            ## Partition Index;

    
def quickSortByEnd(arr,left,right):
    if(left<right):
        pI = partitionByEnd(arr,left,right)                        ## ~ PI: partition Index
        quickSortByEnd(arr,left,pI-1)                              ## PI Is at Correct Position;
        quickSortByEnd(arr,pI+1,right)
        return arr
