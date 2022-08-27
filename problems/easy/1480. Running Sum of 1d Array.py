from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rez = [nums[0]]
        for i in nums[1:]:
            rez.append(rez[-1] + i)
        return rez


if __name__ == "__main__":
    s = Solution()
    print(s.runningSum([1, 2, 3, 4]))
    print(s.runningSum([1, 1, 1, 1, 1]))
    print(s.runningSum([3, 1, 2, 10, 1]))

    print("Time complexity: O(n)")
    print("Space complexity: O(1)")
