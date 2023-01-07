from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0

        one_length = 0
        is_prev_one = False
        for i in nums:
            if i == 1:
                if is_prev_one:
                    one_length += 1
                else:
                    one_length = 1
                is_prev_one = True
            else:
                is_prev_one = False
            if one_length > max_length:
                max_length = one_length
        if one_length > max_length:
            max_length = one_length

        return max_length


if __name__ == "__main__":
    s = Solution()

    rez = s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])  # 3
    print(rez)

    rez = s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])  # 2
    print(rez)
