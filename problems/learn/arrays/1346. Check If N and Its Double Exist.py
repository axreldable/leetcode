from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[i] * 2 == arr[j]:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()

    rez = s.checkIfExist(arr=[10, 2, 5, 3])  # true
    print(rez)

    rez = s.checkIfExist(arr=[3, 1, 7, 11])  # true
    print(rez)

    rez = s.checkIfExist(arr=[7, 1, 14, 11])  # true
    print(rez)
