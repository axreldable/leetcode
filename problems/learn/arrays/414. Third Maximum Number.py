from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_1 = None
        max_2 = None
        max_3 = None
        for i in nums:
            if i == max_1 or i == max_2 or i == max_3:
                continue
            if not max_1 or i > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = i
                continue
            if not max_2 or i > max_2:
                max_3 = max_2
                max_2 = i
                continue
            if not max_3 or i > max_3:
                max_3 = i
                continue

        return max_3 if max_3 or max_3 == 0 else max_1

    def thirdMax_bad(self, nums: List[int]) -> int:
        arr = []

        def add(el):
            if el in arr:
                return
            if len(arr) < 3:
                arr.append(el)
                if len(arr) == 2:
                    if arr[0] < arr[1]:
                        arr[0], arr[1] = arr[1], arr[0]
                    elif arr[0] < arr[1]:
                        arr.pop()
                    return
                if len(arr) == 3:
                    if arr[0] < arr[1]:
                        arr[0], arr[1] = arr[1], arr[0]
                    if arr[1] < arr[2]:
                        arr[1], arr[2] = arr[2], arr[1]
                    if arr[0] < arr[1]:
                        arr[0], arr[1] = arr[1], arr[0]
                    return
                return
            for i in range(3):
                if el > arr[i]:
                    n = 2
                    while n > i:
                        arr[n] = arr[n - 1]
                        n -= 1
                    arr[i] = el
                    return

        for i in nums:
            add(i)

        if len(arr) == 3:
            return arr[2]
        else:
            return arr[0]


if __name__ == "__main__":
    s = Solution()

    rez = s.thirdMax([3, 2, 1])  # 1
    print(rez)

    rez = s.thirdMax([1, 2])  # 2
    print(rez)

    rez = s.thirdMax([2, 2, 3, 1])  # 1
    print(rez)

    rez = s.thirdMax([1, 2, 2, 5, 3, 5])  # 2
    print(rez)

    rez = s.thirdMax([3, 3, 4, 3, 4, 3, 0, 3, 3])  # 0
    print(rez)
