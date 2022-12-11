from typing import List


class Solution:
    def merge_sort(self, arr):
        n = len(arr)

        if n <= 1:
            return arr

        mid = n // 2
        L = arr[:mid]
        R = arr[mid:]
        self.merge_sort(L)
        self.merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = R[j]
                j += 1
            else:
                arr[k] = L[i]
                i += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def binary_search(self, arr, el):
        def inner_search(arr, el, l, r):
            if l > r or l >= len(arr):
                return "absense"

            mid = int((l + r) / 2)
            print("el", el)
            print("mid", mid)
            if el == arr[mid]:
                return mid
            elif el < arr[mid]:
                return inner_search(arr, el, l, mid - 1)
            else:
                return inner_search(arr, el, mid + 1, r)

        return inner_search(arr, el, 0, len(arr))

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         s = nums[i] + nums[j]
        #         if s == target:
        #             return [i, j]
        s_nums = nums.copy()
        self.merge_sort(s_nums)

        print(s_nums)
        for i in range(len(s_nums)):
            s = target - s_nums[i]
            index = self.binary_search(s_nums, s)
            print(i, s_nums[i], index, s)
            if index != "absense":
                first = s_nums[i]
                second = s_nums[index]
                rez = []
                for i in range(len(nums)):
                    if nums[i] == first or nums[i] == second:
                        rez.append(i)
                return rez


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            s = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            d[s] = i


class SolutionNaive:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s == target:
                    return [i, j]


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    t = 9
    print(arr)
    s = Solution1()
    rez = s.twoSum(arr, t)
    print(rez)
    assert SolutionNaive().twoSum(arr, t) == rez
