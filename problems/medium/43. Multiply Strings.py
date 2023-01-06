class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add_lists(list):
            n = len(list[-1])
            for i in range(len(list)):
                l = list[i]
                l = l[::-1]
                while len(l) < n:
                    l.append(0)
                list[i] = l[::-1]
            in_mem = 0
            sum_i = []
            for i in range(n - 1, -1, -1):
                m = 0
                for l in list:
                    m += l[i]
                m += in_mem
                if m > 9:
                    in_mem = int(m / 10)
                    m = m % 10
                else:
                    in_mem = 0
                sum_i.append(str(m))
            if in_mem > 0:
                sum_i.append(str(in_mem))
            sum_i = sum_i[::-1]

            return "".join(sum_i)

        if num1 == "0" or num2 == "0":
            return "0"

        add_zero = 0
        for_sum = []
        for j in range(len(num2) - 1, -1, -1):
            in_mem = 0
            sum_j = []
            for i in range(len(num1) - 1, -1, -1):
                m = int(num1[i]) * int(num2[j]) + in_mem
                if m > 9:
                    in_mem = int(m / 10)
                    m = m % 10
                else:
                    in_mem = 0
                sum_j.append(m)
            if in_mem > 0:
                sum_j.append(in_mem)
            sum_j = sum_j[::-1]
            for _ in range(add_zero):
                sum_j.append(0)
            add_zero += 1
            for_sum.append(sum_j)

        return add_lists(for_sum)


if __name__ == "__main__":
    s = Solution()

    rez = s.multiply("2", "3")  # 6
    print(rez)

    rez = s.multiply(num1="123", num2="456")  # 56088
    print(rez)

    rez = s.multiply(num1="456", num2="123")  # 56088
    print(rez)

    rez = s.multiply(num1="5", num2="123")  # 615
    print(rez)

    rez = s.multiply(num1="55", num2="0")  # 0
    print(rez)
