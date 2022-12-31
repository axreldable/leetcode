class Solution:
    def myAtoi(self, string: str) -> int:
        if len(string) == 0:
            return 0

        while string[0] == " ":
            string = string[1:]
            if len(string) == 0:
                return 0

        is_negative = False
        if string[0] == "-":
            is_negative = True
            string = string[1:]
        elif string[0] == "+":
            string = string[1:]

        s_digits = ""
        for s in string:
            if s in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                s_digits += s
            else:
                break

        if len(s_digits) == 0:
            return 0

        while s_digits[0] == "0":
            s_digits = s_digits[1:]
            if len(s_digits) == 0:
                return 0

        l = len(s_digits)
        if l > 10:
            if is_negative:
                s_digits = "2147483648"
            else:
                s_digits = "2147483647"
        elif l == 10:
            if is_negative:
                if s_digits > "2147483648":
                    s_digits = "2147483648"
            else:
                if s_digits > "2147483647":
                    s_digits = "2147483647"

        if is_negative:
            s_digits = "-" + s_digits

        number = int(s_digits)

        return number


if __name__ == "__main__":
    s = Solution()

    print(s.myAtoi("42"))  # 42
    print(s.myAtoi("   -42"))  # -42
    print(s.myAtoi("4193 with words"))  # 4193
    print(s.myAtoi("-2147483648"))  # -2147483648
    print(s.myAtoi("-2147483649"))  # -2147483648
    print(s.myAtoi("2147483647"))  # 2147483647
    print(s.myAtoi("2147483648"))  # 2147483647

    print(s.myAtoi("words and 987"))  # 0
    print(s.myAtoi("-91283472332"))  # -2147483648
    print(s.myAtoi(""))  # 0
    print(s.myAtoi("21474836460"))  # 2147483647
    print(s.myAtoi("00000-42a1234"))  # 0
    print(s.myAtoi(" "))  # 0
