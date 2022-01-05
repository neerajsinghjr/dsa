'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        i = j = 0
        result = []
        ##--- nums1 and nums2 have only one item in array;
        if m < 1 and n < 1:
            if nums1[0] < nums2[0]:
                result.append(nums1[0])
                result.append(nums2[0])
            else:
                result.append(nums2[0])
                result.append(nums1[0])

        else:
            ## Elements of nums1 and nums2 are equal
            while (i < m and j < n):
                if nums1[i] != 0 and nums1[i] <= nums2[j]:
                    result.append(nums1[i])
                    i += 1
                else:
                    if nums2[j] != 0:
                        result.append(nums2[j])
                    j += 1

            ## Elements of nums1 greater nums2;
            if i < len(nums1):
                while (i < len(nums1)):
                    if nums1[i] != 0:
                        result.append(nums1[i])
                    i += 1

            ## Elements of nums2 greater nums1;
            if j < len(nums2):
                while (j < len(nums2)):
                    if nums2[j] != 0:
                        result.append(nums2[j])
                    j += 1

            ## Update Reference nums1;
            nums1.clear()
            nums1.extend(result)


def main():
    m = 3
    n = 3
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    obj = Solution()
    obj.merge(nums1, m, nums2, n)
    for x in nums1:
        print(x, end=" ")


if __name__ == "__main__":
    main()
