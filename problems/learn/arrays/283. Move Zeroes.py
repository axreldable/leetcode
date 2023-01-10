from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[k + 1], nums[i] = nums[i], nums[k + 1]
            k += 1


if __name__ == "__main__":
    s = Solution()

    arr = [0, 1, 0, 3, 12]
    s.moveZeroes(arr)  # [1,3,12,0,0]
    print(arr)

    arr = [0]
    s.moveZeroes(arr)  # [0]
    print(arr)
