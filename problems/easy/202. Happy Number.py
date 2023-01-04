class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while n != 1:
            n = str(n)
            if n in d:
                return False
            d[n] = 1
            arr = [int(x) for x in n]
            ssum = sum(map(lambda x: x * x, arr))
            n = ssum

        return True


if __name__ == "__main__":
    s = Solution()

    rez = s.isHappy(19)  # true
    print(rez)

    rez = s.isHappy(2)  # false
    print(rez)
