class Solution:
    def __init__(self):
        self.r_d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

    def romanToInt(self, s: str) -> int:
        rez = 0
        i = 0
        l = len(s)
        while i < l:
            if i + 1 < l:
                if s[i:i + 2] in self.r_d:
                    rez += self.r_d[s[i:i + 2]]
                    i += 2
                    continue
            rez += self.r_d[s[i]]
            i += 1
        return rez


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("I") == 1
    assert s.romanToInt("III") == 3
    assert s.romanToInt("XII") == 12
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("XL") == 40
    assert s.romanToInt("XC") == 90
    assert s.romanToInt("CD") == 400
    assert s.romanToInt("CM") == 900
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
