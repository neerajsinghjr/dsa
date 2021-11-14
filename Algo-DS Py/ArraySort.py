from Helpers.mArraySort import *

def printArray(arr, message=None):
    print(f"{message}") if message else print("Given Array...")
    for key,value in enumerate(arr):
        # print(f"{key} => {value}")
        print(value, end=" ")
    print("\n")


def main():
    arr = [9,0,8,2,3,4,6,51,29,87,10,23]
    printArray(arr,"Before...")
    mergeSort(arr)
    printArray(arr,"After...")


if __name__ == "__main__":
    main()