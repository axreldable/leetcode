from random import randint


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    # print(max(a, b))
    # print(a, b)
    return max(a, b)


def stress_test(n):
    count = 0
    while True:
        count += 1
        a = randint(1, n)
        b = randint(1, n)
        print(a, b)
        rez_1 = gcd_naive(a, b)
        rez_2 = gcd(a, b)
        if rez_1 == rez_2:
            print("OK")
        else:
            print("count", count)
            print("Wrong answer:", rez_1, rez_2)
            return


if __name__ == "__main__":
    # a, b = map(int, input().split())
    # print(gcd(a, b))

    gcd(3, 6)  # 3
    gcd(10, 8)  # 2
    gcd(10, 15)  # 5
    gcd(28851538, 1183019)  # 17657

    stress_test(100)
