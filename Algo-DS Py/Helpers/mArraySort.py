"""
Merge Sort Algorithms...
"""

# MERGE(): USED TO MERGE THE MERGE-SHORT RECURSIVE CALL;
def merge(arr,start,mid,end):
    if len(arr) == 1:
        return arr
    x = start
    y = mid + 1
    z = end
    temp = []
    # Case 1: When, Both Half -> Equal;
    while(x <= mid and y <= end):
        if(arr[x] > arr[y]):
            temp.append(arr[x])
        else:
            temp.append(arr[y])
    # Case 2: When, Left Half -> Greater;
    while(x <= mid):
        temp.append(arr[x])
        x += 1
    # Case 3: When, Right Half -> Greater;
    while(y <= end):
        temp.append(y)
        y += 1
    # Remove Temp Array;
    for key,value in enumerate(temp):
        arr[key] = value


# MERGESORT(): USED TO DIVIDE THE ARRAY FROM MID;
def mergeSort(arr:list) -> None:
    
    start = 0
    end = len(arr)-1
    mid = (start + (end-start))//2

    mergeSort(arr[start:mid])                # from start -> mid;
    print("Merge Sort Left:",arr)

    mergeSort(arr[mid+1:end])              # from mid -> end;
    print("Merge Sort Right:",arr)

    merge(arr,start,mid,end)
    print("merge:",arr)
    return arr