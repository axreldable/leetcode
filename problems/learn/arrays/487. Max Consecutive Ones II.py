from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length_1 = 0
        length_2 = 0
        max_length = 0

        is_l1 = True
        for i in range(len(nums)):
            if length_1 > max_length:
                max_length = length_1
            if length_2 > max_length:
                max_length = length_2
            if nums[i] == 1:
                length_1 += 1
                length_2 += 1
            else:
                if is_l1:
                    length_2 += 1
                    is_l1 = False
                    length_1 = 0
                else:
                    length_1 += 1
                    is_l1 = True
                    length_2 = 0

        if length_1 > max_length:
            max_length = length_1
        if length_2 > max_length:
            max_length = length_2

        return max_length


if __name__ == "__main__":
    s = Solution()

    rez = s.findMaxConsecutiveOnes([1, 0, 1, 1, 0])  # 4
    print(rez)

    rez = s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])  # 4
    print(rez)

    rez = s.findMaxConsecutiveOnes([1, 1, 1])  # 3
    print(rez)

    rez = s.findMaxConsecutiveOnes([1, 1, 1, 0, 1, 1, 1])  # 7
    print(rez)

    rez = s.findMaxConsecutiveOnes([0])  # 1
    print(rez)

    rez = s.findMaxConsecutiveOnes([0, 1, 1])  # 3
    print(rez)

    rez = s.findMaxConsecutiveOnes([1, 1, 1, 0, 0])  # 4
    print(rez)
