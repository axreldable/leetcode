from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        k = -1
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums[i] = '_'
                continue
            nums[k + 1], nums[i] = nums[i], nums[k + 1]
            k += 1

        return k + 1


if __name__ == "__main__":
    s = Solution()

    arr = [3, 2, 2, 3]
    rez = s.removeElement(nums=arr, val=2)  # [2,2,_,_]
    print(rez, arr)

    arr = [3, 2, 2, 3]
    rez = s.removeElement(nums=arr, val=3)  # [2,2,_,_]
    print(rez, arr)

    arr = [0, 1, 2, 2, 3, 0, 4, 2]
    rez = s.removeElement(nums=arr, val=2)  # [0,1,4,0,3,_,_,_]
    print(rez, arr)
