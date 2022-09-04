import time

from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        lp = 0
        d = defaultdict(int)
        is_first_odd = True

        for i, c in enumerate(s):
            d[c] += 1

        for i in d.values():
            if i % 2 == 0:
                lp += i
            else:
                if is_first_odd:
                    lp += 1
                    is_first_odd = False
                lp += i - 1

        return lp


if __name__ == "__main__":
    st = time.time()

    s = Solution()
    print(s.longestPalindrome("abccccdd"))  # 7
    print(s.longestPalindrome("a"))  # 1
    print(s.longestPalindrome("bb"))  # 2
    print(s.longestPalindrome("ccc"))  # 3

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("Time complexity: O(n)")
    print("Space complexity: O(1)")
