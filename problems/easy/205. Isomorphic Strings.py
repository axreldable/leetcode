import time


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        values_set = set()
        for i in range(0, len(s)):
            l = s[i]
            if l in d:
                if d[l] != t[i]:
                    return False
            else:
                v = t[i]
                if v in values_set:
                    return False
                d[l] = v
                values_set.add(v)

        return True


if __name__ == "__main__":
    st = time.time()

    s = Solution()
    print(s.isIsomorphic("egg", "add"))
    print(s.isIsomorphic("foo", "bar"))
    print(s.isIsomorphic("paper", "title"))
    print(s.isIsomorphic("badc", "baba"))  # false

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
