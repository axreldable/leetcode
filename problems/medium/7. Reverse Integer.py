class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)

        is_negative = False
        if x_str[0] == "-":
            is_negative = True

        number = x_str
        if is_negative:
            number = x_str[1:]

        number = number[::-1]

        while number[0] == 0:
            number = number[1:]

        z = len("2147483648") - len(number)
        if is_negative:
            if z * "0" + number > "2147483648":
                number = "0"
            elif number != "0":
                number = "-" + number
        else:
            if z * "0" + number > "2147483647":
                number = 0

        number = int(number)

        return number


if __name__ == "__main__":
    s = Solution()

    print(s.reverse(123))  # 321
    print(s.reverse(-123))  # -321
    print(s.reverse(120))  # 21
    print(s.reverse(2147483648))  # 0
    print(s.reverse(-2147483649))  # 0
