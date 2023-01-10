from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        k = -1
        for i in range(0, len(nums)):
            if k >= 0 and nums[k] == nums[i]:
                nums[i] = '_'
                continue
            nums[k + 1], nums[i] = nums[i], nums[k + 1]
            k += 1

        return k + 1


if __name__ == "__main__":
    s = Solution()

    arr = [1, 1, 2]
    rez = s.removeDuplicates(nums=arr)  # [1,2,_]
    print(rez, arr)

    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    rez = s.removeDuplicates(nums=arr)  # [0,1,2,3,4,_,_,_,_,_]
    print(rez, arr)
