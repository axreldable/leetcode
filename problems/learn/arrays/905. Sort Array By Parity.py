from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k = -1
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                continue
            nums[i], nums[k + 1] = nums[k + 1], nums[i]
            k += 1

        return nums


if __name__ == "__main__":
    s = Solution()

    arr = [0, 1, 0, 3, 12]
    s.sortArrayByParity(arr)  # [0,0,1,3,12]
    print(arr)

    arr = [3, 1, 2, 4]
    s.sortArrayByParity(arr)  # [2,4,3,1]
    print(arr)

    arr = [0]
    s.sortArrayByParity(arr)  # [0]
    print(arr)
