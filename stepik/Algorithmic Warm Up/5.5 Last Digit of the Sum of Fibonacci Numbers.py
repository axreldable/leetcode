from random import randint


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def pisano_period(m):
    if m <= 1:
        return

    first = 0
    second = 1
    p = 0
    while True:
        p += 1
        # print(first, second)
        first, second = second, (first + second) % m
        if first == 0 and second == 1:
            return p


def fibonacci_huge(n, m):
    period = pisano_period(m)
    n = n % period

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_sum(n):
    rez = fibonacci_huge(n + 2, 10) - 1
    if rez == -1:
        return 9

    return rez


def stress_test(n):
    count = 0
    while True:
        count += 1
        nr = randint(1, n)
        print(nr)
        rez_1 = fibonacci_sum_naive(nr)
        rez_2 = fibonacci_sum(nr)
        if rez_1 == rez_2:
            print("OK")
        else:
            print("count", count)
            print("Wrong answer:", rez_1, rez_2)
            return


if __name__ == '__main__':
    #     n = int(input())
    #     print(fibonacci_sum(n))

    print(fibonacci_sum(3))
    print(fibonacci_sum(7))
    print(fibonacci_sum(100))

    # stress_test(100)
