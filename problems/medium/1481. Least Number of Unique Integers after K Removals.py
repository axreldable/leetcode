from collections import defaultdict
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)

        for i in arr:
            d[i] += 1

        l = list(d.values())
        l.sort()

        i = 0
        leng = len(l)
        while k >= 0 and i < leng:
            k -= l[i]
            i += 1

        if k == 0:
            rez = len(l[i:])
        elif k < 0:
            rez = len(l[i:]) + 1
        else:
            # k > 0
            rez = 0

        return rez


if __name__ == "__main__":
    s = Solution()
    print(s.findLeastNumOfUniqueInts([5, 5, 4], 1))
    print(s.findLeastNumOfUniqueInts([5, 5, 4], 25))
    print(s.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))

    print("Time complexity: O(nlog(n))")
    print("Space complexity: O(n)")

