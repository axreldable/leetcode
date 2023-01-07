from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        buf = []

        for i, el in enumerate(arr):
            if len(buf) > 0:
                arr[i] = buf.pop(0)
                buf.append(el)
            if el == 0:
                buf.append(0)


if __name__ == "__main__":
    s = Solution()

    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    s.duplicateZeros(arr)  # [1,0,0,2,3,0,0,4]
    print(arr)

    arr = [1, 2, 3]
    s.duplicateZeros(arr)  # [1,2,3]
    print(arr)
