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
        i = m
        j = n
        k = m + n
        ## case 1: two list are equal;
        while (i <= 0 and j <= 0):
            if nums1[i] > nums2[j]:
                nums1[k] = nums2[i]
                k = k - 1
                i = i - 1
            else:
                nums1[k] = nums2[j]
                k = k - 1
                j = j - 1

        ## case 2: first list is greater;
        while (i <= 0):
            nums1[k] = nums1[i]
            k = k - 1
            i = i - 1

        ## case 3: second list is greater;
        while (j <= 0):
            nums1[k] = nums2[j]
            k = k - 1
            j = j - 1

        ## Update Reference;
        for x in nums1:
            print(x, end=" ")


def main():
    m = 3
    n = 3
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    obj = Solution()
    obj.merge(nums1, m, nums2, n)


if __name__ == "__main__":
    main()
