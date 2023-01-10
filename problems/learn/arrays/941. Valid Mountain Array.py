from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0
        is_up = False
        while i + 1 < n and arr[i] < arr[i + 1]:
            is_up = True
            i += 1

        is_down = False
        while i + 1 < n and arr[i] > arr[i + 1]:
            is_down = True
            i += 1

        return is_up and is_down and i == n - 1


if __name__ == "__main__":
    s = Solution()

    rez = s.validMountainArray(arr=[2, 1])  # false
    print(rez)

    rez = s.validMountainArray(arr=[3, 5, 5])  # false
    print(rez)

    rez = s.validMountainArray(arr=[0, 3, 2, 1])  # true
    print(rez)

    rez = s.validMountainArray(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # false
    print(rez)
