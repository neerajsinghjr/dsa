import time

"""
Problem:
Write a function that takes sorted array as an input array and rotated about a pivot point
and finds the index of any given elements
For eg,
sorted = [1,2,3,4,5,6,7,8,9,10], rotated about pivot 6 
Output: [7,9,10,1,2,3,4,5,6]
"""

# Binary Search V1
def rotatedArraySearchV1(arr, key):
    start,end,count, res,size = 0,len(arr),0,"Not Found!",len(arr)
    while(start < end):
        count += 1
        mid = (start + end)//2
        print("start:",start,"end:",end,"mid:",mid)
        print("mid:",mid,"val:",arr[mid])
        if(arr[mid] == key):
            print("Direct Mid: ",arr[mid])
            return f"found: {mid} index"
        else:
            if(arr[mid] > key):     # Key is Smaller;
                print("Key is smaller")
                # Region NEXT To Mid: Smaller;
                if(arr[mid] < arr[mid+1]):
                    print("Next to Mid: ",arr[mid+1])
                    start = mid
                # Region PREVIOUS To Mid: Smaller
                elif (arr[mid-1] < arr[mid]):
                    print("Previous to Mid: ",arr[mid-1])
                    end = mid-1
            else:                   # Key is Greater;
                print("Key is Greater")
                if(arr[mid] < arr[mid+1]):
                    print("Next To mid:", arr[mid+1])
                    start = mid
                else:
                    print("Previous to Mid:",arr[mid-1])
                    end = mid - 1
        
        ## Fallback Prevention;
        if(count == size):
            print("Warning: Program Stopped!")
            break

    return res


## Binary Search V2
def rotatedArraySearchV2(arr, key):
    start,end,count, res,size = 0,len(arr)-1,0,"Not Found!",len(arr)
    while(start <= end):
        count += 1
        mid = (start + end)//2
        if(arr[mid] == key):
            return f"found: {mid} index"
        else:
            if(arr[start] <= arr[mid]):
                if(arr[start] <= key) and (key <= arr[mid]):
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if(key >= arr[mid]) and (key <= arr[end]):
                    start = mid + 1
                else:
                    end = mid - 1

        ## Fallback Prevention;
        if(count == size):
            print("Warning: Program Stopped!")
            break

    return res
            

def main():
    try:
        arr = [7,9,10,1,2,3,4,5,6]
        res = key = None
        key = int(input("Search: "))
        print(arr)
        if (arr and key): res = rotatedArraySearchV1(arr,key)                 ## ~V1
        # if (arr and key): res = rotatedArraySearchV2(arr,key)                 ## ~V2  
        print (res) if (res and arr) else print("Not Found!")
    
    except(ValueError) as e:
        print(f"Program Stopped: {e}")
        
    except(Exception) as e:
        print(f"Program Stopped: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")


if __name__ == "__main__":
    print("#------------- Code Run --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------- Code End --------------#")
