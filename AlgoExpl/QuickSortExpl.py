import time

## PRINTING ARRAY;
def printArray(arr, message=None):
    print(f"{message}") if message else print("Array...")
    for key,value in enumerate(arr):
        print(value, end=" ")
    print("\n")

##----------- Quick Sort Implementation From End;
def partitionByEnd(arr,left,right):
    i,j,pivot = left, right-1,arr[right]
    # print("i:",i,"j:",j,"pivot:",pivot)
    while(i<j):
        # Checking, left values smaller than Pivot;
        while(i < right) and (arr[i] < pivot):
            i += 1
            # print("index i:",i)
        # Checking, right values greater than Pivot;
        while(j > left) and (arr[j] > pivot):
            j -= 1
            # print("index j:",j)
        # Safe Check for i crossover j;
        if(i<j):
            # print("swapping,aI:",arr[i],"aJ:",arr[j])
            arr[i],arr[j] = arr[j],arr[i]
            # print("after swap:",arr)
    
    # Final Pivot Swap 
    if(arr[i] > pivot):
        # print("final swap,aI:",arr[i],"Pivot:",pivot)
        arr[i],arr[right] = arr[right],arr[i]
        # print("final array:",arr)

    # print("partionIndex:",i)
    return i            ## Partition Index;

    
def quickSortByEnd(arr,left,right):
    if(left<right):
        pI = partitionByEnd(arr,left,right)                        ## ~ PI: partition Index
        quickSortByEnd(arr,left,pI-1)                             ## PI Is at Correct Position;
        # print("To pI:",arr)
        quickSortByEnd(arr,pI+1,right)
        # print("To Right :",arr)
        return arr
##----------- /Quick Sort Implementation From End;

##----------- Quick Sort Implementation From Start;
def paritionByStart(arr,left,right):
    i,j,pivot = left+1,right,arr[left]
    print("i:",i,"j:",j,"pivot:",pivot)
    while(i < j):
        print("i",i,"right:",right)
        # Checking, Smaller Values from Left;
        while(i<right) and (arr[i] < pivot):
            print("index i:",i)
            i += 1
        print("j:",j,"left:",left)
        # Checking, Larger Values from Right;
        while(j > left) and (arr[j] > pivot):
            print("index j:",j)
            j -= 1
        # Safe Check, 
        if(i < j):
            print("swapping,aI:",arr[i],"aJ:",arr[j])
            arr[i], arr[j] = arr[j],arr[i]
            print("after swap:",arr)

    # Final Swap With Pivot;
    if(arr[i] > pivot):
        print("final swap,aI:",arr[i],"Pivot:",pivot)
        arr[i], arr[left] = arr[left],arr[i]
        print("final array:",arr)
    
    return i
        

def quickSortByStart(arr,left,right):
    if(left < right):        
        pI = paritionByStart(arr,left,right)
        quickSortByStart(arr,left,pI-1)                     ## Because, PI at Correct Position;
        quickSortByStart(arr,pI+1,right)
        return arr
##----------- /Quick Sort Implementation From Start;


## QUICK SORT EXPL;
def quickSortExpl():
    arrays = [
        # [9,0,8,2,3,4,6,51,29,87,10,23],
        [8,4,3,2,7],
        # [8,4,3,2,9],
    ]
    for arr in arrays:
        printArray(arr,"Before...")
        # quickSortByEnd(arr,left=0,right=len(arr)-1)
        quickSortByStart(arr,left=0,right=len(arr)-1)
        printArray(arr,"After...")    


##--- MAIN EXECUTION
def main():
    quickSortExpl()                         ## QuickSort()


if __name__ == "__main__":
    print("#-------------------Code Start ------------------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime)
    print("#-------------------Code Ends --------------------------#")
    