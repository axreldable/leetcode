from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive_arr = []
        negative_arr = []

        for i in nums:
            if i < 0:
                negative_arr.append(i * i)
            else:
                positive_arr.append(i * i)

        negative_arr = negative_arr[::-1]

        # print(positive_arr)
        # print(negative_arr)

        i = 0
        j = 0
        k = 0
        while i < len(negative_arr) and j < len(positive_arr):
            if negative_arr[i] < positive_arr[j]:
                nums[k] = negative_arr[i]
                i += 1
            else:
                nums[k] = positive_arr[j]
                j += 1
            k += 1

        while i < len(negative_arr):
            nums[k] = negative_arr[i]
            i += 1
            k += 1

        while j < len(positive_arr):
            nums[k] = positive_arr[j]
            j += 1
            k += 1

        return nums


if __name__ == "__main__":
    s = Solution()

    rez = s.sortedSquares([-4, -1, 0, 3, 10])  # [0,1,9,16,100]
    print(rez)

    rez = s.sortedSquares([-7, -3, 2, 3, 11])  # [4,9,9,49,121]
    print(rez)

    rez = s.sortedSquares([-10000, -9999, -7, -5, 0, 0, 10000])  # [0,0,25,49,99980001,100000000,100000000]
    print(rez)
