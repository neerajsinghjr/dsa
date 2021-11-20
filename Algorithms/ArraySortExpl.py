from Helpers.mArraySort import *
import time

## PRINTING ARRAY;
def printArray(arr, message=None):
    print(f"{message}") if message else print("Array...")
    for key,value in enumerate(arr):
        print(value, end=" ")
    print("\n")

## MERGE SORT EXPL;
def mergeSortExpl():
    arr = [9,0,8,2,3,4,6,51,29,87,10,23]
    printArray(arr,"Before...")
    arr = mergeSort(arr)                    ## MergeSort() ~V1
    printArray(arr,"After...")    


def main():
    mergeSortExpl()             # Merge Sort Expl;


if __name__ == "__main__":
    print("#-------------------Code Start ------------------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime)
    print("#-------------------Code Ends --------------------------#")
    