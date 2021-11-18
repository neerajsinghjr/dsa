# """
# Merge Sort Algorithms...
# """

# # MERGE(): USED TO MERGE THE MERGE-SHORT RECURSIVE CALL;
# def merge(leftArr, rightArr):
#     x = y = z = 0
#     temp = []
#     # Case 1: LeftArr == RigthArr
#     while(x < len(leftArr) and y < len(rightArr)):
#         if(leftArr[x] < rightArr[y]):
#             temp.append(leftArr[x])
#             print("leftArr:", leftArr[x])
#             x += 1
#         else:
#             temp.append(rightArr[y])
#             print("RightArr:", rightArr[x])
#             y += 1
#     # Case 2: LeftArr Greater
#     while(x < len(leftArr)):
#         temp.append(leftArr[x])
#         print("leftArr:", leftArr[x])
#         x += 1
#     # Case 3: RigthArr Greater;
#     while(y < len(rightArr)):
#         temp.append(rightArr[y])
#         print("RightArr:", rightArr[x])
#         y += 1
#     print("temp:", temp)
#     # Case 4: Copying it back
#     return temp


# # MERGESORT();
# def mergeSort(arr:list) -> None:
#     size = len(arr)
#     if(size<=1):
#         return arr
#     else:
#         mid = size//2
#         leftArray = mergeSort(arr[:mid])           # from, start -> mid;
#         print("left:",leftArray)
#         rightArray = mergeSort(arr[mid:])          # from, mid -> end;
#         print("right:",rightArray)
#         # return merge(leftArray, rightArray)


# def mergeSort(inp_arr):
#     size = len(inp_arr)
#     if size > 1:
#         middle = size // 2
#         left_arr = inp_arr[:middle]
#         right_arr = inp_arr[middle:]
 
#         mergeSort(left_arr)
#         mergeSort(right_arr)
 
#         p = 0
#         q = 0
#         r = 0
 
#         left_size = len(left_arr)
#         right_size = len(right_arr)

#         while p < left_size and q < right_size:
#             if left_arr[p] < right_arr[q]:
#               inp_arr[r] = left_arr[p]
#               p += 1
#             else:
#                 inp_arr[r] = right_arr[q]
#                 q += 1             
#             r += 1
 
        
#         while p < left_size:
#             inp_arr[r] = left_arr[p]
#             p += 1
#             r += 1
 
#         while q < right_size:
#             inp_arr[r]=right_arr[q]
#             q += 1
#             r += 1
