import time


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        leng = len(t)
        for i in s:
            if j == leng:
                return False
            while i != t[j]:
                j += 1
                if j == leng:
                    return False
            j += 1
        return True


if __name__ == "__main__":
    st = time.time()

    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))  # true
    print(s.isSubsequence("axc", "ahbgdc"))  # flase
    print(s.isSubsequence("abc", ""))  # flase

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("Time complexity: O(s+t)")
    print("Space complexity: O(1)")
