from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_el = arr[len(arr) - 1]
        for i in range(len(arr) - 1)[::-1]:
            tmp = arr[i]
            arr[i] = max_el
            if tmp > max_el:
                max_el = tmp

        arr[len(arr) - 1] = -1
        return arr


if __name__ == "__main__":
    s = Solution()

    rez = s.replaceElements(arr=[17, 18, 5, 4, 6, 1])  # [18,6,6,6,1,-1]
    print(rez)

    rez = s.replaceElements(arr=[400])  # [-1]
    print(rez)
