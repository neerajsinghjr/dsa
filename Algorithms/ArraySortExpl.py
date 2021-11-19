from Helpers.mArraySort import *


## PRINTING ARRAY;
def printArray(arr, message=None):
    print("")
    print(f"{message}") if message else print("Array...")
    for key,value in enumerate(arr):
        # print(f"{key} => {value}")
        print(value, end=" ")
    print("\n")


## MERGE SORT EXPL;
def mergeSortExpl():
    # arr = [9,0,8,2,3,4,6,51,29,87,10,23]
    arr = [9,0,8,2]
    printArray(arr,"Before...")
    temp = mergeSort(arr)
    printArray(arr,"After...")    
    printArray(temp,"temp...")
    

def main():
    mergeSortExpl()             # Merge Sort Expl;


if __name__ == "__main__":
    print("#-------------------Code Start ------------------------#")
    main()
    print("#-------------------Code Ends --------------------------#")
    