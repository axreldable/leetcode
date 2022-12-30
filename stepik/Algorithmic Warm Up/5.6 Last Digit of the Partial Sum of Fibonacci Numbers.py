import sys
from random import randint


def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

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


def fibonacci_partial_sum(from_, to):
    rez = fibonacci_sum(to) - fibonacci_sum(from_-1)
    if rez < 0:
        return 10 + rez

    return rez


def stress_test(n):
    count = 0
    while True:
        count += 1
        f = randint(1, n)
        s = randint(1, n)
        if f > s:
            f, s = s, f
        print(f, s)
        rez_1 = fibonacci_partial_sum_naive(f, s)
        rez_2 = fibonacci_partial_sum(f, s)
        if rez_1 == rez_2:
            print("OK")
        else:
            print("count", count)
            print("Wrong answer:", rez_1, rez_2)
            return


if __name__ == '__main__':
    # input = sys.stdin.read()
    # from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))

    print(fibonacci_partial_sum(3, 7))
    print(fibonacci_partial_sum(10, 10))

    stress_test(100)
