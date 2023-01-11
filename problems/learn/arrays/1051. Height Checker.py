from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0

        arr = [0] * 100
        for i in range(0, n):
            arr[heights[i] - 1] += 1

        k = 0
        i = 0
        rez = 0
        # print(heights, arr)
        while k < 100:
            if arr[k] == 0:
                k += 1
                continue
            j = 0
            while j < arr[k]:
                # print(k + 1, heights[i])
                if k + 1 != heights[i]:
                    rez += 1
                j += 1
                i += 1
            k += 1
            if i == n:
                break

        return rez


if __name__ == "__main__":
    s = Solution()

    arr = [1, 1, 4, 2, 1, 3]
    rez = s.heightChecker(arr)  # 3
    print(rez)

    arr = [5, 1, 2, 3, 4]
    rez = s.heightChecker(arr)  # 5
    print(rez)

    arr = [1, 2, 3, 4, 5]
    rez = s.heightChecker(arr)  # 0
    print(rez)

    arr = [2, 1, 2, 1, 1, 2, 2, 1]
    rez = s.heightChecker(arr)  # 4
    print(rez)
