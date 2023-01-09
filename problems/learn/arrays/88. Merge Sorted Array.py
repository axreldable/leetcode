from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1

        for k in range(m + n - 1, -1, -1):
            if i > -1 and j > -1:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
            elif i > -1:
                nums1[k] = nums1[i]
                i -= 1
            elif j > -1:
                nums1[k] = nums2[j]
                j -= 1


if __name__ == "__main__":
    s = Solution()

    arr = [1, 2, 3, 0, 0, 0]
    s.merge(nums1=arr, m=3, nums2=[2, 5, 6], n=3)  # [1,2,2,3,5,6]
    print(arr)

    arr = [1]
    s.merge(nums1=arr, m=1, nums2=[], n=0)  # [1]
    print(arr)

    arr = [0]
    s.merge(nums1=arr, m=0, nums2=[1], n=1)  # [1]
    print(arr)

    arr = [4, 0, 0, 0, 0, 0]
    s.merge(nums1=arr, m=1, nums2=[1, 2, 3, 5, 6], n=5)  # [1,2,3,4,5,6]
    print(arr)
