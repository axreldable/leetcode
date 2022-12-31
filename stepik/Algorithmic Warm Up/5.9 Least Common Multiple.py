from random import randint


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False


def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    # print(max(a, b))
    # print(a, b)
    return max(a, b)


def lcm(a, b):
    rez = int(a * b / gcd(a, b))
    # print(rez)
    return rez


def stress_test(n):
    count = 0
    while True:
        count += 1
        a = randint(1, n)
        b = randint(1, n)
        print(a, b)
        rez_1 = lcm_naive(a, b)
        rez_2 = lcm(a, b)
        if rez_1 == rez_2:
            print("OK")
        else:
            print("count", count)
            print("Wrong answer:", rez_1, rez_2)
            return


if __name__ == "__main__":
    # a, b = map(int, input().split())
    # print(gcd(a, b))

    lcm(3, 6)  # 6
    lcm(10, 8)  # 40
    lcm(10, 15)  # 30
    lcm(761457, 614573)  # 467970912861

    stress_test(100)
