import time

## PRINTING ARRAY;
def printArray(arr, message=None):
    print(f"{message}") if message else print("Array...")
    for key,value in enumerate(arr):
        print(value, end=" ")
    print("\n")


## Merge Sort Implementation;
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


## MERGE SORT EXPL;
def mergeSortExpl():
    arr = [9,0,8,2,3,4,6,51,29,87,10,23]
    printArray(arr,"Before...")
    arr = mergeSort(arr)                    ## MergeSort() ~V1
    printArray(arr,"After...")    


##--- MAIN EXECUTION
def main():
    mergeSortExpl()                         ## MergeSortExpl()


if __name__ == "__main__":
    print("#-------------------Code Start ------------------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime)
    print("#-------------------Code Ends --------------------------#")
    