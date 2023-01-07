from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        rez = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                rez += 1

        return rez


if __name__ == "__main__":
    s = Solution()

    rez = s.findNumbers([12, 345, 2, 6, 7896])  # 2
    print(rez)

    rez = s.findNumbers([555, 901, 482, 1771])  # 1
    print(rez)
