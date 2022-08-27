import time
from typing import List


class Solution:
    def pivotIndexTimeLimitExceeded(self, nums: List[int]) -> int:
        rez = -1
        for i in range(0, len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i + 1:])

            if left_sum == right_sum:
                rez = i
                break

        return rez

    def pivotIndex(self, nums: List[int]) -> int:
        ls = 0
        rs = sum(nums)

        rez = -1
        for i in range(0, len(nums)):
            el = nums[i]
            rs -= el

            if ls == rs:
                rez = i
                break

            ls += el

        return rez


if __name__ == "__main__":
    st = time.time()

    s = Solution()
    print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(s.pivotIndex([1, 2, 3]))
    print(s.pivotIndex([2, 1, -1]))

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("Time complexity: O(n)")
    print("Space complexity: O(1)")
