from typing import List


class Solution:
    def findDisappearedNumbers_space_o_1(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) + 1):
            if nums[abs(nums[i - 1]) - 1] > 0:
                nums[abs(nums[i - 1]) - 1] *= -1

        rez = []
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                rez.append(i)

        return rez

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 0

        rez = []
        for i in range(1, len(nums) + 1):
            if i not in d:
                rez.append(i)

        return rez


if __name__ == "__main__":
    s = Solution()

    rez = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])  # [5,6]
    print(rez)

    rez = s.findDisappearedNumbers([1, 1])  # [2]
    print(rez)

    rez = s.findDisappearedNumbers_space_o_1([4, 3, 2, 7, 8, 2, 3, 1])  # [5,6]
    print(rez)

    rez = s.findDisappearedNumbers_space_o_1([1, 1])  # [2]
    print(rez)
